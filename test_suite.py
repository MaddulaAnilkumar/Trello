import os
import time
import allure
import pytest
import requests
from openpyxl import load_workbook
from selenium.webdriver import ActionChains, Keys
import re
from Pages.Keen_SOA import Create_SOA_Form
from Pages.aws import keen_aws_session
from selenium.webdriver.common.by import By
from Pages.Keen_Associate_capture_full_member_details import Associate_Capture_full_Member_details
from Pages.Keen_Task import New_Task
from Pages.Keen_account_creation import Keen_Account_creation
from Pages.Keen_scheduleMeeting import Keen_Scedule_Meeting
from tests.test_ALogin import Test_login
from tests.test_AccountCreation import Test_account_creation
from tests.test_GenerateQuote import Test_GenerateQuote
from tests.test_SOA import Test_SOA_Form
from tests.test_associate_Capture_Full_Member_Details import Test_add_Member_details
from tests.test_create_Capture_full_Member_details import Test_create_capture_full_member_details
from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
from tests.test_log_a_call import Test_log_a_call
from utilities import logger_utils
from utilities.XLUtilities import Excel_data
from utilities.action_utils import ActionUtils
from tests.test_Task import Test_New_Task
from Pages.Keen_GenerateQuote import Keen_Quote_Generation
import datetime
now = datetime.datetime.now()
today = now.strftime("%m/%d/%Y")
from utilities.base_test import BaseTest
sheet_account="Account_Creation"
sheet_name='Plans'
path="../test_data/Keen_Testdata.xlsx"
workbook = load_workbook('../test_data/Keen_Testdata.xlsx')
readdata_account=Excel_data(path,"Account_Creation")
readdata_physicians=Excel_data(path,"Physicians")
readdata_pharmacies=Excel_data(path,"Pharmacies")
readdata_medications=Excel_data(path,"Medication")
number=BaseTest()
row_account = number.get_random_number("Account_Creation")
row_practice=number.get_random_number('Practices')
row_plan=number.get_random_number("Plans")
row_planassociate=number.get_random_number("Plans_associate")
row_caregivers=number.get_random_number("Caregiver")
row_tasks=number.get_random_number("Tasks")
row_hospitals=number.get_random_number("Hospitals")
row_events=number.get_random_number("Events")
row_physicians=number.get_random_number("Physicians")
row_medication=number.get_random_number("Medication")
row_pharmacy=number.get_random_number("Pharmacies")
row_soa_number=number.get_random_number("SOA")
row_parent=number.get_random_number('Parent_organization')

class Test_Suit(Test_login):
    log = logger_utils.get_logger()
    @pytest.mark.CaptureFullMemberDetails
    def test_caputure_full(self):
        action_utils=ActionUtils(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        keen = Test_create_capture_full_member_details(self.driver)
        row_community=number.get_random_number("Community")
        ### Plans creation or Associate to a member
        # name=keen.test_plans(row_plan)
        # print("Name:",name)
        # keen.test_validation_plans(row_plan,name)
        keen.test_select_member_to_associate_Cpature_Full_Member_details()
        keen.test_select_practice()
        practice_name=keen.test_practice(row_practice)
        keen.test_select_practice_created_record(practice_name)
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                action_utils.wait_for_element((Create_capture_member_details.practice_record))
                keen_create.click_practice_verify()
                keen.test_validation_practices(row_practice)
                keen.test_edit_Practices()
                keen.test_validation_practices(2)
                if guid == guid:
                    self.driver.close()
                    if parent_guid == parent_guid:
                        self.driver.switch_to.window(parent_guid)
                        keen.close()
                        break
        keen.test_select_member_to_associate_Cpature_Full_Member_details()
        hospital_record=keen.test_hospitals(row_hospitals)
        keen.test_select_hospital_record(hospital_record)
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                action_utils.wait_for_element((Create_capture_member_details.hospital_record))
                keen_create.click_hospital_verify()
                keen.test_validation_hospitals(row_hospitals)
                keen.test_edit_hospitals()
                keen.test_validation_hospitals(2)
                if guid == guid:
                    self.driver.close()
                    if parent_guid == parent_guid:
                        self.driver.switch_to.window(parent_guid)
                        keen.close()
                        break
        keen.test_select_member_to_associate_Cpature_Full_Member_details()
        keen.test_click_physicians()
        physician_name=keen.test_physicians(row_physicians)
        keen.test_select_physician(physician_name)
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                action_utils.wait_for_element((Create_capture_member_details.physician_record_select))
                keen_create.select_physician_record()
                keen.test_validation_of_physicians(row_physicians)
                keen.test_edit_physicians()
                keen.test_validation_of_physicians(2)
                if guid == guid:
                    self.driver.close()
                    if parent_guid == parent_guid:
                        self.driver.switch_to.window(parent_guid)
                        keen.close()
                        break
    @allure.description("Creation of New Account")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.Account_Creation
    def test_new_lead_account(self):
        keen_test=Test_account_creation(self.driver)
        action_utils=ActionUtils(self.driver)
        keen=Keen_Account_creation(self.driver)
        row_account = number.get_random_number("Account_Creation")
        self.log.info("***** Lead Account creation ******")
        verify_account=action_utils.record_verification(row_account,'Account_Creation','account_creation')
        if verify_account == 'YES':
            existing_account=number.retrieve_value(row_account,'A',sheet_account,2)
            print(existing_account)
            self.log.info("***** Member record is already in Salesforce *****")
            self.driver.close()
            self.log.info("****** Closing the driver ******")
        else:
            self.log.info("***** Account is not exists in Salesforce *****")
            keen.New()
            action_utils.wait_for_element((Keen_Account_creation.enter_firstName))
            print("Random number:",row_account)
            status_value=keen_test.test_lead_creation(row_account)
            print("status value:",status_value)
            self.log.info("*****'YES' is saved in excell sheet*****")
            if status_value == "Keen Lead":
                assert keen.Warning_popup().is_displayed(), "popup is not displayed"
                keen.Back_To_Edit()
                keen.scope_of_appointment_date().clear()
                keen.click_save()
                account_created = keen.Success_Message()
                assert account_created.is_displayed(),"Toast message is not displayed"
                self.log.info("******Keen leads and Members record is saved******")
                number.write_result_in_to_excel_sheet(row_account, 'Account_Creation', 'AV')
            else:
                action_utils.wait_for_element((Keen_Account_creation.toast_message))
                account_created = keen.Success_Message()
                assert account_created.is_displayed(), "Success Message is not displayed"
                number.write_result_in_to_excel_sheet(row_account, 'Account_Creation', 'AP')
                self.log.info("*****'YES' is saved in excell sheet*****")
            keen_test.test_account_creation_of_keen_leads_and_members(row_account)
            self.log.info("***** validation of Lead Account creation ******")
            keen_test.test_validation_account_creation(row_account)
            self.log.info("***** Duplicate record cancel ******")
            keen_test.test_Duplicate_records_cancel(row_account)
            self.log.info("***** Created duplicate record and cancel ******")
            keen_test.test_Duplicate_records_Create(row_account)
    ### Associate related_persons to a memebr
    @allure.description("Creation of New Related Persons and Associate to a member")
    @allure.severity(allure.severity_level.NORMAL)
    def test_member_related_persons(self):
        keen_associatepom=Associate_Capture_full_Member_details(self.driver)
        keen_associate=Test_add_Member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        keen_create=Test_create_capture_full_member_details(self.driver)
        self.log.info("*****Select related persons ***** ")
        keen_associate.test_add_Related_persons()
        action_utils.wait_for_element((Associate_Capture_full_Member_details.new_caregiver_relatedpersons))
        keen_associatepom.click_newcaregiver_relatedperson()
        self.log.info("***** Enter caregiver details ****** ")
        action_utils.wait_for_element((Associate_Capture_full_Member_details.new_caregiver_relatedpersons))
        keen_create.enter_edit_data_caregivers(row_caregivers)
        keen_associate.test_assciate_relatedperson_caregiver()
        self.log.info("***** Related persons record is created and associated to member ******")
    ### Associate a Task and Loag a Call to a Member
    ### Verify Satisfaction Score
    @allure.description("Creation of New Task and New log a call and verify the satisfaction Score to a member")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.order(1)
    def test_tasks_and_log_a_call(self):
        keen=Test_New_Task(self.driver)
        keen_task=New_Task(self.driver)
        keen_log=Test_log_a_call(self.driver)
        action_utils = ActionUtils(self.driver)
        self.log.info("***** New Task is creating to associate for a member ******")
        keen.test_new_task_for_member(row_tasks,today,today)
        self.log.info("***** New Task is created and associate to a member ******")
        self.log.info("***** Validating the satisfaction score ******")
        score_task=keen_task.validation_satisfaction_score()
        keen_task.validation_related_to().click()
        action_utils.wait_for_element((New_Task.satisfaction_score))
        score=keen_task.check_satisfaction_score()
        satisfaction_score=score.text
        assert score_task == satisfaction_score,"Satisfaction Score is not matched"
        self.log.info("***** Validated the satisfaction score ******")
        self.log.info("***** Creating a log a call to a member ******")
        keen_log.test_log_a_call(row_tasks,today,today)
        self.log.info("***** Validating the satisfaction score ******")
        score_task = keen_task.validation_satisfaction_score()
        keen_task.validation_related_to().click()
        action_utils.wait_for_element((New_Task.satisfaction_score))
        score = keen_task.check_satisfaction_score()
        satisfaction_score = score.text
        assert score_task == satisfaction_score, "Satisfaction Score is not matched"

    #### Test Case Descirption:- Create New Lead and Quote Geneartion
    #### Test Steps:- Login to SFDC---> Click on Keen Leads and Members--->Click on Generate
    #### Fill the Generate quote details and Click on Transfer to sunfire.
    @allure.description("Quote Generation for Keen Lead")
    @pytest.mark.GenerateQuote
    def test_genarate_quote_new_creation(self):
        action_utils = ActionUtils(self.driver)
        keen_account=Keen_Account_creation(self.driver)
        keen_generate = Test_GenerateQuote(self.driver)
        Keen_Generate=Keen_Quote_Generation(self.driver)
        kee_Create = Create_capture_member_details(self.driver)
        row_account = number.get_random_number("Account_Creation")
        try:
            row_account = number.get_random_number("Account_Creation")
            self.log.info("***** Verifying the Keen lead in Salesforce *****")
            action_utils.wait_for_elements((Create_capture_member_details.Member))
            keen_members = kee_Create.select_member()
            Existing_account = None
            for member in keen_members:
                keen_member = member.get_attribute('title')
                print("existing members:", keen_member)
                if keen_member == 'AutomationTest User DoNOTdeletenew':
                    Existing_account = member
                    print("Length of title:", len(keen_member))
            if Existing_account is not None:
                print("selected_account:",Existing_account.text)
                # print("Length of title:", len(Existing_account))
                # self.log.info("Selected record to Generate Quote",member.text)
                Existing_account.click()
                self.log.info("***** Selected the Keen Member to initiate the generate Quote *****")
                self.log.info(("***** Generating the Quote for selected member *****"))
                keen_generate.test_generatequote_newaccount(row_account)
            else:
                print("Account is not present")
                self.log.info("***** Keen Member is not exists in salesforce *****")
                keen_generate.test_new_for_generate_quote(row_account)
                keen_generate.test_generatequote_newaccount(row_account)
        except Exception as ex:
            self.log.info("***** GenerateQuote Atuomation execution is failed *****")
            print(ex)
            email_sent = keen_aws_session()
            email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                                 "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                                 "subject": "GenerateQuote Automation Execution Failed"+" - "+today,
                                 "body": "GenerateQuoteAutomation results"})
        time.sleep(15)
        from datetime import datetime
        current_datetime = datetime.now()
        formatted_month_day = current_datetime.strftime("%m/%d")
        latest_date = formatted_month_day + "/" + "1947"
        action_utils.wait_for_element((Keen_Quote_Generation.dob))
        Keen_Generate.DoB_GenerateQuote().clear()
        Keen_Generate.DoB_GenerateQuote().send_keys(latest_date)
        action_utils.wait_for_element((Keen_Quote_Generation.gender))
        Keen_Generate.click_gender()
        time.sleep(10)
        keen_generate.test_advanced_need_assessment()
        time.sleep(15)
        keen_generate.test_Medicare_supplimentary_tab(row_account)
        time.sleep(15)
        keen_generate.test_plan_recommendation_tab()
        # os.system("sudo shutdown now")

    @pytest.mark.skip
    def test_schedule_Calendly_meeting(self):
        keen_account = Keen_Account_creation(self.driver)
        action_utils = ActionUtils(self.driver)
        keen = Keen_Scedule_Meeting(self.driver)
        action = ActionChains(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        substring = "Test - Calendly"
        lead = keen_create.select_member()
        member=lead[1]
        member.click()
        member_name = keen.schedule_meeting_member()
        print(member_name)
        name = member_name.text
        print(name)
        email_lead = keen_account.validation_of_email()
        phone_lead = keen_account.validation_of_Phone()
        lead_phone = action_utils.convert_string(phone_lead)
        action_utils.wait_for_element((Keen_Scedule_Meeting.meeting))

        keen.click_schedule_meeting()
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                keen.accept_cookies()
                title = keen.title_calendly()
                verify_title = title.is_displayed()
                if verify_title:
                    assert True
                else:
                    assert False
                action_utils.wait_for_element((Keen_Scedule_Meeting.test))
                keen.click_test()
                page = keen.verify_date_sheet()
                verify_page = page.is_displayed()
                if verify_page:
                    assert True
                else:
                    assert False
                avaliable_dates = keen.pick_dates()
                dates = (avaliable_dates.get_attribute("aria-label"))
                split_values = dates.split("-")
                first_part = split_values[0].strip()
                date_match = re.search(r"(\d+)", first_part)
                date = (date_match.group(1))
                meeting_date = keen.select_dates()
                for meeting in meeting_date:
                    if meeting.text == date:
                        print("Test Pass")
                        action.move_to_element(meeting).click().perform()
                        break
                avaliable_time = keen.select_time()
                for time in avaliable_time:
                    print(time.text)
                    if time.text[1]:
                        action.move_to_element(time).click().perform()
                        break
                action_utils.wait_for_element((Keen_Scedule_Meeting.next))
                keen.click_next()
                action_utils.wait_for_element((Keen_Scedule_Meeting.test_page))
                schedule_meeting = keen.schedule_member_page()
                if schedule_meeting.is_displayed():
                    assert True
                else:
                    assert False
                action_utils.wait_for_element((Keen_Scedule_Meeting.name))
                keen.enter_name(name)
                action_utils.wait_for_element((Keen_Scedule_Meeting.email))
                keen.enter_emali(email_lead)
                action_utils.wait_for_element((Keen_Scedule_Meeting.phone))
                keen.enter_phone_number("+1" + ' ' + lead_phone)
                action_utils.wait_for_element((Keen_Scedule_Meeting.schedule_meeting))
                keen.submit_schedule_meeting()
                action_utils.wait_for_element((Keen_Scedule_Meeting.confirmed_meeting))
                success_message = keen.verify_confirmed_meeting()
                if success_message.is_displayed():
                    assert True
                else:
                    assert False
                if guid == guid:
                    self.driver.close()
                if guid == parent_guid:
                    self.driver.switch_to.window(parent_guid)
                    self.driver.refresh()
                    BD_link = keen.verify_meeting_link()
                    for BD_activity in BD_link:
                        print(BD_activity.text)
                        if substring in BD_activity.text:
                            assert True
                        else:
                            assert False

    @pytest.mark.soa
    def test_soa_for_a_Member(self):
        keen_create = Create_capture_member_details(self.driver)
        keen_soa_test=Test_SOA_Form(self.driver)
        keen_soa_test.test_createSOA_for_Member(row_soa_number)
    @pytest.mark.example
    def test_one_one(self):
        actiuon_utils=ActionUtils(self.driver)
        keen_task_test=Test_New_Task(self.driver)
        keen_task=New_Task(self.driver)
        keen_create=Test_create_capture_full_member_details(self.driver)
        keen_create.test_select_member_to_associate_Cpature_Full_Member_details()
        actiuon_utils.wait_for_element((New_Task.task))
        keen_task.click_Task()
        keen_task_test.test_task(row_tasks)
        # keen_task_test.test_create_new_task()
    def test_example(self):
        keen_Create=Create_capture_member_details(self.driver)
        Keen_test_soa=Test_SOA_Form(self.driver)
        action_utils=ActionUtils(self.driver)
        Keen_test_soa.test_createSOA_for_Member(row_soa_number)

    def test_test(self):
        keen_soa = Create_SOA_Form(self.driver)
        action_utils = ActionUtils(self.driver)
        action = ActionChains(self.driver)
        self.log.info("***** Verify the docusign document *****")
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.log.info("***** switch to Gmail home page *****")
        # Perform actions in the new tab/window (e.g., logging into email)
        self.driver.get("https://yopmail.com/")
        # self.log.info("***** Login in to Gmail to verify docusign *****")
        self.driver.find_element(By.XPATH, "//input[@name='login']").send_keys("anilkumarmaddula@yopmail.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@title='Check Inbox @yopmail.com']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@id='refresh']").click()
        self.driver.refresh()
        # action_utils.wait_for_element((Create_SOA_Form.sign_request))
        # keen_soa.select_document_sign_request()
        self.log.info("***** Docusign erequest message is selected *****")
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@name='ifmail']")
        self.driver.switch_to.frame(iframe_element)
        action_utils.wait_for_element((Create_SOA_Form.view_document))
        keen_soa.click_document()
        self.log.info("***** Review document message is displayed *****")
        self.driver.switch_to.window(self.driver.window_handles[2])
        # if guid != parent_guid:
        #     self.driver.switch_to.window(guid)
        #     self.log.info("***** switch to review document *****")
        action_utils.wait_for_element((Create_SOA_Form.verify_accesscode_page))
        assert keen_soa.verify_access_code_page().is_displayed(), "Access code page is not displayed"
        validate_button = keen_soa.verify_validation_button()
        if validate_button.is_enabled():
            self.log.info("***** Access code is update *****")
            keen_soa.click_validate_button()
        else:
            self.log.info("***** Access code is not update *****")
            keen_soa.enter_verification_code("4653")
            keen_soa.click_validate_button()
        try:
            action_utils.wait_for_element((Create_SOA_Form.phone_security))
            assert keen_soa.verify_phone_security().is_displayed(), "Phone security popup is not displayed"
            keen_soa.verify_phone_security_continue()
        except Exception as ex:
            self.log.info("***** Security phone check is not displayed *****")
        action_utils.wait_for_element((Create_SOA_Form.review_document))
        assert keen_soa.verify_review_act_document(), "Please Review & Act on These Documents page is not displayed"
        keen_soa.click_continue_document()
        # self.driver.switch_to.window(self.driver.window_handles[4])
        self.log.info("***** Member need to sign into document *****")
        action_utils.wait_for_element((Create_SOA_Form.signature_of_member))
        keen_soa.enter_member_signature("Anil")
        self.log.info("***** Member is signed into document *****")
        keen_soa.click_finish()
        self.log.info("***** Finish the review the document *****")
        try:
            action_utils.wait_for_element((Create_SOA_Form.verify_sign))
            assert keen_soa.verify_sign_popup().is_displayed(), "Done signing popup is not displayed"
            keen_soa.click_sign_continue()
        except Exception as ex:
            print(ex)
        self.log.info("***** Signing is contiuned *****")

    @pytest.mark.existing_user
    def test_smartQuote_for_existing_user(self):
        keen_generate_test=Test_GenerateQuote(self.driver)
        kee_Create = Create_capture_member_details(self.driver)
        action = ActionChains(self.driver)
        keen_GQ=Keen_Quote_Generation(self.driver)
        action_utils = ActionUtils(self.driver)
        self.log.info("***** Verifying the Keen lead in Salesforce *****")
        action_utils.wait_for_elements((Create_capture_member_details.Member))
        keen_member = kee_Create.select_member()
        Existing_account = None
        for member in keen_member:
            keen_member = member.get_attribute('title')
            print("existing members:", keen_member)
            if keen_member == 'AutomationTest User DoNOTdeletenew':
                Existing_account = member
                print("Length of title:", len(keen_member))
        if Existing_account is not None:
            print("selected_account:", Existing_account.text)
            # print("Length of title:", len(Existing_account))
            # self.log.info("Selected record to Generate Quote",member.text)
            action.move_to_element(Existing_account).click().perform()
        # keen_generate_test.test_generatequote_newaccount(row_number_account=3)
        action_utils.wait_for_element((Keen_Quote_Generation.smart_quote))
        keen_GQ.click_smart_Quote()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(30)
        keen_generate_test.test_advanced_need_assessment()
        keen_generate_test.test_Medicare_supplimentary_tab(row_account)
        keen_generate_test.test_plan_recommendation_tab()

    @pytest.mark.smartquote_new_user
    def test_smartquote_for_New_user(self):
        keen_generate = Test_GenerateQuote(self.driver)
        # keen_generate.test_aledade_data()
        row_account = number.get_random_number("Account_Creation")
        keen_generate.test_new_for_generate_quote(row_account)
        keen_generate.test_generatequote_newaccount(row_account)
        keen_generate.test_advanced_need_assessment()
        keen_generate.test_Medicare_supplimentary_tab(row_account)
        keen_generate.test_plan_recommendation_tab()


# if __name__ == "__main__":
#     print("url:",os.environ('url'))



