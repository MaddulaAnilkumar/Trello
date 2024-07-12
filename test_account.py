from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from logger_utils import get_logger
from XLUtilities import Excel_data
import time
import boto3

# chrome_driver_path = "C:\\Users\\amaddula\\PycharmProjects\\Keen_Automation\\chromedriver-win32\\chromedriver.exe"
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(20)
# path="C:\\Users\\amaddula\\PycharmProjects\\Keen_Automation\\Keen_data (1).xlsx"
# readdata_tasks=Excel_data(path, "Keen_leads")
# write_data=Excel_data(path, "Keen_leads")
# driver.get("https://choosekeen--qa2.sandbox.lightning.force.com/")
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("engineering@choosekeen.com.qa2")
# time.sleep(2)
# driver.find_element(By.ID,"password").send_keys("InnoK@123")
# time.sleep(2)
# driver.find_element(By.ID,"Login").click() ## login
# for data in range(16,64):
#     First_Name=readdata_tasks.readdata(data, 1)
#     Second_Name=readdata_tasks.readdata(data,2)
#     Month=readdata_tasks.readdata(data, 3)
#     Date=readdata_tasks.readdata(data, 4)
#     Year=readdata_tasks.readdata(data, 5)
#     advisor=readdata_tasks.readdata(data,6)
#     Id=readdata_tasks.readdata(data, 7)
#     Password=readdata_tasks.readdata(data, 8)
#     time.sleep(4)
#     keen_leads = driver.find_element(By.XPATH, "(//span[text()='Keen leads and members'])[1]")
#     driver.execute_script("arguments[0].click();", keen_leads)
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//a[@title='New']").click()
#     driver.find_element(By.XPATH,"//input[@name='FirstName']").send_keys(First_Name)## first_name
#     driver.find_element(By.XPATH,"//input[@name='LastName']").send_keys(Second_Name)## Last_name\
#     time.sleep(2)
#     get_logger().info("Last_name_entered")
#     # date_output=Month+'/'+Date+'/'+Year
#     # print("sdate:",date_output)
#     # driver.find_element(By.XPATH,"//input[@name='dob']").send_keys(date_output)##date_birth
#     # time.sleep(4)
#     driver.find_element(By.XPATH,"//button[@name='Status__c']").click()
#     time.sleep(3)
#     values=driver.find_elements(By.XPATH,"//lightning-base-combobox-item//span[@class='slds-truncate']")
#     for vl in values:
#         print(vl.text)
#         if vl.text == "Keen Member (Sold)":
#             time.sleep(2)
#             print(vl.text)
#             vl.click()
#             get_logger().info("status selected")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//button[@name='submit']").click()
#     print("HI")
#     get_logger().info("save clicked")
#     time.sleep(4)
#     driver.find_element(By.XPATH,"//button[text()='Continue']").click()
#     print("HI")
#     get_logger().info("continued clicked")
#     time.sleep(2)
#     keen_leads = driver.find_element(By.XPATH, "(//span[text()='Keen leads and members'])[1]")
#     driver.execute_script("arguments[0].click();", keen_leads)
#     get_logger().info("leads clicked")
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
        print("Outputfilename:",output_filename)
        conversation_log = transcribe_local(conversation_json, output_filename)
        if len(conversation_log) > 1:
            log_file = open(output_filename, "w")
            log_file.write(conversation_log)

