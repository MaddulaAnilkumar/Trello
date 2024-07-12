from __future__ import print_function
import sqlite3
import mysql.connector
import pandas as pd
from io import BytesIO
import boto3
import base64
from botocore.exceptions import ClientError
import pyarrow.parquet as pq
import s3fs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import json
import os
import traceback
from utilities.logger_utils import get_logger
from files_list import read_data_xlsx
import time

class keen_aws_session:
    def __init__(self, aws_access_key=None, aws_secret_key=None, aws_token=None, region_name=None, profile_name=None):
        self.log=get_logger()
        try:
            if aws_access_key == None:
                self.session = boto3.session.Session()
            else:
                self.session = boto3.session.Session(aws_access_key_id=aws_access_key,
                                   aws_secret_access_key=aws_secret_key,
                                   aws_session_token = aws_token,
                                   region_name=region_name,
                                   profile_name = profile_name)
        except Exception as e:
            print("Failed while connecting to AWS. Check you AWS Credentials")
            print(traceback.format_exc())

    def get_secret(self, secret_name, region_name='us-west-2'):
        # Create a Secrets Manager client
        try:
            client = self.session.client(
                service_name='secretsmanager',
                region_name=region_name
                )
        except Exception as e:
            print("Failed to establish connection with AWS Secrets manager. Check your AWS Policies/credentials")
            print(e)
            return None
#
        try:
            get_secret_value_response = client.get_secret_value(
                    SecretId=secret_name
                    )
        except ClientError as e:
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                raise e
            elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            print("Failed while retrieving the secret")
            return None
        else:
            # Decrypts secret using the associated KMS key.
            # Depending on whether the secret is a string or binary, one of these fields will be populated.
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                return secret
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
                return decoded_binary_secret

    def get_parameter(self, parameter_name, region_name='us-west-2',  need_decryption=False):
        try:
            client = self.session.client(
                service_name='ssm',
                region_name=region_name
                )
        except Exception as e:
            print("Failed to establish connection with AWS Parameter Store (ssm). Check your AWS Policies/credentials")
            print(traceback.format_exc())
            return None

        try:
            parameter = client.get_parameter(Name=parameter_name, WithDecryption=need_decryption)
        except Exception as e:
            print("Failed to retrieve your parameter. Please check the parameter name and try again")
            print(traceback.format_exc())
            return None
        else:
            return parameter['Parameter']['Value']

    def put_parameter(self, parameter_name,  new_value, region_name='us-west-2'):
        client = self.session.client(
                service_name='ssm',
                region_name=region_name
                )

        client.put_parameter(Name=parameter_name, Value=new_value, Overwrite=True)
        return 0

    def write_s3(self, dataframe, s3_bucket, s3_prefix, s3_filename, curr_pull_date, file_format='csv'):
#
        if file_format == "text":
            try:
                client = self.session.client(
                    service_name='s3'
                )
                client.put_object(Body=open(dataframe, 'rb'), Bucket=s3_bucket,
                              Key=s3_prefix + "/" + s3_filename)

#                print("{}/{}/{}".format(s3_bucket,s3_prefix,s3_filename))
#                print(dataframe)
                return True
            except Exception as e:
                print("Failed to establish connection with AWS S3. Check your AWS Policies/credentials")
                print(traceback.format_exc())
                return False
        else:
            df = dataframe
            if s3_bucket[-1] == '/':
                s3_bucket = s3_bucket[: len(s3_bucket)-1]
            file_path = "s3://{}/{}/{}/{}.{}".format(s3_bucket, s3_prefix, s3_filename, curr_pull_date,  file_format)
            print("Writing table {} to S3 at {}".format(s3_filename, file_path))

            try:
                if file_format == 'parquet':
                    df.to_parquet(file_path)
                elif file_format == 'json':
                    df.to_json(file_path)
                else:
                    print(file_path)
                    df.to_csv(file_path, index=False)
                return df.shape[0]
            except Exception as e:
                print("Failed while writing to S3. Please check the access to S3")
                print(traceback.format_exc())
                return 0
#
    def get_s3_obj_list(self, s3_bucket, s3_prefix):
        try:
            if s3_bucket[-1] == '/':
                s3_bucket = s3_bucket[:-1]
            if s3_prefix[-1] != '/':
                s3_prefix = s3_prefix + "/"
            objects = []
            s3 = self.session.resource('s3')
            my_bucket = s3.Bucket(s3_bucket)
            for object in my_bucket.objects.filter(Prefix=s3_prefix):
                object_name = object.key.split("/")[-1]
                objects.append(object_name)
            return objects
        except Exception as e:
            print("Failed while reading from S3 path. Please check the path and S3 access")
            print(traceback.format_exc())
            return None

    def read_s3(self, s3_bucket, s3_filename, file_format):

        df = pd.DataFrame()
        if s3_bucket[-1] == '/':
            s3_bucket = s3_bucket[: len(s3_bucket)-1]
        if s3_filename[-1] == '/':
            s3_filename = s3_filename[: len(s3_filename)-1]

        try:
            s3 = self.session.resource('s3')
            file_path = "{}/{}".format(s3_bucket, s3_filename)

            if file_format == 'parquet':
                df = pq.ParquetDataset(file_path, filesystem=s3fs.S3FileSystem()).read_pandas().to_pandas()
            elif file_format == 'json':
                my_bucket_source = s3.Bucket(s3_bucket)
                for obj in my_bucket_source.objects.filter(Prefix=s3_filename):
                    file_path = 's3://{}/{}'.format(obj.bucket_name, obj.key)
                    print(file_path)
                    if file_path[-4:] == "json":
                        df = pd.concat([df, pd.read_json(file_path, lines=True)], ignore_index=True)
            else:
                obj = s3.Object(s3_bucket, s3_filename)
                with BytesIO(obj.get()['Body'].read()) as bio:
                    df = pd.concat([df, pd.read_csv(bio, index_col=False)], ignore_index=True)
        except Exception as e:
            print("Failed while reading from S3 path. Please check the path and S3 access")
            print(traceback.format_exc())
            return None
        else:
            print(df.shape)
            return df
#
    def object_exists(self, s3_bucket, s3_key):
        if s3_bucket[-1] == '/':
            s3_bucket = s3_bucket[: len(s3_bucket)-1]
        if s3_key[-1] == '/':
            s3_key = s3_key[: len(s3_key)-1]

        try:
            s3 = self.session.client('s3')
            s3.head_object(Bucket=s3_bucket, Key=s3_key)
            return True
        except ClientError:
            return False
#
    def send_email(self, from_email, to_email, subject, body="GenerateQuote Test results", body_type="html", region_name='us-west-2'):
        print("Entered into AWS Send_email ....")
        try:
            client = self.session.client(
                service_name='ses',
                region_name=region_name
                )
        except Exception as e:
            print("Failed to establish connection with AWS Simple Email Servies (ses). Check your AWS Policies/credentials")
            print(traceback.format_exc())
            return None
        CHARSET = "utf-8"
        msg = MIMEMultipart('mixed')
        # Add subject, from and to lines.
        msg['Subject'] = subject
        msg['From'] = from_email
#        msg['To'] = to_email

        msg_body = MIMEMultipart('alternative')
        if body_type == "html":
            part = MIMEText(body.encode(CHARSET), 'html', CHARSET)
        else:
            part = MIMEText(body.encode(CHARSET), 'plain', CHARSET)

        msg_body.attach(part)
        msg.attach(msg_body)
        try:
            # Provide the contents of the email.
            response = client.send_raw_email(
                Source=from_email,
                Destinations=to_email,
                RawMessage={'Data': msg.as_string(), }
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

    def meddical_transcribe(self):
        transcribe = boto3.client('transcribe')
        job_name = "-Q7phjD_ICn4NzLA_1982487653049_1982487653049_20230403"
        job_uri = "s3://restrictedaccessfiles/call_analytics/call_recordings/-Q7phjD_ICn4NzLA_1982487653049_1982487653049_20230403.mp3"
        transcribe.start_medical_transcription_job(
            MedicalTranscriptionJobName=job_name,
            Media={'MediaFileUri': job_uri},
            LanguageCode='en-US',
            ContentIdentificationType='PHI',
            Specialty='PRIMARYCARE',
            Type='DICTATION',
            OutputBucketName='s3://restrictedaccessfiles/call_analytics/call_recordings/call_recording_output/'
        )
        while True:
            status = transcribe.get_medical_transcription_job(MedicalTranscriptionJobName=job_name)
            if status['MedicalTranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break
            print("Not ready yet...")
            time.sleep(5)
        print(status)
    def transcribe(self, input_path, output_path=None, audio_file_name=None,  max_speakers=2, region_name='us-east-2'):
        print("Entered into AWS Transcribe job ....")
        self.log.info("Entered into AWS Transcribe job ....")
        try:
            client = self.session.client(
                service_name='transcribe',
                region_name=region_name
            )
            s3 = boto3.resource('s3')
        except Exception as e:
            print("Failed to establish connection with AWS Transcribe Servie. Check your AWS Policies/credentials")
            self.log.info("Failed to establish connection with AWS Transcribe Servie. Check your AWS Policies/credentials")
            print(traceback.format_exc())
            return False
#
        try:
            input_bucket = input_path.split("/")[0]
            input_prefix = "/".join(input_path.split("/")[1:])
            print("Processing files at S3 path: {}/{}".format(input_bucket, input_prefix))
            print("HI INPUT_S4")
            # self.log.info("Processing files at S3 path: {}/{}".format(input_bucket, input_prefix))
            input_s3_bucket = s3.Bucket(input_bucket)
            print("input_s3_bucket_input:",input_s3_bucket)
            files_list = []
            if audio_file_name is None:
                print("Audio_file_none")
                input_data_user = read_data_xlsx()
                data = input_data_user.process_data()
                print("Input_call_records:",data)
                # list_values = []
                for data_values in data:
                    print("data_values:", data_values)
                    files_list.append(data_values)
                self.log.info(files_list)
                # prefix_objs = input_s3_bucket.objects.filter(Prefix=input_prefix)
                # for obj in prefix_objs:
                #     if len(obj.key.split("/")[-1].split(".")) == 2:
                #         files_list.append(obj.key.split("/")[-1])
            else:
                print("Audio files are there")
                if len(audio_file_name.split(".")) == 2:
                    files_list = [audio_file_name]
            print("List_of_files:",files_list)
            if len(files_list) == 0:
                print("No files found to process in the input path")
                self.log.info("No files found to process in the input path")
                return False
            else:
                print("List of files to be processed: {}".format(files_list))
                self.log.info("List of files to be processed: {}".format(files_list))
        except Exception as e:
            print("Invalid Input path {}".format(input_path))
            self.log.info("Invalid Input path {}".format(input_path))
            print(traceback.format_exc())
            return False
#
        try:
            if output_path is None:
                output_bucket = input_bucket
                output_prefix = input_prefix
            else:
                output_bucket = output_path.split("/")[0]
                output_prefix = "/".join(output_path.split("/")[1:])
            print("Output Path would be: {}/{}".format(output_bucket, output_prefix))
            self.log.info("Output Path would be: {}/{}".format(output_bucket, output_prefix))
        except Exception as e:
            print("Invalid Output path {}".format(output_path))
            self.log.info("Invalid Output path {}".format(output_path))
            print(traceback.format_exc())
            return False
#
        for audio_file in files_list:
            print("Started processing audio file {}".format(audio_file))
            if len(audio_file.split(".")) != 2:
                print("Invalid file name {}".format(audio_file))
                self.log.info("Invalid file name {}".format(audio_file))
                continue
            format = audio_file.split(".")[1]
            output_json_filename = "{}.json".format(audio_file.split(".")[0])
            output_filename = "{}.txt".format(audio_file.split(".")[0])
            if format is None:
                print("File extension missing in the audio file name {}".format(audio_file))
                self.log.info("File extension missing in the audio file name {}".format(audio_file))
                continue
            if format not in ['mp3', 'wav', 'mp4']:
                print("Invalid format {} of input audio file {}".format(format, audio_file))
                print("Valid formats are: mp3, wav & mp4")
                continue
#
            if max_speakers > 10:
                max_speakers = 10
#
            try:
                job_uri = "s3://{}/{}/{}".format(input_bucket, input_prefix, audio_file)
                job_name = (audio_file.split('.')[0]).replace(" ", "")
                incr = 0
                print("job_name:",job_name)
                existed_jobs = client.list_transcription_jobs()
                print("existed_jobs:",existed_jobs)
                job_exists = True
                print("True")
                while job_exists:
                    job_exists = False
                    for job in existed_jobs['TranscriptionJobSummaries']:
                        if job_name == job['TranscriptionJobName']:
                            job_exists = True
                            print("Job Name already exists {}".format(job_name))
                            incr = incr + 1
                            job_name = "{}_{}".format(job_name, incr)
                            print("Changing job name to {}".format(job_name))
                            break
            except Exception as e:
                print("Failed while creating jobname")
                print(traceback.format_exc())
                continue
#
            try:
                client.start_transcription_job(
                    TranscriptionJobName=job_name,
                    Media={'MediaFileUri': job_uri},
                    MediaFormat=format,
                    LanguageCode='en-US',
                    Settings={'ShowSpeakerLabels': True,
                              'MaxSpeakerLabels': max_speakers},
                    OutputBucketName=output_bucket,
                    OutputKey=output_prefix + "/" + output_json_filename
                )
                while True:
                    result = client.get_transcription_job(TranscriptionJobName=job_name)
                    #                    print("Checking job completed or not ...")
                    if result['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                        break
                    time.sleep(15)
                print("Seems job complted ...")
            except Exception as e:
                print("Failed while starting the transcribe job")
                print(traceback.format_exc())
                continue
#
            if result['TranscriptionJob']['TranscriptionJobStatus'] == "COMPLETED":
                print("Job completed ...Getting result")
                try:
                    obj = self.session.resource('s3').Object(output_bucket, output_prefix + "/" + output_json_filename)
                    result = obj.get()['Body'].read()
                    conversation_json = json.loads(result)
                    len_of_conv = len(conversation_json["results"]["items"])
                    prev_speaker = ""
                    conversation_log = ""
                    #
                    for i in range(0, len_of_conv):
                        speaker = conversation_json["results"]["items"][i]["speaker_label"]
                        conversation = conversation_json["results"]["items"][i]["alternatives"][0]["content"]
                        if speaker == prev_speaker:
                            conversation_log = "{} {}".format(conversation_log, conversation)
                        else:
                            conversation_log = "{}\n{}:\n\t{}".format(conversation_log, speaker, conversation)
                        prev_speaker = speaker
                    if len(conversation_log) > 1:
                        print("Writing file ....{}".format(output_filename))
                        transcribe_file = open(output_filename, "w")
                        transcribe_file.write(conversation_log)
                        transcribe_file.close()
                        boto3.session.Session().client(service_name='s3') \
                            .put_object(Body=open(output_filename, 'rb'), Bucket=output_bucket,
                                        Key=output_prefix +"/"+ output_filename)
                        os.remove(output_filename)
                    else:
                        print("There seems to be no conversation in this recording. No transcription is generated")
                        self.log.info("Failed while process the JSON response from the transcribe job. Proceeding for next")
                    self.session.resource('s3').Object(output_bucket, output_prefix + "/" + output_json_filename).delete()
                except Exception as e:
                    print(traceback.format_exc())
                    print("Failed while process the JSON response from the transcribe job. Proceeding for next")
                    self.log.info("Failed while process the JSON response from the transcribe job. Proceeding for next")
            else:
                print("Transcribe job ended with status {}".format(result['TranscriptionJob']['TranscriptionJobStatus']))
                # print("Transcribe job ended with status {}".format(result['MedicalTranscriptionJob']['TranscriptionJobStatus']))
                self.log.info("Transcribe job ended with status")
    def test_detect_entities(self):
        print("Entered into AWS Transcribe job ....")
        self.log.info("Entered into AWS Transcribe job ....")
        ## restrictedaccessfiles/rc_datapipeline/rc_call_recordings
        input_bucket = 'restrictedaccessfiles/call_analytics/call_recordings/call_recording_output'
        input_key = 'restrictedaccessfiles/call_analytics/call_recordings/call_recording_output/A-LPRgMsFyPKDUA_1683512429049_1683512429049_20220802.txt'
        ### s3://restrictedaccessfiles/call_analytics/call_recordings/call_recording_output/A-LPRgMsFyPKDUA_1683512429049_1683512429049_20220802.txt
        output_bucket = 'restrictedaccessfiles/call_analytics/call_recordings/'
        output_key = 'restrictedaccessfiles/call_analytics/call_recordings/call_recording_output/'
        try:
            comprehend_medical = boto3.client('comprehendmedical')

            # Step 1: Upload your data to S3
            s3 = boto3.client('s3')
        except Exception as e:
            print("Failed to establish connection with AWS Transcribe Servie. Check your AWS Policies/credentials")
            self.log.info(
                "Failed to establish connection with AWS Transcribe Servie. Check your AWS Policies/credentials")
            print(traceback.format_exc())
            return False
        s3.upload_file(input_key, input_bucket, input_key)
        job_name = 'A-LPRgMsFyPKDUA_1683512429049_1683512429049_20220802.txt_converted_text'
        response = comprehend_medical.start_entities_detection_v2_job(
            InputDataConfig={
                'S3Bucket': input_bucket,
                'S3Key': input_key
            },
            OutputDataConfig={
                'S3Bucket': output_bucket,
                'S3Key': output_key
            },
            JobName=job_name,
            # DataAccessRoleArn='arn:aws:iam::your-account-id:role/service-role/ComprehendMedicalServiceRole-YourRoleSuffix',
            LanguageCode='en'
        )

        # Step 3: Monitor the progress of the job
        # You can use DescribeEntitiesDetectionV2Job or DescribePHIDetectionJob here
        # Replace 'EntitiesDetectionJobProperties' with 'PHIDetectionJobProperties' if needed
        job_status = comprehend_medical.describe_entities_detection_v2_job(JobId=response['JobId'])

        # You can check the job status and monitor its progress
        print(f"Job Status: {job_status['EntitiesDetectionJobProperties']['JobStatus']}")
        print(f"Job Output S3 URI: {job_status['EntitiesDetectionJobProperties']['OutputDataConfig']['S3Uri']}")

        # Step 4: To stop a job in progress (optional)
        # Uncomment the following lines if you need to stop the job
        # comprehend_medical.stop_entities_detection_v2_job(JobId=response['JobId'])

        # Step 5: View the results in the output S3 bucket
        # You can review the output in the S3 bucket that you configured when you started the job
    def test_aws(self,sample_body):
        import requests
        ##sample_body = {{"from_email": "engineering@choosekeen.com","to_email": ["engineering@choosekeen.com","anil.maddula@choosekeen.com"],"subject":"GenerateQuote Automation status is pass","body":"Automation Execusion results"}}
        method = "POST"
        api_url = "https://internal-service.choosekeentech.com"
        auth_user = "keen_libs"
        auth_password = "CJ63GZcbIp4EIkm"
        path = "/aws/send_email"
        url = api_url + path
        response = requests.request(
            method,
            url,
            auth=(auth_user, auth_password),
            json=sample_body,
        )
        if response.status_code == 200:
            data = response.json()
            print("Response data:", data)
        else:
            print("API request failed with status code:", response.status_code)
            print("Response content:", response.text)

    def test_json_read(self):
        json_file_path = "C:\\Users\\amaddula\\Downloads\\E6R5vcBSCvUGDUA_2297345502049_20231212.txt.json"
        text_file_path = "C:\\Users\\amaddula\\Downloads\\E6R5vcBSCvUGDUA_2297345502049_20231212 (2).txt"  # Replace with the actual path to your text file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        if 'Entities' in data and isinstance(data['Entities'], list):
            text_to_type_mapping = {entry.get('Text', 'N/A'): entry.get('Type', 'N/A') for entry in data['Entities']}
            with open(text_file_path, 'r') as text_file:
                text_content = text_file.read()
            for text, type_value in text_to_type_mapping.items():
                text_content = text_content.replace(text, type_value)
            with open(text_file_path, 'w') as text_file:
                text_file.write(text_content)
            print("Replacement completed successfully.")
        else:
            print("Error: The 'Entities' key is missing or not a list of dictionaries.")
    def get_member_details(self):
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='keen-dev-db.c0711deihaac.us-west-2.rds.amazonaws.com',
            user='qa_user',
            password='IEAnbk4f4l8bvv5',
            database='keen_analytics'
        )
        # connection = sqlite3.connect('keen_analytics')  # Replace with your database file

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a SELECT query to retrieve member details based on member ID
        query = '(SELECT * FROM Account WHERE id = "0018B00000S5iPKQAZ")'
        print("Executing query:", query)
        output=cursor.execute(query)
        print("output:",output)
        # Fetch the result (assuming there is only one member with the given ID)
        member_details = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return output

    # Example usage
    # member_id_to_lookup = "0018B00000S5iPKQAZ"
    # result = get_member_details(member_id)

    # if result:
    #     print("Member details:", result)
    # else:
    #     print("Member not found.")
if __name__ == '__main__':
    print("Hi! This class holds all the Keen AWS related functions.")

