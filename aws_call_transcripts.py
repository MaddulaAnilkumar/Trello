from Pages.aws import keen_aws_session
class aws_transcripts():
    def run_transcripts(self):
        aws_session = keen_aws_session()
        # aws_session.test_json_read()
        details=aws_session.get_member_details()
        print("details:",details)
        if details:
            print("Member details:", details)
        else:
            print("Member not found.")
        # aws_session.transcribe("restrictedaccessfiles/call_analytics/call_recordings/call_recording_output","restrictedaccessfiles/call_analytics/call_recordings/call_recording_output/ACMS_IN","High_frequency_audio_file.mp3")
        #### restrictedaccessfiles/rc_datapipeline/rc_call_recordings/call_recording_output
        ### s3://restrictedaccessfiles/call_analytics/call_recordings/call_recording_output/High_frequency_audio_file.mp3
        # aws_session.test_detect_entities()
        # aws_session.meddical_transcribe()
if __name__  ==  '__main__':
    call_conversion=aws_transcripts()
    call_conversion.run_transcripts()
# class aws_text():
#     import boto3
#     import re
#
#     def lambda_handler(event, context):
#         s3_client = boto3.client('s3')
#
#         # Retrieve information about the S3 object from the event
#         bucket = event['Records'][0]['s3']['bucket']['name']
#         key = event['Records'][0]['s3']['object']['key']
#
#         # Download the text file from S3
#         response = s3_client.get_object(Bucket=bucket, Key=key)
#         text_content = response['Body'].read().decode('utf-8')
#
#         # Process the text content and redact names
#         redacted_content = redact_names(text_content)
#
#         # Upload the redacted content back to S3
#         redacted_key = key.replace('.txt', '_redacted.txt')
#         s3_client.put_object(Bucket=bucket, Key=redacted_key, Body=redacted_content.encode('utf-8'))
#
#     def redact_names(text_content):
#         # Redact names using a regular expression
#         redacted_content = re.sub(r'\b[A-Z][a-z]*\b', 'REDACTED', text_content)
#
#         return redacted_content


# len_of_conv = len(conversation_json.get("results", {}).get("transcripts", [{}]).get("items", []))
# print("length_of_conversation:", len_of_conv)
# prev_speaker = ""
# conversation_log = ""
#
# for i in range(0, len_of_conv):
#     speaker_labels = conversation_json.get("results", {}).get("transcripts", [{}])[i].get("Speaker_labels", {}).get(
#         "segments", [])
#
#     # Assuming you want to iterate over segments and alternatives
#     for segment in speaker_labels:
#         alternatives_array = segment.get("0", {}).get("alternatives", [])
#
#         for alternative in alternatives_array:
#             content_data = alternative.get("0", {}).get("content", "")
#
#             # Use content_data as needed
#             print("Content:", content_data)
#
#             # If you want to append content_data to conversation_log
#             if prev_speaker == "":
#                 conversation_log = "{}".format(content_data)
#             else:
#                 conversation_log = "{}\n{}".format(conversation_log, content_data)
#
#             prev_speaker = content_data
#
# # If you want to print the conversation_log after the loop
# if len(conversation_log) > 1:
#     print("Conversation Log:")
#     print(conversation_log)