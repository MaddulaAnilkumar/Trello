import boto3
import json
import sys
def transcribe_s3(s3_bucket):
    s3 = boto3.resource('s3')
    path = s3_bucket.split("/")
    s3_bucket = path[0]
    if len(path)>1:
        folder1 = path[1]
    else:
        folder1 = "all"
    bucket = s3.Bucket(s3_bucket)
    for obj in bucket.objects.all():
        key = obj.key
#        body = obj.get()['Body'].read()
        if key[-5:] == ".json" and (key.split("/")[-2] == folder1 or folder1 == "all"):
            print(key)
            body = obj.get()['Body'].read()
            input_filename = key.split("/")[-1]
            s3_path = key.replace(input_filename,"")
            output_filename = "{}_formatted.txt".format(input_filename[:-5])
            conversation_log = transcribe_local(json.loads(body))
            if len(conversation_log) > 1:
                print("Writing file ....{}".format(output_filename))
                log_file = open(output_filename, "w")
                log_file.write(conversation_log)
                log_file.close()
                boto3.session.Session().client(service_name='s3')\
                            .put_object(Body=open(output_filename, 'rb'), Bucket=s3_bucket, Key=s3_path+output_filename)


def transcribe_local(conversation_json):
#
    try:
        len_of_conv = len(conversation_json["results"]["items"])
        prev_speaker = ""
        conversation_log = ""
    #
        for i in range(0,len_of_conv):
            speaker = conversation_json["results"]["items"][i]["speaker_label"]
            conversation = conversation_json["results"]["items"][i]["alternatives"][0]["content"]
            if speaker == prev_speaker:
                conversation_log = "{} {}".format(conversation_log, conversation)
            else:
                conversation_log = "{}\n{}:\n\t{}".format(conversation_log, speaker, conversation)
            prev_speaker = speaker
        return conversation_log
    except Exception as e:
        print(e)
        print("Could not process. Proceeding for next")
        return ""

if __name__ == '__main__':

    conversation_filename = sys.argv[1]
    if conversation_filename=="s3":
        s3_path = sys.argv[2]
        transcribe_s3(s3_path)

    else:
        input_json_file = conversation_filename
        output_filename = "{}_output.txt".format(input_json_file[:-5])
        f = open(input_json_file, "r")
        conversation_json = json.loads(f)
        conversation_log = transcribe_local(conversation_json, output_filename)
        if len(conversation_log) > 1:
            log_file = open(output_filename, "w")
            log_file.write(conversation_log)
