import time
from openpyxl import load_workbook
from selenium.webdriver.common.by import By

from Pages.Keen_Login import Keen_login
from selenium.webdriver import ActionChains
import allure
import pytest
from utilities.action_utils import ActionUtils
from utilities.XLUtilities import Excel_data
from selenium.webdriver.common.keys import Keys

from utilities.base_test import BaseTest
path='../test_data/Keen_Testdata.xlsx'
sheet_name="Account_Creation"
from utilities import logger_utils
from Pages.Keen_account_creation import Keen_Account_creation
@allure.description("New Keen Leads and Members account creation")
class Test_account_creation():
    def __init__(self , driver):
        self.driver = driver
        self.log = logger_utils.get_logger()
        self.path = '../test_data/Keen_Testdata.xlsx'
        self.sheet_name = "Account_Creation"
        self.readdata_account = Excel_data(path, sheet_name)
        self.action = ActionChains(self.driver)
        self.action_utils = ActionUtils(self.driver)
        self.sheet = BaseTest()
    ### Test Description:- Create a New Keen Leads and Members Record.
    ### Test Case Steps:- Login to SFDC, Click on Keen Leads and Members Tab, Click on New,
    ### Create and Save the Members record
    @pytest.mark.order(1)
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    @allure.description("Create a New Keen Leads and Membres")
    def test_lead_creation(self,row_number):
        sheet_account=self.sheet.get_sheet_name('Account_Creation')
        data_row = sheet_account[row_number]
        column_field_mapping = {
            'first_Name': 'first_Name', 'Middle_Name': 'MiddleName', 'Last_Name': 'Last_Name',
            'DoB': 'DoB', 'Email': 'Email', 'PTC': 'PTC', 'SOA': 'SOA', 'Phone': 'Phone',
            'Street_Address': 'Street_Address',
            'Source': 'Source',
            'Gender': 'Gender','status': 'Status', 'Origin': 'Origin', 'Language': 'Language',
            'MedicareID': 'MedicareID', 'Member_ID': 'Member_ID','SSN': 'SSN','MedcaidID': 'MedcaidID',
            'Medicaid_Category': 'Medicaid_Category','Low_Income_Subsidy' : 'Low_Income_Subsidy','Medicaid_status_verification_date': 'Medicaid_status_verification_date',
            'Part_A enrollment date': 'Part_A enrollment date','Part_B enrollment date': 'Part_B enrollment date',
            'Zipcode': 'Zipcode', 'City': 'City', 'State_Newcreation': 'State',
            'Member_County': 'Member_County', 'Addressline2': 'Addressline2', 'PTC popup': 'PTC popup',
            'Other_permission': 'Other_permission','Disposition' : 'Disposition','Nickname':'Nickname'
        }
        field_locators = {
            'first_Name': ((Keen_Account_creation.enter_firstName)), 'DoB': (Keen_Account_creation.enter_dob),
            'MiddleName': ((Keen_Account_creation.enter_middleName)),
            'Last_Name': ((Keen_Account_creation.enter_lastName)), 'Email': (Keen_Account_creation.enter_email),
            'PTC': (Keen_Account_creation.enter_PTC),
            'SOA': (Keen_Account_creation.enter_SOA), 'Phone': (Keen_Account_creation.enter_phone),
            'Street_Address': (Keen_Account_creation.enter_address),
            'Gender': (Keen_Account_creation.select_gender),
            'Source': (Keen_Account_creation.click_source),
            'Origin': (Keen_Account_creation.other_details_icon),
            'MedicareID': (Keen_Account_creation.medication_details_popup),
            'Member_ID': (Keen_Account_creation.member_id),
            'SSN': (Keen_Account_creation.SSN),
            'MedcaidID': (Keen_Account_creation.medicaid_id),
            'Medicaid_Category': (Keen_Account_creation.medicaid_category),
            'Low_Income_Subsidy': (Keen_Account_creation.low_income_subsidy),
            'Medicaid_status_verification_date': (Keen_Account_creation.verification_date),
            'Part_A enrollment date': (Keen_Account_creation.part_A),
            'Part_B enrollment date': (Keen_Account_creation.part_B),
            'Status': ((Keen_Account_creation.status)),
            'Language': (Keen_Account_creation.options_in_list),
            'Addressline2': (Keen_Account_creation.enter_newcreationaddress_line_2),
            'Member_County': (Keen_Account_creation.enter_county_newcreation),
            'Zipcode': (Keen_Account_creation.enter_zipcode_newcreation),
            'City': (Keen_Account_creation.enter_city_newcreation), 'State': (Keen_Account_creation.click_state),
            'PTC popup': (Keen_Account_creation.ptc_popup),
            'Other_permission': (Keen_Account_creation.other_permission),
            'Source: Practice':(Keen_Account_creation.practice_record),
            'Disposition' : (Keen_Account_creation.disposition_field),
            'Nickname': (Keen_Account_creation.enter_nickname),
        }
        keen = Keen_Account_creation(self.driver)
        keen_status_value = None
        for cell in data_row:
            column_name = sheet_account.cell(row=2, column=cell.column).value
            if column_name in column_field_mapping:
                field_name = column_field_mapping[column_name]
                self.log.info(field_name)
                # print("mapping is done")
                column_value = cell.value
                # print("input:", column_value)
                # print("column name:", column_name)
                locator = field_locators[field_name]
                element = self.driver.find_element(*locator)
                if element.tag_name == 'button':
                    if field_name == 'Source':
                        element.click()
                        source = keen.select_source()
                        for option in source:
                            if option.get_attribute('title') == column_value:
                                print("clickable option:", column_value)
                                print("options are present")
                                self.driver.execute_script("arguments[0].click();", option)
                                break
                        if column_value == "Community Event":
                            assert keen.pop_up_sourceType().is_displayed(), "Source popup is not displayed"
                            keen.select_community_organization().send_keys("Test Test")
                            list_community = keen.select_record()
                            print(len(list_community))
                            if len(list_community) == 0:
                                print("It is having 0 records")
                                keen.select_community_organization().send_keys(Keys.CONTROL + "a")
                                keen.select_community_organization().send_keys(Keys.BACKSPACE)
                            elif len(list_community) != 0:
                                print("Records are present")
                                for community in list_community:
                                    if community.text == "Test test":
                                        print(community.text)
                                        print("test Community is created")
                                        self.action.move_to_element(community).click().perform()
                                    else:
                                        input_field = keen.select_community_organization()
                                        self.driver.execute_script("arguments[0].value = '';", input_field)
                                        print("test community is not there")
                                        # keen.select_community_organization().clear()
                            keen.select_practice_directory().send_keys("Test Directory")
                            list_practice = keen.select_directory_records()
                            print("practice length: ", len(list_practice))
                            if len(list_practice) == 0:
                                print("It is having 0 records")
                                keen.select_practice_directory().clear()
                            elif len(list_practice) != 0:
                                print("Records are present")
                                for select_practice in list_practice:
                                    print(select_practice.get_attribute('title'))
                                    if select_practice.get_attribute('title') == "Test Directory":
                                        time.sleep(5)
                                        print("test practice is created")
                                        self.action.move_to_element(select_practice).click().perform()
                                    else:
                                        keen.select_practice_directory().clear()
                                        print("test practice is not created")
                            keen.event().send_keys("Test Event")
                            list_events = keen.select_events_records()
                            print("events length: ", len(list_events))
                            if len(list_events) == 0:
                                print("It is having 0 records")
                                keen.event().clear()
                            elif len(list_events) != 0:
                                print("Records are present")
                                for events in list_events:
                                    print(events.get_attribute('title'))
                                    if events.get_attribute('title') == "Test Event":
                                        print("test event is created")
                                        self.action.move_to_element(events).click().perform()
                                        break
                                    else:
                                        keen.event().clear()
                                        print("test event is not created")
                            if len(list_community) == 0 or len(list_practice) == 0 or len(list_events):
                                keen.cancel_sourcetype_popup()
                                print("Popup Cancel")
                            else:
                                keen.ok()
                                print("click ok")
                        elif column_value == "Member Referral" or "Source, Referrals from Redesign":
                            if keen.pop_up_sourceType().is_displayed():
                                assert True
                            else:
                                assert False
                            keen.click_referring_member("Test Member")
                            time.sleep(5)
                            list_referring_member = keen.select_record()
                            if len(list_referring_member) == 0:
                                keen.cancel_sourcetype_popup()
                            else:
                                for associate_member in list_referring_member:
                                    if associate_member.text == "Test Test":
                                        self.action.move_to_element(associate_member).click().perform()
                                        break
                                    keen.member_relationship()
                                    list_relation = keen.relation_member()
                                    for relation in list_relation:
                                        if relation.text == "Friend":
                                            self.action.move_to_element(relation).click().perform()
                                            keen.ok()
                                            break
                        elif column_value == "Provider: Aledade" or "Provider: Archwell" or "Advisor Directory (Aledade)" or "Aledade Call Center" or "Aledade T-65/MAI" or "Provider: ChenM / Ded Call center" or "Source, Provider: ChenM / Ded MCG" or "Source, Provider: Gather" or "Source, Provider: Homeward" or "Source, Provider: IORA" or "Source, Provider: Other":
                            if keen.pop_up_sourceType().is_displayed():
                                assert True
                            else:
                                assert False
                            keen.select_practice_directory().send_keys("Test test")
                            list_practice = keen.select_record()
                            if len(list_practice) == 0:
                                keen.cancel_sourcetype_popup()
                            else:
                                print("select record")
                                for practice_only in list_practice:
                                    print(practice_only.text)
                                    if practice_only.text == "Test test":
                                        self.action.move_to_element(practice_only).click().perform()
                                        keen.ok()
                                        print("Source is selected")
                                        break
                        elif column_value == "Campaign":
                            keen.select_campaign().send_keys("Test Test")
                            campaign_list = keen.select_record()
                            if len(campaign_list) == 0:
                                keen.cancel_sourcetype_popup()
                            else:
                                for campaign in campaign_list:
                                    if campaign.text == "Test test":
                                        self.action.move_to_element(campaign).click().perform()
                                        keen.ok()
                                        break
                        elif column_value == "Other":
                            keen.Lead_other().send_keys("Test Test")
                            keen.ok()
                        else:
                            print("Continue to Next Field")
                    if field_name == 'Status':
                        status_value = cell.value
                        element.click()
                        pick_up_status = keen.select_status()
                        for keen_status in pick_up_status:
                            if keen_status.get_attribute('title') == column_value:
                                keen_status_value = column_value
                                print("clickable option:", column_value)
                                print("options are present")
                                self.driver.execute_script("arguments[0].click();", keen_status)
                                break
                    if field_name == 'Gender':
                        element.click()
                        pick_up_gender = keen.select_gender_in_list()
                        for gender in pick_up_gender:
                            if gender.text == column_value:
                                self.driver.execute_script("arguments[0].click();", gender)
                                break
                    if field_name == 'State':
                        element.click()
                        states = keen.select_state_newlead()
                        for list_states in states:
                            if list_states.text == column_value:
                                self.driver.execute_script("arguments[0].click();", list_states)
                                break
                    if field_name == 'Medicaid_Category':
                        element.click()
                        self.log.info("***** Medicaid field is selected *****")
                        self.action_utils.wait_for_elements((Keen_Account_creation.member_options))
                        medicaid_options = keen.select_state_newlead()
                        for options in medicaid_options:
                            if options.get_attribute('title').strip() == column_value.strip():
                                self.log.info("*****Medicareid option is matched *****")
                                self.driver.execute_script("arguments[0].click();", options)
                                self.log.info("***** medicaid_category option is selected *****")
                                break
                    if field_name == 'Low_Income_Subsidy':
                        element.click()
                        self.log.info("***** low_income_subsidy field is clicked *****")
                        self.action_utils.wait_for_elements((Keen_Account_creation.member_options))
                        medicaid_options = keen.select_state_newlead()
                        for options in medicaid_options:
                            if options.get_attribute('title').strip() == column_value.strip():
                                self.log.info("*****low_income_subsidy option is matched *****")
                                self.driver.execute_script("arguments[0].click();", options)
                                self.log.info("***** medicaid_category option is selected *****")
                                break
                    if field_name == 'Disposition':
                        self.log.info("***** Disposition field is present *****")
                        element.click()
                        self.log.info("***** Disposition field is clicked *****")
                        Disposition_options = keen.tabs_options()
                        for dispositions in Disposition_options:
                            if dispositions.get_attribute('title') == column_value:
                                self.driver.execute_script("arguments[0].click();", dispositions)
                                self.log.info("***** Disposition option is selected *****")
                                break
                    if field_name == 'Member_County':
                        self.log.info("***** County field is present *****")
                        element.click()
                        time.sleep(3)
                        self.action_utils.wait_for_elements((Keen_Account_creation.options_for_county))
                        county_options=keen.select_county()
                        for options in county_options:
                            print("county_value:", options.get_attribute('data-value'))
                            print("county_input_value:",column_value)
                            if options.get_attribute('data-value').strip() == column_value.strip():
                                self.driver.execute_script("arguments[0].click();", options)
                                self.log.info("***** County option is selected *****")

                        # county_value=keen.enter_county_newlead().get_attribute('data-value')

                elif element.tag_name == 'lightning-icon':
                    if field_name == 'MedicareID':
                        print("Medicare detail popup is selecetd")
                        keen.select_medication_details()
                        keen.enter_medicare_ID().send_keys(column_value)
                    if field_name == 'PTC popup':
                        keen.click_ptc_popup()
                        assert keen.pop_up_sourceType().is_displayed(), "Source popup is not displayed"
                        keen.click_permission_to_contact_filed()
                        ptc_popup_options = keen.tabs_options()
                        for options_ptc in ptc_popup_options:
                            if options_ptc.text == column_value:
                                self.driver.execute_script("arguments[0].click();", options_ptc)
                                break
                        if field_name == 'Other_permission':
                            element.send_keys(column_value)
                    if field_name == 'Origin':
                        keen.other_details()
                        keen.Country_of_origin().click()
                        options = keen.select_Country_of_origin()
                        for option in options:
                            print("conutry:", option.text)
                            if option.text == column_value:
                                self.driver.execute_script("arguments[0].click();", option)
                                print("country is selected")
                                break
                        keen.ok()
                elif element.tag_name == 'span':
                    print("Span tag is present")
                    if field_name == 'Language':
                        print("langauage is present")
                        keen.other_details()
                        language_list = keen.tabs_options()
                        for languages in language_list:
                            if languages.text == column_value:
                                self.driver.execute_script("arguments[0].click();", languages)
                                print("Language is selected")
                                break
                        keen.select_to_chosen()
                        keen.ok()
                else:
                    # if field_name == 'Status':
                    #     print("status field is present")
                    #     keen_status_value=column_value
                    element.clear()
                    element.send_keys(column_value)
                    if field_name == 'Member_ID':
                        keen.Click_Ok()
                        self.log.info("***** Medicaredetails popup is closed *****")
                    if field_name == 'Other_permission':
                        keen.ok()
                        self.log.info("***** Other permission popup is closed *****")
        # keen.click_save()
        return keen_status_value
    # def test_validation_account_creation(self,row_number):
    #     keen=Keen_Account_creation(self.driver)
    #     action_utils=ActionUtils(self.driver)
    #     self.log.info("*****Test Data for AccountCreation*****")
    #     first_name = self.readdata_account.readdata(row_number, 1)
    #     middle_name = self.readdata_account.readdata(row_number, 2)
    #     last_name = self.readdata_account.readdata(row_number, 3)
    #     D_o_B = self.readdata_account.readdata(row_number, 4)
    #     Email = self.readdata_account.readdata(row_number, 5)
    #     PTC = self.readdata_account.readdata(row_number, 6)
    #     SOA = self.readdata_account.readdata(row_number, 7)
    #     Phone = self.readdata_account.readdata(row_number, 8)
    #     Street_Address = self.readdata_account.readdata(row_number, 9)
    #     Addressline_2 = self.readdata_account.readdata(row_number, 31)
    #     zipcode = self.readdata_account.readdata(row_number, 23)
    #     county = self.readdata_account.readdata(row_number, 29)
    #     city = self.readdata_account.readdata(row_number, 24)
    #     state = self.readdata_account.readdata(row_number, 32)
    #     Gender = self.readdata_account.readdata(row_number, 10)
    #     source_of_creation = self.readdata_account.readdata(row_number, 11)
    #     status = self.readdata_account.readdata(row_number, 12)
    #     origin = self.readdata_account.readdata(row_number, 13)
    #     MedicareID = self.readdata_account.readdata(row_number, 15)
    #     MedcaidID = self.readdata_account.readdata(row_number, 16)
    #     Part_A_enrollment_date = self.readdata_account.readdata(row_number, 17)
    #     Plan_enrollment_date = self.readdata_account.readdata(row_number, 18)
    #     Part_B_enrollment_date = self.readdata_account.readdata(row_number, 19)
    #     Medicaid_status_verification_date = self.readdata_account.readdata(row_number, 20)
    #     SSN = self.readdata_account.readdata(row_number, 21)
    #     try:
    #         verify_name=keen.validation_name()
    #         assert verify_name == first_name+' '+middle_name+' '+last_name,"Name is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         verify_dob = keen.validation_of_DoB()
    #         assert verify_dob == D_o_B,"DOB is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         verify_email = keen.validation_of_email()
    #         assert verify_email == Email,"Email is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         verify_gender = keen.validation_of_Gender()
    #         assert verify_gender == Gender , "Gender is not mactched"
    #
    #     except Exception as ex:
    #         print(ex)
    #     if source_of_creation == "Keen Lead":
    #         if keen.validation_of_SOA().get_attribute('value') == "None":
    #             assert True
    #         else:
    #             assert False
    #     verify_soa = keen.validation_of_SOA()
    #     if verify_soa == SOA:
    #         assert True
    #     else:
    #         assert False
    #     verify_phone = keen.validation_of_Phone()
    #     if verify_phone == Phone:
    #         assert True
    #     else:
    #         assert False
    #     verify_status = keen.validation_of_status()
    #     if verify_status == status:
    #         assert True
    #     else:
    #         assert False
    #     try:
    #         verify_address=keen.validation_of_Address()
    #         print(verify_address)
    #         assert verify_address == Street_Address+', '+Addressline_2+', '+city+', '+state+', '+zipcode+', '+county, "Address fields are not matched"
    #     except Exception as ex:
    #         print(ex)
    #
    #     verify_source = keen.validation_of_source()
    #     assert verify_source == source_of_creation , "Source is not matched"
    #     try:
    #         keen.select_source_details()
    #         if source_of_creation == "Community Event":
    #             organization = keen.validating_community_organization()
    #             verify_organization = organization.get_attribute("value")
    #             if verify_organization == "Test Community":
    #                 print("Test pass")
    #             else:
    #                 print("Test fail")
    #                 self.log.info("*****Test community record is not in salesforce ******")
    #             practice = keen.validating_practice_directory()
    #             verify_practice = practice.get_attribute("value")
    #             if verify_practice == "Test Directory":
    #                 print("Test pass")
    #             else:
    #                 print("Test fail")
    #                 self.log.info("*****Test directory record is not in salesforce ******")
    #             event = keen.validating_event().get_attribute("value")
    #             if event == "Test Event":
    #                 assert True
    #             else:
    #                 self.log.info("*****Test Event record is not in salesforce ******")
    #         elif source_of_creation == "Member Referral":
    #             member=keen.validating_referral_meber().get_attribute("value")
    #             if member == "Test Anil Kumar":
    #                 print("Test pass")
    #                 realtion_ship = keen.member_relationship().get_attribute("value")
    #                 if realtion_ship == "Friend":
    #                    print("Test pass")
    #                 else:
    #                     print("Test fail")
    #             else:
    #                 print("Test fail")
    #                 self.log.info("*****Test Anil kumar record is not in salesforce ******")
    #             time.sleep(5)
    #         elif source_of_creation == "Provider: Aledade" or "Provider: Archwell":
    #                 practice = keen.validating_practice_directory()
    #                 verify_practice = practice.get_attribute("value")
    #                 if verify_practice == "Test Directory":
    #                     print("Test pass")
    #                 else:
    #                     print("Test fail")
    #                     self.log.info("*****Test Derictory  record is not in salesforce ******")
    #         else:
    #             print("Contiune to next field")
    #     except Exception as ex:
    #         print(ex)
    #     action_utils.wait_for_element((Keen_Account_creation.close_popup))
    #     keen.Click_close_popup()
    #     verify_ptc = keen.validation_of_PTC()
    #     assert verify_ptc == PTC, "PTC is not matched"
    #     keen.select_medication_popup()
    #     medcaid=keen.enter_Medcaid_ID()
    #     verify_medcaid=medcaid.get_attribute("value")
    #     assert verify_medcaid == MedcaidID, "Medication id is not matched"
    #     try:
    #         PartA_date=keen.enter_Part_A_enrollment_date()
    #         verify_PartA_Date=PartA_date.get_attribute("value")
    #         assert verify_PartA_Date == Part_A_enrollment_date,"Part A enrollmentdate is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         PartB_Date=keen.enter_Part_B_enrollment_date()
    #         verfiy_PartB_date=PartB_Date.get_attribute("value")
    #         assert verfiy_PartB_date == Part_B_enrollment_date, "Part B enrollment date is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         ssn=keen.enter_SSN()
    #         verify_ssn=ssn.get_attribute("value")
    #         assert verify_ssn == SSN, "SSN is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         medicare=keen.enter_medicare_ID()
    #         verify_medicareID=medicare.get_attribute("value")
    #         assert verify_medicareID == MedicareID,"MedicareID is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         planEnrollDate=keen.enter_PlanEnrollmentDate()
    #         verfiy_planEnrollmentDate=planEnrollDate.get_attribute("value")
    #         assert verfiy_planEnrollmentDate == Plan_enrollment_date,"Plan_enrollment_date is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         Medicaid_date=keen.enter_Medicaid_status_verification_date()
    #         verify_Medicaid_status_verification_date=Medicaid_date.get_attribute("value")
    #         assert verify_Medicaid_status_verification_date == Medicaid_status_verification_date, "Medicaid status verification date is not matched"
    #     except Exception as ex:
    #         print(ex)
    #     keen.close_medicaredetails_popup()
    #     self.log.info("*****Valiadtion is completed*****")
    # #### Editing the existing Keen leads and Members record
    # ### Test Descriotion:- Editing the Exisiting Keen Leads and Members records
    # ### Test Case Steps:- Login to SFDC, Click on Keen Leads and Members tab,
    # ### Select any one of the record,Edit the record
    # @allure.description("Editing the existing Keen Leads and Members")
    # @pytest.mark.order(2)
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_edit_keen_account(self,row_number):
    #     keen = Keen_Account_creation(self.driver)
    #     action = ActionChains(self.driver)
    #     action_utils=ActionUtils(self.driver)
    #     self.log.info("Editing the Keen leads and membres")
    #     try:
    #         edit_D_o_B = self.readdata_account.readdata( row_number, 4)
    #         edit_Street = self.readdata_account.readdata(row_number, 9)
    #         edit_addressline2 = self.readdata_account.readdata(row_number, 31)
    #         edit_zipcode = self.readdata_account.readdata(row_number, 23)
    #         edit_county = self.readdata_account.readdata(row_number, 29)
    #         edit_city = self.readdata_account.readdata(row_number, 24)
    #         edit_state = self.readdata_account.readdata(row_number, 32)
    #         edit_Email = self.readdata_account.readdata(row_number, 5)
    #         edit_PTC=self.readdata_account.readdata(row_number,6)
    #         edit_SOA=self.readdata_account.readdata(row_number,7)
    #         edit_Phone=self.readdata_account.readdata(row_number,8)
    #         edit_Gender = self.readdata_account.readdata(row_number,10)
    #         edit_source_of_creation=self.readdata_account.readdata(row_number,11)
    #         edit_status = self.readdata_account.readdata(row_number, 12)
    #         edit_origin = self.readdata_account.readdata( row_number, 13)
    #         edit_language= self.readdata_account.readdata(row_number,14)
    #         MedicareID=self.readdata_account.readdata(row_number,15)
    #         MedcaidID=self.readdata_account.readdata(row_number,16)
    #         Part_A_enrollment_date=self.readdata_account.readdata(row_number,17)
    #         Plan_enrollment_date=self.readdata_account.readdata(row_number,18)
    #         Part_B_enrollment_date=self.readdata_account.readdata(row_number,19)
    #         Medicaid_status_verification_date=self.readdata_account.readdata(row_number,20)
    #         edit_SSN=self.readdata_account.readdata(row_number,21)
    #         self.log.info("***** Select keen lead to edit *****")
    #         keen.select_keen_member()
    #         time.sleep(15)
    #         self.log.info("***** Click on edit to edit the keen lead *****")
    #         keen.click_on_edit()
    #         time.sleep(10)
    #         self.log.info("*****Entering the test data *****")
    #         keen.DoB(edit_D_o_B)
    #         keen.email(edit_Email)
    #         keen.premession_to_contact(edit_PTC)
    #         action_utils.wait_for_element((Keen_Account_creation.ptc_popup))
    #         self.log.info("***** Select PTC popup *****")
    #         keen.click_ptc_popup()
    #         keen.click_permession_to_contact()
    #         options_contact=keen.tabs_options()
    #         for permission_to_contact in options_contact:
    #             if permission_to_contact.text == "In person event":
    #                 action.move_to_element(permission_to_contact).click().perform()
    #                 break
    #         keen.enter_other_permission("Call")
    #         keen.save_popup()
    #         self.log.info("***** PTC Data is saved *****")
    #         action_utils.wait_for_element((Keen_Account_creation.toast_message))
    #         permission_message = keen.Success_Message()
    #         if permission_message.is_displayed():
    #             assert True
    #         else:
    #             assert False
    #         keen.scope_of_appointment_date().clear()
    #         keen.scope_of_appointment_date().send_keys(edit_SOA)
    #         keen.phone(edit_Phone)
    #         keen.street_address().send_keys(edit_Street)
    #         keen.gender()
    #         pick_up_gender = keen.select_gender()
    #         for gender in pick_up_gender:
    #             if gender.text == edit_Gender:
    #                 action.move_to_element(gender).click().perform()
    #                 break
    #         self.log.info("*****Select Gender popup *****")
    #         keen.click_gender_popup()
    #         action_utils.wait_for_element((Keen_Account_creation.origin))
    #         keen.Country_of_origin().click()
    #         list_orign = keen.select_Country_of_origin()
    #         for orgin in list_orign:
    #             if orgin.text == edit_origin:
    #                 action.move_to_element(orgin).click().perform()
    #                 break
    #         language_list = keen.tabs_options()
    #         for languages in language_list:
    #             if languages.text == edit_origin:
    #                 action.move_to_element(languages).click().perform()
    #                 break
    #         keen.select_to_chosen()
    #         keen.save_popup()
    #         self.log.info("***** Gender popup data is saved *****")
    #         action_utils.wait_for_element((Keen_Account_creation.toast_message))
    #         gender_message = keen.Success_Message()
    #         if gender_message.is_displayed():
    #             assert True
    #         else:
    #             assert False
    #         self.log.info("***** Select source *****")
    #         action_utils.wait_for_element((Keen_Account_creation.click_source))
    #         source = keen.select_source()
    #         for sourec_list in source:
    #             if sourec_list.text == edit_source_of_creation:
    #                 action.move_to_element(sourec_list).click().perform()
    #                 print("Sorce selected")
    #                 break
    #         if edit_source_of_creation == "Community Event":
    #             assert keen.pop_up_sourceType().is_displayed(), "Source popup is not displayed"
    #             keen.select_community_organization().send_keys("Test Community")
    #             list_record = keen.select_record()
    #             if len(list_record) == 0:
    #                 keen.select_community_organization().clear()
    #             else:
    #                 for community in list_record:
    #                     if community.text == "Test Community":
    #                         action.move_to_element(community).click().perform()
    #             keen.select_practice_directory().send_keys("Test Directory")
    #             list_practice = keen.select_record()
    #             if len(list_practice) == 0:
    #                 keen.select_practice_directory().clear()
    #             else:
    #                 for select_practice in list_practice:
    #                     if select_practice.text == "Test Directory":
    #                         action.move_to_element(select_practice).click().perform()
    #                         break
    #             keen.event().send_keys("Test Test")
    #             list_events = keen.select_record()
    #             if len(list_events) == 0:
    #                 keen.event().clear()
    #             else:
    #                 for events in list_events:
    #                     if events.text == "Test Test":
    #                         action.move_to_element(events).click().perform()
    #             if len(list_record) == 0 or len(list_practice) == 0 or len(list_events) == 0:
    #                 keen.cancel_sourcetype_popup()
    #         elif edit_source_of_creation == "Member Referral":
    #             if keen.pop_up_sourceType().is_displayed():
    #                 assert True
    #             else:
    #                 assert False
    #             keen.click_referring_member("Test Member")
    #             time.sleep(5)
    #             list_referring_member = keen.select_record()
    #             if len(list_referring_member) == 0:
    #                 keen.cancel_sourcetype_popup()
    #             else:
    #                 for associate_member in list_referring_member:
    #                     if associate_member.text == "Test Test":
    #                         action.move_to_element(associate_member).click().perform()
    #                         break
    #                     keen.member_relationship()
    #                     list_relation = keen.relation_member()
    #                     for relation in list_relation:
    #                         if relation.text == "Friend":
    #                             action.move_to_element(relation).click().perform()
    #                             keen.ok()
    #                             break
    #
    #         elif edit_source_of_creation == "Provider: Aledade" or "Provider: Archwell":
    #             if keen.pop_up_sourceType().is_displayed():
    #                 assert True
    #             else:
    #                 assert False
    #             keen.select_practice_directory().send_keys("Test test")
    #             list_practice = keen.select_record()
    #             if len(list_practice) == 0:
    #                 keen.cancel_sourcetype_popup()
    #             else:
    #                 print("select record")
    #                 for practice_only in list_practice:
    #                     print(practice_only.text)
    #                     if practice_only.text == "Test test":
    #                         action.move_to_element(practice_only).click().perform()
    #                         keen.ok()
    #                         print("Source is selected")
    #                         break
    #
    #         else:
    #             print("Continue to Next Field")
    #         keen.status()
    #         pick_up_status=keen.select_status()
    #         # WebDriverWait(driver, 20).until(EC.presence_of_element_located(Keen.save()))
    #         for status_list in pick_up_status:
    #             if status_list.text == edit_status:
    #                 action.move_to_element(status_list).click().perform()
    #                 break
    #         keen.edit_stress_address(edit_Street)
    #         keen.enter_address_line2().send_keys(edit_addressline2)
    #         keen.enter_city_newLead().send_keys(edit_city)
    #         keen.click_state_newLead().click()
    #         lead_states=keen.select_state_newlead()
    #         for states in lead_states:
    #             if states.text == edit_state:
    #                 action.move_to_element(states).click().perform()
    #                 break
    #         keen.save_popup()
    #         self.log.info("***** Address popup is saved ******")
    #         action_utils.wait_for_element((Keen_Account_creation.toast_message))
    #         permission_message = keen.Success_Message()
    #         if permission_message.is_displayed():
    #             assert True
    #         else:
    #             assert False
    #         keen.enter_zipcode_newlead().send_keys(edit_zipcode)
    #         keen.enter_county_newlead().send_keys(edit_county)
    #         self.log.info("***** Eidt Account Owner *****")
    #         keen.click_edit_owner()
    #         action_utils.wait_for_element((Keen_Account_creation.search_owner))
    #         time.sleep(5)
    #         keen.click_search_owner()
    #         time.sleep(5)
    #         owner = keen.tabs_options()
    #         for owners in owner:
    #             if owners.text == "Keen Engineering":
    #                 action.move_to_element(owners).click().perform()
    #                 break
    #         self.log.info("***** Select Medication popup *****")
    #         keen.select_medication_details()
    #
    #         keen.enter_medicare_ID().send_keys(MedicareID)
    #         keen.enter_Part_A_enrollment_date().send_keys(Part_A_enrollment_date)
    #
    #         keen.enter_Part_B_enrollment_date().send_keys(Part_B_enrollment_date)
    #         keen.enter_SSN().send_keys(edit_SSN)
    #         keen.enter_Medcaid_ID().send_keys(MedcaidID)
    #         keen.enter_PlanEnrollmentDate().send_keys(Plan_enrollment_date)
    #         keen.enter_Medicaid_status_verification_date().send_keys(Medicaid_status_verification_date)
    #         time.sleep(10)
    #         keen.save_popup()
    #         self.log.info("***** Medication popup data is saved *****")
    #         action_utils.wait_for_element((Keen_Account_creation.toast_message))
    #         permission_message = keen.Success_Message()
    #         if permission_message.is_displayed():
    #             assert True
    #         else:
    #             assert False
    #         keen.click_save()
    #         self.log.info("*****Edited data is saved*****")
    #         #### Valiadtion of Edited record
    #         self.log.info("*****Valiadtion is started*****")
    #         verify_email=keen.validation_of_email()
    #         assert verify_email == edit_Email, "edit_Email data is not matched"
    #         verify_dob=keen.validation_of_DoB()
    #         assert verify_dob == edit_D_o_B, "edit_D_o_B data is not matched"
    #         verify_ptc=keen.validation_of_PTC()
    #         assert verify_ptc == edit_PTC, "edit_PTC data is not matched"
    #         verify_gender=keen.validation_of_Gender()
    #         assert verify_gender == edit_Gender, "edit_Gender data is not matched"
    #         verify_soa=keen.validation_of_SOA()
    #         if verify_soa == edit_SOA:
    #             assert True
    #         else:
    #             assert False
    #         verify_phone=keen.validation_of_Phone()
    #         assert verify_phone == edit_Phone, "Phone number data is not matched"
    #         verify_status=keen.validation_of_status()
    #         assert verify_status == edit_status," Status is not matched"
    #         verify_source=keen.validation_of_source()
    #         assert verify_source == edit_source_of_creation, "Source is not matched"
    #         try:
    #             keen.select_source_details()
    #             if edit_source_of_creation == "Community Event":
    #                 organization = keen.validating_community_organization()
    #                 verify_organization = organization.get_attribute("value")
    #                 assert verify_organization == "Test Community","Organization is not matched"
    #                 practice = keen.validating_practice_directory()
    #                 verify_practice = practice.get_attribute("value")
    #                 assert verify_practice == "Test Directory", "practice is not matched"
    #                 event = keen.validating_event().get_attribute("value")
    #                 assert event == "Test Event", "Event is not matched"
    #             elif edit_source_of_creation == "Member Referral":
    #                 member = keen.validating_referral_meber().get_attribute("value")
    #                 assert member == "Test Anil Kumar","Member is not matched"
    #                 time.sleep(5)
    #                 realtion_ship = keen.member_relationship().get_attribute("value")
    #                 assert realtion_ship == "Friend","Relation is not matched "
    #             elif edit_source_of_creation == "Provider: Aledade" or "Provider: Archwell":
    #                 practice = keen.validating_practice_directory()
    #                 verify_practice = practice.get_attribute("value")
    #                 assert verify_practice == "Test Directory", "Practice directory is not matched"
    #             else:
    #                 print("Contiune to next field")
    #         except Exception as ex:
    #             print(ex)
    #         self.log.info("*****Valiadtion is completed*****")
    #     except Exception as ex:
    #         print(ex)
    #
    # ### Test description:- Create Duplicate Records
    # ### Test Case Steps :- Login to SFDC, Click on Keen Leads and Members tab,Click on New, Cancel duplicate record creation
    # @allure.description("Verify the Duplicate records")
    # @pytest.mark.order(3)
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_Duplicate_records_cancel(self,row_number):
    #     keen=Keen_Account_creation(self.driver)
    #     action = ActionChains(self.driver)
    #     action_utils=ActionUtils(self.driver)
    #     try:
    #         if keen.pop_up_Duplicate():
    #             assert True
    #         else:
    #             assert False
    #         keen.cancel_record_creation()
    #     except Exception as ex:
    #         print(ex)
    # ### Test description:- Create Duplicate Records
    # ### Test Case Steps :- Login to SFDC, Click on Keen Leads and Members tab,Click on New, Create Duplicate record
    # # @pytest.mark.order(4)
    # @allure.description("Create Duplicate Records")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_Duplicate_records_Create(self,row_number):
    #     try:
    #         keen = Keen_Account_creation(self.driver)
    #         action = ActionChains(self.driver)
    #         keen_login=Keen_login(self.driver)
    #         self.log.info("*****Test Data for AccountCreation*****")
    #         keen.click_save()
    #         if keen.pop_up_Duplicate().is_displayed():
    #             print("Test Pass")
    #         else:
    #             print("Test fail")
    #         keen.create_Duplicate_record()
    #         name=keen.keen_member()
    #         self.log.info("***** Duplicate record is created *****")
    #         tab_options=keen.tabs_options()
    #         for i in tab_options:
    #             if i.text == "Reports":
    #                keen.tab_reports()
    #             else:
    #                 keen.click_more()
    #                 break
    #         time.sleep(5)
    #         keen.click_reports()
    #         time.sleep(5)
    #         keen.click_AllReports()
    #         time.sleep(5)
    #         keen.search_allreports("Duplicate Report Data")
    #         duplicate_data = keen.duplicate_recorddata()
    #         for i in duplicate_data:
    #             if i.text == "Duplicate Report Data":
    #                 action.move_to_element(i).click().perform()
    #                 break
    #         keen.click_Duplicate_reports()
    #         try:
    #             validation_duplicaterecord = keen.validation_recorddata()
    #             for recorddata in validation_duplicaterecord:
    #                 if recorddata.text == name:
    #                     assert True
    #                 else:
    #                     assert False
    #         except Exception as ex:
    #             print(ex)
    #         keen_login.keen_leads_members()
    #         leads=keen.select_member()
    #         keen_members=len(leads)
    #         keen.delete_keen_lead()
    #         keen.click_delete()
    #         delete_popup=keen.verify_delete_popup()
    #         if delete_popup.is_displayed():
    #             assert True
    #         else:
    #             assert False
    #         leads = keen.select_member()
    #         lead_members = len(leads)
    #         assert keen_members == lead_members -1,"Keen lead record is not deleted"
    #     except Exception as ex:
    #         print(ex)
    #
    #











