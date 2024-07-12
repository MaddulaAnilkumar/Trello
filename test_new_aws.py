# import boto3
# class test_aws_records():
#     def test_call_records(self):
#         aws_region = 'us-east-2'
#         transcribe = boto3.client('transcribe',region_name=aws_region)
#
#         response = transcribe.start_transcription_job(
#             TranscriptionJobName='B04enIlNSjaWDUA_1842467188049_20221213.mp3',
#             LanguageCode='en-US',  # Change this based on the language of your audio file
#             MediaFormat='mp3',  # Change this based on the format of your audio file
#             Media={
#                 'MediaFileUri': 's3://restrictedaccessfiles/rc_datapipeline/rc_call_recordings/B04enIlNSjaWDUA_1842467188049_20221213.mp3'
#             }
#         )
#
#         print(response)
#         response = transcribe.list_transcription_jobs()
#
#         for job in response['TranscriptionJobSummaries']:
#             print(job['TranscriptionJobName'])
#     def test_upload_files(self):
#         aws_region = 'us-east-2'
#         transcribe = boto3.client('transcribe', region_name=aws_region)
#
#         # Your transcription job parameters
#         job_name = 'B04enIlNSjaWDUA_1842467188049_20221213.mp3'
#         job_uri = 's3://restrictedaccessfiles/rc_datapipeline/rc_call_recordings/B04enIlNSjaWDUA_1842467188049_20221213.mp3'
#
#         transcribe.start_transcription_job(
#             TranscriptionJobName=job_name,
#             Media={'MediaFileUri': job_uri},
#             OutputBucketName='s3://restrictedaccessfiles/call_analytics/'
#         )
#
#         # Wait for the job to complete
#         print("Files are accessed")
#         response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
#         transcription_result = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
#         print("Job executed")
#         # Assuming the transcript result is in JSON format
#         # You would parse the JSON and process it as needed
#
#         # For example, if you want to break into lines based on time stamps
#         results = transcription_result['results']['items']
#         lines = []
#         print("break Lines based on tym stramp")
#         for item in results:
#             start_time = item.get('start_time', '')
#             content = item.get('alternatives', [])[0].get('content', '')
#             lines.append(f"{start_time}: {content}")
#             print("Line are printed and back to list")
# aws=test_aws_records()
# aws.test_upload_files()
from Pages.aws import keen_aws_session
aws_service=keen_aws_session
class aws_session_connection():
    def aws_verify(self):
        input_path = ['s3://restrictedaccessfiles/rc_datapipeline/rc_call_recordings/B04enIlNSjaWDUA_1842467188049_20221213.mp3,s3://restrictedaccessfiles/rc_datapipeline/rc_call_recordings/3KH3BgzjdD7keDLA_2093327533048_2093327533048_20230629.mp3']
        aws_service.transcribe('s3://restrictedaccessfiles/rc_datapipeline/rc_call_recordings/B04enIlNSjaWDUA_1842467188049_20221213.mp3,s3://restrictedaccessfiles/rc_datapipeline/rc_call_recordings/3KH3BgzjdD7keDLA_2093327533048_2093327533048_20230629.mp3')
aws=aws_session_connection()
aws.aws_verify()