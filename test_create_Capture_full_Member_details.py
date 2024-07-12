import allure
import re
import pytest
import time
from Pages.Keen_Login import Keen_login
from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
from Pages.Keen_Associate_capture_full_member_details import Associate_Capture_full_Member_details
from selenium.webdriver.common.by import By
from utilities.XLUtilities import Excel_data
from utilities.action_utils import ActionUtils
from utilities import logger_utils
import autoit
from openpyxl import load_workbook

from utilities.base_test import BaseTest

path="../test_data/Keen_Testdata.xlsx"
from selenium.webdriver import ActionChains
readdata_form_excel = Excel_data(path, "Plans")
readdata_cargiver=Excel_data(path,"Caregiver")
readdata_plansassociate=Excel_data(path,"Plans_associate")
readdata_practices = Excel_data(path, "Practices")
readdata_medications= Excel_data(path,"Medication")
readdata_hospitals=Excel_data(path,"Hospitals")
readdata_physicians=Excel_data(path, "Physicians")
readdata_events=Excel_data(path,"Events")
readdata_pharmacies=Excel_data(path,"Pharmacies")
readdata_campaigns=Excel_data(path,"Campaigns")
readdata_community=Excel_data(path, "Community")
##Test Case Description: Create and Assosciate Capture Full Member Details to a select Member
##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click on Plans-->Create New Plan and Assosicate Plan to a Selected Member
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create , Assosicate and Edit the Member Details")
@pytest.mark.usefixtures("oneTimeSetup", "actions_utils")
class Test_create_capture_full_member_details():
    log = logger_utils.get_logger()
    sheet_name = BaseTest()
    sheet_plans = sheet_name.get_sheet_name('Plans')
    sheet_medication = sheet_name.get_sheet_name('Medication')
    sheet_practice = sheet_name.get_sheet_name('Practices')
    sheet_parent = sheet_name.get_sheet_name('Parent_organization')
    sheet_event = sheet_name.get_sheet_name('Events')
    sheet_pharmacy = sheet_name.get_sheet_name('Pharmacies')
    sheet_community=sheet_name.get_sheet_name('Community')
    sheet_related = sheet_name.get_sheet_name('Caregiver')
    def __init__(self,driver):
        self.driver=driver
    @allure.title("Create New Plan")
    @allure.description("Create and Assosciate a Plan to a Particular Member")
    ##Test Case Description: Create and Assosciate A New Plan to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click on Plans
    ##Create New Plan and Assosicate Plan to a Selected Member
    def test_select_member_to_associate_Cpature_Full_Member_details(self):
        action_utils = ActionUtils(self.driver)
        keen = Create_capture_member_details(self.driver)
        action = ActionChains(self.driver)
        self.log.info("****Select Member to Create and Assosicate Plans****")
        action_utils.wait_for_element((Create_capture_member_details.Member))
        member = keen.select_member()
        select_firstlead = member[0]
        select_firstlead.click()
        self.log.info("****Click on Capture Full Member Details to Create and Assosicate Plans****")
        action_utils.wait_for_element((Create_capture_member_details.Member_details))
        keen.Capture_Full_Member()
    def test_plans(self, row_number):
        action_utils = ActionUtils(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        print("Row number:", row_number)
        data_row = self.sheet_plans[row_number]
        column_field_mapping = {
            'Members Plan Details Name': 'Members Plan Details Name',
            'PlanID': 'PlanID', 'County': 'County', 'Parent Organization': 'Parent Organization',
            'Contract_Number': 'Contract_Number', 'PBP': 'PBP', 'Segment': 'Segment',
            'Plan_year': 'Plan_year', 'Carrier_name': 'Carrier_name', 'Product_type': 'Product_type', 'State': 'State',
            'Parent_organization' : 'Parent_organization',
        }
        field_locators = {
            'Members Plan Details Name': (Create_capture_member_details.Field_01),
            'PlanID': (Create_capture_member_details.Field_02), 'County': (Create_capture_member_details.Field_04),
            'Parent Organization': (Create_capture_member_details.Field_06),
            'Contract_Number': (Create_capture_member_details.plan_contractnumber),
            'PBP': (Create_capture_member_details.Field_D_03),
            'Segment': (Create_capture_member_details.Field_D_04),
            'Plan_year': (Create_capture_member_details.Field_D_05),
            'Carrier_name': (Create_capture_member_details.plan_carrier),
            'Product_type': (Create_capture_member_details.plan_producttype),
            'State': (Create_capture_member_details.plan_state),
            'Parent_organization' : (Create_capture_member_details.parent_organization)
        }
        self.test_select_member_to_associate_Cpature_Full_Member_details()
        action_utils.wait_for_element((Create_capture_member_details.plans_option))
        self.log.info("***** Click on plans *****")
        keen_create.click_plans()
        action_utils.wait_for_element((Create_capture_member_details.new))
        self.log.info("***** Click on New button *****")
        keen_create.click_new()
        action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
        pop_up = keen_create.pop_up_of_New_Members()
        assert pop_up.text == "New Member's plan", "New Member plans popup is not matched"
        action_utils.wait_for_element((Create_capture_member_details.plans_records))
        verify_plans = action_utils.record_verification(row_number, 'Plans', 'Plans_Created')
        if verify_plans == 'YES':
            self.log.info("***** Plans record is existing in SalesForce *****")
            existing_account=self.sheet_name.retrieve_value(row_number,'Z','Plans',0)
            print("record names:",existing_account)
            keen_create.click_plan_detail_list().send_keys(existing_account)
            action_utils.wait_for_element((Create_capture_member_details.plans_record))
            list_of_plans = keen_create.select_plans_record()
            print(len(list_of_plans))
            for plans in list_of_plans:
                print("exixtining_plans:", plans.get_attribute('title'))
                if plans.get_attribute('title') == existing_account:
                    self.driver.execute_script("arguments[0].click();", plans)
                    self.log.info("***** Plans record is existing in SalesForce *****")
                    break
            # self.test_plans_associate(row_number)
            keen_create.save_button_Add()
            self.log.info("***** Plans record is existing in SalesForce *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen_create.success_message()
            assert success_message_of_records.is_displayed(), "Record is not saved"
            return existing_account
        else:
            plan_name=None
            self.log.info("***** Plans record is not exists in Salesforce *****")
            action_utils.wait_for_element((Create_capture_member_details.plans_records))
            keen_create.click_plan_detail_list().click()
            action_utils.wait_for_element((Create_capture_member_details.new_creation))
            keen_create.click_new_member()
            action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
            pop_up_of_detail_list = keen_create.pop_up_Newcreation()
            pop = pop_up_of_detail_list.text
            assert pop == "New Plan Detail List", "popup is not displayed"
            self.log.info("***** Entering the Plan Details to Create and Assosicate *****")
            for cell in data_row:
                column_name = self.sheet_plans.cell(row=2, column=cell.column).value
                print("Column name:", column_name)
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    self.log.info("***** Column name and Salesforce fields are matched *****")
                    column_value = cell.value
                    print("input:", column_value)
                    locator = field_locators[field_name]
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        if field_name == 'State':
                            element.click()
                            self.log.info("***** State field is clicked *****")
                            action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
                            select_state = keen_create.select_options_in_list()
                            for states in select_state:
                                if states.text == column_value:
                                    self.log.info("***** State option is  displayed *****")
                                    self.driver.execute_script("arguments[0].click();", states)
                                    self.log.info("***** Particular State is selected *****")
                                    break
                        if field_name == 'Product_type':
                            element.click()
                            self.log.info("***** Product_type field  is selected *****")
                            action_utils.wait_for_elements((Create_capture_member_details.plan_options))
                            select_plantype = keen_create.select_product_type()
                            for plan_type in select_plantype:
                                if plan_type.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", plan_type)
                                    self.log.info("***** Particular Product_type option is selected *****")
                                    break
                        if field_name == 'Carrier_name':
                            element.click()
                            self.log.info("***** Carrier_name field  is selected *****")
                            action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
                            select_carrier = keen_create.select_options_in_list()
                            for carrier in select_carrier:
                                if carrier.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", carrier)
                                    self.log.info("***** Particular Carrier_name option is selected *****")
                                    break
                    else:
                        element.clear()
                        element.send_keys(column_value)
                        if field_name == 'Members Plan Details Name':
                            plan_name = cell.value
            keen_create.click_HRA_eligibility()
            keen_create.offers_planD()
        keen_create.save_button_creation()
        action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
        success_message_of_records = keen_create.success_message()
        assert success_message_of_records.is_displayed(), "Record is not saved"
        self.log.info("***** New Plan is created *****")
        self.sheet_name.write_result_in_to_excel_sheet(row_number, "Plans", "Z")
        self.log.info("***** Record is saved and write it back to excel sheet *****")
        self.test_plans_associate(row_number)
        keen_create.save_button_Add()
        action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
        success_message_of_records = keen_create.success_message()
        assert success_message_of_records.is_displayed(), "Record is not saved"
        self.log.info("***** Assosicating the Plan to a Member *****")
        return plan_name
    def test_validation_plans(self, row_number,plans_record):
        try:
            keen = Create_capture_member_details(self.driver)
            action_utils = ActionUtils(self.driver)
            print("Row number:", row_number)
            data_row = self.sheet_plans[row_number]
            column_field_mapping = {
                'Members Plan Details Name': 'Members Plan Details Name',
                'PlanID': 'PlanID',
                # 'County': 'County',
                'Parent Organization': 'Parent Organization',
                'Contract_Number': 'Contract_Number', 'PBP': 'PBP', 'Segment': 'Segment',
                'Plan_year': 'Plan_year', 'Carrier_name': 'Carrier_name', 'Product_type': 'Product_type',
                'State': 'State',
            }
            field_locators = {
                'Members Plan Details Name': (Create_capture_member_details.verify_plan),
                'PlanID': (Create_capture_member_details.verify_planid),
                # 'County': (Create_capture_member_details.verify_county),
                'Parent Organization': (Create_capture_member_details.verify_parent_organization),
                'Contract_Number': (Create_capture_member_details.verify_contract_number),
                'PBP': (Create_capture_member_details.verify_pbp),
                'Segment': (Create_capture_member_details.verify_segment),
                'Plan_year': (Create_capture_member_details.verify_plan_year),
                'Carrier_name': (Create_capture_member_details.verify_carrier_name),
                'Product_type': (Create_capture_member_details.verify_product_type),
                'State': (Create_capture_member_details.verify_state),
            }
            action_utils.wait_for_elements((Create_capture_member_details.existing_record))
            list_of_selected_caregivers = keen.validation_of_records()
            for plans in list_of_selected_caregivers:
                if plans.text == plans_record:
                    self.driver.execute_script("arguments[0].click();", plans)
                    break
            self.log.info("***** Verifing the test data ******")
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    time.sleep(10)
                    keen.click_record()
                    for cell in data_row:
                        column_name = self.sheet_plans.cell(row=2, column=cell.column).value
                        if column_name in column_field_mapping:
                            field_name = column_field_mapping[column_name]
                            self.log.info("***** Column name and Salesforce field are matched *****")
                            column_value = cell.value
                            locator = field_locators[field_name]
                            element = self.driver.find_element(*locator)
                            action_utils.wait_for_element((locator))
                            self.driver.execute_script("arguments[0].scrollIntoView();", element)
                            verify_test_data = element.text
                            try:
                                assert verify_test_data == column_value, "Test data is not matched"
                            except Exception as ex:
                                print(ex)
                    self.log.info("***** Closing the record validation tab *****")
                    if guid == guid:
                        self.driver.close()
                    if parent_guid == parent_guid:
                        self.driver.switch_to.window(parent_guid)
                        keen.close()
        except Exception as ex:
                print(ex)
    def test_plans_associate(self,row_number):
        keen=Create_capture_member_details(self.driver)
        action_utils=ActionUtils(self.driver)
        print("Row number:", row_number)
        data_row = self.sheet_plans[row_number]
        column_field_mapping = {
            'Carrier_memberid': 'Carrier_memberid',
            'HRA Completed': 'HRA Completed', 'Effective date': 'Effective date', 'Enrollment conformation number': 'Enrollment conformation number',
            'Plan End date': 'Plan End date', 'Enrollment_type': 'plan_enrollmenttype', 'App submission date': 'App submission date',
            'App approval date': 'App approval date', 'Disenrollment date': 'Disenrollment date', 'premium_frequency': 'premium_frequency',
            'Premium Amount' : 'Premium Amount','Policy Number' : 'Policy Number',
        }
        field_locators = {
            'Carrier_memberid': (Create_capture_member_details.plan_carrier_member_id),
            'HRA Completed': (Create_capture_member_details.plan_hra_date),
            'Effective date': (Create_capture_member_details.plan_effective_date),
            'Enrollment conformation number': (Create_capture_member_details.plan_number),
            'Plan End date': (Create_capture_member_details.plan_enddate),
            'EnrollmentType': (Create_capture_member_details.plan_enrollmenttype),
            'App submission date': (Create_capture_member_details.plan_appsubmission_date),
            'App approval date': (Create_capture_member_details.plan_app_approvaldate),
            'Disenrollment date': (Create_capture_member_details.plan_disenrollmentdate),
            'premium_frequency': (Create_capture_member_details.plan_premium_frequency),
            'Premium Amount': (Create_capture_member_details.plan_amount),
            'Policy Number': (Create_capture_member_details.plan_policynumber),
            'plan_enrollmenttype':(Create_capture_member_details.plan_enrollmenttype)
        }
        for cell in data_row:
            column_name = self.sheet_plans.cell(row=2, column=cell.column).value
            print("Column name:", column_name)
            if column_name in column_field_mapping:
                field_name = column_field_mapping[column_name]
                column_value = cell.value
                print("input:", column_value)
                locator = field_locators[field_name]
                element = self.driver.find_element(*locator)
                action_utils.wait_for_element((locator))
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                if element.tag_name == 'button':
                    if field_name == 'premium_frequency':
                        element.click()
                        self.log.info("***** premium_frequency field is selected *****")
                        action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                        premium_options=keen.select_options()
                        for options in premium_options:
                            if options.get_attribute('title')== column_value:
                                self.driver.execute_script("arguments[0].click();", options)
                                break
                    if field_name == 'premium_frequency':
                        element.click()
                        self.log.info("***** premium_frequency field is selected *****")
                        action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                        premium_options=keen.select_options()
                        for options in premium_options:
                            if options.get_attribute('title')== column_value:
                                self.driver.execute_script("arguments[0].click();", options)
                                break
                    if field_name == 'plan_enrollmenttype':
                        element.click()
                        self.log.info("***** plan_enrollmenttype field is selected *****")
                        action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                        plan_enrollmenttype = keen.select_options()
                        for options in plan_enrollmenttype:
                            if options.get_attribute('title') == column_value:
                                self.driver.execute_script("arguments[0].click();", options)
                                break
                else:
                    element.clear()
                    element.send_keys(column_value)




    ##Test Case Description: Editing the Assosciated Plan to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Select Member--->Click on Plans
    ##Click on Assosicated Plans-->Edit the plan
    @pytest.mark.order(2)
    def test_edit_plans(self,r,Plan_name):
        try:
                keen = Create_capture_member_details(self.driver)
                action_utils = ActionUtils(self.driver)
                # log=logger_utils.get_logger()
                keen_login = Keen_login(self.driver)
                keen_login.keen_leads_members()
                keen.select_member()
                time.sleep(25)
                keen.Capture_Full_Member()
                self.log.info("*****Test Data For Editing the Plans*****")
                PlanID = readdata_form_excel.readdata(r, 2)
                Product_Type = readdata_form_excel.readdata(r, 10)
                parent_organization = readdata_form_excel.readdata(r, 4)
                Carrier_Name = readdata_form_excel.readdata(r, 9)
                county = readdata_form_excel.readdata(r, 3)
                Contract_Number = readdata_form_excel.readdata(r, 5)
                state = readdata_form_excel.readdata(r, 11)
                PBP = readdata_form_excel.readdata(r, 6)
                Segment = readdata_form_excel.readdata(r, 7)
                Plan_year = readdata_form_excel.readdata(r, 8)
                carrier_member_ID = readdata_plansassociate.readdata(r, 1)
                HRA_Completed_Date = readdata_plansassociate.readdata(r, 2)
                Effective_date = readdata_plansassociate.readdata(r, 3)
                Enrollment_confirmation_number = readdata_plansassociate.readdata(r, 4)
                Plan_End_date = readdata_plansassociate.readdata(r, 5)
                Enrollnment_type = readdata_plansassociate.readdata(r, 6)
                App_subbmission_date = readdata_plansassociate.readdata(r, 7)
                App_approval_date = readdata_plansassociate.readdata(r, 8)
                Disenrollnment_date = readdata_plansassociate.readdata(r, 9)
                Plans = readdata_plansassociate.readdata(r, 10)
                self.driver.execute_script("scroll(0, 150);")
                action = ActionChains(self.driver)
                self.log.info("*****Click on Plans*****")
                keen.click_plans()
                pop_up_members_plans = keen.pop_up()
                if pop_up_members_plans.text == "Member Plan's List":
                    assert True
                else:
                    assert False
                list_of_selected_plans = keen.validation_of_records()
                for i in list_of_selected_plans:
                    if i.text == Plan_name:
                        action.move_to_element(i).click().perform()
                        break
                self.log.info("*****Select Plan Record for Edit******")
                parent_guid = self.driver.current_window_handle
                handle = self.driver.window_handles
                # all_guid = driver.window_handles
                for guid in handle:
                    if guid != parent_guid:
                        self.driver.switch_to.window(guid)
                        time.sleep(10)
                        keen.click_record()
                        # keen.enter_member_plan_details_name().send_keys(Member_Plan_Details_Name)
                        self.log.info("*****Editing the plan*****")
                        keen.edit_memberplan_name()
                        keen.edit_planID(PlanID)
                        keen.edit_Carrier_Name()
                        select_carrier = keen.select_options_in_list()
                        for i in select_carrier:
                            if i.text == Carrier_Name:
                                i.click()
                                break
                        keen.click_product_type()
                        select_plantype = keen.select_product_type()
                        for i in select_plantype:
                            if i.text == Product_Type:
                                action.move_to_element(i).click().perform()
                                break

                        keen.edit_state()
                        select_state = keen.select_options_in_list()
                        for i in select_state:
                            if i.text == state:
                                action.move_to_element(i).click().perform()
                                break
                        keen.edit_county(county)
                        keen.edit_ContractNumber(Contract_Number)
                        keen.edit_PBP(PBP)
                        keen.edit_segment(Segment)
                        keen.edit_planyear(Plan_year)
                        self.log.info("*****Edited the Plan*****")
                        keen.edit_save()
                        self.log.info("*****Saved the Edited Data*****")
                        ##Validation of plans
                        self.log.info("*****Validation is Strating*****")
                        try:
                            verify_name = keen.validation_plan_name()
                            if verify_name == Plan_name:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verfiy_planid = keen.validation_planId()
                            if verfiy_planid == PlanID:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_carrierName = keen.validation_Carrier_Name()
                            if verify_carrierName == Carrier_Name:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_ProductType = keen.edit_product_type()
                            if verify_ProductType == Product_Type:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:

                            verify_ContractNumber = keen.validation_contract_number()
                            if verify_ContractNumber == Contract_Number:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_state = keen.validation_state()
                            if verify_state == state:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_PBP = keen.validation_PBP()
                            if verify_PBP == PBP:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_County = keen.validation_county()
                            if verify_County == county:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_planyear = keen.validation_Planyear()
                            if verify_planyear == Plan_year:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_organization = keen.validation_organization()
                            if verify_organization == parent_organization:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verfiy_app_date = keen.validation_App_approvaldate()
                            if verfiy_app_date == App_approval_date:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        try:
                            verify_disenrollmentdate = keen.validation_Disenrollmentdate()
                            if verify_disenrollmentdate == Disenrollnment_date:
                                assert True
                            else:
                                assert False
                        except Exception as ex:
                            print(ex)
                        self.log.info("*****Validatoon is Completed*****")
                        if guid == guid:
                            self.driver.close()
                        if parent_guid ==  parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            keen.close()
                            break
        except Exception as ex:
            print(ex)

    ##Test Case Description: Create New Caregiver and Assosciating to a  Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Select Member--->Click on Caregivers
    ##Create New record-->Associate a caregiver to member
    def test_related_persons(self, row_number):
        keen = Create_capture_member_details(self.driver)
        action=ActionChains(self.driver)
        self.driver.execute_script("scroll(0, 150);")
        action_utils = ActionUtils(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.related_person))
        keen.click_related_persons()
        action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_up_caregiver = keen.pop_up()
        assert pop_up_caregiver.text == "Related Person's List", "Related Person's List popup is not matched"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
        pop_of_new_caregiver = keen.popup_related_persons()
        assert pop_of_new_caregiver.text == "New Related Person", "New Related Person is not matched"
        verify_caregiver = action_utils.record_verification(row_number, 'Caregiver', 'Caregiver_Created')
        if verify_caregiver == 'YES':
            self.log.info("***** Caregiver record is existing in Salesforce")
            existing_account = self.sheet_name.retrieve_value(row_number, 'L', 'Caregiver',0)
            print("Caregiver record names:", existing_account)
            action_utils.wait_for_elements((Create_capture_member_details.search_record))
            keen.click_Caregiver().send_keys(existing_account)
            action_utils.wait_for_elements((Create_capture_member_details.list_keen_members))
            list_of_caregivers = keen.existing_list_caregivers()
            for caregiver in list_of_caregivers:
                if caregiver.get_attribute('data-name') == existing_account:
                    self.driver.execute_script("arguments[0].click();", caregiver)
                    self.log.info("***** Caregiver record is existing in Salesforce")
                    break
            return existing_account
        else:
            self.log.info("***** Caregiver record is not existing in Salesforce")
            keen.click_Caregiver().click()
            action_utils.wait_for_element((Create_capture_member_details.new_caregiver_creation))
            new_caregiver=keen.click_new_caregiver()
            self.driver.execute_script("arguments[0].scrollIntoView();", new_caregiver)
            new_caregiver.click()
            action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
            pop_up_new_caregiver = keen.pop_up_of_New_Members()
            assert pop_up_new_caregiver.text == "New Caregiver Directory", "New Caregiver Directory is not matched"
            data_row = self.sheet_related[row_number]
            column_field_mapping = {
                'Caregiver Name': 'Caregiver Name',
                'Date of Birth': 'Date of Birth',
                'Email': 'Email',
                'Phone': 'Phone', 'Phone_type': 'Phone_type', 'other_phone': 'other_phone',
                'Address line 1': 'Address line 1', 'City': 'City', 'State': 'State', 'Relationship': 'Relationship',
                'Zipcode': 'Zipcode',
            }
            field_locators = {
                'Caregiver Name': (Create_capture_member_details.new_name),
                'Date of Birth': (Create_capture_member_details.new_caregiver_dob),
                'Email': (Create_capture_member_details.new_email),
                'Phone': (Create_capture_member_details.new_phone),
                'Phone_type': (Create_capture_member_details.new_phonetype),
                'other_phone': (Create_capture_member_details.new_otherphone),
                'State': (Create_capture_member_details.new_caregiver_state),
                'Zipcode': (Create_capture_member_details.new_zipcode),
                'Address line 1': (Create_capture_member_details.new_addressline),
                'Relationship': (Create_capture_member_details.new_relationship),
                'City': (Create_capture_member_details.new_city),
            }
            for cell in data_row:
                column_name = self.sheet_related.cell(row=2, column=cell.column).value
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    self.log.info("***** Column name and Field name is matched ******")
                    column_value = cell.value
                    locator = field_locators[field_name]
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'button':
                        if field_name == 'Relationship':
                            element.click()
                            self.log.info("***** Relationship field is clicked ******")
                            action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                            list_of_relations = keen.select_options()
                            for relation in list_of_relations:
                                if relation.get_attribute('title') == column_value:
                                    print(relation.get_attribute('title'))
                                    action.move_to_element(relation).click().perform()
                                    self.log.info("***** Praticular Relationship option is selected ******")
                                    break
                        if field_name == 'State':
                            element.click()
                            self.log.info("***** State field is clicked ******")
                            action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                            list_of_states = keen.select_options()
                            for state in list_of_states:
                                if state.get_attribute('title') == column_value:
                                    print(state.get_attribute('title'))
                                    self.driver.execute_script("arguments[0].click();", state)
                                    self.log.info("***** Relationship field is clicked ******")
                                    break
                        if field_name == 'Phone_type':
                            element.click()
                            self.log.info("***** Phone_type field is clicked ******")
                            action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                            list_of_phonetypes = keen.select_options()
                            for phone_type in list_of_phonetypes:
                                if phone_type.get_attribute('title') == column_value:
                                    print(phone_type.get_attribute('title'))
                                    self.driver.execute_script("arguments[0].click();", phone_type)
                                    self.log.info("***** Practicular Phone_type option is selected ******")
                                    break
                    else:
                        element.clear()
                        element.send_keys(column_value)
        keen.click_save_caregiver_creation()
        action_utils.wait_for_element((Create_capture_member_details.Success_message_creation))
        success_message = keen.success_message_of_records()
        assert success_message.is_displayed(),"Saved popup is not displayed"
        self.log.info("***** New Caregivers record is created *****")
        self.sheet_name.write_result_in_to_excel_sheet(row_number, "Caregiver", "L")
        self.log.info("***** Caregivers record is saved and write back to excel sheet *****")
        action_utils.wait_for_element((Create_capture_member_details.popup_realted_person))
        pop_of_new_caregiver = keen.popup_related_persons()
        assert pop_of_new_caregiver.text == "New Related Person", "New Related Person is not matched"
        action_utils.wait_for_element((Create_capture_member_details.related_save))
        keen.save_related_person()
        action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
        success_message_of_records = keen.success_message()
        assert success_message_of_records.is_displayed(), "Associated toast message is not displayed"
        self.log.info("***** Caregivers record is associated to member *****")
    # if field_name == 'Caregiver Name':
                #     caregiver_name = cell.value
                #     return caregiver_name
    def test_validation_caregivers(self,row_number,Name):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        list_of_selected_caregivers = keen.validation_of_records()
        for i in list_of_selected_caregivers:
            if i.text == Name:
                self.driver.execute_script("arguments[0].click();", Name)
                break
        self.log.info("*****Select Plan Record for Edit******")
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                action_utils.wait_for_element((Create_capture_member_details.created_record_for_validation))
                self.log.info("***** validating the created record *****")
                keen.click_record()
                data_row = self.sheet_related[row_number]
                try:
                    column_field_mapping = {
                        'Caregiver Name': 'Caregiver Name',
                        'Date of Birth': 'Date of Birth',
                        'Email': 'Email',
                        'Phone': 'Phone','Phone_type': 'Phone_type','other_phone': 'other_phone',
                        'Address line 1': 'Address line 1','City': 'City','State': 'State', 'Relationship': 'Relationship',
                        'Zipcode': 'Zipcode',
                    }
                    field_locators = {
                        'Caregiver Name': (Create_capture_member_details.verify_name),
                        'Date of Birth': (Create_capture_member_details.verify_caregiver_dob),
                        'Email': (Create_capture_member_details.verify_email),
                        'Phone': (Create_capture_member_details.verify_caregiver_phone),
                        'Phone_type': (Create_capture_member_details.verify_caregiver_phone_type),
                        'other_phone': (Create_capture_member_details.verify_caregiver_otherphone),
                        'State': (Create_capture_member_details.verify_caregiver_state),
                        'Zipcode': (Create_capture_member_details.verify_caregiver_zipcode),
                        'Address line 1': (Create_capture_member_details.verify_caregiver_addressline),
                        'Relationship': (Create_capture_member_details.verify_caregiver_relationship),
                        'City': (Create_capture_member_details.verify_caregiver_city),
                    }
                    for cell in data_row:
                        column_name = self.sheet_related.cell(row=2, column=cell.column).value
                        if column_name in column_field_mapping:
                            field_name = column_field_mapping[column_name]
                            self.log.info("***** Column name and Field name is matched ******")
                            column_value = cell.value
                            locator = field_locators[field_name]
                            action_utils.wait_for_element((locator))
                            element = self.driver.find_element(*locator)
                            self.driver.execute_script("arguments[0].scrollIntoView();", element)
                            verify_test_data = element.text
                            if verify_test_data == column_value:
                                assert True
                                self.log.info("***** Test data is matched *****")
                            else:
                                self.log.info("***** Test data is not matched *****")
                                assert False
                except Exception as ex:
                    print(ex)

    ##Test Case Description: Editing the Assosciated Caregivers to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Select Member--->Click on CareGivers
    ##Click on Assosicated CareGiver record--> Edit CareGiver Record
    @allure.description("Editing the CareGivers record assosicated to a Keen Leads and Members")
    def enter_edit_data_caregivers(self,row_number):
        try:
            keen = Create_capture_member_details(self.driver)
            keen_associate = Associate_Capture_full_Member_details(self.driver)
            log = logger_utils.get_logger()
            action_utils=ActionUtils(self.driver)
            action = ActionChains(self.driver)
            keen_login = Keen_login(self.driver)
            edit_Name = readdata_cargiver.readdata(row_number, 1)
            edit_date = readdata_cargiver.readdata(row_number, 2)
            edit_email = readdata_cargiver.readdata(row_number, 3)
            edit_phone = readdata_cargiver.readdata(row_number, 4)
            edit_phone_type = readdata_cargiver.readdata(row_number, 10)
            edit_other_phone = readdata_cargiver.readdata(row_number, 11)
            edit_address = readdata_cargiver.readdata(row_number, 5)
            edit_relationship = readdata_cargiver.readdata(row_number, 8)
            edit_city = readdata_cargiver.readdata(row_number, 6)
            edit_state = readdata_cargiver.readdata(row_number, 9)
            edit_zipcode = readdata_cargiver.readdata(row_number, 7)
            list_of_selected_caregivers = keen.validation_of_records()
            for i in list_of_selected_caregivers:
                if i.text == edit_Name:
                    action.move_to_element(i).click().perform()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles

            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    action_utils.wait_for_element((Create_capture_member_details.created_record_for_validation))
                    log.info("***** validating the created record *****")
                    keen.click_record()
                    keen.edit_caregiver_name(edit_Name)
                    time.sleep(5)
                    keen.edit_Caregiverdate_of_birth(edit_date)
                    keen.edit_Caregiveremail(edit_email)
                    keen.edit_email_opt_out()
                    keen.edit_Caregiverphone(edit_phone)
                    keen.edit_Caregiverphone_type()
                    list_of_phone = keen_associate.Select_record()
                    for phone in list_of_phone:
                        if phone.text == edit_phone_type:
                            action.move_to_element(phone).click().perform()
                            break
                    keen.edit_Caregiverother_phone(edit_other_phone)
                    keen.edit_Caregiveraddress_line_1(edit_address)
                    keen.edit_Caregivercity(edit_city)
                    keen.edit_Caregiver_state()
                    list_of_states = keen_associate.Select_record()
                    for states in list_of_states:
                        if states.text == edit_state:
                            action.move_to_element(states).click().perform()
                            break
                    keen.edit_Caregiverrelationship()
                    list_of_relations = keen_associate.Select_record()
                    for relation in list_of_relations:
                        if relation.text == edit_relationship:
                            action.move_to_element(relation).click().perform()
                            break
                    keen.edit_Caregiverzipcode(edit_zipcode)
                    log.info("*****Edited the Selected CareGivers record*****")
                    keen.edit_save()
                    log.info("*****Saved the Edited Data*****")
        except Exception as ex:
            print(ex)
    def validation_of_edit_caregivers(self):
        try:
            keen = Create_capture_member_details(self.driver)
            action_utils=ActionUtils(self.driver)
            action = ActionChains(self.driver)
            keen_login = Keen_login(self.driver)
            log=logger_utils.get_logger()
            Name = readdata_cargiver.readdata(4, 1)
            edit_Name = readdata_cargiver.readdata(5, 1)
            edit_date = readdata_cargiver.readdata(5, 2)
            edit_email = readdata_cargiver.readdata(5, 3)
            edit_phone =readdata_cargiver.readdata(5, 4)
            edit_phone_type =readdata_cargiver.readdata(5,10)
            edit_other_phone = readdata_cargiver.readdata(5, 11)
            edit_address = readdata_cargiver.readdata(5, 5)
            edit_relationship = readdata_cargiver.readdata(5, 8)
            edit_city =readdata_cargiver.readdata(5, 6)
            edit_state = readdata_cargiver.readdata(5, 9)
            edit_zipcode = readdata_cargiver.readdata(5, 7)
            log.info("*****Validation is Started*****")
            list_of_selected_caregivers = keen.validation_of_records()
            for i in list_of_selected_caregivers:
                if i.text == Name:
                    action.move_to_element(i).click().perform()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles

            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    action_utils.wait_for_element((Create_capture_member_details.created_record_for_validation))
                    log.info("***** validating the created record *****")
                    keen.click_record()
                    list_of_phone = keen.validation_phone()
                    try:
                        if list_of_phone.text == edit_phone:
                            assert True
                        else:
                            assert False
                        verify_name = keen.validation_Caregiver_Name()
                        if verify_name.text == edit_Name:
                            assert True
                        else:
                            assert False
                        verify_DOB = keen.validation_Date_of_birth()
                        if verify_DOB.text == edit_date:
                            assert True
                        else:
                            assert False
                        verify_email = keen.validation_Email()
                        if verify_email.text == edit_email:
                            assert True
                        else:
                            assert False
                        verify_phoneType = keen.validation_edit_Phonetype()
                        if verify_phoneType.text == edit_phone_type:
                            assert True
                        else:
                            assert False
                        verify_address = keen.validation__Address()
                        if verify_address.text == edit_address:
                            assert True
                        else:
                            assert False
                        verify_city = keen.validation__city()
                        if verify_city.text == edit_city:
                            assert True
                        else:
                            assert False
                        verify_state = keen.validation_state_caregiver()
                        if verify_state.text == edit_state:
                            assert True
                        else:
                            assert False
                        verify_zipcode = keen.validation_zipcode()
                        if verify_zipcode.text == edit_zipcode:
                            assert True
                        else:
                            assert False
                        log.info("******Validation is Completed*****")
                    except Exception as ex:
                        print(ex)
                    if guid == guid:
                        self.driver.close()
                        if guid != parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            try:
                                list_of_selected_caregivers = keen.validation_of_records()
                                for i in list_of_selected_caregivers:
                                    if i.text == edit_Name:
                                        assert True
                                    else:
                                        assert False
                            except Exception as ex:
                                print(ex)
                            keen.close()
        except Exception as ex:
            print(ex)
    def test_parent_organization_record(self,row_number):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        print("Row number parent:", row_number)
        sheet_parent = self.sheet_name.get_sheet_name('Parent_organization')
        data_row = sheet_parent[row_number]
        verify_organization = action_utils.record_verification(row_number, 'Parent_organization','Organization_Created')
        if verify_organization == 'YES':
            self.log.info("***** Parent organization is exists in Salesforce *****")
            existing_account = self.sheet_name.retrieve_value(row_number, 'K', 'Parent_organization', 0)
            print("record names:", existing_account)
            keen.click_practice_organization().send_keys(existing_account)
            action_utils.wait_for_elements((Create_capture_member_details.practice_records))
            list_of_practice = keen.select_practice_records()
            for parent_practice in list_of_practice:
                if parent_practice.get_attribute('title') == existing_account:
                    self.driver.execute_script("arguments[0].click();", parent_practice)
                    self.log.info("***** Existing record is selected *****")
                    break
            return existing_account
        else:
            Parent_organization_Name = None
            column_field_mapping = {
                'Name': 'Name',
                'Address line 1': 'Address line 1',
                'TaxID': 'TaxID',
                'Email': 'Email',
                'City': 'City', 'Phone': 'Phone', 'State': 'State',
                'Zip code': 'Zip code', 'Website': 'Website', 'Status': 'Status',
            }
            field_locators = {
                'Name': (Create_capture_member_details.parent_organizationname),
                'Address line 1': (Create_capture_member_details.parent_organization_Address_line_1),
                'TaxID': (Create_capture_member_details.parent_organization_TaxId),
                'Email': (Create_capture_member_details.parent_organization_Email),
                'City': (Create_capture_member_details.parent_organization_city),
                'Phone': (Create_capture_member_details.parent_organization_phone),
                'State': (Create_capture_member_details.parent_organization_state),
                'Zip code': (Create_capture_member_details.parent_organization_zipcode),
                'Website': (Create_capture_member_details.parent_organization_website),
                'Status': (Create_capture_member_details.parent_organization_status),

            }
            self.log.info("***** Parent organization is creating *****")
            keen.click_practice_organization().click()
            action_utils.wait_for_element((Create_capture_member_details.click_new_parent_organization))
            keen.click_organization()
            action_utils.wait_for_element((Create_capture_member_details.parent_organization_popup))
            popup = keen.new_parent_organization_popup()
            assert popup, "New Parent organization popup is not displayed"
            for cell in data_row:
                column_name = sheet_parent.cell(row=2, column=cell.column).value
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    self.log.info("***** Column name and Salesforce field are matched *****")
                    column_value = cell.value
                    locator = field_locators[field_name]
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        if field_name == 'State':
                            element.click()
                            self.log.info("***** State field is clicked *****")
                            state_list = keen.select_options_in_list()
                            for states in state_list:
                                if states.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", states)
                                    self.log.info("***** Practicular State option is selected *****")
                                    break
                        if field_name == 'Status':
                            element.click()
                            self.log.info("***** Status field is clicked")
                            status_list = keen.select_options_in_list()
                            for status in status_list:
                                if status.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", status)
                                    self.log.info("***** Praticular status option is selected *****")
                                    break
                    else:
                        element.clear()
                        element.send_keys(column_value)
                if column_name == 'Name':
                    Parent_organization_Name = cell.value
        action_utils.wait_for_element((Create_capture_member_details.parent_organization_save))
        keen.click_save_parent_organization()
        self.log.info("***** New organization record is Created *****")
        action_utils.wait_for_element((Create_capture_member_details.Success_message_creation))
        success_message = keen.success_message_of_records()
        assert success_message.is_displayed(), "organization toast message is not displayed"
        self.sheet_name.write_result_in_to_excel_sheet(row_number, "Parent_organization", "K")
        return Parent_organization_Name
    def test_parent_organization(self,row_number):
        keen=Create_capture_member_details(self.driver)
        action_utils=ActionUtils(self.driver)
        print("Row number parent:", row_number)
        sheet_parent=self.sheet_name.get_sheet_name('Parent_organization')
        data_row = sheet_parent[row_number]
        column_field_mapping = {
            'Name': 'Name',
            'Address line 1': 'Address line 1',
            'TaxID': 'TaxID',
            'Email': 'Email',
            'City': 'City', 'Phone': 'Phone', 'State': 'State',
            'Zip code': 'Zip code', 'Website': 'Website', 'Status': 'Status',
            }
        field_locators = {
            'Name': (Create_capture_member_details.parent_organizationname),
            'Address line 1': (Create_capture_member_details.parent_organization_Address_line_1),
            'TaxID': (Create_capture_member_details.parent_organization_TaxId),
            'Email': (Create_capture_member_details.parent_organization_Email),
            'City': (Create_capture_member_details.parent_organization_city),
            'Phone': (Create_capture_member_details.parent_organization_phone),
            'State': (Create_capture_member_details.parent_organization_state),
            'Zip code': (Create_capture_member_details.parent_organization_zipcode),
            'Website': (Create_capture_member_details.parent_organization_website),
            'Status': (Create_capture_member_details.parent_organization_status),

        }
        Parent_organization_Name=None
        verify_organization = action_utils.record_verification(row_number, 'Parent_organization', 'Organization_Created')
        if verify_organization == 'YES':
            self.log.info("***** Parent organization is exists in Salesforce *****")
            existing_account=self.sheet_name.retrieve_value(row_number,'K','Parent_organization',0)
            print("record names:",existing_account)
            keen.click_practice_organization().send_keys(existing_account)
            action_utils.wait_for_elements((Create_capture_member_details.practice_records))
            list_of_organization = keen.select_practice_records()
            for organization in list_of_organization:
                if organization.get_attribute('title') == existing_account:
                    self.driver.execute_script("arguments[0].click();", organization)
                    self.log.info("***** Existing record is selected *****")
                    break
            return existing_account
        else:
            self.log.info("***** Parent organization is creating *****")
            keen.click_practice_organization().click()
            action_utils.wait_for_element((Create_capture_member_details.click_new_parent_organization))
            keen.click_organization()
            action_utils.wait_for_element((Create_capture_member_details.parent_organization_popup))
            popup=keen.new_parent_organization_popup()
            assert popup,"New Parent organization popup is not displayed"
            for cell in data_row:
                column_name = sheet_parent.cell(row=2, column=cell.column).value
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    self.log.info("***** Column name and Salesforce field are matched *****")
                    column_value = cell.value
                    locator = field_locators[field_name]
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        if field_name == 'State':
                            element.click()
                            self.log.info("***** State field is clicked *****")
                            state_list=keen.select_options_in_list()
                            for states in state_list:
                                if states.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", states)
                                    self.log.info("***** Practicular State option is selected *****")
                                    break
                        if field_name == 'Status':
                            element.click()
                            self.log.info("***** Status field is clicked")
                            status_list = keen.select_options_in_list()
                            for status in status_list:
                                if status.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", status)
                                    self.log.info("***** Praticular status option is selected *****")
                                    break
                    else:
                        element.clear()
                        element.send_keys(column_value)
                if column_name == 'Name':
                    Parent_organization_Name=cell.value
        action_utils.wait_for_element((Create_capture_member_details.parent_organization_save))
        keen.click_save_parent_organization()
        self.log.info("***** New organization record is Created *****")
        action_utils.wait_for_element((Create_capture_member_details.Success_message_creation))
        success_message = keen.success_message_of_records()
        assert success_message.is_displayed(),"organization toast message is not displayed"
        self.sheet_name.write_result_in_to_excel_sheet(row_number, "Parent_organization", "K")
        return Parent_organization_Name
    def test_select_practice(self):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.select_practices))
        keen.click_practices()
        self.log.info("***** Practices option is selected *****")
        action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_of_members_practice = keen.pop_up()
        assert pop_of_members_practice.text == "Member's practices", "Member's practices popup is not displayed"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
        action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
        New_Members_practice = keen.pop_up_of_New_Members()
        assert New_Members_practice.text == "New Member's practice", "New Member's practice popup is not displayed"
    def test_practice_event(self,row_number):
        action_utils = ActionUtils(self.driver)
        keen = Create_capture_member_details(self.driver)
        print("Row number:", row_number)
        sheet_practices = self.sheet_name.get_sheet_name('Practices')
        data_row = sheet_practices[row_number]
        column_field_mapping = {
            'Practice_name': 'Practice_name',
            'Practice_NPI': 'Practice_NPI', 'TaxID': 'TaxID', 'Phone_practices': 'Phone_practices',
            'Practice_email': 'Practice_email', 'Address_1': 'Address_1', 'City': 'City',
            'State': 'State', 'Zipcode': 'Zipcode', 'Aledade Practice Type': 'Aledade Practice Type',
            'Practice URL': 'Practice URL', 'Accepted Carriers': 'Accepted Carriers',
            'Status': 'Status', 'Parent_organization': 'Parent_organization'
        }
        field_locators = {
            'Practice_name': (Create_capture_member_details.prcatice_name),
            'Practice_NPI': (Create_capture_member_details.practice_NPI),
            'TaxID': (Create_capture_member_details.practice_taxid),
            'Phone_practices': (Create_capture_member_details.practice_phone),
            'Practice_email': (Create_capture_member_details.practice_email),
            'Address_1': (Create_capture_member_details.practice_addressline1),
            'City': (Create_capture_member_details.practice_city),
            'State': (Create_capture_member_details.practice_state),
            'Zipcode': (Create_capture_member_details.practice_zipcode),
            'Aledade Practice Type': (Create_capture_member_details.practice_aledade),
            'Practice URL': (Create_capture_member_details.practice_url),
            'Accepted Carriers': (Create_capture_member_details.move_carriers_event),
            'Status': (Create_capture_member_details.practice_status),
            'Parent_organization': (Create_capture_member_details.parent_organization)
        }
        verify_organization = action_utils.record_verification(row_number, 'Practices', 'Practices_created')
        if verify_organization == 'YES':
            self.log.info("***** Practices record is exists in Salesforce *****")
            existing_account = self.sheet_name.retrieve_value(row_number, 'O', 'Practices', 0)
            print("record names:", existing_account)
            keen.click_practice_directory().send_keys(existing_account)
            action_utils.wait_for_elements((Create_capture_member_details.practice_records))
            list_of_practice = keen.select_practice_records()
            for organization in list_of_practice:
                if organization.get_attribute('title') == existing_account:
                    self.driver.execute_script("arguments[0].click();", organization)
                    self.log.info("***** Existing record is selected *****")
                    break
            keen.save_button_Add()
            self.log.info("***** Practices record is existing in SalesForce *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen.success_message()
            assert success_message_of_records.is_displayed(), "Record is not saved"
            return existing_account
        else:
            practice_name = None
            self.log.info("***** Practices record is not exists in Salesforce *****")
            keen.click_practice_directory().click()
            action_utils.wait_for_element((Create_capture_member_details.new_practice))
            keen.click_new_practice_event()
            action_utils.wait_for_element((Create_capture_member_details.pop_up_creation_new))
            pop_up_of_practice = keen.pop_up_Newcreation_event()
            assert pop_up_of_practice.text == "New Practice directory","New Practice directory is not matched"
            self.log.info("***** Entering the Practice Details to Create and Assosicate the record to member *****")
            for cell in data_row:
                column_name = sheet_practices.cell(row=2, column=cell.column).value
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    column_value = cell.value
                    self.log.info("***** Practices Column names and field names are matched *****")
                    locator = field_locators[field_name]
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        if field_name == 'Status':
                            element.click()
                            self.log.info("***** Status field is clicked *****")
                            list_of_status = keen.select_options_in_list()
                            for status_options in list_of_status:
                                if status_options.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", status_options)
                                    self.log.info("***** Practicular Status option is selectd *****")
                                    break
                        if field_name == 'State':
                            element.click()
                            self.log.info("***** State field is clicked *****")
                            select_state = keen.select_options_in_list()
                            print("select state:", len(select_state))
                            for states in select_state:
                                if states.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", states)
                                    self.log.info("***** Practicular Status option is selected *****")
                                    break
                        if field_name == 'Aledade Practice Type':
                            element.click()
                            self.log.info("***** Aledade Practice Type field is clicked *****")
                            list_of_practices = keen.select_options_in_list()
                            for practice_type in list_of_practices:
                                if practice_type.get_attribute('title') == column_value:
                                    self.driver.execute_script("arguments[0].click();", practice_type)
                                    self.log.info("***** Practicular Aledade Practice Type option is selected *****")
                                    break
                    elif element.tag_name == 'span':
                        if field_name == 'Accepted Carriers':
                            action_utils.wait_for_elements((Create_capture_member_details.newoptions_type))
                            list_of_options = keen.select_options_type()
                            for carriers in list_of_options:
                                if carriers.get_attribute('title') == column_value:
                                    self.driver.execute_script("arguments[0].click();", carriers)
                                    self.log.info("***** Practicular Aledade Practice Type option is selected *****")
                                    keen.click_move_to_chosen()
                    elif element.tag_name == 'div':
                        if field_name == 'Parent_organization':
                            self.log.info("***** Create Parent organization record or associate *****")
                            print("organization name:", column_value)
                            row_organization = self.sheet_name.retrieve_row_number('Parent_organization', column_value,
                                                                                   'A')
                            print("parent_organization row_number:", row_organization)
                            self.test_parent_organization_record(row_organization)
                            break
                    else:
                        element.clear()
                        element.send_keys(column_value)
                        self.log.info("***** Test data is entered in to the field *****")
                        if field_name == "Practice_name":
                            practice_name = cell.value
        keen.click_save_practice_directroy()
        self.log.info("*****New Practice record is Created*****")
        success_message = keen.success_message_of_records()
        assert success_message.is_displayed(), "Practice cerated toast message is not displayed"
        self.sheet_name.write_result_in_to_excel_sheet(row_number, "Practices", "O")
        self.log.info("***** Practice record is saved and write back to excel sheet *****")
        return practice_name
        ##click_new_practice_event
        ### Test Description:- Create And Assosicate New Practices to Member
        ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
        ### Click on Practices, Create and Assosicate Practices
    @allure.severity(allure.severity_level.NORMAL)
    def test_practice(self, row_number):
        action_utils = ActionUtils(self.driver)
        keen = Create_capture_member_details(self.driver)
        print("Row number:", row_number)
        sheet_practices=self.sheet_name.get_sheet_name('Practices')
        data_row = sheet_practices[row_number]
        column_field_mapping = {
            'Practice_name': 'Practice_name',
            'Practice_NPI': 'Practice_NPI', 'TaxID': 'TaxID', 'Phone_practices': 'Phone_practices',
            'Practice_email': 'Practice_email', 'Address_1': 'Address_1', 'City': 'City',
            'State': 'State', 'Zipcode': 'Zipcode', 'Aledade Practice Type': 'Aledade Practice Type',
            'Practice URL': 'Practice URL','Accepted Carriers': 'Accepted Carriers',
            'Status': 'Status','Parent_organization' : 'Parent_organization'
        }
        field_locators = {
            'Practice_name': (Create_capture_member_details.Field_01),
            'Practice_NPI': (Create_capture_member_details.Field_02),
            'TaxID': (Create_capture_member_details.Field_03),
            'Phone_practices': (Create_capture_member_details.Field_04),
            'Practice_email': (Create_capture_member_details.Field_05),
            'Address_1': (Create_capture_member_details.Field_D_01),
            'City': (Create_capture_member_details.Field_D_03),
            'State': (Create_capture_member_details.Field_SD_01),
            'Zipcode': (Create_capture_member_details.Field_D_04),
            'Aledade Practice Type': (Create_capture_member_details.Field_S_04),
            'Practice URL': (Create_capture_member_details.Field_06),
            'Accepted Carriers': (Create_capture_member_details.move_carriers),
            'Status': (Create_capture_member_details.Field_S_02),
            'Parent_organization': (Create_capture_member_details.parent_organization)
        }
        verify_organization = action_utils.record_verification(row_number,'Practices','Practices_created')
        if verify_organization == 'YES':
            self.log.info("***** Practices record is exists in Salesforce *****")
            existing_account = self.sheet_name.retrieve_value(row_number, 'O', 'Practices',0)
            print("record names:", existing_account)
            keen.click_practice_directory().send_keys(existing_account)
            action_utils.wait_for_element((Create_capture_member_details.existing_record))
            list_of_practice = keen.select_existing_records()
            for organization in list_of_practice:
                if organization.text == existing_account:
                    self.driver.execute_script("arguments[0].click();", organization)
                    self.log.info("***** Existing record is selected *****")
                    break
            keen.save_button_Add()
            self.log.info("***** Practices record is existing in SalesForce *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen.success_message()
            assert success_message_of_records.is_displayed(), "Record is not saved"
        else:
            practice_name=None
            self.log.info("***** Practices record is not exists in Salesforce *****")
            keen.click_practice_directory().click()
            action_utils.wait_for_element((Create_capture_member_details.new_creation))
            keen.click_new_member()
            action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
            pop_up_of_detail_list = keen.pop_up_Newcreation()
            pop = pop_up_of_detail_list.text
            assert pop == "New Practice directory", "New Practice directory is not displayed"
            self.log.info("***** Entering the Practice Details to Create and Assosicate the record to member *****")
            for cell in data_row:
                column_name = sheet_practices.cell(row=2, column=cell.column).value
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    column_value = cell.value
                    self.log.info("***** Practices Column names and field names are matched *****")
                    locator = field_locators[field_name]
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        if field_name == 'Status':
                            element.click()
                            self.log.info("***** Status field is clicked *****")
                            list_of_status = keen.select_options_in_list()
                            for status_options in list_of_status:
                                if status_options.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", status_options)
                                    self.log.info("***** Practicular Status option is selectd *****")
                                    break
                        if field_name == 'State':
                            element.click()
                            self.log.info("***** State field is clicked *****")
                            select_state = keen.select_options_in_list()
                            print("select state:", len(select_state))
                            for states in select_state:
                                if states.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", states)
                                    self.log.info("***** Practicular Status option is selected *****")
                                    break
                        if field_name == 'Aledade Practice Type':
                            element.click()
                            self.log.info("***** Aledade Practice Type field is clicked *****")
                            list_of_practices = keen.select_options_in_list()
                            for practice_type in list_of_practices:
                                if practice_type.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", practice_type)
                                    self.log.info("***** Practicular Aledade Practice Type option is selected *****")
                                    break
                    elif element.tag_name == 'span':
                        if field_name == 'Accepted Carriers':
                            action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
                            list_of_options = keen.select_options()
                            for carriers in list_of_options:
                                if carriers.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", carriers)
                                    self.log.info("***** Practicular Aledade Practice Type option is selected *****")
                                    keen.click_move_to_chosen()
                    elif element.tag_name == 'div':
                        if field_name == 'Parent_organization':
                            self.log.info("***** Create Parent organization record or associate *****")
                            print("organization name:", column_value)
                            row_organization = self.sheet_name.retrieve_row_number('Parent_organization',column_value, 'A')
                            print("parent_organization row_number:", row_organization)
                            self.test_parent_organization(row_organization)
                            break
                    else:
                        element.clear()
                        element.send_keys(column_value)
                        self.log.info("***** Test data is entered in to the field *****")
                        if field_name == "Practice_name":
                            practice_name=cell.value
        self.test_parent_organization(row_number)
        keen.click_save_practice_directroy()
        self.log.info("*****New Practice record is Created*****")
        action_utils.wait_for_element((Create_capture_member_details.Success_message_creation))
        success_message = keen.success_message_of_records()
        assert success_message.is_displayed(),"Practice cerated toast message is not displayed"
        self.sheet_name.write_result_in_to_excel_sheet(row_number, "Practices", "O")
        self.log.info("***** Practice record is saved and write back to excel sheet *****")
        action_utils.wait_for_element((Create_capture_member_details.Add))
        keen.save_button_Add()
        self.log.info("***** Practice is Assosicated to a Member *****")
        action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
        success_message_of_records = keen.success_message()
        assert success_message_of_records.is_displayed(),"Assosicated record saved toast message is displayed"
        self.log.info("***** Practice record is associated to member *****")
        return practice_name
    def test_select_practice_created_record(self,new_practice_name):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        action = ActionChains(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_up_list = keen.pop_up()
        assert pop_up_list.text == "Member's practices","Members practices popup is not displayed"
        self.log.info("*****Verifing the Assosicated practice record *****")
        action_utils.wait_for_elements((Create_capture_member_details.existing_records))
        list_of_selected_practices = keen.validation_of_records()
        for practices in list_of_selected_practices:
            if practices.text == new_practice_name:
                action.move_to_element(practices).click().perform()
                break
    @allure.description("Validation of New Practices to  Member")
    @allure.severity(allure.severity_level.NORMAL)
    def test_validation_practices(self,row_number):
        keen=Create_capture_member_details(self.driver)
        action_utils=ActionUtils(self.driver)
        action=ActionChains(self.driver)
        Practice_name = readdata_practices.readdata( row_number,1)
        Practice_NPI = readdata_practices.readdata(row_number,2)
        TaxID = readdata_practices.readdata(row_number, 3)
        Phone_practices = readdata_practices.readdata(row_number, 4)
        Practice_email = readdata_practices.readdata(row_number, 5)
        Status = readdata_practices.readdata(row_number, 6)
        Address_1 =readdata_practices.readdata(row_number, 7)
        City = readdata_practices.readdata(row_number, 8)
        state = readdata_practices.readdata(row_number, 9)
        zipcode_of_practices = readdata_practices.readdata(row_number, 10)
        Aledade_Practice_Type = readdata_practices.readdata(row_number, 11)
        Practice_url = readdata_practices.readdata(row_number, 12)
        Accepted_Carriers = readdata_practices.readdata(row_number, 13)
        self.log.info("*****Validating TestData of New Practice Creation*****")
        try:
            phone_validation = keen.validation_phone()
            sf_phone = action_utils.convert_string(phone_validation)
            print("SF phone....." + sf_phone)
            print("Input phone value......" + Phone_practices)
            if sf_phone == Phone_practices:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verfiy_practiceName = keen.validation_practice_name()
            print("SFName....." + verfiy_practiceName)
            print("Input name value......" + Practice_name)
            if verfiy_practiceName == Practice_name:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_Addressline1 = keen.validation_PracticeAddress_line_1()
            print("SF Address....." + verify_Addressline1)
            print("Input Address value......" + Address_1)
            if verify_Addressline1 == Address_1:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_PracticeNPI = keen.validation_practice_NPI()
            sf_NPI = action_utils.convert_string(verify_PracticeNPI)
            print("SF NPI....." + sf_NPI)
            print("Input NPI value......" + Practice_NPI)
            if sf_NPI == Practice_NPI:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_TaxID = keen.validation_practice_taxID()
            sf_Taxid = action_utils.convert_string(verify_TaxID)
            print("SF Taxid....." + sf_Taxid)
            print("Input Taxid value......" + TaxID)
            if sf_Taxid == TaxID:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_City = keen.validation_PracticeCity()
            print("SF city....." + verify_City)
            print("Input city value......" + City)
            if verify_City == City:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_State = keen.validation_state_practice()
            print("SF state....." + verify_State)
            print("Input state value......" + state)
            if verify_State == state:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_Practiceemail = keen.validation_practice_email()
            print("SF email....." + verify_Practiceemail)
            print("Input email value......" + Practice_email)
            if verify_Practiceemail == Practice_email:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_Zipcode = keen.validation_practice_zipcode()
            sf_zipcode = action_utils.convert_string(verify_Zipcode)
            print("SF Zipcode....." + sf_zipcode)
            print("Input zipcode value......" + zipcode_of_practices)
            if sf_zipcode == zipcode_of_practices:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_Status = keen.validation_Practice_status()
            print("SF status....." + verify_Status)
            print("Input status value......" + Status)
            if verify_Status == Status:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        # Maincontact
        try:
            verify_AcceptedCarriers = keen.validation_Practiceacceptedcarriers()
            print("SF carriers....." + verify_AcceptedCarriers)
            print("Input carriers value......" + Accepted_Carriers)
            if verify_AcceptedCarriers == Accepted_Carriers:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_AledadePracticeType = keen.validation_Aledade_Practice_Type()
            print("SF Type....." + verify_AledadePracticeType)
            print("Input type value......" + Aledade_Practice_Type)
            if verify_AledadePracticeType == Aledade_Practice_Type:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        try:
            verify_PracticeUrl = keen.validation_practice_url()
            print("SF url....." + verify_PracticeUrl)
            print("Input url value......" + Practice_url)
            if verify_PracticeUrl == Practice_url:
                assert True
            else:
                assert False
        except Exception as ex:
            print(ex)
        self.log.info("*****Validation is Completed*****")
    ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
    ### Click on Practices, Edit Practices
    @allure.description("Edit the Practices Associated to a Member")
    def test_edit_Practices(self,row_number=2):
        Practice_NPI = readdata_practices.readdata(row_number, 2)
        TaxID = readdata_practices.readdata(row_number, 3)
        Phone_practices = readdata_practices.readdata(row_number, 4)
        Practice_email = readdata_practices.readdata(row_number, 5)
        Status = readdata_practices.readdata(row_number, 6)
        Address_1 = readdata_practices.readdata(row_number, 7)
        City = readdata_practices.readdata(row_number, 8)
        state = readdata_practices.readdata(row_number, 9)
        zipcode_of_practices = readdata_practices.readdata(row_number, 10)
        Aledade_Practice_Type =readdata_practices.readdata(row_number, 11)
        Practice_url = readdata_practices.readdata(row_number, 12)
        edit_Accepted_Carriers = readdata_practices.readdata(row_number, 13)
        Accepted_Carriers = readdata_practices.readdata(row_number, 13)
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        action=ActionChains(self.driver)
        self.log.info("***** Editing the selected record *****")
        action_utils.wait_for_element((Create_capture_member_details.edit_practices))
        keen.click_edit_practices()
        action_utils.wait_for_element((Create_capture_member_details.PracticesNew_NPI))
        keen.edit_practices_NPI(Practice_NPI)
        time.sleep(6)
        keen.enter_taxID(TaxID)
        keen.enter_Practice_Phone(Phone_practices)
        action_utils.wait_for_element((Create_capture_member_details.PracticesNew_email))
        keen.edit_practice_email(Practice_email)
        # self.keen.click_practice_organization().send_keys()
        time.sleep(5)
        # driver.execute_script("scroll(0, 250);")
        action_utils.wait_for_elements((Create_capture_member_details.existing_record))
        keen.edit_practice_status()
        list_of_status = keen.select_existing_records()
        for status in list_of_status:
            print(status.get_attribute('title'))
            if status.get_attribute('title') == Status:
                action.move_to_element(status).click().perform()
                break
        time.sleep(5)
        pop_up_window = keen.click_move_to_chosen()
        self.driver.execute_script("arguments[0].scrollIntoView();", pop_up_window)
        list_of_options = keen.select_options_type()
        for options in list_of_options:
            print(options.text)
            if options.text == Accepted_Carriers:
                time.sleep(10)
                action.move_to_element(options).click().perform()
                break
        keen.click_to_available()
        list_of_options = keen.select_options_type()
        for options in list_of_options:
            print(options.text)
            if options.text == edit_Accepted_Carriers:
                action.move_to_element(options).click().perform()
                break
        keen.click_move_to_chosen()
        keen.click_Aledade_Practice_Type()
        list_of_practices = keen.select_options_in_list()
        for i in list_of_practices:
            if i.text == Aledade_Practice_Type:
                action.move_to_element(i).click().perform()
                break
        keen.enter_Address_line_1(Address_1)
        keen.enter_practice_url(Practice_url)
        keen.enter_City(City)
        keen.click_state_of_practice()
        list_of_states = keen.select_options_in_list()
        for i in list_of_states:
            print(i.text)
            if i.text == state:
                action.move_to_element(i).click().perform()
                break
        keen.enter_Zipcode(zipcode_of_practices)
        keen.edit_save().click()
        self.log.info("***** Saved the Edited data *****")
        # self.log.info("***** Validation is started *****")
        # try:
        #     phone_validation = keen.validation_phone()
        #     if phone_validation.text == Phone_practices:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verfiy_practiceName = keen.validation_practice_name()
        #     if verfiy_practiceName.text == practice_name:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_Addressline1 = keen.validation_PracticeAddress_line_1()
        #     if verify_Addressline1.text == Address_1:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_PracticeNPI = keen.validation_practice_NPI()
        #     if verify_PracticeNPI == Practice_NPI:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_TaxID = keen.validation_practice_taxID()
        #     if verify_TaxID == TaxID:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        #
        # try:
        #     verify_City = keen.validation_PracticeCity()
        #     if verify_City == City:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_Phone = keen.validation_PracticePhone()
        #     if verify_Phone == Phone_practices:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_State = keen.validation_state_practice()
        #     if verify_State == state:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_Practiceemail = keen.validation_practice_email()
        #     if verify_Practiceemail == Practice_email:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_Zipcode = keen.validation_practice_zipcode()
        #     if verify_Zipcode == zipcode_of_practices:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_Status = keen.validation_Practice_status()
        #     if verify_Status == Status:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # # Maincontact
        # try:
        #     verify_AcceptedCarriers = keen.validation_Practiceacceptedcarriers()
        #     if verify_AcceptedCarriers == Accepted_Carriers:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_AledadePracticeType = keen.validation_Aledade_Practice_Type()
        #     if verify_AledadePracticeType == Aledade_Practice_Type:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # try:
        #     verify_PracticeUrl = keen.validation_practice_url()
        #     if verify_PracticeUrl == Practice_url:
        #         assert True
        #     else:
        #         assert False
        # except Exception as ex:
        #     print(ex)
        # self.log.info("***** Validation is completed *****")
    def test_click_medication_option(self):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.medication))
        keen.Medication_option()
        self.log.info("***** Medication option is selected *****")
        action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_of_members_medication = keen.pop_up()
        assert pop_of_members_medication.text == "Member's Medications", "Member's Medications popup is not displayed"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
        action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
        New_Members_mediaction = keen.pop_up_of_New_Members()
        assert New_Members_mediaction.text == "New Member Medication", "New Member Medication popup is not displayed"
    def test_Member_medication(self,row_number):
        keen=Create_capture_member_details(self.driver)
        action_utils=ActionUtils(self.driver)
        print("Row number:", row_number)
        data_medication = self.sheet_medication[row_number]
        column_field_mapping = {
            'Refill frequency': 'Refill frequency',
            'Quantity per refill': 'Quantity per refill',
        }
        field_locators = {
            'Refill frequency': (Create_capture_member_details.refillfrequency),
            'Quantity per refill': (Create_capture_member_details.quantityperfill),
        }
        for cell in data_medication:
            column_name = self.sheet_medication.cell(row=2, column=cell.column).value
            print("Column name:", column_name)
            if column_name in column_field_mapping:
                field_name = column_field_mapping[column_name]
                column_value = cell.value
                print("input:", column_value)
                locator = field_locators[field_name]
                element = self.driver.find_element(*locator)
                action_utils.wait_for_element((locator))
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                if element.tag_name == 'button':
                    if field_name == 'Refill frequency':
                        element.click()
                        self.log.info("***** Refill frequency field is clicked *****")
                        select_month = keen.select_frequency()
                        for frequency_month in select_month:
                            if frequency_month.text == column_value:
                                self.driver.execute_script("arguments[0].click();", frequency_month)
                                break
                else:
                    element.clear()
                    element.send_keys(column_value)
    ### Test Description:- Create and Assosicate Medications to a Member
    ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
    ### Click on Medications, Create Medications ans Associate to member.
    @allure.description("Create New Medictions and Assosicate to a Member")
    def test_medications(self,row_number):
        keen = Create_capture_member_details(self.driver)
        action = ActionChains(self.driver)
        action_utils = ActionUtils(self.driver)
        verify_medication = action_utils.record_verification(row_number, 'Medication', 'Medication_creation')
        if verify_medication == 'YES':
            self.log.info("***** Medication record is exists in Salesforce *****")
            existing_medication_record = self.sheet_name.retrieve_value(row_number, 'N', 'Medication',0)
            print("Medication record names:", existing_medication_record)
            keen.medication_search().send_keys(existing_medication_record)
            self.log.info("***** Associate existing medication record to member  *****")
            list_of_medication = keen.select_existing_records()
            for medication in list_of_medication:
                if medication.text == existing_medication_record:
                    self.driver.execute_script("arguments[0].click();", medication)
                    self.log.info("***** Existing record is selected *****")
                    break
            keen.save_button_Add()
            self.log.info("***** Medication record is existing in SalesForce *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen.success_message()
            assert success_message_of_records.is_displayed(), "Record is not saved"
        else:
            self.log.info("***** Medication record is not exists in Salesforce *****")
            self.log.info("***** Creating a medication record to member  *****")
            action_utils.wait_for_element((Create_capture_member_details.new_creation))
            keen.click_new_member()
            action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
            pop_up_of_detail_list = keen.pop_up_Newcreation()
            pop = pop_up_of_detail_list.text
            assert pop == "New Medication List", "New Medication List is not displayed"
            self.log.info("***** Entering the Practice Details to Create and Assosicate the record to member *****")
            self.log.info("***** Entering the test data *****")
            print("Row number:", row_number)
            data_row = self.sheet_medication[row_number]
            column_field_mapping = {
                'Name': 'Name',
                'Branded Generic': 'Branded Generic',
                'Drug Form': 'Drug Form',
                'Strength': 'Strength',
                'Strength_units': 'Strength_units', 'Packaging': 'Packaging', 'Daily Frequency': 'Daily Frequency',
                'Daily Quantity': 'Daily Quantity', 'Valid Until': 'Valid Until', 'Refill quantity': 'Refill quantity',
                'Refill frequency': 'Refill frequency',
            }
            field_locators = {
                'Name': (Create_capture_member_details.Field_01),
                'Branded Generic': (Create_capture_member_details.Field_S_01),
                'Drug Form': (Create_capture_member_details.Field_S_02),
                'Strength': (Create_capture_member_details.Field_02),
                'Strength_units': (Create_capture_member_details.Field_03),
                'Packaging': (Create_capture_member_details.Field_04),
                'Daily Frequency': (Create_capture_member_details.Field_05),
                'Daily Quantity': (Create_capture_member_details.Field_06),
                'Valid Until': (Create_capture_member_details.medication_ValidUntil),
                'Refill quantity': (Create_capture_member_details.Field_08),
                'Refill frequency': (Create_capture_member_details.Field_S_03),
            }
            for cell in data_row:
                column_name = self.sheet_medication.cell(row=2, column=cell.column).value
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    self.log.info("***** Medication column names and Salesforce fields are matched *****")
                    column_value = cell.value
                    locator = field_locators[field_name]
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        print("a tag is present in elements")
                        if field_name == 'Branded Generic':
                            element.click()
                            self.log.info("****** Branded field is clicked *****")
                            list_Brand = keen.select_options_in_list()
                            for brand in list_Brand:
                                if brand.get_attribute('title') == column_value:
                                    self.driver.execute_script("arguments[0].click();", brand)
                                    self.log.info("***** Practicular brand option is selected *****")
                                    break
                        if field_name == 'Drug Form':
                            element.click()
                            self.log.info("****** Drug field is clicked *****")
                            action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
                            list_type_drug = keen.select_options_in_list()
                            for drug in list_type_drug:
                                if drug.get_attribute('title') == column_value:
                                    self.driver.execute_script("arguments[0].click();", drug)
                                    self.log.info("****** Practicular drug option is selected *****")
                                    break
                        if field_name == 'Refill frequency':
                            element.click()
                            self.log.info("***** Refill frequency field is clicked *****")
                            action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
                            list_refill_frequency = keen.select_options_in_list()
                            for refill in list_refill_frequency:
                                if refill.get_attribute('title') == column_value:
                                    self.driver.execute_script("arguments[0].click();", refill)
                                    self.log.info("***** Practicular refill option is selected *****")
                                    break
                    else:
                        element.clear()
                        element.send_keys(column_value)
            self.log.info("***** Test data is entered *****")
            keen.save_button_creation()
            success_message = keen.success_message_of_records()
            assert success_message.is_displayed(),"Success toast message is not displayed"
            self.log.info("***** New Medication record is cerated *****")
            self.number.write_result_in_to_excel_sheet(row_number, "Medication", "N")
            self.log.info("***** Medication record is saved and write back to excel sheet *****")
            self.test_Member_medication(row_number)
            keen.save_button_Add()
            self.log.info("***** created record is associated *****")
            success_Message_of_Medication = keen.success_message()
            assert success_Message_of_Medication.is_displayed(),"Success toast message is not displayed"
    def test_validation_medication(self,row_number):
        Medication_Name = readdata_medications.readdata(row_number, 1)
        branded = readdata_medications.readdata(row_number, 2)
        Drug_form = readdata_medications.readdata(row_number, 3)
        Strength = readdata_medications.readdata(row_number, 4)
        Strength_units = readdata_medications.readdata(row_number, 5)
        Packaging = readdata_medications.readdata(row_number, 6)
        Daily_Frequency = readdata_medications.readdata(row_number, 7)
        Daily_Quantity = readdata_medications.readdata(row_number, 8)
        Valid_Until = readdata_medications.readdata(row_number, 9)
        Pharm_class = readdata_medications.readdata(row_number, 10)
        Refill_quantity = readdata_medications.readdata(row_number, 11)
        Refill_frequency = readdata_medications.readdata(row_number, 12)
        action=ActionChains(self.driver)
        action_utils=ActionUtils(self.driver)
        log = logger_utils.get_logger()
        keen = Create_capture_member_details(self.driver)
        time.sleep(5)
        action_utils.wait_for_element((Create_capture_member_details.medication))
        keen.Medication_option()
        selected_Medication = keen.validation_of_records()
        action_utils.wait_for_elements((Create_capture_member_details.existing_records))
        for i in selected_Medication:
            if i.text == Medication_Name:
                action.move_to_element(i).click().perform()
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        # all_guid = driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                action_utils.wait_for_element((Create_capture_member_details.created_record_for_validation))
                time.sleep(5)
                log.info("***** Click associated record *****")
                keen.click_record()
                log.info("***** Validation is Started *****")
                verify_name=keen.validation_MedicationName()
                print(verify_name)
                if verify_name == Medication_Name:
                    assert True
                else:
                    assert False

                verfiy_BrandedGenric = keen.validation_BrandedGenric()
                print(verfiy_BrandedGenric)
                if verfiy_BrandedGenric == branded:
                    assert True
                else:
                    assert False
                try:
                    verify_DrugForm = keen.validation_DrugForm()
                    print(verify_DrugForm)
                    if verify_DrugForm == Drug_form:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_strength = keen.validation_Strength()
                    if verify_strength == Strength:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_strengthUnits = keen.validation_StrengthUnits()
                    if verify_strengthUnits == Strength_units:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_Packaging = keen.validation_Packaging()
                    if verify_Packaging == Packaging:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_DailyFrequency = keen.validation_DailyFrequency()
                    if verify_DailyFrequency == Daily_Frequency:
                        assert True
                    else:
                        assert False
                except Exception as ex:

                    print(ex)
                try:
                    verify_DailyQuantity = keen.validation_DailyQuantity()
                    if verify_DailyQuantity == Daily_Quantity:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_validUntil = keen.validation_ValidUntil()
                    if verify_validUntil == Valid_Until:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_refillfrequency = keen.validation_RefillFrequency()
                    if verify_refillfrequency == Refill_frequency:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_refillquantity = keen.validation_RefillQuantity()
                    if verify_refillquantity == Refill_quantity:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                log.info("***Validation is completed***")
                if guid == guid:
                    self.driver.close()
                    if parent_guid == parent_guid:
                        self.driver.switch_to.window(parent_guid)
                        keen.close()
                        break
    ### Test Description:- Edit Assosicated Medications to a Member
    ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
    ### Click on Medication, Edit Medications
    @allure.description("Editing the Medications for a Member")
    @pytest.mark.order(6)
    def test_edit_Medications(self):
        keen = Create_capture_member_details(self.driver)
        log=logger_utils.get_logger()
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        action_utils=ActionUtils(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.Member))
        keen.select_member()
        action_utils.wait_for_element(())
        keen.Capture_Full_Member()
        self.driver.execute_script("scroll(0, 150);")
        action=ActionChains(self.driver)
        # keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        Medication_Name = readdata_medications.readdata( 3, 1)
        branded = readdata_medications.readdata(4, 2)
        Drug_form = readdata_medications.readdata(4, 3)
        Strength = readdata_medications.readdata(4, 4)
        Strength_units = readdata_medications.readdata(4, 5)
        Packaging = readdata_medications.readdata(4, 6)
        Daily_Frequency = readdata_medications.readdata(4, 7)
        Daily_Quantity = readdata_medications.readdata(4, 8)
        Valid_Until = readdata_medications.readdata(4, 9)
        Pharm_class = readdata_medications.readdata(4, 10)
        Refill_quantity = readdata_medications.readdata(4, 11)
        Refill_frequency = readdata_medications.readdata(4, 12)
        log.info("***** Select Medication Option *****")
        keen.Medication_option()
        time.sleep(10)
        pop_up_of_Members_Medications = keen.pop_up()
        if pop_up_of_Members_Medications.text == "Member's Medications":
            assert True
        else:
            assert False
        log.info("***Select the Assosicated Medication record***")
        selected_Medication = keen.validation_of_records()
        for i in selected_Medication:
            if i.text == Medication_Name:
                action.move_to_element(i).click().perform()
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        # all_guid = driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                time.sleep(10)
                keen.click_record()
                log.info("***Editing the Medication recotd***")
                keen.click_NewBranded_generic()
                list_Brand = keen.select_options_in_list()
                for i in list_Brand:
                    print(i.text)
                    if i.text == branded:
                        action.move_to_element(i).click().perform()
                        break
                time.sleep(5)
                keen.click_NewDrug_form()
                list_type_drug = keen.select_options_in_list()
                for i in list_type_drug:
                    if i.text == Drug_form:
                        action.move_to_element(i).click().perform()
                        break
                keen.enter_Newstrength(Strength)
                keen.enter_Newstrength_units(Strength_units)
                keen.enter_Newpackaging(Packaging)
                keen.enter_Newdaily_frequency(Daily_Frequency)
                keen.enter_Newdaily_quantity(Daily_Quantity)
                keen.enter_Newvalid_until(Valid_Until)
                # self.keen.enter_pharm_class().send_keys(Pharm_class)
                keen.enter_Newrefill_quantity(Refill_quantity)
                keen.click_Newrefill_frequency()
                list_refill_frequency = keen.select_options_in_list()
                for i in list_refill_frequency:
                    if i.text == Refill_frequency:
                        action.move_to_element(i).click().perform()
                        break

                keen.edit_save()
                log.info("***** Saved the Edited Data *****")
                log.info("***** Validation is Started *****")
                try:
                    verfiy_BrandedGenric = keen.validation_BrandedGenric()
                    if verfiy_BrandedGenric.text == branded:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_DrugForm = keen.validation_DrugForm()
                    if verify_DrugForm.text == Drug_form:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_strength = keen.validation_Strength()
                    if verify_strength.text == Strength:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_strengthUnits = keen.validation_StrengthUnits()
                    if verify_strengthUnits.text == Strength_units:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_Packaging = keen.validation_Packaging()
                    if verify_Packaging.text == Packaging:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_DailyFrequency = keen.validation_DailyFrequency()
                    if verify_DailyFrequency.text == Daily_Frequency:
                        assert True
                    else:
                        assert False
                except Exception as ex:

                    print(ex)
                try:
                    verify_DailyQuantity = keen.validation_DailyQuantity()
                    if verify_DailyQuantity.text == Daily_Quantity:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_validUntil = keen.validation_ValidUntil()
                    if verify_validUntil.text == Valid_Until:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_refillfrequency = keen.validation_RefillFrequency()
                    if verify_refillfrequency.text == Refill_frequency:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                try:
                    verify_refillquantity = keen.validation_Practice_status()
                    if verify_refillquantity.text == Refill_quantity:
                        assert True
                    else:
                        assert False
                except Exception as ex:
                    print(ex)
                self.log.info("***** Validation is completed *****")
                if guid == guid:
                    self.driver.close()
                    if parent_guid == parent_guid:
                        self.driver.switch_to.window(parent_guid)
                        keen.close()
                        break

    ### Test Description:- Create and Assosicate Hospitals to a Member
    ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
    ### Click on Hospitals, Create and Assosicate Hospitals
    # @pytest.mark.order(7)
    @allure.description("Create and Assosicate Hospitals to a Member")
    def test_hospitals(self,row_number):
        try:
            keen = Create_capture_member_details(self.driver)
            action_utils = ActionUtils(self.driver)
            action_utils.wait_for_element((Create_capture_member_details.select_hospitals))
            keen.click_hospitals()
            action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
            pop_up_of_Members_hospitals = keen.pop_up()
            assert pop_up_of_Members_hospitals.text == "Member's hospitals","Member's hospitals popup is not matched"
            action_utils.wait_for_element((Create_capture_member_details.new))
            keen.click_new()
            pop_up_of_New_Members_hospital = keen.pop_up_of_New_Members()
            assert pop_up_of_New_Members_hospital.text == "New Member's hospital", "New Member's hospital is not matched"
            verify_hospitals = action_utils.record_verification(row_number, 'Hospitals', 'Hospital_Created')
            if verify_hospitals == 'YES':
                self.log.info("***** Hospital record is exists in Salesforce *****")
                existing_hospital_record = self.sheet_name.retrieve_value(row_number, 'O', 'Hospitals',0)
                print("Hospital record names:", existing_hospital_record)
                action_utils.wait_for_element((Create_capture_member_details.new_hospital))
                keen.click_Hospital_directory().send_keys(existing_hospital_record)
                self.log.info("***** Associating existing 'HOSPITAL' record to member  *****")
                list_of_medication = keen.select_existing_records()
                for medication in list_of_medication:
                    if medication.text == existing_hospital_record:
                        self.driver.execute_script("arguments[0].click();", medication)
                        self.log.info("***** Existing record is selected *****")
                        break
                keen.save_button_Add()
                self.log.info("***** Associated existing 'HOSPITAL' record to member *****")
                action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                success_message_of_records = keen.success_message()
                assert success_message_of_records.is_displayed(), "Record is not saved"
                return existing_hospital_record
            else:
                hospital_record=None
                keen.click_Hospital_directory().click()
                action_utils.wait_for_element((Create_capture_member_details.new_creation))
                keen.click_new_member()
                action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
                pop_up_of_new_hospital_directory = keen.pop_up_Newcreation()
                print(pop_up_of_new_hospital_directory.text)
                assert pop_up_of_new_hospital_directory.text == "New Hospital and health system directory","New Hospital and health system directory pop is not matched"
                self.log.info("***** Entering the test data *****")
                print("Row number:", row_number)
                sheet_hospitals=self.sheet_name.get_sheet_name('Hospitals')
                data_row = sheet_hospitals[row_number]
                column_field_mapping = {
                    'Hospital_Name': 'Hospital_Name',
                    'Hospital_location': 'Hospital_location',
                    'Address_line_1': 'Address_line_1',
                    'City': 'City',
                    'State': 'State', 'Zipcode': 'Zipcode', 'NPI': 'NPI',
                    'TaxID': 'TaxID', 'Status': 'Status', 'Phone': 'Phone',
                    'Contact_name': 'Contact_name','Contact_email': 'Contact_email','Contact _phone' : 'Contact _phone',
                    'Website' : 'Website'
                }
                field_locators = {
                    'Hospital_Name': (Create_capture_member_details.Field_01),
                    'Hospital_location': (Create_capture_member_details.hospital_location),
                    'Address_line_1': (Create_capture_member_details.hospital_addressline_1),
                    'City': (Create_capture_member_details.hospital_city),
                    'State': (Create_capture_member_details.Field_S_01),
                    'Zipcode': (Create_capture_member_details.hospital_zipcode),
                    'NPI': (Create_capture_member_details.hospital_npi),
                    'TaxID': (Create_capture_member_details.hospital_taxid),
                    'Status': (Create_capture_member_details.Field_S_02),
                    'Phone': (Create_capture_member_details.hospital_phone),
                    'Contact_name': (Create_capture_member_details.hospital_contactname),
                    'Contact_email':(Create_capture_member_details.hospital_contactemail),
                    'Contact _phone': (Create_capture_member_details.hospital_contactphone),
                    'Website' : (Create_capture_member_details.hospital_website)
                }
                for cell in data_row:
                    column_name = sheet_hospitals.cell(row=2, column=cell.column).value
                    print("Column name:", column_name)
                    if column_name in column_field_mapping:
                        field_name = column_field_mapping[column_name]
                        column_value = cell.value
                        print("input:", column_value)
                        locator = field_locators[field_name]
                        action_utils.wait_for_element((locator))
                        element = self.driver.find_element(*locator)
                        action_utils.wait_for_element((locator))
                        self.driver.execute_script("arguments[0].scrollIntoView();", element)
                        if element.tag_name == 'a':
                            print("a tag is present in elements")
                            if field_name == 'State':
                                element.click()
                                self.log.info("***** State field is clicked *****")
                                list_of_states = keen.select_options_in_list()
                                for states in list_of_states:
                                    if states.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", states)
                                        self.log.info("***** Practicular status optuon is selected *****")
                                        break
                            if field_name == 'Status':
                                element.click()
                                self.log.info("***** Practicular status field is clicked *****")
                                list_of_status = keen.select_options_in_list()
                                for status in list_of_status:
                                    if status.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", status)
                                        self.log.info("***** Practicular status optuon is selected *****")
                                        break
                        else:
                            element.clear()
                            element.send_keys(column_value)
                            if field_name == "Hospital_Name":
                                hospital_record=cell.value
            keen.save_button_creation()
            self.log.info("***** New Medication record is cerated *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_creation))
            success_message = keen.success_message_of_records()
            assert success_message.is_displayed(),"Hospital record toast message is not displayed"
            self.number.write_result_in_to_excel_sheet(row_number, "Hospitals", "O")
            action_utils.wait_for_element((Create_capture_member_details.Add))
            keen.save_button_Add()
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen.success_message()
            assert success_message_of_records.is_displayed(),"Successs toast message is not displayed"
            return hospital_record
        except Exception as ex:
            print(ex)
    def test_select_hospital_record(self,hospital_name):
        action_utils=ActionUtils(self.driver)
        action = ActionChains(self.driver)
        keen = Create_capture_member_details(self.driver)
        pop_up_list = keen.pop_up()
        if pop_up_list.text == "Member's hospitals":
            assert True
        else:
            assert False
        list_of_selected_caregivers = keen.validation_of_records()
        for records in list_of_selected_caregivers:
            if records.text == hospital_name:
                action.move_to_element(records).click().perform()
                break

    def test_validation_hospitals(self,row_number):
        Hospital_name = readdata_hospitals.readdata(row_number, 1)
        Hospital_location = readdata_hospitals.readdata(row_number, 2)
        Address_line_hospitals = readdata_hospitals.readdata(row_number, 3)
        City_hospitals = readdata_hospitals.readdata(row_number, 4)
        State_hospitals =readdata_hospitals.readdata(row_number, 5)
        Zipcode_hospitals = readdata_hospitals.readdata(row_number, 6)
        NPI_hopitals = readdata_hospitals.readdata(row_number, 7)
        TaxID_hospitals = readdata_hospitals.readdata(row_number, 8)
        Status_hospitals = readdata_hospitals.readdata(row_number, 9)
        Phone_hospitals = readdata_hospitals.readdata(row_number, 10)
        Contact_name_hospitals = readdata_hospitals.readdata(row_number, 11)
        Contact_email_hospitals = readdata_hospitals.readdata(row_number, 12)
        Contact_name_phone = readdata_hospitals.readdata(row_number, 13)
        Website_hospitals =readdata_hospitals.readdata(row_number, 14)
        keen=Create_capture_member_details(self.driver)
        try:
            verify_Name = keen.validation_HospitalName()
            assert verify_Name.text == Hospital_name,"Hospital name is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_hospital_loaction=keen.validation_HospitalLocation()
            assert verify_hospital_loaction == Hospital_location,"Hospital location is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_hospital_ddress=keen.validation_HospitalAddress()
            assert verify_hospital_ddress == Address_line_hospitals,"Hospital address is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_city = keen.validation_HospitalCity()
            assert verify_city == City_hospitals,"Hospitals city is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_state = keen.validation_HospitalState()
            assert verify_state == State_hospitals,"Hospotals state is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_zipcode = keen.validation_HospitalZipcode()
            assert verify_zipcode == Zipcode_hospitals,"Hospital zipcode is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_NPI = keen.validation_HospitalNPI()
            assert verify_NPI == NPI_hopitals,"Hospitals NPI is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_TaxID = keen.validation_HospitalTaxID()
            assert verify_TaxID == TaxID_hospitals,"Hospitals taxid is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_status = keen.validation_HospitalStatus()
            assert verify_status == Status_hospitals,"Hospital status is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_phone = keen.validation_HospitalPhone()
            assert verify_phone == Phone_hospitals,"Hospitals phone is not matched"
        except Exception as ex:
                print(ex)
        try:
            verify_contactName = keen.validation_HospitalContactName()
            assert verify_contactName == Contact_name_hospitals,"Contact name is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_Email = keen.validation_HospitalContact_Email()
            assert verify_Email == Contact_email_hospitals,"Hospital contact email is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_Contactphone = keen.validation_HospitalContact_Phone()
            assert verify_Contactphone == Contact_name_phone,"Hospital contact name is not matched"
        except Exception as ex:
            print(ex)
        try:
            verify_website = keen.validation_Hospital_Website()
            assert verify_website == Website_hospitals,"hospital website is not matched"
        except Exception as ex:
            print(ex)

    ### Test Description:- Edit Assosicated Hospitals to a Member
    ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
    ### Click on Hospitals, Edit Assosicated Hospitals
    @pytest.mark.order(8)
    @allure.description("Editing the Assosicated Hospitals")
    def test_edit_hospitals(self,row_number=2):
        keen=Create_capture_member_details(self.driver)
        action_utils=ActionUtils(self.driver)
        action=ActionChains(self.driver)
        Hospital_location = readdata_hospitals.readdata(row_number, 2)
        Address_line_hospitals = readdata_hospitals.readdata(row_number, 3)
        City_hospitals = readdata_hospitals.readdata(row_number, 4)
        State_hospitals = readdata_hospitals.readdata(row_number, 5)
        Zipcode_hospitals = readdata_hospitals.readdata(row_number, 6)
        NPI_hopitals = readdata_hospitals.readdata(row_number, 7)
        TaxID_hospitals = readdata_hospitals.readdata(row_number, 8)
        Status_hospitals = readdata_hospitals.readdata(row_number, 9)
        Phone_hospitals = readdata_hospitals.readdata(row_number, 10)
        Contact_name_hospitals = readdata_hospitals.readdata(row_number, 11)
        Contact_email_hospitals = readdata_hospitals.readdata(row_number, 12)
        Contact_name_phone = readdata_hospitals.readdata(row_number, 13)
        Website_hospitals = readdata_hospitals.readdata(row_number, 14)
        action_utils.wait_for_element((Create_capture_member_details.click_eidt_hospitals))
        keen.edit_hospitals()
        keen.edit_hospital_location(Hospital_location)
        keen.edit_address_line1_hospital(Address_line_hospitals)
        keen.edit_city_hospitals(City_hospitals)
        keen.edit_state_hospitals()
        list_of_states = keen.select_options_in_list()
        for states in list_of_states:
            print(states.text)
            if states.text == State_hospitals:
                action.move_to_element(states).click().perform()
                break
        action_utils.wait_for_element((Create_capture_member_details.new_hospital_zipcode))
        keen.edit_zipcode_hospital(Zipcode_hospitals)
        time.sleep(3)
        keen.edit_NPI(NPI_hopitals)
        time.sleep(3)
        keen.edit_status_hospitals()
        time.sleep(3)
        list_of_status = keen.select_options_in_list()
        for status in list_of_status:
            print(status.text)
            if status.text == Status_hospitals:
                action.move_to_element(status).click().perform()
                break
        time.sleep(3)
        keen.edit_TaxId_hospital(TaxID_hospitals)
        keen.edit_phone_hospital(Phone_hospitals)
        keen.edit_contact_name_hospital(Contact_name_hospitals)
        keen.edit_contact_phone_hospital(Contact_name_phone)
        keen.edit_contact_email_hospital(Contact_email_hospitals)
        keen.edit_website_hospital(Website_hospitals)
        keen.edit_save()

    ### Test Description:- Create New Campaigns and Assosicated to a Member
    ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
    ### Click on Campaigns,create and  Assosicate to a member
    @allure.description("Create New Campaigns and Assosicated to a Member")
    def  test_campaigns(self,row_number):
        keen = Create_capture_member_details(self.driver)
        self.driver.execute_script("scroll(0, 150);")
        action_utils = ActionUtils(self.driver)
        self.test_select_member_to_associate_Cpature_Full_Member_details()
        self.log.info("***** Campaign option is selected *****")
        action_utils.wait_for_element((Create_capture_member_details.click_campaigns))
        keen.select_campaigns()
        action_utils.wait_for_element((Create_capture_member_details.click_campaigns))
        pop_up_of_Members_campaigns = keen.pop_up()
        assert pop_up_of_Members_campaigns.text == "Member's Campaign","Member's Campaign popup is not displayed"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
        action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
        pop_up_of_New_Members_campaigns = keen.pop_up_of_New_Members()
        assert pop_up_of_New_Members_campaigns.text == "New Member campaign","New Member campaign popup is not displayed"
        verify_hospitals = action_utils.record_verification(row_number, 'Campaigns', 'Campaigns_Created')
        if verify_hospitals == 'YES':
            self.log.info("***** CAMPAIGN record is exists in Salesforce *****")
            existing_Campaign_record = self.sheet_name.retrieve_value(row_number, 'J', 'Campaigns')
            print("Campaign record names:", existing_Campaign_record)
            action_utils.wait_for_element((Create_capture_member_details.new_hospital))
            keen.search_keen_campaign().send_keys(existing_Campaign_record)
            self.log.info("***** Associating existing 'CAMPAIGN' record to member  *****")
            list_of_medication = keen.select_existing_records()
            for medication in list_of_medication:
                if medication.text == existing_Campaign_record:
                    self.driver.execute_script("arguments[0].click();", medication)
                    self.log.info("***** Existing record is selected *****")
                    break
            keen.save_button_Add()
            self.log.info("***** Associated existing 'HOSPITAL' record to member *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen.success_message()
            assert success_message_of_records.is_displayed(), "Record is not saved"
        else:
            action_utils.wait_for_element((Create_capture_member_details.new_creation))
            keen.click_new_member()
            pop_up_of_new_campaigns = keen.pop_up_Newcreation()
            if pop_up_of_new_campaigns.text == "New Keen campaign":
                assert True
            else:
                assert False
            print("Row number:", row_number)
            sheet_campaign=self.sheet_name.get_sheet_name('Campaigns')
            data_row = sheet_campaign[row_number]
            column_field_mapping = {
                'Parent_organization_Name': 'Parent_organization_Name',
                # 'Available Type': 'Available Type',
                # 'Available Type1': 'Available Type1',
                'Available Type2': 'Available Type2',
                'Start Date': 'Start Date', 'Start Time': 'Start Time', 'End Date': 'End Date',
                'End Time': 'End Time',
            }
            field_locators = {
                'Parent_organization_Name': (Create_capture_member_details.Field_01),
                'Available Type': (Create_capture_member_details.type_avaliable),
                # 'Available Type1': (Create_capture_member_details.type_avaliable),
                # 'Available Type2': (Create_capture_member_details.type_avaliable),
                'Start Date': (Create_capture_member_details.Field_SD_01),
                'Start Time': (Create_capture_member_details.Field_D_04),
                'End Date': (Create_capture_member_details.status_event),
                'End Time': (Create_capture_member_details.start_date),
            }
            for cell in data_row:
                column_name = sheet_campaign.cell(row=2, column=cell.column).value
                print("Column name:", column_name)
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    self.log.info("*****Campaign field names and column names are matched *****")
                    column_value = cell.value
                    locator = field_locators[field_name]
                    action_utils.wait_for_element((locator))
                    element = self.driver.find_element(*locator)

                    if element.tag_name == 'div':
                        if field_name == 'Available Type':
                            list_of_types = keen.select_options_in_list()
                            for type in list_of_types:
                                if type.text == column_value:
                                    self.driver.execute_script("arguments[0].click();", type)
                                    keen.click_move_to_chosen()
                                    self.log.info("***** Particular type option is seleected *****")
                                    break
                    else:
                        element.clear()
                        element.send_keys(column_value)
    def test_create_campaigns(self):
        for r in range(3,4):
            Campaign_Name=readdata_campaigns.readdata(r,1)
            Campaign_description=readdata_campaigns.readdata(r,2)
            Available_type=readdata_campaigns.readdata(r,3)
            Available_type1=readdata_campaigns.readdata(r,4)
            Available_type2=readdata_campaigns.readdata(r,5)
            start_date=readdata_campaigns.readdata(r,6)
            start_time=readdata_campaigns.readdata(r,7)
            end_date=readdata_campaigns.readdata(r,8)
            end_time=readdata_campaigns.readdata(r,9)
            keen = Create_capture_member_details(self.driver)
            action=ActionChains(self.driver)
            keen_login = Keen_login(self.driver)
            keen_login.keen_leads_members()
            time.sleep(10)
            keen.select_member()
            time.sleep(25)
            keen.Capture_Full_Member()
            self.driver.execute_script("scroll(0, 150);")
            action_utils = ActionUtils(self.driver)
            keen.select_campaigns()
            pop_up_of_Members_campaigns = keen.pop_up()
            if pop_up_of_Members_campaigns.text == "Member's Campaign":
                assert True
            else:
                assert False
            keen.click_new()
            pop_up_of_New_Members_campaigns = keen.pop_up_of_New_Members()
            print(pop_up_of_New_Members_campaigns.text)
            if pop_up_of_New_Members_campaigns.text == "New Member campaign":
                assert True
            else:
                assert False
            time.sleep(5)
            keen.search_keen_campaign()
            time.sleep(5)
            keen.click_new_member()
            pop_up_of_new_campaigns = keen.pop_up_Newcreation()
            if pop_up_of_new_campaigns.text == "New Keen campaign":
                assert True
            else:
                assert False
            time.sleep(15)
            keen.enter_campaign_name(Campaign_Name)
            # driver.switch_to.frame("Rich Text Editor, editor")
            # keen.enter_description_campaign().send_keys(Campaign_description)
            pop_up_window = keen.click_move_to_chosen()
            self.driver.execute_script("arguments[0].scrollIntoView();", pop_up_window)
            list_of_types = keen.select_options_in_list()
            for i in list_of_types:
                print(i.text)
                if i.text == Available_type:
                    action.move_to_element(i).click().perform()
                    break
            time.sleep(5)
            keen.click_move_to_chosen()
            keen.enter_startdate(start_date)
            keen.enter_enddate(end_date)

            keen.enter_starttime(start_time)
            keen.enter_endtime(end_time)
            keen.save_button_creation()
            success_message_campaign=keen.success_message_of_records()
            print(success_message_campaign.text)
            if success_message_campaign.is_displayed():
                assert True
            else:
                assert False
            keen.save_button_Add()
            success_message_saved = keen.success_message()
            print(success_message_saved.text)
            if success_message_saved.is_displayed():
                assert True
            else:
                assert False
            pop_up_of_New_Members_campaigns = keen.pop_up_of_New_Members()
            # print(pop_up_of_New_Members_campaigns.text)
            if pop_up_of_New_Members_campaigns.text == "New Member campaign":
                assert True
            else:
                assert False
            list_of_selected_Campaign = keen.validation_of_records()
            for i in list_of_selected_Campaign:
                if i.text == Campaign_Name:
                    action.move_to_element(i).click().perform()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    time.sleep(10)
                    keen.click_record()
                    try:
                        verify_Name = keen.validation_Caregiver_Name()
                        if verify_Name.text == Campaign_Name:
                            assert True
                        else:
                            assert True
                        verify_StartDate_Time = keen.validation_StartTime_Date()
                        if verify_StartDate_Time.text == start_time + ' ' + start_time:
                            assert True
                        else:
                            assert False
                        verify_EndDate_Time = keen.validation_EndTime_Date()
                        if verify_EndDate_Time.text == end_date + ' ' + end_time:
                            assert True
                        else:
                            assert False

                        if guid == guid:
                            self.driver.close()
                        if parent_guid == parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            keen.close()
                            break
                    except Exception as ex:
                        print(ex)

    ### Test Description:- Editing the Assosicated Campaigns to a Member
    ### Test Steps:-Login to SFDC, Click on Keen Leads and Members, Select Member, Click on CFMD
    ### Click on Campaigns,create and  Assosicate to a member
    @pytest.mark.order(10)
    @allure.description("Editing the Assosicated Campaigns to a Member")
    def test_validation_campaigns(self):
        Campaign_Name = readdata_campaigns.readdata(3, 1)
        Campaign_description = readdata_campaigns.readdata(4, 2)
        Available_type = readdata_campaigns.readdata(3, 3)
        edit_available_type=readdata_campaigns.readdata(4,4)
        Available_type1 = readdata_campaigns.readdata(4, 4)
        Available_type2 = readdata_campaigns.readdata(4, 5)
        start_date = readdata_campaigns.readdata(4, 6)
        start_time = readdata_campaigns.readdata(4, 7)
        end_date = readdata_campaigns.readdata(4, 8)
        end_time = readdata_campaigns.readdata(4, 9)
        keen = Create_capture_member_details(self.driver)
        action=ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(10)
        keen.select_member()
        time.sleep(25)
        keen.Capture_Full_Member()
        self.driver.execute_script("scroll(0, 150);")
        action_utils = ActionUtils(self.driver)
        keen.select_campaigns()
        pop_up_of_Members_campaigns = keen.pop_up()
        if pop_up_of_Members_campaigns.text == "Member's Campaign":
            assert True
        else:
            assert False
        list_Campaigns = keen.validation_of_records()
        for i in list_Campaigns:
            if i.text == Campaign_Name:
                action.move_to_element(i).click().perform()
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                time.sleep(10)
                keen.click_record()
                try:
                    keen.edit_caregiver()
                    list_of_types = keen.select_options_in_list()
                    for i in list_of_types:
                        print(i.text)
                        if i.text == Available_type:
                            action.move_to_element(i).click().perform()
                            break
                    time.sleep(5)
                    keen.click_to_available()
                    list_of_types = keen.select_options_in_list()
                    for i in list_of_types:
                        print(i.text)
                        if i.text == edit_available_type:
                            action.move_to_element(i).click().perform()
                            break
                    keen.click_move_to_chosen()
                    keen.edit_StartDate(start_date)
                    keen.edit_EndDate(end_date)
                    keen.edit_StartTime(start_time)
                    keen.edit_EndTime(end_time)
                    keen.edit_save()
                    time.sleep(5)
                    verify_Name=keen.validation_Caregiver_Name()
                    if verify_Name.text == Campaign_Name:
                        assert True
                    else:
                        assert True
                    verify_StartDate_Time=keen.validation_StartTime_Date()
                    if verify_StartDate_Time.text == start_time+' ' +start_time:
                        assert True
                    else:
                        assert False
                    verify_EndDate_Time=keen.validation_EndTime_Date()
                    if verify_EndDate_Time.text == end_date+' ' +end_time:
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                        if parent_guid == parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            keen.close()
                            break
                except Exception as ex:
                    print(ex)

    def test_member_physicians(self,row_number):
        keen=Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        sheet_physicians = self.sheet_name.get_sheet_name('Physicians')
        data_row = sheet_physicians[row_number]
        column_field_mapping = {
            'City': 'City',
            'State': 'State', 'Zip code': 'Zip code'
        }
        field_locators = {
            'City': (Create_capture_member_details.new_city),
            'State': (Create_capture_member_details.member_physician_state),
            'Zip code': (Create_capture_member_details.new_zipcode),
        }
        for cell in data_row:
            column_name = sheet_physicians.cell(row=2, column=cell.column).value
            print("Column name:", column_name)
            if column_name in column_field_mapping:
                field_name = column_field_mapping[column_name]
                column_value = cell.value
                self.log.info("***** Column name and Field name is matched *****")
                locator = field_locators[field_name]
                action_utils.wait_for_element((locator))
                element = self.driver.find_element(*locator)
                if element.tag_name == 'button':
                    if field_name == 'State':
                        element.click()
                        self.log.info("***** State field is clicked *****")
                        state_options=keen.select_options()
                        for state in state_options:
                            if state.get_attribute('title') == column_value:
                                self.driver.execute_script("arguments[0].click();", state)
                                break
                else:
                    element.clear()
                    element.send_keys(column_value)

    def test_click_physicians(self):
        keen=Create_capture_member_details(self.driver)
        action_utils=ActionUtils(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.click_physicians))
        keen.select_physicians()
        action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_up_of_Members_hospitals = keen.pop_up()
        assert pop_up_of_Members_hospitals.text == "Member's Physicians", "Member's Physicians popup is not matched"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
    #Testcase Description:"Create New Physicians and Assosicate to a Member"
    #TestCase Steps:1.Login to SFDC, 2.Click on Keen Leads and Member.
    # 3.Capture Full Member Details.
    #4.Click on Physicians
    #5.Create and Assosicate Physicians
    @allure.description("Create a New Physicians and Associate to a Member")
    def test_physicians(self,row_number):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        pop_up_of_New_Members_physicians = keen.pop_up_of_New_Members()
        assert pop_up_of_New_Members_physicians.text == "New Member's physician","New Member's physician popup is not matched"
        verify_hospitals = action_utils.record_verification(row_number, 'Physicians', 'physicians_created')
        if verify_hospitals == 'YES':
            self.log.info("***** Physician record is exists in Salesforce *****")
            existing_physician_record = self.sheet_name.retrieve_value(row_number, 'L', 'Physicians',0)
            print("physician record names:", existing_physician_record)
            action_utils.wait_for_element((Create_capture_member_details.new_hospital))
            keen.click_physician_directory().send_keys(existing_physician_record)
            self.log.info("***** Associating existing 'physician' record to member  *****")
            action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
            list_of_physicians = keen.select_options()
            for physicians in list_of_physicians:
                if physicians.text == existing_physician_record:
                    self.driver.execute_script("arguments[0].click();", physicians)
                    self.log.info("***** Existing record is selected *****")
                    break
            return existing_physician_record
        else:
            action_utils.wait_for_element((Create_capture_member_details.new_creation))
            keen.click_new_member()
            pop_up_of_new_physicians = keen.pop_up_Newcreation()
            assert pop_up_of_new_physicians.text == "New Physician directory","New Physician directory popup is not matched"
            print("Row number:", row_number)
            sheet_physicians=self.sheet_name.get_sheet_name('Physicians')
            data_row = sheet_physicians[row_number]
            column_field_mapping = {
                'Last Name': 'Last Name',
                'First name': 'First name',
                'Address line': 'Address line',
                'City': 'City',
                'State': 'State', 'Zip code': 'Zip code', 'NPI': 'NPI',
                'TaxID': 'TaxID', 'Status': 'Status', 'Phone': 'Phone',
                'Specialty': 'Specialty', 'Email': 'Email', 'Sub_Speciality': 'Sub_Speciality',
            }
            field_locators = {
                'Last Name': (Create_capture_member_details.Field_01),
                'First name': (Create_capture_member_details.Field_02),
                'NPI': (Create_capture_member_details.Field_03),
                'Address line': (Create_capture_member_details.Field_D_01),
                'City': (Create_capture_member_details.Field_D_03),
                'Phone': (Create_capture_member_details.Field_04),
                'State': (Create_capture_member_details.Field_SD_01),
                'Zip code': (Create_capture_member_details.Field_D_04),
                'TaxID': (Create_capture_member_details.hospital_taxid),
                'Status': (Create_capture_member_details.Field_S_02),
                'Specialty': (Create_capture_member_details.moveto_subspecialty),
                'Email': (Create_capture_member_details.Field_05),
                'Sub_Speciality': (Create_capture_member_details.moveto_subspecialty),
            }
            for cell in data_row:
                column_name = sheet_physicians.cell(row=2, column=cell.column).value
                print("Column name:", column_name)
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    column_value = cell.value
                    print("input:", column_value)
                    locator = field_locators[field_name]
                    action_utils.wait_for_element((locator))
                    element = self.driver.find_element(*locator)
                    if element.tag_name == 'a':
                        if field_name == 'State':
                            element.click()
                            action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
                            list_states = keen.select_options_in_list()
                            for states in list_states:
                                print(states.text)
                                if states.text == column_value:
                                    states.click()
                                    # action.move_to_element(states).click().perform()
                                    break
                    elif element.tag_name == 'div':
                        if field_name == 'Specialty':
                            list_specality = keen.edit_superspecialty()
                            for specality in list_specality:
                                if specality.text == column_value:
                                    self.driver.execute_script("arguments[0].click();",specality)
                                    break
                            keen.click_move_to_chosen()
                        if field_name == 'Sub_Speciality':
                            list_subspecialty = keen.edit_Subspecialty()
                            for subspecialty in list_subspecialty:
                                if subspecialty.text == column_value:
                                    self.driver.execute_script("arguments[0].click();",subspecialty)
                                    break
                            keen.Click_Move_to_choosen_2()
                    else:
                        element.clear()
                        element.send_keys(column_value)
                        if field_name  == "Last Name":
                            physician_name=cell.value
        self.log.info("****Saving the data**********")
        keen.save_button_creation()
        action_utils.wait_for_element((Create_capture_member_details.Success_message_creation))
        success_message = keen.success_message_of_records()
        assert success_message.is_displayed(),"Created record is not saved"
        self.log.info("****Assosicate physicians to  Keen Leads and Members**********")
        self.number.write_result_in_to_excel_sheet(row_number, "Physicians", "L")
        self.test_member_physicians(row_number)
        keen.save_button_Add()
        action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
        success_message_of_records = keen.success_message()
        assert success_message_of_records.is_displayed(), "Record is saved"
        return physician_name
    def test_select_physician(self,name):
        keen = Create_capture_member_details(self.driver)
        action = ActionChains(self.driver)
        action_utils=ActionUtils(self.driver)
        self.log.info("****Verifing the Assosicated record**********")
        list_of_selected_caregivers = keen.validation_of_records()
        for records in list_of_selected_caregivers:
            if name in records.text:
                action.move_to_element(records).click().perform()
                break
    def test_validation_of_physicians(self,row_number):
        Last_Name = readdata_physicians.readdata(row_number, 1)
        First_name = readdata_physicians.readdata(row_number, 2)
        NPI = readdata_physicians.readdata(row_number, 3)
        Address_line = readdata_physicians.readdata(row_number, 4)
        City = readdata_physicians.readdata(row_number, 5)
        Phone = readdata_physicians.readdata(row_number, 6)
        State = readdata_physicians.readdata(row_number, 7)
        Email = readdata_physicians.readdata(row_number, 8)
        Zip_code = readdata_physicians.readdata(row_number, 9)
        Specialty = readdata_physicians.readdata(row_number, 10)
        Sub_specialty = readdata_physicians.readdata(row_number, 11)
        keen=Create_capture_member_details(self.driver)
        action=ActionChains(self.driver)
        #### Validating the entered data
        self.log.info("****Validating the data**********")
        verify_lastname = keen.validation_Physician_LastName()
        if verify_lastname.text == Last_Name:
            assert True
        else:
            assert False
        verify_firstname = keen.validation_Physician_Firstname()
        if verify_firstname.text == First_name:
            assert True
        else:
            assert False
        verify_address = keen.validation_Physician_Addressline()
        if verify_address.text == Address_line:
            assert True
        else:
            assert False
        verify_NPI = keen.validation_Physician_NPI()
        if verify_NPI.text == NPI:
            assert True
        else:
            assert False
        verify_city = keen.validation_Physician_City()
        if verify_city.text == City:
            assert True
        else:
            assert False
        verify_phone = keen.validation_Physicain_Phone()
        if verify_phone.text == Phone:
            assert True
        else:
            assert False
        verify_state = keen.validation_Physician_State()
        if verify_state.text == State:
            assert True
        else:
            assert False
        verify_email = keen.validation_Physician_Email()
        if verify_email.text == Email:
            assert True
        else:
            assert False
        verify_zipcode = keen.validation_Physician_Zipcode()
        if verify_zipcode.text == Zip_code:
            print("Test Pass")
            # assert True
        else:
            print("Test fail")
            # assert False
        verify_specialty = keen.validation_Physician_Specialty()
        if verify_specialty.text == Specialty:
            assert True
        else:
            assert False
        verify_Subpecialty = keen.validation_Physician_Subspecialty()
        if verify_Subpecialty.text == Sub_specialty:
            assert True
        else:
            assert False
        self.log.info("****Validation is completed**********")
    ### Test Description:- Editing the Assosicated Physicians to a Member
    ### Test Steps:- Login to SFDC,Click on Keen Leads and Member,Capture Full Member Details.
    #4.Click on Physician, Edit the Assosicated Physicians
    @pytest.mark.order(12)
    def test_edit_physicians(self,row_number=2):
        keen = Create_capture_member_details(self.driver)
        action=ActionChains(self.driver)
        First_name = readdata_physicians.readdata(row_number, 2)
        NPI = readdata_physicians.readdata(row_number, 3)
        Address_line = readdata_physicians.readdata(row_number, 4)
        City = readdata_physicians.readdata(row_number, 5)
        Phone = readdata_physicians.readdata(row_number, 6)
        State = readdata_physicians.readdata(row_number, 7)
        Email = readdata_physicians.readdata(row_number, 8)
        Zip_code = readdata_physicians.readdata(row_number, 9)
        Specialty = readdata_physicians.readdata(row_number, 10)
        Sub_specialty = readdata_physicians.readdata(row_number, 11)
        keen.edit_physicians()
        keen.edit_firstname_physicians(First_name)
        keen.edit_NPI(NPI)
        keen.edit_address_line_1_physicians(Address_line)
        keen.edit_city_physicians(City)
        keen.edit_phone_physicians(Phone)
        keen.edit_state_physicians()
        list_states = keen.select_options_in_list()
        for state in list_states:
            if state.text == State:
                action.move_to_element(state).click().perform()
                break
        keen.edit_Email_physicians(Email)
        keen.edit_zipcode_physicians(Zip_code)
        # page_to_scroll = keen.Subspecialty()
        # self.driver.execute_script("arguments[0].scrollIntoView();", page_to_scroll)
        list_specality = keen.edit_superspecialty()
        for i in list_specality:
            if i.text == Specialty:
                i.click()
                break
        list_subspecialty = keen.edit_Subspecialty()
        for i in list_subspecialty:
            if i.text == Sub_specialty:
                i.click()
                break
        keen.edit_save()
    ### Test Description:- Create and Assosicate Outbound Referral Practice to a Member
    ### TestCase Steps:1.Login to SFDCClick on Keen Leads and Member,Capture Full Member Details.
    ### Click on OutboundRefreralPractice,Create and Assosicate Outbound Referral Practice
    @allure.description("Create and Assosicate Outbound Referral Practice to a Member")
    @pytest.mark.order(13)
    def test_create_outbound_referral_practice(self):
        keen = Create_capture_member_details(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(10)
        action = ActionChains(self.driver)
        action_utils=ActionUtils(self.driver)
        for r in range(4,5):
            Practice_name = readdata_practices.readdata(r, 1)
            Practice_NPI = readdata_practices.readdata(r, 2)
            TaxID = readdata_practices.readdata(r, 3)
            Phone_practices = readdata_practices.readdata(r, 4)
            Practice_email = readdata_practices.readdata(r, 5)
            Status = readdata_practices.readdata(r, 6)
            Address_1 = readdata_practices.readdata(r, 7)
            City = readdata_practices.readdata(r, 8)
            state =readdata_practices.readdata(r, 9)
            zipcode_of_practices = readdata_practices.readdata(r, 10)
            Aledade_Practice_Type = readdata_practices.readdata(r, 11)
            Practice_url = readdata_practices.readdata(r, 12)
            Accepted_Carriers = readdata_practices.readdata(r, 13)
            keen.select_outbound_referral()
            pop_of_members_practice = keen.pop_up()
            if pop_of_members_practice.text == "Outbound Referral Practices":
                assert True
            else:
                assert False
            time.sleep(10)
            keen.click_new()
            New_Members_practice = keen.pop_up_of_New_Members()
            if New_Members_practice.text == "New Outbound Referral: Practice":
                assert True
            else:
                assert False
            time.sleep(15)
            keen.search_practice_directory()
            keen.click_new_member()
            pop_up_of_new_practice_directory = keen.pop_up_Newcreation()
            if pop_up_of_new_practice_directory.text == "New Practice directory":
                assert True
            else:
                assert False
            time.sleep(10)
            keen.enter_practice_name(Practice_name)

            keen.enter_practice_NPI(Practice_NPI)
            time.sleep(6)
            keen.enter_taxID(TaxID)
            keen.enter_Practice_Phone(Phone_practices)
            time.sleep(10)
            keen.enter_practice_email(Practice_email)
            keen.enter_Address_line_1(Address_1)
            keen.enter_City(City)
            keen.click_state_of_practice()
            list_of_states = keen.select_options_in_list()
            for i in list_of_states:
                print(i.text)
                if i.text == state:
                    action.move_to_element(i).click().perform()
                    break
            keen.enter_Zipcode(zipcode_of_practices)
            # self.keen.click_practice_organization().send_keys()
            keen.click_status()
            list_of_status = keen.select_options_in_list()
            for i in list_of_status:
                if i.text == Status:
                    action.move_to_element(i).click().perform()
                    break
            time.sleep(5)
            scrollable_popup = self.driver.find_element(By.XPATH,"//button[@title='Move selection to Chosen']")
            self.driver.execute_script("arguments[0].scrollIntoView();", scrollable_popup)
            list_of_options = keen.select_options_type()
            for i in list_of_options:
                print(i.text)
                if i.text == Accepted_Carriers:
                    time.sleep(10)
                    action.move_to_element(i).click().perform()
                    break
            keen.click_move_to_chosen()
            keen.click_Aledade_Practice_Type()
            list_of_practices = keen.select_options_in_list()
            for i in list_of_practices:
                if i.text == Aledade_Practice_Type:
                    action.move_to_element(i).click().perform()
                    break
            keen.enter_practice_url(Practice_url)
            keen.save_button_creation()
            success_message = keen.success_message_of_records()
            print(success_message.text)
            if success_message.is_displayed():
                assert True
            else:
                assert False
            keen.save_button_Add()
            time.sleep(5)
            success_message_of_records = keen.success_message()
            if success_message_of_records.is_displayed():
                assert True
            else:
                assert False
            pop_up_list = keen.pop_up()
            if pop_up_list.text == "Outbound Referral Practices":
                assert True
            else:
                assert False
            list_of_practices = keen.validation_of_records()
            for i in list_of_practices:
                if i.text == Practice_name:
                    action.move_to_element(i).click().perform()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_record()
                    phone_validation=keen.validation_phone()
                    if phone_validation.text == Phone_practices:
                        assert True
                    else:
                        assert False
                    list_of_data = keen.validation_of_record_data()
                    for i in list_of_data:
                        print(i.text)
                        try:
                            if i.text == Practice_name:
                                assert True

                            elif i.text == Practice_NPI:
                                assert True

                            elif i.text == TaxID:
                                assert True

                            elif i.text == Practice_email:
                                assert True
                            elif i.text == Status:
                                assert True
                            elif i.text == Address_1:
                                assert True
                            elif i.text == City:
                                assert True
                            elif i.text == state:
                                assert True
                            elif i.text == zipcode_of_practices:
                                assert True
                            elif i.text ==  Aledade_Practice_Type:
                                assert True
                            elif i.text == Practice_url:
                                assert True
                            elif i.text == Accepted_Carriers:
                                assert True
                            else:
                                assert False
                        except Exception as Ex:
                            print(Ex)

                    if guid == guid:
                        self.driver.close()
                        if parent_guid == parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            keen.close()
                            break
    ### TestCase Description:- Select referral organization and Edit the record
    ### TesCase Steps:- Login to SFDC,Select Member, Click Capture full member Details, click outbound_referral_organization
    ### Select Record and Edit
    @allure.description("Edit outbound_referral_organization")
    @pytest.mark.order(14)
    def test_edit_outbound_referral_practice(self):
        keen = Create_capture_member_details(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(10)
        action = ActionChains(self.driver)
        keen.select_member()
        time.sleep(25)
        keen.Capture_Full_Member()
        self.driver.execute_script("scroll(0, 150);")
        Practice_name = readdata_practices.readdata(4, 1)
        Practice_NPI = readdata_practices.readdata(5, 2)
        TaxID = readdata_practices.readdata(5, 3)
        Phone_practices = readdata_practices.readdata(5, 4)
        Practice_email = readdata_practices.readdata(5, 5)
        Status = readdata_practices.readdata(5, 6)
        Address_1 = readdata_practices.readdata(5, 7)
        City = readdata_practices.readdata(5, 8)
        state = readdata_practices.readdata(5, 9)
        zipcode_of_practices = readdata_practices.readdata(5, 10)
        Aledade_Practice_Type = readdata_practices.readdata(5, 11)
        Practice_url = readdata_practices.readdata(5, 12)
        Accepted_Carriers = readdata_practices.readdata(5, 13)
        keen.select_outbound_referral()
        pop_of_members_practice = keen.pop_up()
        if pop_of_members_practice.text == "Outbound Referral Practices":
            assert True
        else:
            assert False
        time.sleep(10)
        list_of_Organization = self.keen.validation_of_records()
        for i in list_of_Organization:
            if i.text == Practice_name:
                action.move_to_element(i).click().perform()
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        # all_guid = driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
            time.sleep(10)
            keen.click_record()
            # print(driver.title)
            keen.edit_practices_NPI()
            keen.enter_practice_NPI(Practice_NPI)
            time.sleep(6)
            keen.enter_taxID(TaxID)
            keen.enter_Practice_Phone(Phone_practices)
            time.sleep(10)
            keen.enter_practice_email(Practice_email)
            # self.keen.click_practice_organization().send_keys()
            time.sleep(5)
            # driver.execute_script("scroll(0, 250);")
            keen.click_status()
            list_of_status = keen.select_options_in_list()
            for i in list_of_status:
                print(i.text)
                if i.text == Status:
                    action.move_to_element(i).click().perform()
                    break
            time.sleep(5)
            pop_up_window = keen.click_move_to_chosen()
            self.driver.execute_script("arguments[0].scrollIntoView();", pop_up_window)

            list_of_options = keen.select_options_type()
            for i in list_of_options:
                print(i.text)
                if i.text == Accepted_Carriers:
                    time.sleep(10)
                    action.move_to_element(i).click().perform()
                    break
            keen.click_to_available()
            list_of_options = keen.select_options_type()
            for i in list_of_options:
                print(i.text)
                if i.text == Accepted_Carriers:
                    action.move_to_element(i).click().perform()
                    break
            keen.click_move_to_chosen()
            keen.click_Aledade_Practice_Type()
            list_of_practices = keen.select_options_in_list()
            for i in list_of_practices:
                if i.text == Aledade_Practice_Type:
                    action.move_to_element(i).click().perform()
                    break

            keen.enter_Address_line_1(Address_1)

            keen.enter_practice_url(Practice_url)
            keen.enter_City(City)
            keen.click_state_of_practice()
            list_of_states = keen.select_options_in_list()
            for i in list_of_states:
                print(i.text)
                if i.text == state:
                    action.move_to_element(i).click().perform()
                    break
            keen.enter_Zipcode(zipcode_of_practices)
            keen.edit_save().click()
            phone_validation = keen.validation_phone()
            if phone_validation.text == Phone_practices:
                assert True
            else:
                assert False
            verfiy_practiceName = keen.validation_practice_name()
            if verfiy_practiceName == Practice_name:
                assert True
            else:
                assert False
            verify_Addressline1 = keen.validation_PracticeAddress_line_1()
            if verify_Addressline1 == Address_1:
                assert True
            else:
                assert False
            verify_PracticeNPI = keen.validation_practice_NPI()
            if verify_PracticeNPI == Practice_NPI:
                assert True
            else:
                assert False
            verify_TaxID = keen.validation_practice_taxID()
            if verify_TaxID == TaxID:
                assert True
            else:
                assert False
            verify_City = keen.validation_PracticeCity()
            if verify_City == City:
                assert True
            else:
                assert False
            verify_Phone = keen.validation_PracticePhone()
            if verify_Phone == Phone_practices:
                assert True
            else:
                assert False
            verify_State = keen.validation_state_practice()
            if verify_State == state:
                assert True
            else:
                assert False
            verify_Practiceemail = keen.validation_practice_email()
            if verify_Practiceemail == Practice_email:
                assert True
            else:
                assert False
            verify_Zipcode = keen.validation_practice_zipcode()
            if verify_Zipcode == zipcode_of_practices:
                assert True
            else:
                assert False
            verify_Status = keen.validation_Practice_status()
            if verify_Status == Status:
                assert True
            else:
                assert False
            # Maincontact
            verify_AcceptedCarriers = keen.validation_Practiceacceptedcarriers()
            if verify_AcceptedCarriers == Accepted_Carriers:
                assert True
            else:
                assert False
            verify_AledadePracticeType = keen.validation_Aledade_Practice_Type()
            if verify_AledadePracticeType == Aledade_Practice_Type:
                assert True
            else:
                assert False
            verify_PracticeUrl = keen.validation_practice_url()
            if verify_PracticeUrl == Practice_url:
                assert True
            else:
                assert False
            if guid == guid:
                self.driver.close()
                if parent_guid == parent_guid:
                    self.driver.switch_to.window(parent_guid)
                    keen.close()
                    break
    def test_click_pharmacies(self):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.pharmacies))
        keen.select_pharmacies()
        action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
        pop_up_of_Members_hospitals = keen.pop_up()
        assert pop_up_of_Members_hospitals.text == "Member's Pharmacies", "Member's Pharmacies popup is not matched"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
    ### TestCase Description:- Create New Pharmacies and Associate to a Member
    ### TesCase Steps:- Login to SFDC,Select Member, Click Capture full member Details, click Pharmacies
    ### Create new record and associate to a member
    @allure.description("Create New Pharmacies and Associate to a Member")
    def test_pharmacies(self,row_number):
        keen = Create_capture_member_details(self.driver)
        self.driver.execute_script("scroll(0, 150);")
        action_utils = ActionUtils(self.driver)
        action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
        pop_up_pharmacies = keen.pop_up_of_New_Members()
        assert pop_up_pharmacies.text == "New Member's pharmacy","New Member's pharmacy popup is not matched"
        verify_pharmacies = action_utils.record_verification(row_number, 'Pharmacies', 'pharmacy_created')
        if verify_pharmacies == 'YES':
            self.log.info("***** Pharmacies record is exists in Salesforce *****")
            existing_pharmacies_record = self.sheet_name.retrieve_value(row_number, 'J', 'Pharmacies',0)
            print("Pharamacies record names:", existing_pharmacies_record)
            action_utils.wait_for_element((Create_capture_member_details.search_pharmacy))
            keen.pharmacy_directory().send_keys(existing_pharmacies_record)
            self.log.info("***** Associating existing 'Pharmacies' record to member  *****")
            list_of_pharmacies = keen.select_existing_records()
            for pharmacies in list_of_pharmacies:
                if pharmacies.text == existing_pharmacies_record:
                    self.driver.execute_script("arguments[0].click();", pharmacies)
                    self.log.info("***** Existing record is selected *****")
                    break
            keen.save_button_Add()
            self.log.info("***** Associated existing 'Pharmacies' record to member *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen.success_message()
            assert success_message_of_records.is_displayed(), "Record is not saved"
        else:
            action_utils.wait_for_element((Create_capture_member_details.new_creation))
            keen.click_new_member()
            action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
            pop_up_New_Pharmacy_directory = keen.pop_up_Newcreation()
            assert pop_up_New_Pharmacy_directory.text == "New Pharmacy directory","New Pharmacy directory popup is not matched"
            print("Row number:", row_number)
            data_row = self.sheet_pharmacy[row_number]
            column_field_mapping = {
                'Pharmacy name': 'Pharmacy name',
                'Address Line1': 'Address Line1',
                'Phone': 'Phone',
                'City': 'City',
                'State': 'State', 'Zipcode': 'Zipcode','Status': 'Status',
                'Pharmacy chain': 'Pharmacy chain', 'Mail Order': 'Mail Order',
            }
            field_locators = {
                'Pharmacy name': (Create_capture_member_details.Field_01),
                'Address Line1': (Create_capture_member_details.Field_D_01),
                'City': (Create_capture_member_details.Field_D_03),
                'Phone': (Create_capture_member_details.Field_02),
                'State': (Create_capture_member_details.Field_SD_01),
                'Zipcode': (Create_capture_member_details.Field_D_04),
                'Status': (Create_capture_member_details.Field_S_03),
                'Pharmacy chain': (Create_capture_member_details.Field_S_01),
                'Mail Order': (Create_capture_member_details.Field_S_02),
            }
            for cell in data_row:
                column_name = self.sheet_pharmacy.cell(row=2, column=cell.column).value
                print("Column name:", column_name)
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    column_value = cell.value
                    print("input:", column_value)
                    locator = field_locators[field_name]
                    action_utils.wait_for_element((locator))
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        if field_name == 'Pharmacy chain':
                            self.log.info("***** Pharmacy chain field is present *****")
                            element.click()
                            self.log.info("***** Pharmacy chain field is selected *****")
                            list_of_chains = keen.select_options_in_list()
                            self.log.info("***** Options for pharmacy chains  field *****")
                            for pharmacy_chains in list_of_chains:
                                if pharmacy_chains.text == column_value:
                                    self.driver.execute_script("arguments[0].click();",pharmacy_chains)
                                    self.log.info("***** Required Option is selected for pharmacy chain field *****")
                                    break
                        if field_name == 'Mail Order':
                            self.log.info("***** Mail order field is present *****")
                            element.click()
                            self.log.info("***** Mail order field is selected *****")
                            list_mail_order = keen.select_options_in_list()
                            for mail in list_mail_order:
                                self.log.info("***** Options for Pharmacy chain field *****")
                                if mail.text == column_value:
                                    self.driver.execute_script("arguments[0].click();",mail)
                                    self.log.info("***** Required Option is selected of Pharmacy chain field *****")
                                    break
                        if field_name == 'State':
                            self.log.info("***** State field is present *****")
                            element.click()
                            self.log.info("***** State field is selected *****")
                            states = keen.select_options_in_list()
                            self.log.info("***** Options for state field *****")
                            for pharmacy_state in states:
                                if pharmacy_state.text == column_value:
                                    self.driver.execute_script("arguments[0].click();",pharmacy_state)
                                    self.log.info("***** Required Option is selected for State field *****")
                                    break
                        if field_name == 'Status':
                            self.log.info("***** Status field is present *****")
                            element.click()
                            self.log.info("***** Status field is selected *****")
                            status = keen.select_options_in_list()
                            self.log.info("***** Options for status field *****")
                            for pharmacy_status in status:
                                if pharmacy_status.text == column_value:
                                    self.driver.execute_script("arguments[0].click();",pharmacy_status)
                                    self.log.info("***** Required Option is selected for Status field *****")
                                    break
                    else:
                        self.log.info("***** Entering the test data to the respected fields *****")
                        element.clear()
                        element.send_keys(column_value)
            keen.save_button_creation()
            success_message_creation = keen.success_message_of_records()
            assert success_message_creation.is_displayed(),"New creation toast message is not displayed"
            self.number.write_result_in_to_excel_sheet(row_number, "Pharmacies", "J")
            keen.save_button_Add()
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            assosciate_record_message = keen.success_message()
            assert assosciate_record_message.is_displayed(),"Associated toast message is not displayed"
    ### TestCase Description:-Validation of Pharmacies
    ### TesCase Steps:- Login to SFDC,Select Member, Click Capture full member Details, click Pharmacies
    ### Click pharmacy record and Validate the record
    def test_validation_pharmacy(self,row_pharmacy):
        Pharmacy_name = readdata_pharmacies.readdata(row_pharmacy, 1)
        Address_Line1 = readdata_pharmacies.readdata(row_pharmacy, 2)
        Phone = readdata_pharmacies.readdata(row_pharmacy, 3)
        Pharmacy_chain = readdata_pharmacies.readdata(row_pharmacy, 4)
        City = readdata_pharmacies.readdata(row_pharmacy, 5)
        Mail_Order = readdata_pharmacies.readdata(row_pharmacy, 6)
        State = readdata_pharmacies.readdata(row_pharmacy, 7)
        Status = readdata_pharmacies.readdata(row_pharmacy, 8)
        Zip_code = readdata_pharmacies.readdata(row_pharmacy, 9)
        keen = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        action_utils = ActionUtils(self.driver)
        list_of_selected_pharmacies = keen.validation_of_records()
        for i in list_of_selected_pharmacies:
            if i.text == Pharmacy_name:
                i.click()
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                action_utils.wait_for_element((Create_capture_member_details.created_record_for_validation))
                keen.click_record()
                phone_validation = keen.validation_phone()
                if phone_validation.text == Phone:
                    assert True
                else:
                    assert False
                list_of_data = keen.validation_of_record_data()
                for i in list_of_data:
                    print(i.text)
                    try:
                        if i.text == Pharmacy_name:
                            assert True

                        elif i.text == Address_Line1:
                            assert True

                        elif i.text == Pharmacy_chain:
                            assert True

                        elif i.text == City:
                            assert True
                        elif i.text == Mail_Order:
                            assert True
                        elif i.text == State:
                            assert True
                        elif i.text == Status:
                            assert True
                        elif i.text == Zip_code:
                            assert True
                        else:
                            assert False
                    except Exception as Ex:
                        print(Ex)
                    if guid == guid:
                        self.driver.close()
                        if guid != parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            keen.close()
                            break
    def test_select_outbound_referral_organization(self):
        keen = Create_capture_member_details(self.driver)
        action_utils = ActionUtils(self.driver)
        keen.select_outbound_organization()
        pop_up_outbound_organization = keen.pop_up()
        assert pop_up_outbound_organization.text == "Outbound Referral Organization", "Outbound Referral Organization poppup id not displayed"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
        action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
        pop_of_new_outbound = keen.pop_up_of_New_Members()
        assert pop_of_new_outbound.text == "New Outbound Referral: Organization", "New Outbound Referral: Organization popup is not displayed"
    ### TestDescreption:- Create and Associate the outbound_referral_organization  to a Member
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Select a Keen Member
    ### Click on CFMD, Click on outbound_referral_organization,create and associate the outbound_referral_organizationto a member
    def test_event_community_organization(self,row_number):
        try:
            keen = Create_capture_member_details(self.driver)
            action_utils = ActionUtils(self.driver)
            verify_community_organization = action_utils.record_verification(row_number, 'Community', 'Community_Created')
            if verify_community_organization == 'YES':
                self.log.info("***** Community Organization record is existing in Salesforce *****")
                existing_community_record = self.sheet_name.retrieve_value(row_number, 'O', 'Community', 0)
                print("Community Organization:", existing_community_record)
                action_utils.wait_for_element((Create_capture_member_details.search_community))
                keen.search_Community_and_senior_organization().send_keys(verify_community_organization)
                self.log.info("***** Associating existing 'Community Organization' record to member  *****")
                action_utils.wait_for_elements((Create_capture_member_details.practice_records))
                list_of_community = keen.select_practice_records()
                for community in list_of_community:
                    if community.get_attribute('title') == existing_community_record:
                        self.driver.execute_script("arguments[0].click();", community)
                        self.log.info("***** Existing record is selected *****")
                        break
                keen.save_button_Add()
                self.log.info("***** Associated existing 'Pharmacies' record to member *****")
                action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                success_message_of_records = keen.success_message()
                assert success_message_of_records.is_displayed(), "Record is not saved"
                return existing_community_record
            else:
                community_name=None
                action_utils.wait_for_element((Create_capture_member_details.event_community))
                keen.click_new_event_community()
                action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
                pop_up_new_organization_creation = keen.pop_up_Newcreation()
                assert pop_up_new_organization_creation.text == "New Community and senior organization", "New Community and senior organization popup is not displayed"
                print("Row number:", row_number)
                data_row = self.sheet_community[row_number]
                column_field_mapping = {
                    'Organization name': 'Organization name',
                    'Address Line1': 'Address Line1', 'City': 'City',
                    'State': 'State', 'Zipcode': 'Zipcode',
                    'Phone': 'Phone', 'Website': 'Website', 'Email': 'Email', 'Services': 'Services',
                    'Servicing region (county)': 'Servicing region (county)',
                    'Organization type': 'Organization type', 'Status': 'Status',
                    'Parent_organization': 'Parent_organization',
                    # 'Main Contact': 'Main Contact',
                }
                field_locators = {
                    'Organization name': (Create_capture_member_details.organization_name),
                    'Address Line1': (Create_capture_member_details.organization_Address_line_1),
                    'City': (Create_capture_member_details.organization_city),
                    'State': (Create_capture_member_details.oragnization_state),
                    'Zipcode': (Create_capture_member_details.Field_05),
                    'Phone': (Create_capture_member_details.Field_06),
                    'Website': (Create_capture_member_details.Field_07),
                    'Email': (Create_capture_member_details.Field_08),
                    'Services': (Create_capture_member_details.organization_service_available),
                    'Servicing region (county)': (Create_capture_member_details.Field_09),
                    'Organization type': (Create_capture_member_details.Organization_type_Available),
                    'Status': (Create_capture_member_details.Field_S_04),
                    'Parent_organization': (Create_capture_member_details.parent_organization),
                    # 'Main Contact': (Create_capture_member_details.Field_S_02),
                }
                for cell in data_row:
                    column_name = self.sheet_community.cell(row=2, column=cell.column).value
                    print("Column name:", column_name)
                    if column_name in column_field_mapping:
                        field_name = column_field_mapping[column_name]
                        self.log.info("*****Parent organization field and column name is matched ***** ")
                        column_value = cell.value
                        locator = field_locators[field_name]
                        action_utils.wait_for_element((locator))
                        element = self.driver.find_element(*locator)
                        action_utils.wait_for_element((locator))
                        self.driver.execute_script("arguments[0].scrollIntoView();", element)
                        if element.tag_name == 'a':
                            if field_name == 'State':
                                element.click()
                                self.log.info("***** State field is clicked *****")
                                list_of_states = keen.select_options_in_list()
                                for states in list_of_states:
                                    if states.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", states)
                                        break
                            if field_name == 'Status':
                                element.click()
                                self.log.info("***** Status field is clicked *****")
                                list_status = keen.select_options_in_list()
                                for status in list_status:
                                    if status.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", status)
                                        break
                        elif element.tag_name == 'span':
                            if field_name == 'Services':
                                list_services = keen.select_options_in_list()
                                for services in list_services:
                                    if services.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", services)
                                        break
                            if field_name == 'Organization type':
                                list_organization_type = keen.select_options_in_list()
                                for type in list_organization_type:
                                    if type.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", type)
                                        break
                        elif element.tag_name == 'input':
                            if field_name == 'Parent_organization':
                                self.test_parent_organization(row_number)
                            if field_name == 'Main Contact':
                                print("Contcat")
                        else:
                            element.clear()
                            element.send_keys(column_value)
                    if field_name == "Organization name":
                        community_name=cell.value
                keen.click_save_community_organization()
                success_message_creation = keen.success_message_of_records()
                assert success_message_creation.is_displayed(), "New creation toast message is not displayed"
                self.sheet_name.write_result_in_to_excel_sheet(row_number, "Community", "O")
                return community_name
        except Exception as ex:
            print(ex)
    @allure.description("Create and Associate the outbound_referral_organization  to a Member")
    @pytest.mark.order(17)
    def test_create_outbound_referral_organization(self,row_number):
        try:
            keen = Create_capture_member_details(self.driver)
            action_utils = ActionUtils(self.driver)
            verify_community_organization=action_utils.record_verification(row_number, 'Community', 'Community_Created')
            if verify_community_organization == 'YES':
                self.log.info("***** Community Organization record is existing in Salesforce *****")
                existing_community_record = self.sheet_name.retrieve_value(row_number, 'O', 'Community',0)
                print("Community Organization:", existing_community_record)
                action_utils.wait_for_element((Create_capture_member_details.search_community))
                keen.search_Community_and_senior_organization().send_keys(verify_community_organization)
                self.log.info("***** Associating existing 'Community Organization' record to member  *****")
                list_of_pharmacies = keen.select_existing_records()
                for pharmacies in list_of_pharmacies:
                    if pharmacies.text == existing_community_record:
                        self.driver.execute_script("arguments[0].click();", pharmacies)
                        self.log.info("***** Existing record is selected *****")
                        break
                keen.save_button_Add()
                self.log.info("***** Associated existing 'Pharmacies' record to member *****")
                action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                success_message_of_records = keen.success_message()
                assert success_message_of_records.is_displayed(), "Record is not saved"
            else:
                action_utils.wait_for_element((Create_capture_member_details.new_creation))
                keen.click_new_member()
                action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
                pop_up_new_organization_creation = keen.pop_up_Newcreation()
                assert pop_up_new_organization_creation.text == "New Community and senior organization","New Community and senior organization popup is not displayed"
                print("Row number:", row_number)
                data_row = self.sheet_community[row_number]
                column_field_mapping = {
                    'Organization name': 'Organization name',
                    'Address Line1': 'Address Line1','City': 'City',
                    'State': 'State', 'Zipcode': 'Zipcode',
                    'Phone': 'Phone', 'Website' : 'Website' , 'Email' :'Email','Services' :'Services','Servicing region (county)' : 'Servicing region (county)',
                    'Organization type':'Organization type','Status': 'Status',
                    'Parent_organization': 'Parent_organization',
                    # 'Main Contact': 'Main Contact',
                }
                field_locators = {
                    'Organization name': (Create_capture_member_details.organization_name),
                    'Address Line1': (Create_capture_member_details.organization_Address_line_1),
                    'City': (Create_capture_member_details.organization_city),
                    'State': (Create_capture_member_details.oragnization_state),
                    'Zipcode': (Create_capture_member_details.Field_05),
                    'Phone': (Create_capture_member_details.Field_06),
                    'Website': (Create_capture_member_details.Field_07),
                    'Email' : (Create_capture_member_details.Field_08),
                    'Services' : (Create_capture_member_details.organization_service_available),
                    'Servicing region (county)' : (Create_capture_member_details.Field_09),
                    'Organization type': (Create_capture_member_details.Organization_type_Available),
                    'Status': (Create_capture_member_details.Field_S_04),
                    'Parent_organization': (Create_capture_member_details.parent_organization),
                    # 'Main Contact': (Create_capture_member_details.Field_S_02),
                }
                for cell in data_row:
                    column_name = self.sheet_community.cell(row=2, column=cell.column).value
                    print("Column name:", column_name)
                    if column_name in column_field_mapping:
                        field_name = column_field_mapping[column_name]
                        self.log.info("*****Parent organization field and column name is matched ***** ")
                        column_value = cell.value
                        locator = field_locators[field_name]
                        action_utils.wait_for_element((locator))
                        element = self.driver.find_element(*locator)
                        action_utils.wait_for_element((locator))
                        self.driver.execute_script("arguments[0].scrollIntoView();", element)
                        if element.tag_name == 'a':
                            if field_name == 'State':
                                element.click()
                                self.log.info("***** State field is clicked *****")
                                list_of_states = keen.select_options_in_list()
                                for states in list_of_states:
                                    if states.text == column_value:
                                        self.driver.execute_script("arguments[0].click();",states)
                                        break
                            if field_name == 'Status':
                                element.click()
                                self.log.info("***** Status field is clicked *****")
                                list_status = keen.select_options_in_list()
                                for status in list_status:
                                    if status.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", status)
                                        break
                        elif element.tag_name == 'span':
                            if field_name == 'Services':
                                list_services = keen.select_options_in_list()
                                for services in list_services:
                                    if services.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", services)
                                        break
                            if field_name == 'Organization type':
                                list_organization_type = keen.select_options_in_list()
                                for type in list_organization_type:
                                    if type.text == column_value:
                                        self.driver.execute_script("arguments[0].click();", type)
                                        break
                        elif element.tag_name == 'input':
                            if field_name == 'Parent_organization':
                                self.test_parent_organization(row_number)
                            if field_name == 'Main Contact':
                                print("Contcat")
                        else:
                            element.clear()
                            element.send_keys(column_value)
                keen.click_save_community_organization()
                success_message_creation = keen.success_message_of_records()
                assert success_message_creation.is_displayed(), "New creation toast message is not displayed"
                self.number.write_result_in_to_excel_sheet(row_number, "Community", "O")
                action_utils.wait_for_element((Create_capture_member_details.Add))
                keen.save_button_Add()
                action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
                assosciate_record_message = keen.success_message()
                assert assosciate_record_message.is_displayed(), "Associated toast message is not displayed"
        except Exception as ex:
            print(ex)
    ### TestDescreption:- Create a New Event and Assosicate to a Member
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Select a Keen Member
    ### Click on CFMD, Click on Events, Create a New Event and assosicate to member
    def test_events(self,row_number,row_practice,row_community):
        keen = Create_capture_member_details(self.driver)
        self.driver.execute_script("scroll(0, 150);")
        action_utils = ActionUtils(self.driver)
        self.test_select_member_to_associate_Cpature_Full_Member_details()
        action_utils.wait_for_element((Create_capture_member_details.select_event))
        keen.select_events()
        pop_up_event = keen.pop_up()
        assert pop_up_event.text == "Member's Event","Members event popup is not matched"
        action_utils.wait_for_element((Create_capture_member_details.new))
        keen.click_new()
        pop_of_new_outbound = keen.pop_up_of_New_Members()
        assert pop_of_new_outbound.text == "New Member at event","New Member at Event is not matched"
        verify_events = action_utils.record_verification(row_number, 'Pharmacies', 'pharmacy_created')
        if verify_events == 'YES':
            self.log.info("***** Event record is exists in Salesforce *****")
            existing_events_record = self.sheet_name.retrieve_value(row_number, 'T', 'Events',0)
            print("Campaign record names:", existing_events_record)
            action_utils.wait_for_element((Create_capture_member_details.search_pharmacy))
            keen.click_keen_event().send_keys(existing_events_record)
            self.log.info("***** Associating existing 'Event' record to member  *****")
            list_of_pharmacies = keen.select_existing_records()
            for pharmacies in list_of_pharmacies:
                if pharmacies.text == existing_events_record:
                    self.driver.execute_script("arguments[0].click();", pharmacies)
                    self.log.info("***** Existing record is selected *****")
                    break
            keen.save_button_Add()
            self.log.info("***** Associated existing 'HOSPITAL' record to member *****")
            action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
            success_message_of_records = keen.success_message()
            assert success_message_of_records.is_displayed(), "Record is not saved"
            return existing_events_record
        else:
            self.log.info("***** Creating the New event record *****")
            keen.click_keen_event().click()
            action_utils.wait_for_element((Create_capture_member_details.new_creation))
            keen.click_new_member()
            action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
            pop_up_new_event = keen.pop_up_Newcreation()
            assert pop_up_new_event.text == "New Keen Event","New Keen Event is not matched"
            print("Row number:", row_number)
            data_row = self.sheet_event[row_number]
            column_field_mapping = {
                'Event_Name': 'Event_Name',
                'Address Line 1': 'Address Line 1',
                'Phone': 'Phone',
                'City': 'City',
                'State': 'State', 'Zip code': 'Zipcode', 'Status': 'Status',
                'Start date': 'Start date',
                # 'Start Time': 'Start Time',
                'End date' : 'End date',
                # 'End Time' : 'End Time',
                'Report date' : 'Report date','Carriers submitted to' : 'Carriers submitted to',
                'Type': 'Type','Number_of_attendees' : 'Number_of_attendees','RegistrationCost': 'RegistrationCost','FoodCost' : 'FoodCost'

            }
            field_locators = {
                'Event_Name': (Create_capture_member_details.Field_01),
                'Address Line 1': (Create_capture_member_details.Field_D_01),
                'City': (Create_capture_member_details.Field_D_03),
                'Phone': (Create_capture_member_details.Field_D_05),
                'State': (Create_capture_member_details.Field_SD_01),
                'Zipcode': (Create_capture_member_details.Field_D_04),
                'Status': (Create_capture_member_details.status_event),
                'Start date': (Create_capture_member_details.start_date),
                # 'Start Time': (Create_capture_member_details.start_time),
                'End date' : (Create_capture_member_details.End_date),
                # 'End Time' : (Create_capture_member_details.End_time),
                'Report date' : (Create_capture_member_details.reportdate_events),
                'Carriers submitted to' : (Create_capture_member_details.carrires),
                'Type' : (Create_capture_member_details.type_avaliable),
                'Number_of_attendees' : (Create_capture_member_details.Field_02),
                'RegistrationCost': (Create_capture_member_details.Field_03),
                'FoodCost' : (Create_capture_member_details.Field_04)

            }
            event_name=None
            for cell in data_row:
                column_name = self.sheet_event.cell(row=2, column=cell.column).value
                if column_name in column_field_mapping:
                    field_name = column_field_mapping[column_name]
                    column_value = cell.value
                    self.log.info("***** Event field name and column name is matched  *****")
                    locator = field_locators[field_name]
                    action_utils.wait_for_element((locator))
                    element = self.driver.find_element(*locator)
                    action_utils.wait_for_element((locator))
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    if element.tag_name == 'a':
                        if field_name == 'State':
                            self.log.info("***** State field is present *****")
                            element.click()
                            self.log.info("***** State field is selected *****")
                            states = keen.select_options_in_list()
                            self.log.info("***** Options for state field *****")
                            for events_state in states:
                                if events_state.text == column_value:
                                    self.log.info("***** State option is displayed *****")
                                    self.driver.execute_script("arguments[0].click();", events_state)
                                    self.log.info("***** State is selected *****")
                                    break
                        if field_name == 'Status':
                            self.log.info("***** Status field is present *****")
                            element.click()
                            self.log.info("***** Status field is selected *****")
                            status = keen.select_options_in_list()
                            self.log.info("***** Options for status field *****")
                            for event_status in status:
                                if column_value in event_status.get_attribute('title'):
                                    self.driver.execute_script("arguments[0].click();", event_status)
                                    self.log.info("***** Required Option is selected for Status field *****")
                                    break
                    elif element.tag_name == 'div':
                        if field_name == 'Type':
                            self.log.info("***** Type field is present *****")
                            list_types = keen.select_options()
                            for types in list_types:
                                if types.get_attribute('title') == column_value:
                                    self.driver.execute_script("arguments[0].click();", types)
                                    self.log.info("***** Type option is selected *****")
                                    keen.click_type_choosen()
                                    break
                        if field_name == 'Carriers submitted to':
                            self.log.info("***** Carriers submitted to field is present *****")
                            list_types = keen.select_options()
                            for types in list_types:
                                if types.get_attribute('title') == column_value:
                                    self.driver.execute_script("arguments[0].click();", types)
                                    keen.click_type_choosen()
                                    break
                            keen.click_carrier_choosen()
                    else:
                        element.clear()
                        self.log.info("***** Entering the test data to the respected fields *****")
                        element.send_keys(column_value)
                if column_name == "Event_Name":
                    event_name = cell.value
            self.test_practice_event(row_practice)
            self.test_event_community_organization(row_community)
            keen.save_button_creation()
            created_record_message = keen.success_message_of_records()
            assert created_record_message.is_displayed(),"New creation toast message is not displayed"
            self.sheet_name.write_result_in_to_excel_sheet(row_number, "Events", "T")
            self.log.info("****New Event record was Created********")
            action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
            pop_of_new_event = keen.pop_up_of_New_Members()
            assert pop_of_new_event.text == "New Member at event","New Member at event popup is not displayed"
            keen.save_button_Add()
            self.log.info("**** New Event is Assosicate to a Member ****")
            assosciate_record_message = keen.success_message()
            assert assosciate_record_message.is_displayed(),"Associated record toast message is not displayed"
            return event_name
    def test_validation_events(self,r):
        keen = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action_utils=ActionUtils(self.driver)
        action = ActionChains(self.driver)
        Name_Event = readdata_events.readdata(r, 1)
        Address_event = readdata_events.readdata(r, 2)
        start_date_event = readdata_events.readdata(r, 3)
        start_time_event = readdata_events.readdata(r, 4)
        end_date_event = readdata_events.readdata(r, 5)
        end_time_event = readdata_events.readdata(r, 6)
        city_event = readdata_events.readdata(r, 7)
        state_event = readdata_events.readdata(r, 8)
        zipcode_event = readdata_events.readdata(r, 9)
        phone_event = readdata_events.readdata(r, 10)
        report_date_event = readdata_events.readdata(r, 11)
        status_evnet = readdata_events.readdata(r, 12)
        Carriers_submitted_to_event = readdata_events.readdata(r, 13)
        type_event = readdata_events.readdata(r, 14)
        PracticeDirectory=readdata_events.readdata(r,15)
        CommunityOrganization= readdata_events.readdata(r, 16)
        Event_cost= readdata_events.readdata(r, 18)
        Food_cost= readdata_events.readdata(r, 19)
        count= readdata_events.readdata(r, 17)
        self.log.info("****Entered the data in to Event fileds********")
        self.log.info("**** Validation is started****")
        list_of_selected_pharmacies = keen.validation_of_records()
        for i in list_of_selected_pharmacies:
            if i.text == Name_Event:
                action.move_to_element(i).click().perform()
                break
            self.log.info("**** Selected the validating record****")
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            # all_guid = driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_record()
                    time.sleep(5)
                    if keen.Validation_event_name() == Name_Event:
                        print(keen.Validation_event_name)
                        print("Test Pass")
                    else:
                        print("Test fail")
                    if keen.Validation_start_Date_Timeevent() == start_date_event+ ', '+start_date_event:
                        print("Test Pass")
                    else:
                        print("Test Fail")
                    if keen.Validation_End_Date_Timeevent() == (end_date_event+ ', ' +end_time_event):
                        print("Test Pass")
                    else:
                        print("Test fail")
                    if keen.Validation_Adress_event()== Address_event:
                        print("Test Pass")
                    else:
                        print("Test Fail")
                    if keen.Validation_type_choosen() == type_event:
                        print("Test Pass")
                    else:
                        print("Test Fail")
                    if keen.Validation_state_event() == state_event:
                        print("Test Pass")
                    else:
                        print("Test Fail")
                    if keen.Validation_Number_Attendees() == count:
                        assert True
                    else:
                        assert False
                    if keen.Validation_city_event() == city_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_zipcode_events() == zipcode_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_RegistrationCost() == Event_cost:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Phone_events() == phone_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_food_Cost_Event() == Food_cost:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Community_Organization() == CommunityOrganization:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Report_date_events() == report_date_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_PracticeDirectory()  == PracticeDirectory:
                        assert True
                    else:
                        assert False
                    if keen.Validation_status_events() == status_evnet:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Carriers_Submitted() == Carriers_submitted_to_event:
                        assert True
                    else:
                        assert False
                    time.sleep(5)
                    if guid == guid:
                        self.driver.close()
                        time.sleep(5)
                        if guid != parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            keen.close()
                            break
                    self.log.info("**** Validation is com[pleted *****")
                    keen.click_CommunityOrganization_Tab()
                    list_records=keen.select_AssosicateRecords()
                    for i in list_records:
                        if i.text == CommunityOrganization:
                            action.move_to_element(i).click().perform()
                            break
                    self.driver.execute_script("scroll(0, 400);")
                    list_events=keen.Event_Organization()
                    for i in list_events:
                        if i.text == Name_Event:
                            assert True
                        else:
                            assert False
                    keen.close()

    ### TestDescreption:- Create a New Event and Assosicate to a Member
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Select a Keen Member
    ### Click on CFMD, Click on Events, Create a New Event and assosicate to member
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Editing the Assosicate Events")
    @pytest.mark.order(20)
    def test_edit_Events(self):
        keen = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        Name_Event = readdata_events.readdata(3, 1)
        Address_event = readdata_events.readdata(4, 2)
        start_date_event = readdata_events.readdata(4, 3)
        start_time_event = readdata_events.readdata(4, 4)
        end_date_event = readdata_events.readdata(4, 5)
        end_time_event = readdata_events.readdata(4, 6)
        city_event = readdata_events.readdata(4, 7)
        state_event = readdata_events.readdata(4, 8)
        zipcode_event = readdata_events.readdata(4, 9)
        phone_event = readdata_events.readdata(4, 10)
        report_date_event = readdata_events.readdata(4, 11)
        status_evnet = readdata_events.readdata(4, 12)
        Carriers_submitted_to_event = readdata_events.readdata(4, 13)
        type_event = readdata_events.readdata(4, 14)
        PracticeDirectory =readdata_events.readdata(4, 15)
        CommunityOrganization = readdata_events.readdata(4, 16)
        Event_cost = readdata_events.readdata(4, 18)
        Food_cost = readdata_events.readdata(4, 19)
        count = readdata_events.readdata(4, 17)
        self.driver.execute_script("scroll(0, 150);")
        self.log.info("****Select Events for Creation********")
        self.test_select_member_to_associate_Cpature_Full_Member_details()
        keen.select_events()
        pop_up_outbound_organization = keen.pop_up()
        if pop_up_outbound_organization.text == "Member's Event":
            assert True
        else:
            assert False
        time.sleep(10)
        saved_events = self.keen.validation_of_records()
        for i in saved_events:
            if i.text == Name_Event:
                action.move_to_element(i).click().perform()

        log.info("****Entering the Data in to Events fields********")
        keen.enter_event_name(Name_Event)
        keen.enter_NewAddress_event(Address_event)
        keen.enter_Newstart_date_event(start_date_event)
        keen.enter_NewEnd_date_event(end_date_event)
        keen.enter_Newcity_event(city_event)
        keen.enter_Newstart_time_event(start_time_event)
        keen.enter_End_time_event(end_time_event)
        keen.click_Newstate_event()
        list_of_states = keen.select_options_in_list()
        for i in list_of_states:
            if i.text == state_event:
                i.click()
                break
        list_types = keen.select_optionsType()
        for i in list_types:
            if i.text == type_event:
                action.move_to_element(i).click().perform()
                keen.click_type_choosen()
                break
        keen.enter_NewNumber_of_Attendees_Event(count)
        keen.enter_NewRegistartionCost_Event(Event_cost)
        keen.enter_NewFoodCost_Event(Food_cost)
        keen.enter_NewCommunityOrganization(CommunityOrganization)
        select_Organization = keen.select_records()
        for i in select_Organization:
            if i.text == CommunityOrganization:
                action.move_to_element(i).click().perform()
                break
        keen.enter_NewPracticeDirectory_Event(PracticeDirectory)
        select_Practice=keen.select_records()
        for i in select_Practice:
            if i.text == PracticeDirectory:
                action.move_to_element(i).click().perform()
                break
        keen.enter_Newzipcode_events(zipcode_event)
        keen.enter_NewPhone_events(phone_event)
        keen.enter_NewReport_date_events(report_date_event)
        keen.click_status()
        list_status=keen.select_options_in_list()
        for i in list_status:
            if i.text == status_evnet:
                action.move_to_element(i).click().perform()
                break
        keen.New_Report_as_marketing_event()
        keen.New_Submitted_to_carrier()
        list_carriers=keen.select_optionsType()
        for i in list_carriers:
            if i.text == Carriers_submitted_to_event:
                action.move_to_element(i).click().perform()
                break
        keen.click_carrier_choosen()
        keen.click_Recurring_event()
        log.info("****Entered the data in to Event fileds********")
        keen.save_button_creation()
        log.info("****New Event was Created********")
        pop_of_new_outbound = keen.pop_up_of_New_Members()
        if pop_of_new_outbound.text == "New Member at event":
            assert True
        else:
            assert False
        keen.save_button_Add()
        log.info("****New Event is Assosicate to a Member****")
        assosciate_record_message = self.keen.success_message()
        if assosciate_record_message.is_displayed():
            assert True
        else:
            assert False
        list_of_selected_pharmacies = self.keen.validation_of_records()
        for i in list_of_selected_pharmacies:
            if i.text == Name_Event:
                action.move_to_element(i).click().perform()
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid == guid:
                self.driver.close()
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                keen.click_record()
                try:
                    if keen.Validation_event_name() == Name_Event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_start_Date_Timeevent() == start_date_event+' '+start_date_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_End_Date_Timeevent() == end_date_event+' '+end_time_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Adress_event()== Address_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_type_choosen() == type_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_state_event() == state_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Number_Attendees() == count:
                        assert True
                    else:
                        assert False
                    if keen.Validation_city_event() == city_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_zipcode_events() == zipcode_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_RegistrationCost() == Event_cost:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Phone_events() == phone_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_food_Cost_Event() == Food_cost:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Community_Organization() == CommunityOrganization:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Report_date_events() == report_date_event:
                        assert True
                    else:
                        assert False
                    if keen.Validation_PracticeDirectory()  == PracticeDirectory:
                        assert True
                    else:
                        assert False
                    if keen.Validation_status_events() == status_evnet:
                        assert True
                    else:
                        assert False
                    if keen.Validation_Carriers_Submitted() == Carriers_submitted_to_event:
                        assert True
                    else:
                        assert False
                    # if keen.Validation_Recurring_event():
                except Exception as ex:
                    print(ex)
                try:
                    keen.click_CommunityOrganization_Tab()
                    list_records=keen.select_AssosicateRecords()
                    for i in list_records:
                        if i.text == CommunityOrganization:
                            action.move_to_element(i).click().perform()
                            break
                    self.driver.execute_script("scroll(0, 400);")
                    list_events=keen.Event_Organization()
                    for i in list_events:
                        if i.text == Name_Event:
                            assert True
                        else:
                            assert False
                except Exception as ex:
                    print(ex)
            try:
                keen.PracticeDirectory()
                list_practices=keen.list_PracticeDirectory()
                for i in list_practices:
                    if i.text == PracticeDirectory:
                        action.move_to_element(i).click().perform()
                        break
                self.driver.execute_script("scroll(0, 400);")
                keen.Events_IN_Practice()
                list_records=keen.Records_Events()
                for i in list_records:
                    if i.text == Name_Event:
                        assert True
                    else:
                        assert False
            except Exception as ex:
                print(ex)

    ### TestDescreption:- Assosicate Advisor to a Member
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Select a Keen Member
    ### Click on Keen advisor for a Member, select advisor and Associate a advisor to member
    @allure.description("Associate a Advisor to a Member")
    def test_Associate_Advisor_to_a_Member(self):
        try:
            keen=Create_capture_member_details(self.driver)
            action=ActionChains(self.driver)
            action_utils=ActionUtils(self.driver)
            keen_login = Keen_login(self.driver)
            keen_login.keen_leads_members()
            time.sleep(10)
            keen.select_member()
            time.sleep(15)
            self.driver.execute_script("scroll(0, 600);")
            time.sleep(20)
            # # action_utils.wait_for_element(By.XPATH,"(//div[@class='slds-media__body slds-align-middle'])[4]")
            keen.click_New_Keen_advisor_for_a_member()
            time.sleep(5)
            popup=keen.pop_up_of_New_Members()
            if popup.text == "New Keen advisor for a member":
                assert True
            else:
                assert False
            keen.Search_advisor("Innominds")
            time.sleep(5)
            list_advisors=keen.Select_advisor()
            for i in list_advisors:
                if i.text == "Innominds Devteam":
                    action.move_to_element(i).click().perform()
                    break
            keen.save_button_Add()
            time.sleep(3)
            success_message=keen.success_message_of_records()
            toast_message=success_message.text
            print(toast_message)
            if success_message.is_displayed():
                assert True
            else:
                assert False
            match = re.search(r'"(\d+)"', toast_message)
            if match:
                record_number = match.group(1)
                print(record_number)
            else:
                print("Record number not found")
            list_lead=keen.Keen_Advisor_for_a_Lead()
            for i in list_lead:
                print(i.text)
                if i.text == record_number:
                    assert True
                else:
                    assert False
        except Exception as ex:
            print(ex)

    ### TestDescreption:- Assosicate a files to a Member
    ### TestCase Steps:- Login to SFDC,Click on Keen leads and Members,Select a Keen Member
    ### Click on Files, Associate a File to a Member
    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.order()
    def test_AddFiles(self,file,keen_member):
        ### login in another window

        try:
            keen = Create_capture_member_details(self.driver)
            action = ActionChains(self.driver)
            action_utils = ActionUtils(self.driver)
            keen_login = Keen_login(self.driver)
            log=logger_utils.get_logger()
            keen_login.keen_leads_members()
            action_utils.wait_for_elements((Create_capture_member_details.Member))
            member=keen.select_member()
            for i in member:
                if i.text == keen_member:
                    action.move_to_element(i).click().perform()
                    break
            time.sleep(2)
            self.driver.execute_script("scroll(0, 200);")
            action_utils.wait_for_element((Create_capture_member_details.add_files))
            keen.Associate_Files()
            action_utils.wait_for_element((Create_capture_member_details.popup_file))
            popup=keen.Popup_title_files()
            print(popup)
            keen.Upload_files()
            log.info("***** Search file to upload *****")
            autoit.win_active("Open")
            time.sleep(5)
            log.info("***** Search file to upload *****")
            autoit.control_set_text('Open','Edit1',file)
            time.sleep(5)
            log.info("***** Select file to upload *****")
            autoit.control_click("Open", "Button1")
            upload_files = keen.pop_up_Newcreation()
            assert upload_files.is_displayed(),"upload popup is not displayed"
            action_utils.wait_for_element((Create_capture_member_details.done))
            keen.click_done()
            action_utils.wait_for_element((Create_capture_member_details.view_all))
            keen.click_view_all()
            action_utils.wait_for_element((Create_capture_member_details.verify_file))
            associate_to_member=keen.Validation_File()
            if associate_to_member in file:
                print("File is uploaded")
            else:
                print("File is not uploaded")
        except Exception as ex:
             print(ex)



    def test_ana(self):
        self.test_select_member_to_associate_Cpature_Full_Member_details()










