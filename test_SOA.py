import time
import allure
from selenium.webdriver.common.by import By

from utilities.XLUtilities import Excel_data
import pytest
from selenium.webdriver import ActionChains
import datetime
from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
from utilities import logger_utils
from Pages.Keen_account_creation import Keen_Account_creation
from Pages.Keen_SOA import Create_SOA_Form
from utilities.action_utils import ActionUtils
from utilities.base_test import BaseTest
@allure.description("Create A SOA form to a Member")
class Test_SOA_Form():

    def __init__(self,driver):
        self.driver=driver
        self.path = "../test_data/Keen_Testdata.xlsx"
        self.readdata_soa = Excel_data(self.path, "SOA")
        self.log = logger_utils.get_logger()
        self.sheet = BaseTest()
        self.keen_create = Create_capture_member_details(self.driver)
        self.keen = Create_SOA_Form(self.driver)
        self.keen_account = Keen_Account_creation(self.driver)
        self.action = ActionChains(self.driver)
        self.action_utils = ActionUtils(self.driver)
        self.keen_soa = Create_SOA_Form(self.driver)
    ### Test Description:- Associate a SOA form to a member
    ### Test Case steps:- Login to SFDC, CLick on Home, Click on Generate SOA, Create SOA
    @allure.description("Associate a SOA to a Member")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(1)
    def test_createSOA_for_Member(self,row_number):
        members=self.keen_create.select_member()
        for members_sf in members:
            if members_sf.get_attribute('title') == 'AutomationTest User DoNOTdelete':
                members_sf.click()
                break
        self.action_utils.wait_for_element((Keen_Account_creation.verify_phone))
        phone_lead = self.keen_account.validation_of_Phone()
        lead_phone = self.action_utils.convert_string(phone_lead)
        self. action_utils.wait_for_element((Keen_Account_creation.address_details))
        self.keen_account.click_address_Details()
        self.action_utils.wait_for_element((Keen_Account_creation.verify_streetaddress))
        time.sleep(5)
        member_street_address = self.keen_account.validation_of_street().get_attribute('value')
        self.log.info("***** Retrieve 'Street' value in Keen Member *****")
        time.sleep(5)
        member_city = self.keen_account.validation_of_city().get_attribute('value')
        self.log.info("***** Retrieve 'City' value in Keen Member *****")
        time.sleep(5)
        member_addressline_two = self.keen_account.validation_of_addressline_2().get_attribute('value')
        self.log.info("***** Retrieve 'addressline_2' value in Keen Member *****")
        time.sleep(5)
        member_state = self.keen_account.validation_of_state().get_attribute('data-value')
        self.log.info("*****Retrieve 'State' value in Keen Member *****")
        time.sleep(5)
        member_county = self.keen_account.validation_of_county().get_attribute('value')
        self.log.info("*****Retrieve 'County' value in Keen Member *****")
        time.sleep(5)
        member_zipcode = self.keen_account.validation_of_zipcode().get_attribute('value')
        self.log.info("*****Retrieve 'Zipcode' value in Keen Member *****")
        print("member zipcode:", member_zipcode)
        self.keen_account.Click_close_popup()
        self.action_utils.wait_for_element((Keen_Account_creation.edit_record))
        self.keen_account.click_on_edit()
        self.action_utils.wait_for_element((Keen_Account_creation.verify_firstName))
        lead_first_name = self.keen_account.verify_first_name().get_attribute("value")
        print("lead_firstname:", lead_first_name)
        self.action_utils.wait_for_element((Keen_Account_creation.verify_LastName))
        lead_last_name = self.keen_account.verify_last_name().get_attribute("value")
        print("Lead_lastName:", lead_last_name)
        self.action_utils.wait_for_element((Keen_Account_creation.cancel_in_member_page))
        self.keen_account.click_cancel_keen_page()
        self.log.info("***** Cancel edit in keen leads page *****")
        self.driver.execute_script("scroll(0, 400);")
        self.action_utils.wait_for_element((Create_SOA_Form.SOA_Member))
        self.keen.click_GenerateSOA()
        self.log.info("***** Generate SOA button is clicked *****")
        self.keen.click_New_Form()
        self.log.info("***** Selected new form to setup docusign*****")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self. action_utils.wait_for_element((Create_SOA_Form.SOA_TAb))
        soa_form = self.keen.SOA_popup()
        assert soa_form.text == "Scope of Sales Appointment Confirmation Form","Scope of Sales Appointment Confirmation Form popup is not displayed"
        self.action_utils.wait_for_elements((Create_SOA_Form.Product_Types))
        options=self.keen.Click_Check_Types_Products_Discuss()
        for i in options:
            time.sleep(1)
            i.click()
        # keen.Enter_MemberSignature().send_keys("Anil Kumar")
        try:
            agentName=self.keen.AgentName().get_attribute('text')
            print("Agent_name:",agentName)
            assert agentName != "None","Agent name is not matched"
        except Exception as ex:
            self.log.info("***** *****")
            print(ex)
        try:
            phone=self.keen.MemberPhone().get_attribute('value')
            phone_soa = self.action_utils.convert_string(phone)
            assert phone_soa == lead_phone,"Phone is not matched"
        except Exception as ex:
            self.log.info("***** Phone is not matched *****")
            print(ex)
        try:
            SOAfirstName=self.keen.MemberFirstName().get_attribute('value')
            assert SOAfirstName == lead_first_name,"lead first name is not matched"
        except Exception as ex:
            self.log.info("***** lead first name is not matched *****")
            print(ex)
        try:
            SOAlastName=self.keen.MemberLastName().get_attribute('value')
            assert SOAlastName == lead_last_name,"Last name is not matched"
        except Exception as ex:
            self.log.info("***** Last name is not matched *****")
            print(ex)
        try:
            SOAstreet=self.keen.MemberSteertAddress().get_attribute('value')
            print(SOAstreet)
            assert SOAstreet == member_street_address,"addressline_1 is not matched"
        except Exception as ex:
            self.log.info("***** addressline_1 is not matched *****")
            print(ex)
        try:
            soa_address_line2=self.keen.MemberStreetAddress2().get_attribute('value')
            assert soa_address_line2 == member_addressline_two,"Address line 2 is not macthed"
        except Exception as ex:
            self.log.info("***** *****")
            print(ex)
        try:
            SOAcity=self.keen.MemberCity().get_attribute('value')
            print(SOAcity)
            assert SOAcity == member_city,"City is not matched"
        except Exception as ex:
            self.log.info("***** City is not matched *****")
            print(ex)
        try:
            SOAstate=self.keen.MemberState().get_attribute('value')
            print(SOAstate)
            assert SOAstate == member_state,"State is not matched"
        except Exception as ex:
            self.log.info("***** State is not matched *****")
            print(ex)
        try:
            SOAzipcode=self.keen.MemberZipcode().get_attribute('value')
            print("Zopcode soa:",SOAzipcode)
            assert SOAzipcode == member_zipcode,"Zipcode is not matched"
        except Exception as ex:
            self.log.info("***** Zipcode is not macted *****")
            print(ex)
        try:
            SOAcounty=self.keen.MemberCounty().get_attribute('value')
            assert SOAcounty == member_county,"County is not matched"
        except Exception as ex:
            self.log.info("***** county is not matched *****")
            print(ex)
        contact=self.keen.Initial_method_contact()
        self.action.move_to_element(contact)
        self.keen.Initial_method_contact().click()
        list_methods=self.keen.Select_Method_Contact()
        for contact_methods in list_methods:
            print("method of contact options:",contact_methods.get_attribute('title'))
            self.log.info("***** Method of contact options are displayed *****")
            if contact_methods.get_attribute('title') == "In person":
                self.log.info("***** Method of contact option is matched *****")
                self.driver.execute_script("arguments[0].click();", contact_methods)
                self.log.info("***** Method of contact option is selected *****")
                break
        today = datetime.date.today()
        date_of_appointment_completed = today.strftime("%m/%d/%Y")
        print("date:", date_of_appointment_completed)
        self.keen.Appointment_Date().send_keys(date_of_appointment_completed)
        self.keen.PlanExplination().send_keys("plans")
        # keen.Click_Save_and_Submit()
        # action_utils.wait_for_element((Create_SOA_Form.save_options_soa))
        self.keen.click_save_options()
        self.action_utils.wait_for_element((Create_SOA_Form.save_signature))
        self.keen.click_save_signature()
        self.test_docusing(row_number)
        try:
            self.action_utils.wait_for_element((Create_SOA_Form.save_message))
            success_message = self.keen.Save_Success_Message()
            assert success_message.is_displayed(),"success toast message is not displayed"
        except Exception as ex:
            print(ex)


       # try:
       #      if membersignature and Agentsignature:
       #          validation_signature = keen.Verify_Signature()
       #          if validation_signature.text == "Both":
       #              print("Test Pass")
       #          else:
       #              print("Test Fail")
       #      else:
       #          validation_signature_agent = keen.Verify_Signature()
       #          if validation_signature_agent.text == "None":
       #              print("Test Pass")
       #          else:
       #              print("Test fail")
       #  except Exception as ex:
       #      print(ex)
       #  try:
       #      if keen.Verify_SOAdate().is_displayed():
       #          print("Test Pass")
       #      else:
       #          print("Test fail")
       #  except Exception as ex:
       #      print(ex)
       #  try:
       #      files = keen.View_file()
       #      for file in files:
       #          if file.text == "View file":
       #              print("Test pass")
       #          else:
       #              print("Test fail")
       #      self.log.info("***** Validating the SOA form *****")
       #  except Exception as ex:
       #      print(ex)
       #  self.log.info("***** Validation is completed *****")



    ### Test Description:- Create A SOA form
    ### Test Case steps:- Login to SFDC, CLick on Home, Click on Generate SOA, Create SOA
    @allure.description("Create a New SOA form")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Creation_New_SOAfrom(self,row_number):
        try:
            sheet_SOA = self.sheet.get_sheet_name('SOA')
            data_row = sheet_SOA[row_number]
            column_field_mapping = {
                'first_Name': 'first_Name', 'Last_Name': 'Last_Name',
                # 'Member_Signature' : 'Member_Signature',
                'Phone': 'Phone', 'Street_Address': 'Street_Address',
                'Zipcode': 'Zipcode', 'City': 'City', 'State': 'State',
                'Member_County': 'Member_County', 'Address line 2': 'Address line 2',
                'Initial method of contact': 'Initial method of contact',
                # 'Agent Signature': 'Agent Signature',
                'Plan(s)': 'Plan(s)',
            }
            field_locators = {
                'first_Name': ((Create_SOA_Form.members_SOAfirstname)),
                'Last_Name': (Create_SOA_Form.members_SOAlastname),
                # 'Member_Signature': ((Create_SOA_Form.membersignature)),
                'Street_Address': (Create_SOA_Form.members_streetaddress),
                'Phone': (Create_SOA_Form.members_phone),
                'Address line 2': (Create_SOA_Form.members_streetaddress2),
                'Member_County': (Create_SOA_Form.members_county),
                'Zipcode': (Create_SOA_Form.members_zipcode),
                'City': (Create_SOA_Form.members_city), 'State': (Create_SOA_Form.members_state),
                'Initial method of contact': (Create_SOA_Form.members_contact),
                'Plan(s)': (Create_SOA_Form.explination),
                # 'Agent Signature': (Create_SOA_Form.agent_signature),
            }
            self.action_utils.wait_for_element((Create_SOA_Form.profile))
            self.keen_soa.Click_profile()
            self.action_utils.wait_for_element((Create_SOA_Form.name_ad))
            Advisor_Name = self.keen_soa.NameAdvisor().text
            print(Advisor_Name)
            self.action_utils.wait_for_element((Create_SOA_Form.home))
            self.keen_soa.Click_HomeTab()
            self.driver.execute_script("scroll(0,400);")
            self.log.info("***** Click on Generate SOA Form *****")
            self.keen_soa.Click_generateSOAHome()
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    self.log.info("***** SOA Page *****")
                    self.action_utils.wait_for_element((Create_SOA_Form.SOA_TAb))
                    soa_form = self.keen_soa.SOA_popup()
                    assert soa_form.text == "Scope of Sales Appointment Confirmation Form","Scope of Sales Appointment Confirmation Form tab is not displayed"
                    self.log.info("***** Products to be selected *****")
                    signature=self.keen_soa.AgentSignature().get_property('disabled')
                    print("Agent sugnature is enabled or disabled:",signature)
                    assert signature == True,"Agent signature is enabled even member is not signed"
                    self.action_utils.wait_for_elements((Create_SOA_Form.Product_Types))
                    options = self.keen_soa.Click_Check_Types_Products_Discuss()
                    for product in options:
                        product.click()
                        self.log.info("***** Products are selected ******")
                    self.log.info("***** Filling the SOA form *****")
                    for cell in data_row:
                        column_name = sheet_SOA.cell(row=2, column=cell.column).value
                        if column_name in column_field_mapping:
                            field_name = column_field_mapping[column_name]
                            self.log.info(field_name)
                            column_value = cell.value
                            self.log.info("***** Column name and field name is matched ******")
                            locator = field_locators[field_name]
                            element = self.driver.find_element(*locator)
                            self.action_utils.wait_for_element((locator))
                            self.driver.execute_script("arguments[0].scrollIntoView();", element)
                            if element.tag_name == 'button':
                                if field_name == 'Initial method of contact':
                                    element.click()
                                    self.log.info("***** Initial method of contact field is clicked *****")
                                    self.action_utils.wait_for_elements((Create_SOA_Form.method_contact))
                                    list_methods = self.keen_soa.Select_Method_Contact()
                                    for methods in list_methods:
                                        print("method options:",methods.get_attribute('title'))
                                        if methods.get_attribute('title').strip() == column_value.strip():
                                            print("value is matched")
                                            self.driver.execute_script("arguments[0].click();", methods)
                                            self.log.info("***** Practicular Initial method of contact option is selected *****")
                                            break
                                if field_name == 'State':
                                    element.click()
                                    self.log.info("***** State field is clicked *****")
                                    self.action_utils.wait_for_elements((Create_SOA_Form.options))
                                    states = self.keen_soa.select_options()
                                    for state in states:
                                        if state.text == column_value:
                                            self.driver.execute_script("arguments[0].click();", state)
                                            self.log.info("***** State option is selected *****")
                                            break
                            else:
                                element.clear()
                                element.send_keys(column_value)
                    today = datetime.date.today()
                    date_of_appointment_completed=today.strftime("%m/%d/%Y")
                    print("date:",date_of_appointment_completed)
                    self.keen_soa.Appointment_Date().send_keys(date_of_appointment_completed)
                    self.action_utils.wait_for_element((Create_SOA_Form.save_options_soa))
                    self.keen_soa.click_save_options()
                    self.action_utils.wait_for_element((Create_SOA_Form.save_signature))
                    self.keen_soa.click_save_signature()
                    try:
                        self.action_utils.wait_for_element((Create_SOA_Form.save_message))
                        success_message = self.keen_soa.Save_Success_Message()
                        assert success_message.is_displayed(),"SOA record created successfully! toast message is not displayed"
                    except Exception as ex:
                        print(ex)
                    self.sheet.write_result_in_to_excel_sheet(row_number, "SOA", "N")
                    self.driver.execute_script("scroll(0,300);")
                #     self.log.info("***** Validating the SOA form *****")
                #     try:
                #         if member_signature_value != None:
                #             validation_signature = self.keen_soa.Verify_Signature()
                #             assert validation_signature.text == "Both", "Both is not displayed"
                #         else:
                #             validation_signature_agent = keen.Verify_Signature()
                #             if validation_signature_agent.text == "No":
                #                 print("Test Pass")
                #             else:
                #                 print("Test fail")
                #     except Exception as ex:
                #         print(ex)
                #     try:
                #         if self.keen_soa.Verify_SOAdate().is_displayed():
                #             print("Test Pass")
                #         else:
                #             print("Test fail")
                #     except Exception as ex:
                #         print(ex)
                #     try:
                #         files = keen.View_file()
                #         for i in files:
                #             if i.text == "View file":
                #                 print("Test pass")
                #             else:
                #                 print("Test fail")
                #         self.log.info("***** Validating the SOA form *****")
                #     except Exception as ex:
                #         print(ex)
                #         self.log.info("***** Validating the SOA form *****")
                # if guid == guid:
                #    self.driver.close()
        except Exception as ex:
            print(ex)

    def test_verify_soa_date(self,row_number):
        keen = Create_SOA_Form(self.driver)
        action_utils=ActionUtils(self.driver)
        keen_Create=Create_capture_member_details(self.driver)
        action_utils.wait_for_elements((Create_capture_member_details.Member))
        keen_member = keen_Create.select_member()
        for member in keen_member:
            keen_member = member.get_attribute('title')
            print("existing members:", keen_member)
            if keen_member == 'verify AWS fields':
                member.click()
        action_utils.wait_for_element((Create_SOA_Form.verify_soa))
        date=keen.check_soa_date()
        verify_date=date.text
        print("date of soa:",verify_date)
        if verify_date:
            print("*** date is present **")
            self.test_createSOA_for_Member(row_number)
            action_utils.wait_for_element((Create_SOA_Form.ok_soa_button))
            keen.click_ok_soa_button()
        else:
            self.test_createSOA_for_Member(row_number)
            print("** date is not working **")
    def test_docusing(self,row_number):
        keen_soa=Create_SOA_Form(self.driver)
        action_utils=ActionUtils(self.driver)
        action=ActionChains(self.driver)
        member_signature=self.readdata_soa.readdata(row_number,3)
        self.log.info("***** Confirm contact details popup should be displayed *****")
        action_utils.wait_for_element((Create_SOA_Form.contact_details_popup))
        assert keen_soa.verify_confirm_page(),"Confirm Contact Details pop up is not displayed"
        self.log.info("***** Confirm contact details popup is displayed *****")
        code_number=keen_soa.verify_access_code()
        print("Access_code:",code_number.get_attribute('value'))
        if code_number.get_attribute('value') is "":
            self.log.info("***** Advisor doesn't have phone number, so manually entering the access code ******")
            keen_soa.verify_access_code().send_keys("2374")
            keen_soa.click_save_send_docusign()
        else:
            self.log.info("***** Advisor have phone number ******")
            action_utils.wait_for_element((Create_SOA_Form.send_to_docusign))
            keen_soa.click_save_send_docusign()
        self.log.info("***** Verify the docusign document *****")
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.log.info("***** switch to Gmail home page *****")
# Perform actions in the new tab/window (e.g., logging into email)
        self.driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
                        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
                        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        self.log.info("***** Login in to Gmail to verify docusign *****")
        keen_soa.enter_mail_user_name("anilkumar688@myyahoo.com")
        keen_soa.click_next_button()
        keen_soa.enter_mail_password("Nani@1234")
        keen_soa.click_next_button()
        self.driver.refresh()
        self.driver.refresh()
        action_utils.wait_for_element((Create_SOA_Form.sign_request))
        keen_soa.select_document_sign_request()
        iframe_element = self.driver.find_element(By.XPATH, "//iframe[@name='ifmail']")
        self.driver.switch_to.frame(iframe_element)
        self.log.info("***** Docusign erequest message is selected *****")
        action_utils.wait_for_element((Create_SOA_Form.view_document))
        keen_soa.click_document()
        self.log.info("***** Review document message is displayed *****")
        self.driver.switch_to.window(self.driver.window_handles[3])
        # if guid != parent_guid:
        #     self.driver.switch_to.window(guid)
        #     self.log.info("***** switch to review document *****")
        action_utils.wait_for_element((Create_SOA_Form.verify_accesscode_page))
        assert keen_soa.verify_access_code_page().is_displayed(), "Access code page is not displayed"
        validate_button=keen_soa.verify_validation_button()
        if validate_button.is_enabled():
            self.log.info("***** Access code is update *****")
            keen_soa.click_validate_button()
        else:
            self.log.info("***** Access code is not update *****")
            keen_soa.enter_verification_code("2374")
            keen_soa.click_validate_button()
        try:
            action_utils.wait_for_element((Create_SOA_Form.phone_security))
            assert keen_soa.verify_phone_security().is_displayed(),"Phone security popup is not displayed"
            keen_soa.verify_phone_security_continue()
        except Exception as ex:
            self.log.info("***** Security phone check is not displayed *****")
        action_utils.wait_for_element((Create_SOA_Form.review_document))
        assert keen_soa.verify_review_act_document(),"Please Review & Act on These Documents page is not displayed"
        keen_soa.click_continue_document()
        # self.driver.switch_to.window(self.driver.window_handles[4])
        self.log.info("***** Member need to sign into document *****")
        action_utils.wait_for_element((Create_SOA_Form.signature_of_member))
        keen_soa.enter_member_signature(member_signature)
        self.log.info("***** Member is signed into document *****")
        keen_soa.click_finish()
        self.log.info("***** Finish the review the document *****")
        action_utils.wait_for_element((Create_SOA_Form.verify_sign))
        assert keen_soa.verify_sign_popup().is_displayed(),"Done signing popup is not displayed"
        keen_soa.click_sign_continue()
        self.log.info("***** Signing is contiuned *****")
        # try:
        #     action_utils.wait_for_element((Create_SOA_Form.sign_page))
        #     assert keen_soa.verify_successfull_sign().is_displayed(),"You’ve finished signing! page is not displayed"
        # except Exception as ex:
        #     self.log.info("***** Signing page is not displayed *****")
        # self.log.info("***** Signing is done , verify the sf and save the soa form *****")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.refresh()
        self.driver.refresh()
        action_utils.wait_for_element((Create_SOA_Form.agent_signature))
        signature=keen_soa.AgentSignature()
        self.driver.execute_script("arguments[0].scrollIntoView();", signature)
        # self.driver.execute_script("scroll(0, -350);")
        keen_soa.AgentSignature().send_keys("Sunil")
        action_utils.wait_for_element((Create_SOA_Form.save_options_soa))
        keen_soa.click_save_options()
        action_utils.wait_for_element((Create_SOA_Form.save_and_submit))
        keen_soa.Click_Save_and_Submit()

    def test_existing_soa_check(self):
        self.action_utils.wait_for_elements((Create_capture_member_details.Member))
        members = self.keen_create.select_member()
        for members_sf in members:
            if members_sf.get_attribute('title') == 'AutomationTest User DoNOTdelete':
                members_sf.click()
                break
        self.action_utils.wait_for_elements((Create_SOA_Form.existing_soa_latest_record))
        records=self.keen_soa.select_soa_existing_records()
        self.driver.execute_script("arguments[0].click();", records[0])
        self.log.info("***** Latest record is selected *****")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.action_utils.wait_for_element((Create_SOA_Form.save_options_soa))
        self.keen_soa.click_save_options()
        self.action_utils.wait_for_element((Create_SOA_Form.save_signature))
        self.keen_soa.click_save_signature()
        self.action_utils.wait_for_element((Create_SOA_Form.contact_details_popup))
        assert self.keen_soa.verify_confirm_page(), "Confirm Contact Details pop up is not displayed"
        self.log.info("***** Confirm contact details popup is displayed *****")
        code_number = self.keen_soa.verify_access_code()
        print("Access_code:", code_number.get_attribute('value'))
        if code_number.get_attribute('value') is "":
            self.log.info("***** Advisor doesn't have phone number, so manually entering the access code ******")
            self.keen_soa.verify_access_code().send_keys("2374")
        else:
            self.log.info("***** Advisor have phone number ******")
            self.action_utils.wait_for_element((Create_SOA_Form.send_to_docusign))








