import allure
from selenium.common import TimeoutException

from Pages.Keen_Associate_capture_full_member_details import Associate_Capture_full_Member_details
from Pages.Keen_Login import Keen_login
from Pages.aws import keen_aws_session
from selenium.webdriver import ActionChains
import time
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.Keen_account_creation import Keen_Account_creation
from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
from utilities.XLUtilities import Excel_data
from Pages.Keen_GenerateQuote import Keen_Quote_Generation
from utilities import logger_utils
from utilities.action_utils import ActionUtils
from utilities.base_test import BaseTest
from datetime import datetime
# import datetime
# now = datetime.datetime.now()
# today = now.strftime("%m/%d/%Y")
class Test_GenerateQuote():
    log = logger_utils.get_logger()
    path = "../test_data/Keen_Testdata.xlsx"
    today = datetime.today()
    formatted_date = today.strftime("%m/%d/%Y")
    readdata_account = Excel_data(path, "Account_Creation")
    readdata_medications = Excel_data(path, "Medication")
    readdata_physicians = Excel_data(path, "Physicians")
    readdata_pharmacies = Excel_data(path, "Pharmacies")
    sheet=BaseTest()
    def __init__(self,driver):
        self.driver=driver
        self.action_utils = ActionUtils(self.driver)
        self.action=ActionChains(self.driver)
        self.keen = Keen_Account_creation(self.driver)
        self.keen_login = Keen_login(self.driver)
        self.Keen_create = Create_capture_member_details(self.driver)
        self.Keen_Generate = Keen_Quote_Generation(self.driver)
        self.Keen_associate=Associate_Capture_full_Member_details(self.driver)
        self.account_data=self.readdata_account
    def test_login_to_advisor_GenerateQuote(self):
        action_utils = ActionUtils(self.driver)
        keen = Keen_Account_creation(self.driver)
        keen_login = Keen_login(self.driver)
        self.log.info("***** click on settings *****")
        action_utils.wait_for_element((Keen_Account_creation.setup_settings))
        self.log.info("***** click on setup option *****")
        keen.click_setup_settings()
        action_utils.wait_for_element((Keen_Account_creation.setup_option))
        keen.click_setup_option().click()
        window_handles = []
        parent_guid = self.driver.current_window_handle
        window_handles.append(parent_guid)
        All_windows = self.driver.window_handles
        for guid in All_windows:
            if guid != parent_guid:
                self.log.info("***** Navigate to setup windows *****")
                self.driver.switch_to.window(guid)
                action_utils.wait_for_element((Keen_Account_creation.quick_find))
                self.log.info("***** Search users to select advisor *****")
                keen.search_users_in_quickfind("Users")
                action_utils.wait_for_element((Keen_Account_creation.select_users))
                keen.click_users()
                self.log.info("***** Users option is selected *****")
                action_utils.wait_for_element((Keen_Account_creation.users_page))
                assert keen.verify_usres_page().is_displayed,"Users are not selected"
                time.sleep(10)
                # action_utils.wait_for_element((Keen_Account_creation.login_advisor))
                # WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,"//a[@title='Login - Record 18 - Vijayaraghavan, Arthi' and text()='Login']")))
                keen.click_advisor()
                self.log.info("***** Advisor is selected *****")
                if guid != window_handles[1]:
                    self.driver.switch_to.window(window_handles[1])
                    keen_login.keen_leads_members()
                    self.log.info("***** Keen leads and members tab is displayed*****")
    ### Test Description : Creating a new keen lead for generate a quote
    ### Test steps : login to SFDC ....>click on Keen leads and Members.....>click new
    ####....> Fill the data as per the test data ...> Click on Save.
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Create a New Keen Leads and Membres")
    def test_new_for_generate_quote(self, row_number):
        action_utils = ActionUtils(self.driver)
        current_date = datetime.today().date()
        last_name = self.sheet.convert_date_to_string(current_date)
        action_utils.wait_for_element((Keen_Account_creation.new_button))
        self.keen.New()
        sheet_name = 'Account_Creation'
        sheet = self.sheet.workbook[sheet_name]
        data_row = sheet[row_number]
        column_field_mapping = {
            'first_Name': 'first_Name', 'Middle_Name': 'MiddleName',
            'Nickname': 'Nickname',
            'DoB': 'DoB',
            'Email': 'Email',
            'Phone': 'Phone',
            'Street_Address': 'Street_Address',
            'Gender': 'Gender',
            'MedicareID': 'MedicareID', 'MedcaidID': 'MedcaidID',
            'Part_A enrollment date': 'Part_A enrollment date',
            'Part_B enrollment date': 'Part_B enrollment date',
            'Medicaid_status_verification_date': 'Medicaid_status_verification_date',
            'SSN': 'SSN', 'Status': 'Status',
            'Zipcode': 'Zipcode', 'City': 'City', 'State_Newcreation': 'State',
            'Member_County': 'Member_County', 'Addressline2': 'Addressline2',
            'Disposition': 'Disposition','Medicaid_Category' : 'Medicaid_Category','low_income_subsidy' : 'low_income_subsidy',
            'Member_ID': 'Member_ID'
        }
        field_locators = {
            'first_Name': ((Keen_Account_creation.enter_firstName)), 'DoB': (Keen_Account_creation.enter_dob),
            'MiddleName': ((Keen_Account_creation.enter_middleName)),
            'Email': (Keen_Account_creation.enter_email),
            'Phone': (Keen_Account_creation.enter_phone),
            'Street_Address': (Keen_Account_creation.enter_address),
            'Gender': (Keen_Account_creation.select_gender),
            'MedicareID': (Keen_Account_creation.medication_details_popup),
            'MedcaidID': (Keen_Account_creation.medicaid_id),
            'Part_A enrollment date': (Keen_Account_creation.part_A),
            'Part_B enrollment date': (Keen_Account_creation.part_B),
            'Medicaid_status_verification_date': (Keen_Account_creation.verification_date),
            'SSN': (Keen_Account_creation.SSN),
            'Addressline2': (Keen_Account_creation.enter_newcreationaddress_line_2),
            'Member_County': (Keen_Account_creation.enter_county_newcreation),
            'Zipcode': (Keen_Account_creation.enter_zipcode_newcreation),
            'City': (Keen_Account_creation.enter_city_newcreation), 'State': (Keen_Account_creation.click_state),
            'Disposition': (Keen_Account_creation.disposition_field),
            'Nickname': (Keen_Account_creation.enter_nickname),
            'Medicaid_Category': (Keen_Account_creation.medicaid_category),
            'low_income_subsidy': (Keen_Account_creation.low_income_subsidy),
            'Member_ID': (Keen_Account_creation.member_id)
        }
        for cell in data_row:
            column_name = sheet.cell(row=2, column=cell.column).value
            if column_name in column_field_mapping:
                field_name = column_field_mapping[column_name]
                self.log.info(field_name)
                self.log.info("***** column name and field name is matched *****")
                column_value = cell.value
                locator = field_locators[field_name]
                element = self.driver.find_element(*locator)
                if element.tag_name == 'button':
                    if field_name == 'Gender':
                        self.log.info("***** Gender field is present *****")
                        element.click()
                        pick_up_gender = self.keen.select_gender_in_list()
                        for gender in pick_up_gender:
                            if gender.text == column_value:
                                self.driver.execute_script("arguments[0].click();", gender)
                                self.log.info("***** Gender option is selected *****")
                                break
                    if field_name == 'State':
                        self.log.info("***** state field is present *****")
                        element.click()
                        self.log.info("***** State field is clicked *****")
                        action_utils.wait_for_elements((Keen_Account_creation.member_options))
                        states = self.keen.select_state_newlead()
                        for list_states in states:
                            if list_states.text == column_value:
                                self.driver.execute_script("arguments[0].click();", list_states)
                                self.log.info("***** State option is selected *****")
                                break
                    if field_name == 'Disposition':
                        self.log.info("***** Disposition field is present *****")
                        element.click()
                        self.log.info("***** Disposition field is clicked *****")
                        Disposition_options = self.keen.tabs_options()
                        for dispositions in Disposition_options:
                            if dispositions.get_attribute('title') == column_value:
                                self.driver.execute_script("arguments[0].click();", dispositions)
                                self.log.info("***** Disposition option is selected *****")
                                break
                    if field_name == 'Medicaid_Category':
                        element.click()
                        self.log.info("***** Medicaid field is selected *****")
                        action_utils.wait_for_elements((Keen_Account_creation.member_options))
                        medicaid_options = self.keen.select_state_newlead()
                        for options in medicaid_options:
                            if options.get_attribute('title').strip() == column_value.strip():
                                self.log.info("*****Medicareid option is matched *****")
                                self.driver.execute_script("arguments[0].click();", options)
                                self.log.info("***** medicaid_category option is selected *****")
                                break
                    if field_name == 'low_income_subsidy':
                        element.click()
                        self.log.info("***** low_income_subsidy field is clicked *****")
                        action_utils.wait_for_elements((Keen_Account_creation.member_options))
                        medicaid_options = self.keen.select_state_newlead()
                        for options in medicaid_options:
                            if options.get_attribute('title').strip() == column_value.strip():
                                self.log.info("*****low_income_subsidy option is matched *****")
                                self.driver.execute_script("arguments[0].click();", options)
                                self.log.info("***** medicaid_category option is selected *****")
                                break

                elif element.tag_name == 'lightning-icon':
                    if field_name == 'MedicareID':
                        self.log.info("****** MedicareID field is present *****")
                        self.keen.select_medication_details()
                        self.keen.enter_medicare_ID().send_keys(column_value)
                else:
                    element.clear()
                    element.send_keys(column_value)
                    if field_name == 'Member_ID':
                        self.keen.Click_Ok()
                        self.log.info("***** Medicaredetails popup is closed *****")
        self.keen.last_name().send_keys(last_name)
        self.keen.click_save()
        action_utils.wait_for_element((Keen_Account_creation.toast_message))
        account_created = self.keen.Success_Message()
        assert account_created.is_displayed(), "Toast message is not displayed"

    ### Test Description:- Generate a Quote to a Member
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Click on New, Create a New account,
    ### Click on GenerateQuote,Fill the Test data and Click on TransferToSunfire
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Quote Generation for Keen Leads and Members")
    def test_generatequote_newaccount(self,row_number_account):
        try:
            Extra_help = "Yes"
            self.log.info("***** Validating the leads data to generate quote data *****")
            self.action_utils.wait_for_element((Keen_Account_creation.verify_field_DoB))
            lead_dob = self.keen.validation_of_DoB()
            email_lead = self.keen.validation_of_email()
            phone_lead = self.keen.validation_of_Phone()
            lead_phone = self.action_utils.convert_string(phone_lead)
            self.action_utils.wait_for_element((Keen_Account_creation.address_details))
            self.keen.click_address_Details()
            self.action_utils.wait_for_element((Keen_Account_creation.verify_streetaddress))
            time.sleep(5)
            member_street_address=self.keen.validation_of_street().get_attribute('value')
            self.log.info("***** Retrieve 'Street' value in Keen Member *****")
            time.sleep(5)
            member_city=self.keen.validation_of_city().get_attribute('value')
            self.log.info("***** Retrieve 'City' value in Keen Member *****")
            time.sleep(5)
            member_addressline_two=self.keen.validation_of_addressline_2().get_attribute('value')
            self.log.info("***** Retrieve 'addressline_2' value in Keen Member *****")
            time.sleep(5)
            member_state=self.keen.validation_of_state().get_attribute('data-value')
            self.log.info("*****Retrieve 'State' value in Keen Member *****")
            time.sleep(5)
            member_county=self.keen.validation_of_county().get_attribute('value')
            self.log.info("*****Retrieve 'County' value in Keen Member *****")
            time.sleep(5)
            member_zipcode=self.keen.validation_of_zipcode().get_attribute('value')
            self.log.info("*****Retrieve 'Zipcode' value in Keen Member *****")
            print("member zipcode:",member_zipcode)
            self.keen.Click_close_popup()
            self.log.info("***** popup is closed *****")
            self.action_utils.wait_for_element((Keen_Account_creation.edit_record))
            self.keen.click_on_edit()
            self.action_utils.wait_for_element((Keen_Account_creation.verify_firstName))
            lead_first_name=self.keen.verify_first_name().get_attribute("value")
            print("lead_firstname:",lead_first_name)
            self.action_utils.wait_for_element((Keen_Account_creation.verify_LastName))
            lead_last_name=self.keen.verify_last_name().get_attribute("value")
            print("Generate:", lead_last_name)
            self.action_utils.wait_for_element((Keen_Account_creation.cancel_in_member_page))
            self.keen.click_cancel_keen_page()
            ########## action_utils.wait_for_element((Keen_Quote_Generation.generate_quote))
            ########### keen_GQ.click_GenerateQuote()\
            self.action_utils.wait_for_element((Keen_Quote_Generation.smart_quote))
            self.Keen_Generate.click_smart_Quote()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.action_utils.wait_for_element((Keen_Quote_Generation.bna_tab))
            assert self.Keen_Generate.smart_quote_tab().is_displayed(),"Tab is not displayed"
            self.log.info("***** Compare the data in memebers record is reflected to 'Generate Quote' *****")
            time.sleep(5)
            try:
                self.action_utils.wait_for_element((Keen_Quote_Generation.first_name))
                first_name = self.Keen_Generate.firstName_Generate_Quote().get_attribute('value')
                print("Generate first name:",first_name)
                assert first_name == lead_first_name,"First name is not matched"
            except Exception as ex:
                self.log.info("***** First name is not matched *****")
                print(ex)
            try:
                last_name_generate = self.Keen_Generate.enter_lastname_GenerateQuote().get_attribute('value')
                print("Generate last name:", last_name_generate)
                # entered_value = self.driver.execute_script("return arguments[0].value;", last_name_generate)
                assert lead_last_name == last_name_generate,"Last name is not matched"
            except Exception as ex:
                self.log.info("***** Last name is not matched *****")
                print(ex)
            time.sleep(5)
            self.action_utils.wait_for_element((Keen_Quote_Generation.dob))
            dob = self.Keen_Generate.DoB_GenerateQuote()
            generate_dob = dob.get_attribute("value")
            print("Generate:", generate_dob)
            try:
                assert lead_dob == generate_dob,"DOB is not matched"
            except Exception as ex:
                self.log.info("***** DOB is not matched *****")
            email_generate=self.Keen_Generate.Email_GenerateQuote().get_attribute("value")
            print("Generate:", email_generate)
            try:
                assert email_lead == email_generate,"Email is not matched"
            except Exception as ex:
                self.log.info("***** Email is not matched *****")
            self.Keen_Generate.Phone_GenerateQuote()
            phone_generate=self.Keen_Generate.Phone_GenerateQuote().get_attribute("value")
            generate_phone=self.action_utils.convert_string(phone_generate)
            try:
                assert generate_phone == lead_phone,"Phone number is not matched"
            except Exception as ex:
                self.log.info("***** phonenumber address is not matched *****")
            generate_zipcode=self.Keen_Generate.zipcode_GenerateQuote().get_attribute("value")
            print("generate zipcode:",generate_zipcode)
            try:
                assert generate_zipcode == member_zipcode,"Zipcode is not matched"
            except Exception as ex:
                self.log.info("***** Zipcode is not matched *****")
            street_address=self.Keen_Generate.street_address().get_attribute("value")
            try:
                assert street_address == member_street_address,"Street address is not matched"
            except Exception as ex:
                self.log.info("***** Street address is not matched *****")
            generate_address_line2=self.Keen_Generate.enter_addressline2().get_attribute("value")
            try:
                assert member_addressline_two == generate_address_line2,"Address line is not matched"
            except Exception as ex:
                self.log.info("***** Address line is not matched *****")
            generate_city=self.Keen_Generate.enter_city().get_attribute("value")
            try:
                assert member_city == generate_city,"City is not matched"
            except Exception as ex:
                self.log.info("***** City is not matched *****")
            generate_county=self.Keen_Generate.Member_county().get_attribute("value")
            try:
                self.log.info(member_county)
                self.log.info(generate_county)
                assert member_county == generate_county,"county is not matched"
            except Exception as ex:
                self.log.info("***** county is not matched *****")
            generate_state=self.Keen_Generate.select_generate_state().get_attribute("data-value")
            try:
                assert member_state == generate_state,"State is not matched"
            except Exception as ex:
                self.log.info("***** State is not matched *****")
            time.sleep(10)
            # plan=self.driver.find_element(By.XPATH," //label[text()=' Do you have the member’s current plan information?']/following::input[@name='isPlanDetailsRequired' and @value='n']/parent::span//span[text()='No']")
            # action.move_to_element(plan).click().perform()
            # time.sleep(3)
            # pharmacy=self.driver.find_element(By.XPATH," //label[text()='Do you want to add a preferred pharmacy?']/following::input[@name='isPharmaciesRequired' and @value='n']/parent::span//span[text()='No']")
            # action.move_to_element(pharmacy).click().perform()
            # time.sleep(2)
            try:
               if self.Keen_Generate.verify_current_plan().is_displayed:
                   self.action_utils.wait_for_element((Keen_Quote_Generation.current_plan_new))
                   self.Keen_Generate.click_current_plan_new()
                   try:
                       self.action_utils.wait_for_element((Create_capture_member_details.plans_records))
                       self.Keen_create.click_plan_detail_list().send_keys("Test Plan")
                       self.log.info("***** Searching the plan *****")
                       WebDriverWait(self.driver,5)
                       self.action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                       existing_plans=self.Keen_create.select_options()
                       for plans in existing_plans:
                           if plans.get_attribute('title') == "Test Plan":
                               self.driver.execute_script("arguments[0].click();", plans)
                               break
                       self.Keen_create.edit_save()
                       try:
                           self.action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                           success_message_of_records = self.Keen_create.success_message()
                           assert success_message_of_records.is_displayed(), "Record is saved"
                       except Exception as ex:
                           self.log.info("***** Plan is not available in Salesforce *****")
                           self.action_utils.wait_for_element((Keen_Quote_Generation.close_plan_popuop))
                           self.Keen_Generate.smart_quote_plan_close()
                   except Exception as ex:
                       self.log.info("Plan is not associated to member")
                       self.Keen_Generate.click_current_plan_no()
            except Exception as ex:
                self.log.info("Plan is associated to member")
            self.log.info("***** Click on sunfire button *****")
            self.Keen_Generate.click_TransferToSunfire()
            self.action_utils.wait_for_elements((Keen_Quote_Generation.data_failure_message))
            toast_message = self.Keen_Generate.verify_toast_message()
            WebDriverWait(self.driver, 2)
            time.sleep(2)
            self.log.info(toast_message.text)
            self.log.info("***** Verifing the quote is already generated *****")
            if "Error!" in toast_message.text:
                self.log.info("***** Filling the inputdata *****")
                self.action_utils.wait_for_element((Keen_Quote_Generation.move_to_plans))
                self.log.info("***** Filling the inputdata *****")
                scroll_to_plans = self.Keen_Generate.scroll_plans()
                self.action.move_to_element(scroll_to_plans)
                self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_plans)
                self.action_utils.wait_for_elements((Keen_Quote_Generation.plans_types_name))
                plans_to_discuss = self.Keen_Generate.click_plan_types()
                for plans in plans_to_discuss:
                    plans.click()
                WebDriverWait(self.driver, 5)
                move_to_tobacco_section = self.Keen_Generate.move_to_tobaccco_label()
                self.driver.execute_script("arguments[0].scrollIntoView();", move_to_tobacco_section)
                self.action_utils.wait_for_element((Keen_Quote_Generation.tobacco_consumption_yes))
                self.Keen_Generate.click_tobacco_yes().click()
                self.log.info("***** Medicare Advantage/Part D or Special Needs plan is selected*****")
                self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_label))
                medicare_label = self.Keen_Generate.verify_medicare_label()
                self.driver.execute_script("arguments[0].scrollIntoView();", medicare_label)
                assert medicare_label.is_displayed(), "Medicare Options are displayed"
                self.log.info("***** Assosicating the doctors record *****")
                self.action_utils.wait_for_element((Keen_Quote_Generation.doctors_vist_yes))
                self.Keen_Generate.click_doctor_yes()
                self.Keen_Generate.select_Doctors_Generate()
                self.action_utils.wait_for_element((Create_capture_member_details.new_medication_popup))
                pop_up_of_New_Members_physicians = self.Keen_create.popup_of_new_medication()
                print("Popup heading:",pop_up_of_New_Members_physicians)
                assert pop_up_of_New_Members_physicians.is_displayed(),"New Member's physician popup is displayed"
                        ####== "New Member's physician"), "New Member's physician popup is not matched"
                self.action_utils.wait_for_element(Create_capture_member_details.physician)
                self.Keen_create.click_physician_directory().send_keys("Aer")
                self.log.info("***** Associating existing 'physician' record to member  *****")
                WebDriverWait(self.driver, 5)
                self.action_utils.wait_for_elements((Create_capture_member_details.physician_record_list))
                list_of_physicians = self.Keen_create.new_physcians_list()
                # print("physicians_list:", list_of_physicians.text)
                self.driver.execute_script("arguments[0].click();", list_of_physicians[1])
                print("Selected_physician:",list_of_physicians[1].get_attribute('title'))
                self.Keen_create.click_Is_Primary_Care_Physician()
                self.action_utils.wait_for_element((Keen_Quote_Generation.network_preference))
                self.Keen_Generate.click_network_preference()
                self.action_utils.wait_for_elements((Keen_Quote_Generation.network_preference_list))
                network_options=self.Keen_Generate.select_network_options()
                self.driver.execute_script("arguments[0].click();", network_options[1])
                WebDriverWait(self.driver, 5)
                self.Keen_create.click_members_details_save()
                self.action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                success_message_of_records = self.Keen_create.success_message()
                try:
                    assert success_message_of_records.is_displayed(), "Record is saved"
                except Exception as ex:
                    self.log.info("***** sucess toast message is not displayed *****")
                    print("toast is not displayed")
                self.action_utils.wait_for_elements((Keen_Quote_Generation.doctor_visit_or_receive_medicalcare))
                doctor_visit = self.Keen_Generate.member_doctor_vist()
                self.log.info("***** doctor visit option should be selected*****")
                for doctor_visit_receive in doctor_visit:
                    if doctor_visit_receive.text == "Frequently":
                        self.driver.execute_script("arguments[0].click();", doctor_visit_receive)
                        self.log.info("***** doctor visit option is selected*****")
                        break
                try:
                    self.action_utils.wait_for_element((Keen_Quote_Generation.search_mediaction_field))
                    scroll_to_medication = self.Keen_Generate.move_to_medication()
                    self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_medication)
                    self.log.info("***** Medications option *****")
                    time.sleep(3)
                    self.action_utils.wait_for_element((Keen_Quote_Generation.medication_add))
                    self.Keen_Generate.select_medication_GenerateQuote()
                    pop_up_of_New_Members_medication = self.Keen_create.Member_medication_popup()
                    assert pop_up_of_New_Members_medication.text == "New Member Medication", "New Member Medication is not matched"
                    ### medication = Actemra
                    self.Keen_create.medication_search().send_keys("Actemra")
                    self.log.info("***** Associate existing medication record to member  *****")
                    time.sleep(3)
                    self.action_utils.wait_for_elements((Create_capture_member_details.physicians_records))
                    list_of_medication = self.Keen_create.select_physicians_records()
                    print("Medications_list:",list_of_medication)
                    for medications in list_of_medication:
                        print("Medications_list:",medications.get_attribute('data-value'))
                        if medications.get_attribute('data-value').strip() == "Actemra":
                            self.driver.execute_script("arguments[0].click();", medications)
                            self.log.info("***** Existing record is selected *****")
                    self.action_utils.wait_for_element((Create_capture_member_details.drug_form))
                    drug_value=self.Keen_create.verify_drug_form().get_attribute('data-value')
                    print("Drug_value:",drug_value)
                    if drug_value == "":
                        self.log.info("***** Medication have multiple Drug forms and Strengths. So select the first drug form and strength *****")
                        self.action_utils.wait_for_element((Create_capture_member_details.drug_form))
                        click_drug=self.Keen_create.verify_drug_form()
                        self.driver.execute_script("arguments[0].click();", click_drug)
                        self.action_utils.wait_for_elements((Create_capture_member_details.select_first_option))
                        select_first_option=self.Keen_create.click_first_element()
                        self.driver.execute_script("arguments[0].click();", select_first_option[1])
                        # print("selected_option_text:",click_option.get_attribute('data-value'))
                        # self.driver.execute_script("arguments[0].click();", click_option)
                        # action_utils.wait_for_element((Create_capture_member_details.drug_form))
                        # strength_value = keen_create.verify_strength().get_attribute('data-value')
                        # if drug_value == "":
                        self.action_utils.wait_for_element((Create_capture_member_details.drug_strength))
                        self.Keen_create.verify_strength()
                        self.action_utils.wait_for_element((Create_capture_member_details.select_first_option_strength))
                        self.Keen_create.click_firstoption_strength()
                        self.log.info("***** Drug Strength selected *****")
                    else:
                        self.log.info("***** Medication has single drug and strength *****")
                    self.action_utils.wait_for_element((Create_capture_member_details.quantityperfill))
                    self.Keen_create.Quantity_per_fill("1")
                    self.action_utils.wait_for_element((Create_capture_member_details.refillfrequency))
                    self.Keen_create.Refill_frequency()
                    self.action_utils.wait_for_elements((Create_capture_member_details.options))
                    frequency_options = self.Keen_create.select_frequency()
                    for frequency in frequency_options:
                        if frequency.get_attribute('data-value') == 'Daily':
                            self.log.info("***** Daily is displayed *****")
                            self.driver.execute_script("arguments[0].click();", frequency)
                            self.log.info("***** Daily frequency  *****")
                            self.Keen_create.click_members_details_save()
                except Exception as ex:
                    print(ex)
                    self.log.info(print(ex))
                    self.log.info("***** Medication record is existing in SalesForce *****")
                self.action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                success_message_of_records = self.Keen_create.success_message()
                try:
                    assert success_message_of_records.is_displayed(), "Record is not saved"
                except Exception as ex:
                    self.log.info("***** Save popup is not displayed *****")
                time.sleep(3)
                self.action_utils.wait_for_element((Keen_Quote_Generation.pharmacy_add))
                scroll_to_pharmacy = self.Keen_Generate.move_to_pharmacy()
                self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_pharmacy)
                self.action_utils.wait_for_element((Keen_Quote_Generation.pharmacy_add))
                self.Keen_Generate.click_pharamcy()
                self.action_utils.wait_for_element((Create_capture_member_details.search_pharmacy))
                self.Keen_create.pharmacy_directory().send_keys("Gaint Food")
                self.log.info("***** Associating existing 'Pharmacies' record to member  *****")
                time.sleep(2)
                self.action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                list_of_pharmacies = self.Keen_create.select_existing_records()
                print("len of pharmacies:", len(list_of_pharmacies))
                for pharmacies in list_of_pharmacies:
                    print("Pharmacies_list:",pharmacies.get_attribute('title'))
                    if pharmacies.get_attribute('title') == "Giant Food":
                        self.driver.execute_script("arguments[0].click();", pharmacies)
                        self.log.info("***** Existing record is selected *****")
                self.Keen_create.save_button_Add()
                self.log.info("***** Associated existing 'Pharmacies' record to member *****")
                try:
                    self.action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                    success_message_of_records = self.Keen_create.success_message()
                    assert success_message_of_records.is_displayed(), "Record is not saved"
                except TimeoutError:
                    self.log.info("***** Pharmacy record is not present in Salesforce *****")
                    self.Keen_create.click_cancel_pharcmacy()
                    self.action_utils.wait_for_element((Keen_Quote_Generation.pharmacy_no))
                    self.Keen_Generate.click_pharmacy_no()
                scroll_to_extra_help = self.Keen_Generate.move_to_extra_help_section()
                self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_extra_help)
                options_help = self.Keen_Generate.click_extra_help_or_subsidy()
                for subsidy in options_help:
                    if subsidy.text == Extra_help:
                        self.driver.execute_script("arguments[0].click();", subsidy)
                        self.log.info("***** Extra help option is selcted *****")
                        break
                if Extra_help == "Yes":
                    self.log.info("***** Extra help option is 'Yes' *****")
                    drug_cost = self.Keen_Generate.verify_drug_pay()
                    assert drug_cost.is_displayed(), "Drug_pay filed is not displayed"
                    self.log.info("***** Drug pay option is to be selected *****")
                    options_pay = self.Keen_Generate.select_drug_pay()
                    for drug_cost in options_pay:
                        if drug_cost.text == "$1.55-$4.60 for covered drugs":
                            self.driver.execute_script("arguments[0].click();", drug_cost)
                            self.log.info("***** Drug pay option is selected *****")
                            break
                    self.Keen_Generate.click_TransferToSunfire()
                    self.log.info("***** Quote is initiated *****")
                    try:
                        self.log.info("***** Waiting for the Quote response *****")
                        WebDriverWait(self.driver, 180).until(
                            EC.presence_of_element_located((By.XPATH, "//h2[text()='Quote created in Sunfire!']"))
                            )
                        self.log.info("***** Quote generation popup is displayed *****")
                        WebDriverWait(self.driver, 10)
                        self.Keen_Generate.Quote_close()
                        self.log.info("***** Quote generation popup is closed *****")
                        # email_sent = keen_aws_session()
                        # email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                        #                      "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                        #                      "subject": "GenerateQuote Automation testing status is passed"+" - "+self.formatted_date,
                        #                      "body": "GenerateQuoteAutomation results"})
                    except TimeoutException:
                        self.log.info("***** Quote generation is failed *****")
                        # email_sent = keen_aws_session()
                        # email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                        #                      "to_email":"engineering@choosekeen.com,anil.maddula@choosekeen.com",
                        #                      "subject": "GenerateQuote Automation testing status  failed"+" - "+self.formatted_date,
                        #                      "body": "GenerateQuoteAutomation results"})
                else:
                    self.Keen_Generate.click_TransferToSunfire()
                    self.log.info("***** Quote is initiated *****")
                    try:
                        self.log.info("***** Waiting for the Quote response *****")
                        WebDriverWait(self.driver, 180).until(
                            EC.presence_of_element_located((By.XPATH, "//h2[text()='Quote created in Sunfire!']"))
                            )
                        self.log.info("***** Quote generation popup is displayed *****")
                        WebDriverWait(self.driver, 10)
                        self.Keen_Generate.Quote_close()
                        self.log.info("***** Quote generation popup is closed *****")
                        # email_sent = keen_aws_session()
                        # email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                        #                      "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                        #                      "subject": "GenerateQuote Automation testing status  passed"+" - "+self.formatted_date,
                        #                      "body": "GenerateQuoteAutomation results"})
                    except TimeoutException:
                            self.log.info("***** Quote generation is failed *****")
                            # email_sent = keen_aws_session()
                            # email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                            #                      "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                            #                      "subject": "GenerateQuote Automation status is Failed"+" - "+self.formatted_date,
                            #                      "body": "GenerateQuoteAutomation results"})
            else:
                    try:
                        self.log.info("***** Waiting for the Quote response *****")
                        WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.XPATH,"//h2[text()='Quote created in Sunfire!']"))
                        )
                        WebDriverWait(self.driver, 10)
                        self.log.info("***** GenerateQuote popup is displayed *****")
                        self.Keen_Generate.Quote_close()
                        self.log.info("***** Quote generation popup is closed *****")
                        # email_sent=keen_aws_session()
                        # email_sent.test_aws({"from_email": "engineering@choosekeen.com","to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com","subject":"GenerateQuote Automation testing status is passed"+" - "+self.formatted_date,"body":"GenerateQuoteAutomation results"})
                    except TimeoutException:
                        self.log.info("***** Quote generation is failed *****")
                        # email_sent = keen_aws_session()
                        # email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                        #                      "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                        #                      "subject": "GenerateQuote Automation status is Failed"+" - "+self.formatted_date,
                        #                      "body": "GenerateQuoteAutomation results"})
        except Exception as ex:
            print("error_message:",ex)
            self.log.info(ex)
            self.log.info("***** Execution is failed *****")
    ### Test Description:- Generate a Quote to a New Keen Leads and Member Creation
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Click on New, Create a New account,
    ### Click on GenerateQuote,Fill the Test data and Click on TransferToSunfire
    ### Click on Capture Full member Details---> Verify the Physician, Medication and Pharmacies created from GenerateQuote
    def test_validation_of_capture_full_member_details(self,row_medication,row_physicians,row_pharmacy):
        Medicine = self.readdata_medications.readdata(row_medication, 1)
        first_name = self.readdata_physicians.readdata(row_physicians, 2)
        last_name = self.readdata_physicians.readdata(row_physicians, 1)
        physicians = first_name + ' ' + last_name
        Pharmacy = self.readdata_pharmacies.readdata(row_pharmacy, 1)
        self.Keen_create.Capture_Full_Member()
        self.log.info("***** Verifing Mediaction record in Capture Full Member Details  *****")
        self.Keen_create.Medication_option()
        self.action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_up_of_Members_Medications = self.Keen_create.pop_up()
        if pop_up_of_Members_Medications.text == "Member's Medications":
            assert True
        else:
            assert False
        selected_Medication = self.Keen_Generate.validation_of_records()
        for associated_records in selected_Medication:
            if associated_records.text == Medicine:
                assert True
            else:
                assert False
        self.Keen_create.close()
        self.log.info("***** Verifed Medication record in Capture Full Member Details  *****")
        time.sleep(5)
        self.log.info("***** Verifing Physicians record in Capture Full Member Details  *****")
        self.Keen_create.select_physicians()
        self.action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_up_of_Members_physicians = self.Keen_create.pop_up()
        assert pop_up_of_Members_physicians.text == "Member's Physicians", "physicians are not selected"
        selected_physician = self.Keen_Generate.validation_of_records()
        for associated_physicians in selected_physician:
            if associated_physicians.text == physicians:
                assert True
            else:
                assert False
        self.Keen_create.close()
        self.log.info("***** Verifed Physician record in Capture Full Member Details  *****")
        self.log.info("***** Verifing Pharmacy record in Capture Full Member Details  *****")
        self.Keen_create.pharmacy_directory()
        self.action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_up_of_Members_pharmacy = self.Keen_create.pop_up()
        assert pop_up_of_Members_pharmacy.text == "Member's Pharmacies", "pharamices  are not updated"
        list_of_selected_pharmacies = self.Keen_Generate.validation_of_records()
        for selected_pharamcies in list_of_selected_pharmacies:
            if selected_pharamcies.text == Pharmacy:
                assert True
            else:
                assert False
        self.Keen_create.close()
        self.log.info("***** Verifed Pharmacy record in Capture Full Member Details  *****")
     ####### Advanced Need Assessment Tab
    ### Test Description:- Fill the details taken form the Member in  Advanced Need Assessment Tab
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Click on any one of the Keen Lead, Click on Smart Quote,
    ### Click on Advanced Need Assessment Tab
    def test_advanced_need_assessment(self):
        financial_concerns = "Yes"
        previous_question = "Yes"
        year = "1-4"
        dental_issues = "Yes"
        services_options = "Oral Exams"
        glass_lenses = "No"
        hearing_problem = "No"
        hearing_aids = "No"
        need_ride = "Yes"
        healthy_meals = "Yes"
        list_carriers = "Aetna"
        preference_plan_type = "PPO"
        part_b = "Yes"
        try:
            self.action_utils.wait_for_element((Keen_Quote_Generation.advanced_needs_assessment))
            self.Keen_Generate.click_advanced_need_assessment()
        except Exception as ex:
            self.log.info("***** Success are failure message is not displayed *****")
        #### Verify dataof birth for Alret Message!
        try:
            self.action_utils.wait_for_element((Keen_Quote_Generation.alert_message))
            message=self.Keen_Generate.verify_alert()
            if message.text == "Message!":
                self.action_utils.wait_for_element((Keen_Quote_Generation.proceed_button))
                self.Keen_Generate.click_proceed()
                self.log.info("***** Proceed button clicked *****")
        except Exception as ex:
            print(ex)
        if financial_concerns == 'Yes':
            self.action_utils.wait_for_element((Keen_Quote_Generation.financial_concerns_yes))
            self.Keen_Generate.click_financial_concerns_yes()
            self.log.info("***** Financial Concerns is selected as Yes *****")
            if previous_question == 'Yes':
                self.action_utils.wait_for_element((Keen_Quote_Generation.yes_to_previousquestion))
                self.Keen_Generate.click_yes_to_previousquestion()
                self.log.info("***** Previous question is selected as Yes *****")
            else:
                self.Keen_Generate.click_no_to_previousquestion()
                self.log.info("***** Previous question is selected as No *****")
        else:
            self.Keen_Generate.click_financial_concerns_no()
            self.log.info("***** Financial Concerns is selected as No *****")
        dental_options=self.Keen_Generate.move_to_dental_options()
        self.action.move_to_element(dental_options)
        self.action_utils.wait_for_element((Keen_Quote_Generation.dental_vision_hearing))
        self.Keen_Generate.click_dental_vision_hearing()
        self.action_utils.wait_for_elements((Create_capture_member_details.options))
        dental_vision_options=self.Keen_create.select_frequency()
        for year_options in dental_vision_options:
            if year_options.get_attribute('data-value') == year:
                self.log.info(year_options.get_attribute('data-value'))
                WebDriverWait(self.driver,10)
                self.driver.execute_script("arguments[0].click();", year_options)
                self.log.info("***** how often do you go to the dentist each year option is selected *****")
        if dental_issues == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.major_dental_issues_yes))
            self.Keen_Generate.click_major_dental_issues_yes()
            self.log.info("***** Dental issue yes option selected *****")
            dental_services=self.Keen_Generate.move_dental_services_need()
            self.action.move_to_element(dental_services)
            self.action_utils.wait_for_element((Keen_Quote_Generation.services_you_need))
            self.Keen_Generate.click_dental_services_need()
            self.action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
            dental_services=self.Keen_create.select_options()
            for services in dental_services:
                print("Services_options:", services.get_attribute('title'))
                WebDriverWait(self.driver,15)
                if services.get_attribute('title') == services_options:
                    print("Services_options:",services.get_attribute('title'))
                    self.action.move_to_element(services).click().perform()
                    # self.driver.execute_scriptself.driver.execute_script("arguments[0].click();", services)
                    self.log.info("***** Dental services options selected *****")
            move_to_lense=self.Keen_Generate.move_to_lenses()
            self.action.move_to_element(move_to_lense).click().perform()
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.major_dental_issues_no))
            self.Keen_Generate.click_major_dental_issues_no()
            self.log.info("***** Dental issue no option selected *****")

        move_to_glasses_and_lenses=self.Keen_Generate.move_to_lenses()
        self.action.move_to_element(move_to_glasses_and_lenses)
        if glass_lenses == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_wearglasses_or_lenses_yes))
            self.Keen_Generate.click_do_you_wearglasses_or_lenses_yes()
            self.log.info("***** Member glass yes button is selected *****")
        else:
            self.Keen_Generate.click_do_you_wearglasses_or_lenses_no()
            self.log.info("***** Member glasses and lenses no button is selected *****")
        move_to_hearing=self.Keen_Generate.move_to_hearing()
        self.action.move_to_element(move_to_hearing)
        self.log.info("***** Page scroll to Hearing field *****")
        if hearing_problem == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_have_trouble_hearing_yes))
            self.Keen_Generate.click_do_you_have_trouble_hearing_yes()
            self.log.info("***** Member have hearing problem so Yes button clicked *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_have_trouble_hearing_no))
            self.Keen_Generate.click_do_you_have_trouble_hearing_no()
            self.log.info("***** Member does not have hearing problem so No button clicked *****")
        move_to_hearing_aids=self.Keen_Generate.move_to_hearing_aids_field()
        self.action.move_to_element(move_to_hearing_aids)
        if hearing_aids == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_use_hearing_aids_yes))
            self.Keen_Generate.click_do_you_use_hearing_aids_yes()
            self.log.info("***** Member have hearing aids problem , so yes button clicked *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_use_hearing_aids_no))
            self.Keen_Generate.click_do_you_use_hearing_aids_no()
            self.log.info("***** Member have hearing aids problem , no yes button clicked *****")
        move_to_need_ride_field=self.Keen_Generate.move_to_ride()
        self.action.move_to_element(move_to_need_ride_field)
        self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_drive_or_does_a_family_member))
        self.Keen_Generate.click_do_you_drive_or_does_a_family_member()
        self.action_utils.wait_for_elements((Create_capture_member_details.options))
        driver_options=self.Keen_create.select_frequency()
        for selected_options in driver_options:
            if selected_options.get_attribute('data-value') == "Need a ride":
                self.driver.execute_script("arguments[0].click();", selected_options)
                self.log.info("***** Member required option  selected ***** ")
        move_to_ride_field=self.Keen_Generate.move_to_need_ride_field()
        self.action.move_to_element(move_to_ride_field)
        if need_ride == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.free_rides_to_the_doctor_yes))
            self.Keen_Generate.click_free_rides_to_the_doctor_yes()
            self.log.info("***** Member Need a drive , so Yes button clicked *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.free_rides_to_the_doctor_no))
            self.Keen_Generate.click_free_rides_to_the_doctor_no()
            self.log.info("***** Member does not Need a drive , so No button clicked *****")
        move_to_meals=self.Keen_Generate.move_to_meals_fields()
        self.action.move_to_element(move_to_meals)
        if healthy_meals == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_typically_eat_healthy_meals_yes))
            self.Keen_Generate.click_do_you_typically_eat_healthy_meals_yes()
            move_daily_meals=self.Keen_Generate.move_to_meals_daily_fields()
            self.action.move_to_element(move_daily_meals)
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_have_trouble_getting_healthy_meals_daily_no))
            self.Keen_Generate.click_do_you_have_trouble_getting_healthy_meals_daily_no()
            move_to_food_card=self.Keen_Generate.move_to_food_card()
            self.action.move_to_element(move_to_food_card)
            self.action_utils.wait_for_element((Keen_Quote_Generation.have_otccard_foodcard_yes))
            self.Keen_Generate.click_have_otccard_foodcard_yes()
            self.action_utils.wait_for_element((Keen_Quote_Generation.food_card_type))
            self.Keen_Generate.click_food_card_type()
            self.action_utils.wait_for_elements((Create_capture_member_details.options))
            food_card_options = self.Keen_create.select_frequency()
            for card_options in food_card_options:
                if card_options.get_attribute('data-value') == "OTC card":
                    WebDriverWait(self.driver,10)
                    self.driver.execute_script("arguments[0].click();",card_options)
                    self.log.info("***** Member card option selected *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_typically_eat_healthy_meals_no))
            self.Keen_Generate.click_do_you_typically_eat_healthy_meals_no()
            move_daily_meals = self.Keen_Generate.move_to_meals_daily_fields()
            self.action.move_to_element(move_daily_meals)
            self.log.info("***** Page scroll to Daly Meals field *****")
            self.action_utils.wait_for_element((Keen_Quote_Generation.do_you_have_trouble_getting_healthy_meals_daily_yes))
            self.Keen_Generate.click_do_you_have_trouble_getting_healthy_meals_daily_yes()
            move_to_food_card = self.Keen_Generate.move_to_food_card()
            self.action.move_to_element(move_to_food_card)
            self.log.info("***** Page scroll to food cart field *****")
            self.action_utils.wait_for_element((Keen_Quote_Generation.have_otccard_foodcard_no))
            self.Keen_Generate.click_have_otccard_foodcard_no()
        move_to_plan_refrence_section=self.Keen_Generate.move_to_plans()
        self.action.move_to_element(move_to_plan_refrence_section)
        self.log.info("***** Page scroll to plan refrence field *****")
        self.action_utils.wait_for_element((Keen_Quote_Generation.insurance_carriers))
        self.Keen_Generate.click_insurance_carriers()
        self.action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
        insurance_carriers=self.Keen_create.select_options()
        for insurance_carriers_options in insurance_carriers:
            if insurance_carriers_options.get_attribute('title') == list_carriers:
                WebDriverWait(self.driver,10)
                self.driver.execute_script("arguments[0].click();", insurance_carriers_options)
        plan_field=self.Keen_Generate.move_to_preference_plan_field()
        self.action.move_to_element(plan_field).click().perform()
        if preference_plan_type == "HMO":
            self.action_utils.wait_for_element((Keen_Quote_Generation.preference_hmo))
            self.Keen_Generate.click_preference_hmo()
            self.log.info("***** Member have high priority of HMO plans *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.preference_ppo))
            self.Keen_Generate.click_preference_ppo()
            self.log.info("***** Member have high priority of PPO plans *****")
        move_to_part_b=self.Keen_Generate.move_to_part_B_field()
        self.action.move_to_element(move_to_part_b)
        self.log.info("***** Page scroll to Part B field *****")
        if part_b == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.part_b_give_back_yes))
            self.Keen_Generate.click_part_b_give_back_yes()
            self.log.info("***** Member Need Part B Plan so Yes button clicked *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.part_b_give_back_no))
            self.Keen_Generate.click_part_b_give_back_no()
            self.log.info("***** Member Need Part B Plan so NO button clicked *****")



    def test_Medicare_supplimentary_tab(self,r):
        guaranteed_issue="No"
        overall_health=self.account_data.readdata(r,50)
        surgeries=self.account_data.readdata(r,51)
        mobility_limitations=self.account_data.readdata(r,52)
        mobility_limitation_condition=self.account_data.readdata(r,53)
        mobility_experienced_year=self.account_data.readdata(r,54)
        health_conditions=self.account_data.readdata(r,55)
        major_health_conditions=self.account_data.readdata(r,56)
        major_health_condition_experienced_year=self.account_data.readdata(r,57)
        pacemaker_high_PSA=self.account_data.readdata(r,58)
        pacemaker_high_PSA_condition=self.account_data.readdata(r,59)
        pacemaker_high_PSA_experienced_year=self.account_data.readdata(r,60)
        confined_hospital_last_two_years=self.account_data.readdata(r,61)
        advised_by_a_medical_professional_for_further_treatments=self.account_data.readdata(r,62)
        drugs_usage=self.account_data.readdata(r,63)
        self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_supplimentary_tab))
        self.Keen_Generate.click_medicaretab()
        self.action_utils.wait_for_element((Keen_Quote_Generation.success_toast_message))
        if self.Keen_Generate.verify_toast_message_success().is_displayed():
            self.log.info("***** Adavnced Need Assessments tab data saved*****")
        if guaranteed_issue == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.guaranteed_issue_yes))
            self.Keen_Generate.member_eligible_for_guaranteed_issue_yes()
            self.log.info("***** Member is eligible for guaranteed_issue *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.guaranteed_issue_no))
            self.Keen_Generate.member_eligible_for_guaranteed_issue_no()
            self.log.info("***** Member is eligible for guaranteed_issue *****")
        self.action_utils.wait_for_element((Keen_Quote_Generation.overall_health))
        self.Keen_Generate.click_overall_health()
        self.log.info("***** Overall health option should be displayed *****")
        self.action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
        overall_health_optons=self.Keen_create.select_options()
        for health_options in overall_health_optons:
            if health_options.get_attribute('title').strip() == overall_health.strip():
                time.sleep(5)
                self.driver.execute_script("arguments[0].click();", health_options)
                self.log.info("***** Overall option is selected *****")
        if surgeries == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.guaranteed_issue_yes))
            self.Keen_Generate.click_surgeries_yes()
            self.log.info("***** Surgeries yes option is selected *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.guaranteed_issue_no))
            self.Keen_Generate.click_surgeries_no()
            self.log.info("***** Surgeries no option is selected *****")
        mobility_section=self.Keen_Generate.move_to_mobility_limitations()
        self.action.move_to_element(mobility_section)
        if mobility_limitations == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.mobility_limitations_yes))
            self.Keen_Generate.click_mobility_limitations_yes()
            self.log.info("***** Mobility Yes option is selected *****")
            self.action_utils.wait_for_element((Keen_Quote_Generation.limitation_input))
            self.Keen_Generate.search_limitation(mobility_limitation_condition)
            self.action_utils.wait_for_elements((Keen_Quote_Generation.med_supp_options))
            mobility_limitation_option=self.Keen_Generate.click_medsupp_options()
            verify_mobility_limitation_option = None
            for select_option in mobility_limitation_option:
                if select_option.get_attribute('data-label').strip() == mobility_limitation_condition.strip():
                    verify_mobility_limitation_option=select_option
                    time.sleep(5)
            if verify_mobility_limitation_option is not None:
                    self.driver.execute_script("arguments[0].click();", verify_mobility_limitation_option)
                    self.log.info("***** Mobility limitation is selected *****")
                    self.action_utils.wait_for_element((Keen_Quote_Generation.experienced_year))
                    self.Keen_Generate.click_experienced_years()
                    self.log.info("***** Mobility Experienced option is selected *****")
                    self.action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                    mobility_year_option=self.Keen_create.select_options()
                    for year_option in mobility_year_option:
                        if year_option.get_attribute('title').strip() == mobility_experienced_year.strip():
                            time.sleep(5)
                            self.driver.execute_script("arguments[0].click();", year_option)
                            self.log.info("***** Mobility limitation experienced is selected *****")
            else:
                email_sent = keen_aws_session()
                email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                                     "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                                     "subject": "Mobility_limitations_options is not present in Salesforce"+" - "+self.formatted_date,
                                     "body": "SmartQuote options results"})
                self.action_utils.wait_for_element((Keen_Quote_Generation.mobility_limitations_no))
                self.Keen_Generate.click_mobility_limitations_no()
                self.log.info("***** Mobility No option is selected *****")
        try:
            self.action_utils.wait_for_element((Keen_Quote_Generation.move_to_major_health))
            move_major_health=self.Keen_Generate.move_to_major_health_conditions()
            self.action.move_to_element(move_major_health)
            if health_conditions == "Yes":
                self.action_utils.wait_for_elements((Keen_Quote_Generation.major_health_condition_yes))
                self.Keen_Generate.click_major_health_conditions_yes()
                self.log.info("***** Major health condition Yes option selected *****")
                conditions_field = self.Keen_Generate.enter_major_health_condition()
                self.action.move_to_element(conditions_field)
                time.sleep(5)
                print("Value:",conditions_field.get_attribute('value'))
                if conditions_field.get_attribute('value') == major_health_conditions:
                    self.action.move_to_element(conditions_field)
                    conditions_field.send_keys(major_health_conditions)
                     # .send_keys(major_health_conditions).perform())
                    self.action_utils.wait_for_elements((Keen_Quote_Generation.med_supp_options))
                    health_conditions_options = self.Keen_Generate.click_medsupp_options()
                    verify_health_condition_option=None
                    # print("Health_conditions_options_values:",health_conditions_options.get_attribute('data-label'))
                    # self.log.info(health_conditions_options.get_attribute('data-label'))
                    for condition_option in health_conditions_options:
                        if condition_option.get_attribute('data-label').strip() == major_health_conditions.strip():
                            time.sleep(5)
                            verify_health_condition_option=condition_option
                    if verify_health_condition_option is not None:
                            self.driver.execute_script("arguments[0].click();", verify_health_condition_option)
                            # condition_option.click()
                            self.log.info("***** Major health conditions option is selected  *****")
                            self.action_utils.wait_for_element((Keen_Quote_Generation.experienced_year))
                            self.Keen_Generate.click_experienced_years()
                            self.action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                            major_health_experienced_year_options=self.Keen_create.select_options()
                            for experienced_year_options in major_health_experienced_year_options:
                                if experienced_year_options.get_attribute('title').strip() == major_health_condition_experienced_year.strip():
                                    time.sleep(5)
                                    self.driver.execute_script("arguments[0].click();", experienced_year_options)
                                    # experienced_year_options.click()
                                    self.log.info("***** Health Condition experienced Year option selected *****")
                                else:
                                    self.log.info("*****Health condition and Experienced is existing for Member  *****")
                        # else:
                        #     self.log.info("***** Condition was selected *****")
                    else:
                        email_sent = keen_aws_session()
                        email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                                             "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                                             "subject": "Health_condition_options is not present in Salesforce" + " - " + self.formatted_date,
                                             "body": "SmartQuote options results"})
                        self.action_utils.wait_for_elements((Keen_Quote_Generation.major_health_condition_no))
                        self.Keen_Generate.click_major_health_conditions_no()
                        self.log.info("***** Major health condition No option selected *****")
            else:
                self.action_utils.wait_for_elements((Keen_Quote_Generation.major_health_condition_no))
                self.Keen_Generate.click_major_health_conditions_no()
                self.log.info("***** Major health condition No option selected *****")
        except Exception as ex:
            self.log.info(ex)
            self.log.info("***** Failed to enter the major health conditions *****")
            time.sleep(5)
            self.action_utils.wait_for_elements((Keen_Quote_Generation.major_health_condition_no))
            self.Keen_Generate.click_major_health_conditions_no()
            self.log.info("***** Major health condition No option selected *****")
        self.action_utils.wait_for_element((Keen_Quote_Generation.move_psa))
        move_high_psa_section=self.Keen_Generate.move_high_psa()
        self.action.move_to_element(move_high_psa_section)
        if pacemaker_high_PSA == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.pacemaker_highpsa_yes))
            self.Keen_Generate.click_pacemaker_highpsa_yes()
            self.log.info("***** Pacemaker high psa Yes option is selected *****")
            self.action_utils.wait_for_element((Keen_Quote_Generation.pacemaker_search))
            pace_maker=self.Keen_Generate.pacemaker_search_input()
            self.action.move_to_element(pace_maker)
            time.sleep(5)
            if pace_maker.get_attribute('value') == pacemaker_high_PSA_condition:
                self.action.move_to_element(pace_maker).send_keys(pacemaker_high_PSA_condition).perform()
                self.action_utils.wait_for_elements((Keen_Quote_Generation.med_supp_options))
                health_conditions_options = self.Keen_Generate.click_medsupp_options()
                verify_pacemaker_option = None
                for condition_option in health_conditions_options:
                    if condition_option.get_attribute('data-label').strip() == pacemaker_high_PSA_condition.strip():
                        verify_pacemaker_option=condition_option
                if verify_pacemaker_option is not None:
                        time.sleep(5)
                        self.driver.execute_script("arguments[0].click();", verify_pacemaker_option)
                        self.log.info("***** Pacemaker and High PSA condition option is selected  *****")
                        self.action_utils.wait_for_element((Keen_Quote_Generation.pacemaker_experience_year))
                        self.Keen_Generate.click_pacemaker_experience_year()
                        self.log.info("***** High PSA experienced year button is clicked *****")
                        High_PSA = self.Keen_create.select_options()
                        for experienced_year_options in High_PSA:
                            if experienced_year_options.get_attribute('title').strip() == pacemaker_high_PSA_experienced_year.strip():
                                time.sleep(5)
                                self.driver.execute_script("arguments[0].click();", experienced_year_options)
                                self.log.info("***** High PSA experienced Year option selected *****")
                else:
                    email_sent = keen_aws_session()
                    email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                                         "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                                         "subject": "Pace Maker option is not present in Salesforce" + " - " + self.formatted_date,
                                         "body": "SmartQuote options results"})
                    self.action_utils.wait_for_element((Keen_Quote_Generation.pacemaker_highpsa_no))
                    self.Keen_Generate.click_pacemaker_highpsa_no()
                    self.log.info("***** Pacemaker high psa No option is selected *****")
        hospital_section=self.Keen_Generate.move_confined_hospital()
        self.action.move_to_element(hospital_section)
        if confined_hospital_last_two_years == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.confined_hospital_last_two_year_yes))
            self.Keen_Generate.click_confined_hospital_last_two_year_yes()
            self.log.info("***** Confined Hospital option Yes selected *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.confined_hospital_last_two_year_no))
            self.Keen_Generate.click_confined_hospital_last_two_year_no()
            self.log.info("***** Confined Hospital option No slected *****")
        move_to_medical_professor=self.Keen_Generate.move_medical_professional_advice()
        self.action.move_to_element(move_to_medical_professor)
        if advised_by_a_medical_professional_for_further_treatments == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.advised_by_a_medical_professional_yes))
            self.Keen_Generate.click_advised_by_a_medical_professional_yes()
            self.log.info("***** Medicare Professional Option Yes Selected *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.advised_by_a_medical_professional_no))
            self.Keen_Generate.click_advised_by_a_medical_professional_no()
            self.log.info("***** Medicare Professional Option Yes Selected *****")
        move_to_drug=self.Keen_Generate.move_drug_usage_section()
        self.action.move_to_element(move_to_drug)
        if drugs_usage == "Yes":
            self.action_utils.wait_for_element((Keen_Quote_Generation.tobacco_electronic_cigarette_consumption_yes))
            self.Keen_Generate.click_tobacco_electronic_cigarette_consumption_yes()
            self.log.info("***** Tobacco Use Yes option is selected *****")
        else:
            self.action_utils.wait_for_element((Keen_Quote_Generation.tobacco_electronic_cigarette_consumption_no))
            self.Keen_Generate.click_tobacco_electronic_cigarette_consumption_no()
            self.log.info("***** Tobacco Use No option is selected *****")
    def test_plan_recommendation_tab(self):
        try:
            self.action_utils.wait_for_element((Keen_Quote_Generation.plan_recommendations_tab))
            self.Keen_Generate.click_plan_recommendations_tab()
            try:
                self.action_utils.wait_for_element((Keen_Quote_Generation.plan_proceed))
                self.Keen_Generate.click_plan_proceed()
            except Exception as ex:
                print(ex)
                self.log.info(ex)
            self.action_utils.wait_for_element((Keen_Quote_Generation.plans_failed_message))
            self.Keen_Generate.verfiy_plans_for_user()
            self.log.info("*****  Failed to get plan recommendations for this Member *****")
            self.action_utils.wait_for_element((Keen_Quote_Generation.close_failed_popup))
            self.Keen_Generate.click_close_failed_popup()
            email_sent = keen_aws_session()
            email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                                 "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                                 "subject": "SmartQuote Automation status is Failed" + " - " + self.formatted_date,
                                 "body": "SmartQuote Automation results"})
        except Exception as ex:
            self.log.info(ex)
            self.log.info("***** Plans are loading *****")
            try:
                email_sent = keen_aws_session()
                email_sent.test_aws({"from_email": "engineering@choosekeen.com",
                                     "to_email": "engineering@choosekeen.com,anil.maddula@choosekeen.com",
                                     "subject": "SmartQuote Automation status is Passed"+" - "+self.formatted_date,
                                     "body": "SmartQuote Automation results"})
            except Exception as ex:
                print(ex)
            try:
                self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_supplimentary_plans))
                supplementary_plans=self.Keen_Generate.verify_medicare_supplimentary_plans()
                if supplementary_plans.text == "Medicare Supplement":
                    # is_displayed():
                    self.log.info("***** Medcare supplimentary plan section is displayed *****")
                    self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_supplimentary_plans_list))
                    time.sleep(5)
                    supp_plans_list = self.Keen_Generate.verify_medicare_supplimentary_plans_list()
                    print("Supp_plans_list:", supp_plans_list.text)
                    if supp_plans_list.text == "The client will not pass underwriting for any med. supp. plans. Please discuss this with the client and confirm if they would prefer to look at MAPD plans.":
                        self.log.info("***** Medicare Supplimentary plans is not available for this member *****")
                    else:
                        self.log.info("***** Medicare Supplimentary plans are  available for this member *****")
                else:
                    self.log.info("***** Medicare supplimentary plan section is not displayed *****")
            except Exception as ex:
                print(ex)
                self.log.info("***** Medicare Supplimentary option is not selected *****")
            try:
                self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_advantage_part_d_plan))
                medicare_advantage_part_d_plan=self.Keen_Generate.verify_medicare_advantage_part_d_plan()
                time.sleep(10)
                if medicare_advantage_part_d_plan.text == "Medicare Advantage/Part D":
                    # is_displayed():
                    self.log.info("***** medicare advantage part d plan option was selected *****")
                    self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_advantage_part_d_plan_list))
                    time.sleep(5)
                    medicare_advantage_part_d_plan_list = self.Keen_Generate.verify_medicare_advantage_part_d_plan_list()
                    print("medicare_advantage_part_d_plan_list:", medicare_advantage_part_d_plan_list.text)
                    if medicare_advantage_part_d_plan_list.text == "No plans available.":
                        self.log.info("***** Medicare Advantage/Part D plans are not available for this member *****")
                    else:
                        self.log.info("***** Medicare Advantage/Part D plans are  available for this member *****")
            except Exception as ex:
                print(ex)
                self.log.info(ex)
                self.log.info("***** medicare advantage part d plan option was not selected *****")
            try:
                self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_advantage_plan))
                time.sleep(10)
                if self.Keen_Generate.verify_medicare_advantage_plan().text == "Medicare Advantage":
                    # is_displayed():
                    self.log.info("***** Medicare advantage plan option was selected *****")
                    self.action_utils.wait_for_element((Keen_Quote_Generation.medicare_advantage_plan_list))
                    time.sleep(5)
                    medicare_advantage_plan_list=self.Keen_Generate.verify_medicare_advantage_plan_list()
                    print("Medicare_advantage_palns:",medicare_advantage_plan_list.text)
                    if medicare_advantage_plan_list.text == "No plans available.":
                        self.log.info("***** Medicare advantage plans are not available for this member  *****")
                    else:
                        self.log.info("***** Medicare advantage plans are available for this member *****")
            except Exception as ex:
                print(ex)
                self.log.info(ex)
                self.log.info("***** Medicare advantage plan option was not selected *****")
            try:
                self.action_utils.wait_for_element((Keen_Quote_Generation.part_d_plan))
                partd_section=self.Keen_Generate.verify_part_d()
                time.sleep(10)
                if partd_section.text == "Part D":
                    # is_displayed():
                    self.log.info("***** Part D plan was selected for this member *****")
                    try:
                        self.action_utils.wait_for_element((Keen_Quote_Generation.pard_d_plan_detail_list))
                        PartD_plans_list=self.Keen_Generate.verify_part_d_list()
                        time.sleep(5)
                        print("PartD_Plans_list_text:",PartD_plans_list.text)
                        if PartD_plans_list == "No plans available.":
                            self.log.info("***** PartD plans are not available for this member *****")
                    except Exception as ex:
                        self.log.info("***** PartD plans are available for this member *****")
                        print(ex)
                        self.log.info(ex)
            except Exception as ex:
                print(ex)
                self.log.info(ex)
                self.log.info("***** Part D plan was not selected for this member *****")
    def test_aledade_data(self):
        consent_member_data="Yes"
        self.log.info("***** Verifying the Keen lead in Salesforce *****")
        self.action_utils.wait_for_elements((Create_capture_member_details.Member))
        keen_member = self.Keen_create.select_member()
        Existing_account = None
        for member in keen_member:
            keen_member = member.get_attribute('title')
            print("existing members:", keen_member)
            if keen_member == 'ARTHUR DAVIS':
                Existing_account = member
        if Existing_account is not None:
            print("selected_account:", Existing_account.text)
            self.log.info(Existing_account.text)
            self.action.move_to_element(Existing_account).click().perform()
        self.action_utils.wait_for_element((Keen_Account_creation.verfiy_text_source))
        source = self.keen.validation_source_text()
        WebDriverWait(self.driver,15)
        if source == "Aledade T-65/MAI" or "Advisor Directory (Aledade)" or "Provider: Aledade":
            try:
                self.action_utils.wait_for_element((Keen_Quote_Generation.aledade_button))
                aldeade_button = self.Keen_Generate.verfiy_aledade_button()
                if aldeade_button.is_displayed():
                    self.log.info("***** Aledade button is enabled *****")
                self.Keen_Generate.verfiy_aledade_button().click()
                try:
                    self.action_utils.wait_for_element((Keen_Quote_Generation.text_msg))
                    aledade_member=self.Keen_Generate.verify_member_is_aledade()
                    if "This member's prescription and doctors are not available." in aledade_member.text:
                        self.log.info("***** This member prescription and doctors are not available in Aledade data *****")
                        self.action_utils.wait_for_element((Keen_Quote_Generation.close_aledade_data))
                        self.Keen_Generate.click_close_aledade_message()
                except Exception as ex:
                    self.log.info(ex)
                    try:
                        self.log.info("***** This member prescription and doctors are available in Aledade data *****")
                        if consent_member_data == "Yes":
                            self.action_utils.wait_for_element((Keen_Quote_Generation.data_accept))
                            self.Keen_Generate.consent_member_data_yes()
                            self.log.info("***** Member accepted for data transfer *****")
                            self.action_utils.wait_for_element((Keen_Quote_Generation.success_message))
                            toast_message=self.Keen_Generate.verify_toast_message_aledade()
                            if "Success!" in toast_message.text:
                                self.log.log("***** Aledade data transfered into Salesforce *****")
                        else:
                            self.log.info("***** Member didn't accept to trnsfer the data into salesforce *****")
                    except Exception as ex:
                        self.log.info(ex)
            except Exception as ex:
                self.log.info("***** Aledade button is disabled *****")
        else:
            self.log.info("***** Aledade button is disbaled *****")


    def test_verify_aledade_plans_data(self):
        self.log.info("***** Verifing the aledadeplans data *****")
        self.action_utils.wait_for_element((Create_capture_member_details.Member_details))
        self.Keen_create.Capture_Full_Member()
        self.action_utils.wait_for_element((Create_capture_member_details.plans_option))
        self.Keen_create.click_plans()
        self.action_utils.wait_for_elements((Create_capture_member_details.associated_plans_for_member))
        self.Keen_create.verify_associated_plans_for_member()
        self.log.info("***** Plans are verified *****")
        self.Keen_associate.close().click()
    def test_validate_aledade_medications(self):
        self.log.info("***** Verifing the Aledade Medications data *****")
        self.action_utils.wait_for_element((Create_capture_member_details.medication))
        self.Keen_create.Medication_option()
        self.action_utils.wait_for_element((Create_capture_member_details.existing_records))
        selected_Medication = self.Keen_create.validation_of_records()
        for i in selected_Medication:
            if i.text == "Test Medicine":
                print("Test pass")
            else:
                print("Test fail")
        self.log.info("***** Validation is completed and Member record is associated *****")
        self.Keen_associate.close().click()
    def test_validate_physicians(self):
        self.log.info("***** Verifiing Aledade Physicians *****")
        self.action_utils.wait_for_element((Create_capture_member_details.click_physicians))
        self.Keen_create.select_physicians()
        self.action_utils.wait_for_element(())
    def test_verify_one(self):
        self.Keen_Generate.save_related_person()




















