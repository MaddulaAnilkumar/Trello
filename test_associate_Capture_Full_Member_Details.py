import allure
import pytest
from Pages.Keen_Login import Keen_login
import time
from Pages.Keen_Associate_capture_full_member_details import Associate_Capture_full_Member_details
from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
from utilities.XLUtilities import Excel_data
from utilities import logger_utils
from utilities.action_utils import ActionUtils
path= "../test_data/Keen_Testdata.xlsx"
readdata_plans=Excel_data(path ,"Plans_associate")
readdata_caregiver=Excel_data(path,"Caregiver")
from selenium.webdriver import ActionChains
@allure.description(" Associate  Capture Full Member Details to a Member")
@allure.severity(allure.severity_level.CRITICAL)
class Test_add_Member_details():
    def __init__(self,driver):
        self.driver=driver
    ##Test Case Description: Assosciate A New Plan to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click on Plans
    ##Assosicate Plan to Member
    @pytest.mark.order(1)
    def test_add_plans(self):
        try:
            for rows in range(2,3):
                carrier_member_ID = readdata_plans.readdata(rows, 1)
                HRA_Completed_Date = readdata_plans.readdata(rows, 2)
                Effective_date = readdata_plans.readdata(rows, 3)
                Enrollment_confirmation_number = readdata_plans.readdata(rows, 4)
                Plan_End_date = readdata_plans.readdata(rows, 5)
                Enrollnment_type = readdata_plans.readdata(rows, 6)
                App_subbmission_date = readdata_plans.readdata(rows, 7)
                App_approval_date = readdata_plans.readdata(rows, 8)
                Disenrollnment_date = readdata_plans.readdata(rows, 9)
                Beneficary=readdata_plans.readdata(rows,11)
                Plans = readdata_plans.readdata(rows, 10)
                keen_associate = Associate_Capture_full_Member_details(self.driver)
                keen=Create_capture_member_details(self.driver)
                action = ActionChains(self.driver)
                action_utils=ActionUtils(self.driver)
                log = logger_utils.get_logger()
                log.info("***** Select Member to associate a plan ******")
                list_lead=keen.select_member()
                for lead in list_lead:
                    if lead.text == "Test Pant":
                        action.move_to_element(lead).click().perform()
                action_utils.wait_for_element((Create_capture_member_details.Member_details))
                keen.Capture_Full_Member()
                log.info("***** Associate a Plan to a Member ******")
                keen.click_plans()
                pop_up_of_members_plans = keen.pop_up()
                assert pop_up_of_members_plans.text == "Member Plan's List" , "Member Plan's List is not matched"
                present_count = keen_associate.count_records()
                for count in present_count:
                    print(len(count))
                keen.new()
                action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
                pop_up_of_New_Membersplans = keen.pop_up_of_New_Members().text
                assert pop_up_of_New_Membersplans == "New Member's plan", "New Member's Plans Popup is not matched"
                keen_associate.search_plan_detail("Test")
                list_of_plans = keen_associate.select_existing_records()
                for plans in list_of_plans:
                    if plans.text == "Test Plan":
                        action.move_to_element(plans).click().perform()
                        break
                time.sleep(10)
                keen.Enrolled_by_Keen()
                keen.Carrier_member_ID(carrier_member_ID)
                keen.hra_completd().click()
                keen.HRA_completed_date(HRA_Completed_Date)
                keen.Effective_date__c(Effective_date)
                keen.Enrollment_confirmation_number(Enrollment_confirmation_number)
                keen.plan_end_date(Plan_End_date)
                keen.enrollment_type()
                enrollment_list = keen_associate.select_enrollment_type()
                for enroll in enrollment_list:
                    print(enroll.text)
                    if enroll.text == Enrollnment_type:
                        enroll.click()
                        break
                keen.App_approval_date(App_approval_date)
                keen.App_submission_date(App_subbmission_date)
                keen.Disenrollment_date(Disenrollnment_date)
                keen.save_button_Add()
                log.info("***** Plans is added *****")

                success_Message_of_Plans = keen.success_message()
                if success_Message_of_Plans.is_displayed():
                    print("Test pass")
                else:
                    print("Test Fail")
                log.info("***** Plans was added for keen leads and members *****")
                keen.close()

                time.sleep(5)
                log.info("***** Validation of selected plans is starting *****")
                keen.click_plans()
                selected_plan = keen.validation_of_records()
                for associateplans in selected_plan:
                    print(associateplans.text)
                    if associateplans.text == "Test Plan Three":
                        assert True
                    else:
                        assert False

                verify_plan_id=keen.validation_plan_name()
                if verify_plan_id == "Test Plan Three":
                    assert True
                else:
                    assert False
                verify_id=keen_associate.validation_Carrier_member_ID()
                if verify_id == carrier_member_ID:
                    assert True
                else:
                    assert False
                verfiy_hradate=keen_associate.validation_HRA_completed()
                if verfiy_hradate == HRA_Completed_Date:
                    assert True
                else:
                    assert False
                verfiy_effective_date=keen_associate.valiadtion_Effective_date()
                if verfiy_effective_date == Effective_date:
                    assert True
                else:
                    assert False
                verfiy_enrollnumber=keen_associate.validation_Enrollment_confirmation_number()
                if verfiy_enrollnumber == Enrollment_confirmation_number:
                    assert True
                else:
                    assert False
                verify_plansenddate=keen_associate.validation_Plan_enddate()
                if verify_plansenddate == Plan_End_date:
                    assert True
                else:
                    assert False
                verify_enrollmentype=keen_associate.validation_Enrollment_type()
                if verify_enrollmentype == Enrollnment_type:
                    assert True
                else:
                    assert False
                verify_app_submissiondate=keen_associate.validation_App_submissiondate()
                if verify_app_submissiondate == App_subbmission_date:
                    assert True
                else:
                    assert False
                verify_app_approvaldate=keen_associate.validation_App_approvaldate()
                if verify_app_approvaldate == App_approval_date:
                    assert True
                else:
                    assert False
                verify_disenrollment_date=keen_associate.validation_Disenrollmentdate()
                if verify_disenrollment_date == Disenrollnment_date:
                    assert True
                else:
                    assert False
                keen.close()
                log.info("validation is completed")
        except Exception as ex:
            print(ex)

    ##Test Case Description: Editing A associated plan to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click on Plans
    ##Edit the plans
    @pytest.mark.order(2)
    def test_edit_plans(self):
        for rows in range(3,4):
            carrier_member_ID = readdata_plans.readdata(rows, 1)
            HRA_Completed_Date = readdata_plans.readdata(rows, 2)
            Effective_date = readdata_plans.readdata(rows, 3)
            Enrollment_confirmation_number = readdata_plans.readdata(rows, 4)
            Plan_End_date = readdata_plans.readdata(rows, 5)
            Enrollnment_type = readdata_plans.readdata(rows, 6)
            App_subbmission_date = readdata_plans.readdata(rows, 7)
            App_approval_date = readdata_plans.readdata(rows, 8)
            Disenrollnment_date = readdata_plans.readdata(rows, 9)
            Plans = readdata_plans.readdata(rows, 10)
            keen_associate = Associate_Capture_full_Member_details(self.driver)
            keen=Create_capture_member_details(self.driver)
            action = ActionChains(self.driver)
            log = logger_utils.get_logger()
            log.info("***** Editing a Associated Plan to a Select Member ******")
            keen_login = Keen_login(self.driver)
            keen_login.keen_leads_members()
            time.sleep(6)
            keen.select_member()
            time.sleep(5)
            keen.Capture_Full_Member()
            keen.click_plans()
            pop_up_of_members_plans = self.keen.pop_up()
            if pop_up_of_members_plans.text == "Member Plan's List":
                assert True
            else:
                assert False
            list_plans=keen_associate.list_plans()
            for i in list_plans:
                print(i.text)
                if i.text == "Test Plan ":
                    print("Test pass")
                    i.click()
                    break
            time.sleep(10)
            keen_associate.list_plans()
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            # all_guid = driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen_associate.edit_plan()
                    keen_associate.search_plan_detail("Test")
                    list_of_plans = keen_associate.select_existing_records()
                    for i in list_of_plans:
                        if i.text == Plans:
                            i.click()
                            break
                    time.sleep(10)
                    keen.Enrolled_by_Keen()
                    keen.Carrier_member_ID(carrier_member_ID)
                    keen.hra_completd()
                    keen.HRA_completed_date(HRA_Completed_Date)
                    keen.Effective_date__c(Effective_date)
                    keen.Enrollment_confirmation_number(Enrollment_confirmation_number)

                    keen.plan_end_date(Plan_End_date)
                    keen.enrollment_type()
                    enrollment_list = keen_associate.select_enrollment_type()
                    for i in enrollment_list:
                        print(i.text)
                        if i.text == Enrollnment_type:
                            i.click()
                            break
                    keen.App_approval_date(App_approval_date)

                    keen.App_submission_date(App_subbmission_date)

                    keen.Disenrollment_date(Disenrollnment_date)
                    keen.save_button_Add()

                    plan=keen_associate.validation_plan()
                    if plan.text == Plans:
                        assert True
                    else:
                        assert False
                    verify_Carrier_memberID=keen_associate.validation_Carrier_member_ID()
                    if verify_Carrier_memberID.text == carrier_member_ID:
                        assert True
                    else:
                        assert False
                    verify_HRA_completed_Effectivedate=keen_associate.validation_HRA_completed_date()
                    if verify_HRA_completed_Effectivedate.text == HRA_Completed_Date:
                        assert True
                    else:
                        assert False
                    verify_Enrollment_confirmationnumber=keen_associate.validation_Enrollment_confirmation_number()
                    if verify_Enrollment_confirmationnumber.text == Enrollment_confirmation_number:
                        assert True
                    else:
                        assert False

                    verify_Plan_enddate=keen_associate.validation_Plan_enddate()
                    if verify_Plan_enddate.text == Plan_End_date:
                        assert True
                    else:
                        assert False
                    verify_Enrollment_type=keen_associate.validation_Enrollment_type()
                    if verify_Enrollment_type.text == Enrollnment_type:
                        assert True
                    else:
                        assert False
                    verify_App_submission_date=keen_associate.validation_App_submissiondate()
                    if verify_App_submission_date.text == App_subbmission_date:
                        assert True
                    else:
                        assert False
                    verify_App_approvaldate=keen_associate.validation_App_approvaldate()
                    if verify_App_approvaldate.text == App_subbmission_date:
                        assert True
                    else:
                        assert False
                    verify_Disenrollment_date=keen_associate.validation_Disenrollmentdate()
                    if verify_Disenrollment_date.text == Disenrollnment_date:
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                        if guid !=guid:
                            self.driver.switch_to.window(parent_guid)
                            self.driver.close()
                            selected_plan = keen.validation_of_records()
                            for i in selected_plan:
                                print(i.text)
                                if i.text == Plans:
                                    assert True
                                else:
                                    assert False
                            keen.close()

    ##Test Case Description: Assosciate A New Caregiver to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click on Related Persons
    ##Assosicate Caregiver to Member
    def test_add_Related_persons(self):
        keen_associate=Associate_Capture_full_Member_details(self.driver)
        keen=Create_capture_member_details(self.driver)
        log=logger_utils.get_logger()
        action=ActionChains(self.driver)
        action_utils=ActionUtils(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen_lead=keen.select_member()
        for Lead in keen_lead:
            if Lead.text == "Anil TestAnil":
                action.move_to_element(Lead).click().perform()
                break
        action_utils.wait_for_element((Associate_Capture_full_Member_details.Member_Details))
        keen.Capture_Full_Member()
        log.info("***** Associate Caregiver record to Member *****")
        action_utils.wait_for_element((Associate_Capture_full_Member_details.related_persons))
        time.sleep(5)
        keen_associate.click_related_persons()
        pop_up_of_Related_persons=keen.pop_up().text
        assert pop_up_of_Related_persons == "Related Person's List" , "Popup of Related Persons is not matched"
        keen.click_new()
        pop_up_of_new_member_related_person=keen.popup_related_persons()
        if pop_up_of_new_member_related_person.text == "New Related Person":
            assert True
        else:
            assert False
        action_utils.wait_for_element((Associate_Capture_full_Member_details.keen_leads_member))
        keen_associate.search_caregiver_person().click()

    ##Test Case Description: Associate Caregiver to a member
    def test_assciate_relatedperson_caregiver(self):
        try:
            keen_associate = Associate_Capture_full_Member_details(self.driver)
            keen = Create_capture_member_details(self.driver)
            log = logger_utils.get_logger()
            action = ActionChains(self.driver)
            action_utils = ActionUtils(self.driver)
            action_utils.wait_for_element((Associate_Capture_full_Member_details.relation))
            time.sleep(10)
            keen_associate.click_realtion()
            select_realtion = keen_associate.Select_record()
            for i in select_realtion:
                if i.text == "Friend":
                    action.move_to_element(i).click().perform()
                    break
            action_utils.wait_for_element((Associate_Capture_full_Member_details.power_of_attorney_yes))
            keen_associate.click_power_of_attorney_yes()
            enable = keen_associate.check_caregiver_member()
            print(enable.is_enabled())
            keen_associate.click_save_related_person()
            action_utils.wait_for_element((Associate_Capture_full_Member_details.related_person_save_message))
            success_message_of_caregivers = keen_associate.success_message_related_persons()
            print(success_message_of_caregivers)
            keen.close()
        except Exception as ex:
            print(ex)

    ##Test Case Description: Associate Keen lead to a member
    def test_associate_realtedpersontomember(self):
        keen_associate = Associate_Capture_full_Member_details(self.driver)
        keen = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        action_utils = ActionUtils(self.driver)
        keen_associate.Select_SOA_Member()
        log.info("***** Select realtion *****")
        keen_associate.click_realtion()
        select_realtion=keen_associate.Select_record()
        for relation in select_realtion:
            if relation.text == "Friend":
                action.move_to_element(relation).click().perform()
                break
        log.info("***** Realtion is selected *****")
        keen_associate.click_caregiver_yes()
        keen_associate.click_power_of_attorney_yes()
        enable=keen_associate.check_caregiver_person()
        print(enable.is_enabled())
        action_utils.wait_for_element((Associate_Capture_full_Member_details.save_related_person))
        keen_associate.click_save_related_person()
        log.info("***** Keen Lead is associated to a member *****")
        action_utils.wait_for_element((Associate_Capture_full_Member_details.related_person_save_message))
        success_message_of_caregivers = keen_associate.success_message_related_persons()
        print(success_message_of_caregivers)
        keen.close()

    ##Test Case Description: validating the  Keen lead to a member
    def test_validation_relatedpersons(self,r):
        keen_associate = Associate_Capture_full_Member_details(self.driver)
        keen = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        action_utils = ActionUtils(self.driver)
        keen_login = Keen_login(self.driver)
        caregiver_name=readdata_caregiver.readdata(r,1)
        action_utils.wait_for_element((Associate_Capture_full_Member_details.related_persons))
        keen_associate.click_related_persons()
        log.info("***** Validating the associated record to member *****")
        selected_relatedpersons_record=keen.validation_of_records()
        for associated_record in selected_relatedpersons_record:
            if associated_record.text == caregiver_name:
                action.move_to_element(associated_record).click().perform()
                log.info("***** Selected validation record *****")
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid == guid:
                self.driver.switch_to.window(guid)
                try:
                    poa=keen_associate.check_poa().is_selected()
                    if poa:
                        assert True
                    else:
                        assert False
                    caregiver=keen_associate.check_caregiver().is_selected()
                    if caregiver:
                        assert True
                    else:
                        assert False

                except Exception as ex:
                    print(ex)
                self.driver.close()
                if guid != guid:
                    self.driver.switch_to.window(parent_guid)
                    keen.close()
                    log.info("***** Validation is completed *****")

    ##Test Case Description: Assosciate A New Caregiver to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click on Related Persons
    ##Edit related member to Member
    @pytest.mark.order(4)
    @allure.description("Associate and Delete Caregivers record to a member")
    @pytest.mark.skip
    def test_edit_Related_Persons(self):
        keen_associate = Associate_Capture_full_Member_details(self.driver)
        keen = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        action_utils = ActionUtils(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen_lead = keen.select_member()
        for lead in keen_lead:
            if lead.text == "TestAnil":
                action.move_to_element(lead).click().perform()
                break
        action_utils.wait_for_element((Associate_Capture_full_Member_details.Member_Details))
        keen.Capture_Full_Member()
        log.info("***** Associate Caregiver record to Member *****")
        action_utils.wait_for_element((Associate_Capture_full_Member_details.related_persons))
        time.sleep(5)
        keen_associate.click_related_persons()
        pop_up_of_Related_persons = keen.pop_up().text
        assert pop_up_of_Related_persons == "Related Person's List", "Popup of Related Persons is not matched"
        present_count = keen_associate.count_records()
        count = len(present_count)
        print(count)
        associated_realtaedrecord=keen.validation_of_records()
        for i in associated_realtaedrecord:
            if i.text == "Test CG":
                action.move_to_element(i).click().perform()
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                keen_associate.click_delete()
                log.info("***** Delete the associated record ******")
                keen_associate.click_delete_button()
                pop_delete = keen_associate.success_message_delete()
                print(pop_delete.text)
                if pop_delete.is_displayed():
                    assert True
                else:
                    assert False
                log.info("***** Associated record is Deleted ******")
                if guid == guid:
                    self.driver.close()
                    if guid != parent_guid:
                        self.driver.switch_to.window(parent_guid)
                        log.info("***** Validating the Associated record is delete ******")
                        selected_caregiver_record = keen.validation_of_records()
                        for i in selected_caregiver_record:
                            assert  i.text != "Test CG", "Record is not  Deleted"
                        keen.close()
                        log.info("***** Associated record is deleted ******")
                        break

    ##Test Case Description: Assosciate a Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ##Assosicate Practices to Member
    @pytest.mark.order(5)
    @allure.description("Associate Practices to member")
    def test_add_practices(self):
        keen_associate=Associate_Capture_full_Member_details(self.driver)
        keen=Create_capture_member_details(self.driver)
        log=logger_utils.get_logger()
        action=ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        try:
            log.info("***** Selcet practices to assoscioate ******")
            keen.click_practices()
            practices_pop_up = keen.pop_up()
            if practices_pop_up.text == "Member's practices":
                assert True
            else:
                assert False
            keen.new()
            New_Members_practice_pop_up = keen.pop_up_new_members()
            if New_Members_practice_pop_up.text == "New Member's practice":
                assert True
            else:
                assert False
            log.info("***** Select practice record to associate ******")
            keen_associate.practice_directory().send_keys("Test Practice")
            select_practices = keen_associate.select_existing_records()
            for i in select_practices:
                if i.text == "Test Practice":
                    i.click()
                    break
            keen.save_button_Add()
            log.info("*****  practice record is associated to member ******")
            time.sleep(5)
            success_practices = keen.success_message()
            if success_practices.is_displayed():
                print("Test pass")
            else:
                print("Test Fail")
            keen.close()
            time.sleep(4)
            log.info("***** Validating the Associated record ******")
            keen.click_practices()
            selected_practices = keen_associate.select_existing_records()
            for i in selected_practices:
                if i.text == "Test Practice":
                    assert True
                    log.info("***** Practices record Associated to member ******")
                else:
                    assert False
            log.info("***** Validating the Associated record ******")
            keen.close()
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(6)
    @allure.description("Associate and Delete Practices to member")
    def test_edit_practices(self):
        keen_associate = Associate_Capture_full_Member_details(self.driver)
        keen = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)

        try:
            log.info("***** Click Practices to edit the record ******")
            keen.click_practices()
            practices_pop_up = keen.pop_up()
            if practices_pop_up.text == "Member's practices":
                assert True
            else:
                assert False
            present_count = keen_associate.count_records()
            count = len(present_count)
            print(count)
            New_Members_practice_pop_up = keen.pop_up_new_members()
            if New_Members_practice_pop_up.text == "New Member's practice":
                assert True
            else:
                assert False

            keen_associate.practice_directory().send_keys("Test")
            select_practices = keen_associate.select_existing_records()
            for i in select_practices:
                if i.text == "Test Practice":
                    i.click()
                    break
            keen.save_button_Add()
            time.sleep(5)
            success_practices = keen.success_message()
            if success_practices.is_displayed():
                print("Test pass")
            else:
                print("Test Fail")
            added_count = keen_associate.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            deleted_practice_record = keen.validation_of_records()
            for i in deleted_practice_record:
                if i.text == "Test Practice":
                    i.click()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    log.info("***** Associated Practice record is deleting ******")
                    keen_associate.click_delete()
                    keen_associate.click_delete_button()
                    log.info("***** Associated Practice record is deleted ******")
                    pop_delete = keen_associate.success_message_delete()
                    print(pop_delete.text)
                    if pop_delete.is_displayed():
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                    if guid != guid:
                        self.driver.switch_to.window(parent_guid)
                        log.info("***** Validating the delected record ******")
                        selected_practice_record = keen.validation_of_records()
                        for i in selected_practice_record:
                            if i.text != "Test Practice":
                                assert True
                            else:
                                assert False
                        keen.close()
                        log.info("***** Associated record is delected ******")
                        break
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(7)
    @allure.description("Associate  Medications to member")
    def test_add_Medications(self):
        keen_associate = Associate_Capture_full_Member_details(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        keen=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        try:
            log.info("*****Select Medications option  to associate medication records to member *****")
            keen.Medication_option()
            time.sleep(10)
            pop_up_of_Members_Medications = keen.pop_up()
            if pop_up_of_Members_Medications.text == "Member's Medications":
                assert True
            else:
                assert False
            keen.new()
            time.sleep(10)
            pop_up_of_new_medication = keen.pop_up_new_members()
            if pop_up_of_new_medication.text == "New Member Medication":
                assert True
            else:
                assert False
            log.info("***** Search Medication record to associate *****")
            keen.medication_search().send_keys("Test Medicine")
            time.sleep(10)
            select_medicine = keen_create.select_options_in_list()
            for i in select_medicine:
                log.info("***** Select Medication record to associate *****")
                if i.text == "Test Medicine":
                    i.click()
                    break
            log.info("***** Selected Medication record to associate *****")
            keen.Quantity_per_fill("12")
            keen.Refill_frequency().click()
            select_month = keen.select_frequency()
            for month in select_month:
                print(month.text)
                if month.text == "Every month":
                    month.click()
                    break
            keen_associate.save()
            log.info("*****  Medication record to associated to member *****")
            success_Message_of_Medication = keen.success_message()
            if success_Message_of_Medication.is_displayed():
                print("Test pass")
            else:
                print("Test Fail")
            keen.close()

            log.info("***** Validating the associated record *****")
            keen.Medication_option()
            selected_Medication = keen.validation_of_records()
            for i in selected_Medication:
                if i.text == "Test Medicine":
                    print("Test pass")
                else:
                    print("Test fail")
            log.info("***** Validation is completed and Member record is associated *****")
            keen.close().click()

        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(8)
    @allure.description("Associate and delete Medications to member")
    def test_edit_Medications(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        action_utils=ActionUtils(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        action_utils.wait_for_element((Create_capture_member_details.Member_details))
        keen.Capture_Full_Member()
        log.info("*****Select Medications to associate and delete records *****")
        keen.Medication_option()
        action_utils.wait_for_element((Associate_Capture_full_Member_details.capture_popup))
        pop_up_of_Members_Medications = keen.pop_up()
        if pop_up_of_Members_Medications.text == "Member's Medications":
            assert True
        else:
            assert False
        present_count = keen.count_records()
        count = len(present_count)
        print(count)
        pop_up_of_new_medication = keen.pop_up_new_members()
        if pop_up_of_new_medication.text == "New Member Medication":
            assert True
        else:
            assert False
        log.info("*****Search the record to associated *****")
        keen.medication_search().send_keys("Test Medicine")
        time.sleep(10)
        select_medicine = keen.Select_record()
        for medicine in select_medicine:
            if medicine.text == "Zovirak":
                medicine.click()
                break
        log.info("***** Medication record is selected *****")
        keen.save()
        log.info("***** Medication record is associated *****")
        success_message_of_medication = keen.success_message()
        if success_message_of_medication.is_displayed():
            print("Test Pass")
        else:
            print("Test Fail")
        time.sleep(15)
        added_count = keen.count_records()
        count_a = len(added_count)
        print(count)
        if count + 1 == count_a:
            assert True
        else:
            assert False
        log.info("***** Deleting the associate member record *****")
        selected_caregiver_record = keen_create.validation_of_records()
        log.info("***** selecting the associated record for Delete *****")
        for i in selected_caregiver_record:
            if i.text == "Zovirak":
                i.click()
                break
        parent_guid = self.driver.current_window_handle
        handle = self.driver.window_handles
        for guid in handle:
            if guid != parent_guid:
                self.driver.switch_to.window(guid)
                keen.click_delete().click()
                keen.click_delete_button().click()
                pop_delete = keen.success_message_delete()
                print(pop_delete.text)
                if pop_delete.is_displayed():
                    assert True
                else:
                    assert False
                log.info("***** Associated record is deleted *****")
                if guid == guid:
                    self.driver.close()
                    if guid != guid:
                        self.driver.switch_to.window(parent_guid)
                        log.info("***** Validating the deleted record *****")
                        selected_caregiver_record = keen_create.validation_of_records()
                        for i in selected_caregiver_record:
                            if i.text != "Zovirak":
                                assert True
                            else:
                                assert False
                        log.info("***** Validation is completeed *****")
                        keen.close()
                    break

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(9)
    @allure.description("Associate Hospitals to member")
    def test_add_hospitals(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        log.info("***** Associate the hospitals to  member*****")
        try:
            log.info("*****Select hospital to associate the record *****")
            keen.hospitals()
            pop_up_of_Members_hospitals = keen.pop_up()
            if pop_up_of_Members_hospitals.text == "Member's hospitals":
                assert True
            else:
                assert False
            keen.new().click()
            pop_up_of_New_Members_hospital = keen.pop_up_new_members()
            if pop_up_of_New_Members_hospital.text == "New Member's hospital":
                assert True
            else:
                assert False
            log.info("***** Search hospitals record to associate *****")
            keen.Hospital_directory().send_keys("Test")
            time.sleep(10)
            select_hospital = keen.Select_record()
            for hospital in select_hospital:
                if hospital.text == "Test Hospital one":
                    action.move_to_element(hospital).click().perform()
                    break
            log.info("***** Hospital record is selected to associate *****")
            keen.save()
            log.info("***** Hospital record is associated to member *****")
            success_message_of_Hospitals = keen.success_message()
            if success_message_of_Hospitals.is_displayed():
                assert True
            else:
                assert False
            keen.close()
            keen.hospitals()
            time.sleep(5)
            log.info("***** Validating the associated record *****")
            selected_record_of_hospitals = keen_create.validation_of_records()
            for hospital in selected_record_of_hospitals:
                if hospital.text == "Test Hospital one":
                    assert True
                else:
                    assert False
            time.sleep(5)
            log.info("***** Validation is completed *****")
            keen.close()
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(10)
    @allure.description("Associate and delete hospitals to member")
    def test_edit_hospitals(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        log.info("***** Associate and Delete the hospitals *****")
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        try:
            log.info("*****Select hospital to associate the record *****")
            keen.hospitals()
            pop_up_of_Members_hospitals = keen.pop_up()
            if pop_up_of_Members_hospitals.text == "Member's hospitals":
                assert True
            else:
                assert False
            present_count = keen.count_records()
            count = len(present_count)
            print(count)
            time.sleep(10)
            keen.new()
            pop_up_of_New_Members_hospital = keen.pop_up_new_members()
            if pop_up_of_New_Members_hospital.text == "New Member's hospital":
                assert True
            else:
                assert False
            log.info("***** Search hospitals record to associate *****")
            keen.Hospital_directory().send_keys("Test")
            time.sleep(10)
            log.info("***** Select hospitals record to associate *****")
            select_hospital = keen.Select_record()
            for hospital in select_hospital:
                if hospital.text == "Test Hospital Two":
                    action.move_to_element(hospital).click().perform()
                    break
            keen.save()
            log.info("***** Hospitals record is associated *****")
            success_message_of_Hospitals = keen.success_message()
            if success_message_of_Hospitals.is_displayed():
                assert True
            else:
                assert False
            added_count = keen.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            log.info("***** Select Hospitals record for deletion *****")
            selected_hospital_record = keen_create.validation_of_records()
            for record in selected_hospital_record:
                if record.text == "Test Hospital Two":
                    action.move_to_element(record).click().perform()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_delete().click()
                    keen.click_delete_button().click()
                    log.info("***** Selected Hospital record is deleted *****")
                    pop_delete = keen.success_message_delete()
                    print(pop_delete.text)
                    if pop_delete.is_displayed():
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                        if guid != guid:
                            self.driver.switch_to.window(parent_guid)
                            log.info("***** Validating the deleted record *****")
                            deleted_hospital_record = keen_create.validation_of_records()
                            for delete_record in deleted_hospital_record:
                                if delete_record.text != "Test Hospital Two":
                                    assert True
                                else:
                                    assert False
                            log.info("***** Validation is completed *****")
                            keen.close()
                            break
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(11)
    @allure.description("Associate Campaigns record to member")
    def test_add_campaigns(self):
            keen = Associate_Capture_full_Member_details(self.driver)
            keen_create=Create_capture_member_details(self.driver)
            log = logger_utils.get_logger()
            action = ActionChains(self.driver)
            action_utils=ActionUtils(self.driver)
            keen_login = Keen_login(self.driver)
            keen_login.keen_leads_members()
            time.sleep(6)
            keen.select_member()
            time.sleep(10)
            keen.Capture_Full_Member()
            time.sleep(5)
            log.info("***** Associate and Delete the hospitals *****")
            try:
                log.info("*****Select Campaigns to associate records *****")
                keen_create.select_campaigns()
                pop_up_of_campaigns = keen.pop_up()
                if pop_up_of_campaigns.text == "Member's Campaign":
                    assert True
                else:
                    assert False
                keen.new()
                action_utils.wait_for_element((Associate_Capture_full_Member_details.popup_newmembers))
                New_member_pop_up = keen.pop_up_new_members()
                if New_member_pop_up.text == "New Member campaign":
                    assert True
                else:
                    assert False
                log.info("*****Search Campaigns to associate *****")
                keen.search_keen_campaign().send_keys("Test campaign")
                pick_campaign = keen.Select_record()
                for campaign in pick_campaign:
                    if campaign.text == "Test campaign":
                        action.move_to_element(campaign).click().perform()
                        break
                log.info("*****Select Campaigns to associate records *****")
                keen.save()
                log.info("***** Campaigns record is associated to member *****")
                success_message_of_campaign = keen.success_message()
                if success_message_of_campaign.is_displayed():
                    assert True
                else:
                    assert False
                keen.close()
                action_utils.wait_for_element(())
                keen.select_campaigns()
                time.sleep(10)
                log.info("***** Validating the associated record to member *****")
                selected_campaign_record = keen_create.validation_of_records()
                for record in selected_campaign_record:
                    if record.text == "Test campaign":
                        print("Test Pass")
                    else:
                        print("Test Fail")
                log.info("***** Validation is completed *****")
                keen.close()
            except Exception as ex:
                print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(12)
    @allure.description("Associate and delete Campaigns records to member")
    def test_edit_campaign(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        log.info("***** Associate and Delete the campaigns records *****")
        try:
            log.info("*****Select Campaigns to associate *****")
            keen.select_campaigns()
            time.sleep(6)
            pop_up_of_campaigns = keen.pop_up()
            if pop_up_of_campaigns.text == "Member's Campaign":
                assert True
            else:
                assert False
            present_count = keen.count_records()
            count = len(present_count)
            print(count)
            time.sleep(10)
            keen.new()
            time.sleep(8)
            New_member_pop_up = keen.pop_up_new_members()
            if New_member_pop_up.text == "New Member campaign":
                assert True
            else:
                assert False
            log.info("*****Search Campaigns records to associate *****")
            keen.search_keen_campaign().send_keys("Test campaign")
            time.sleep(10)
            pick_campaign = keen.Select_record()
            for i in pick_campaign:

                if i.text == "Test keen":
                    i.click()
                    break
            log.info("*****Select Campaigns records to associate *****")
            time.sleep(10)
            keen.save()
            log.info("***** Campaigns records is associated *****")
            success_message_of_campaign = keen.success_message()
            if success_message_of_campaign.is_displayed():
                assert True
            else:
                assert False
            added_count = keen.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            log.info("*****Select Campaigns records to delete *****")
            selected_campaign_record = keen_create.validation_of_records()
            for i in selected_campaign_record:
                if i.text == "Test keen":
                    i.click()
                    break
            log.info("***** Campaigns records is selected to delete the record *****")
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_delete().click()
                    keen.click_delete_button().click()
                    pop_delete = keen.success_message_delete()
                    print(pop_delete.text)
                    if pop_delete.is_displayed():
                        assert True
                    else:
                        assert False
                    log.info("*****Selected Campaigns records is deleted *****")

                    if guid == guid:
                        self.driver.close()
                        if guid != guid:
                            self.driver.switch_to.window(parent_guid)
                            log.info("*****Validating the deleted record *****")
                            deleted_campaign_record = keen.validation_of_records()
                            for i in deleted_campaign_record:
                                if i.text != "Test keen":
                                    assert True
                                else:
                                    assert False
                            keen.close()
                            break
                        log.info("***** Validation is completed *****")

        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(13)
    @allure.description("Associate Physicians records to member")
    def test_add_physicians(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        log.info("***** Associate physicians records to member *****")
        try:
            log.info("*****Select Physicians option to associate records *****")
            keen.physicians()
            pop_up_of_physicians = keen.pop_up()
            if pop_up_of_physicians.text == "Member's Physicians":
                assert True
            else:
                assert False
            keen.new()
            pop_of_new_physicians = keen.pop_up_new_members()
            if pop_of_new_physicians.text == "New Member's physician":
                assert True
            else:
                assert False
            log.info("***** Search physicians records to associate *****")
            keen.physician_directory().send_keys("Test CVS")
            log.info("***** Select physicians records to associate *****")
            select_physician_directory = keen.Select_record()
            for i in select_physician_directory:
                print(i.text)
                if i.text == "Test CVS":
                    i.click()
                    break
            log.info("***** Physician record is selected to associate *****")
            keen.Is_Primary_Care_Physician().click()
            keen.city().send_keys("North California")
            time.sleep(10)
            keen.state()
            select_state= keen.select_state()
            for i in select_state:
                print(i.text)
                if i.text == "NC":
                    i.click()
                    break
            keen.zipcode().send_keys("65302")
            keen.save().click()
            log.info("***** Physician record is associated *****")
            success_message_of_physicians = keen.success_message()
            if success_message_of_physicians.is_displayed():
                print("Test Pass")
            else:
                print("Test fail")
            keen.close().click()
            time.sleep(5)
            keen.physicians().click()
            log.info("***** Validating the selected record *****")
            selected_physician = keen.validation_of_records()
            for i in selected_physician:
                if i.text == "Test CVS":
                    assert True
                else:
                    assert False
            time.sleep(5)
            keen.close().click()
            log.info("***** Validation is completed *****")
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(14)
    @allure.description("Associate and delete Physicains records to member")
    def test_edit_physicians(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action_utils=ActionUtils(self.driver)
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        time.sleep(6)
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        log.info("***** Associate and delete Physicains records to member *****")
        try:
            log.info("*****Select physicians to associate *****")
            keen.physicians()
            pop_up_of_physicians = keen.pop_up()
            if pop_up_of_physicians.text == "Member's Physicians":
                assert True
            else:
                assert False
            present_count = keen.count_records()
            count = len(present_count)
            print(count)
            keen.new()
            action_utils.wait_for_element((Associate_Capture_full_Member_details.popup_newmembers))
            pop_of_new_physicians = keen.pop_up_new_members()
            if pop_of_new_physicians.text == "New Member's physician":
                assert True
            else:
                assert False
            log.info("*****Search physicians to associate *****")
            keen.physician_directory().send_keys("Anil")
            select_physician_directory = keen.Select_record()
            for directory in select_physician_directory:
                print(directory.text)
                if directory.text == "Anil Kumar":
                    action.move_to_element(directory).click().perform()
                    break
            log.info("*****physicianrecord is selected to associate *****")
            keen.Is_Primary_Care_Physician().click()
            keen.city().send_keys("North California")
            select_state = keen.select_state()
            for state in select_state:
                print(state.text)
                if state.text == "NC":
                    action.move_to_element(state).click().perform()
                    break
            keen.zipcode().send_keys("65302")
            keen.save()
            log.info("*****Physicians record is associated to member *****")
            success_message_of_physicians = keen.success_message()
            if success_message_of_physicians.is_displayed():
                print("Test Pass")
            else:
                print("Test fail")
            added_count = keen.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            log.info("***** Selecet the record to delete*****")
            selected_physicians_record = keen_create.validation_of_records()
            for record in selected_physicians_record:
                if record.text == "Anil Kumar":
                    action.move_to_element(record).click().perform()
                    break
            log.info("***** Record is selected to delete *****")
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_delete().click()
                    keen.click_delete_button().click()
                    log.info("***** Associated record is deleted *****")
                    pop_delete = keen.success_message_delete()
                    print(pop_delete.text)
                    if pop_delete.is_displayed():
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                        if guid != parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            log.info("***** Validating the deleted record*****")
                            deleted_campaign_record = keen_create.validation_of_records()
                            for i in deleted_campaign_record:
                                if i.text != "Anil Kumar":
                                    assert True
                                else:
                                    assert False
                            keen.close()
                            log.info("***** Validation is completed *****")
                            break
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(15)
    @allure.description("Associate outbound_referrals practices records to member")
    def test_add_outbound_referrals(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login=Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        time.sleep(5)
        log.info("***** Associate outbound referral practices records to member *****")
        try:
            keen.select_outbound_referral()
            time.sleep(5)
            pop_up_of_outbound = keen.pop_up()
            if pop_up_of_outbound.text == "Outbound Referral Practices":
                assert True
            else:
                assert False
            time.sleep(4)
            keen.new()
            time.sleep(5)
            pop_up_of_new_outbound = keen.pop_up_new_members()
            if pop_up_of_new_outbound.text == "New Outbound Referral: Practice":
                assert True
            else:
                assert False
            time.sleep(5)
            log.info("***** Search outbound referral practices records to associate *****")
            keen.search_practice_directory().send_keys("Test")
            time.sleep(5)
            select_practice_directory = keen.Select_record()
            log.info("***** Select outbound referral practices records to associate *****")
            for directory in select_practice_directory:

                if directory.text == "Test Directory":
                    action.move_to_element(directory).click().perform()
                    break
            keen.save()
            log.info("***** outbound referral practices record is associated *****")
            success_message_of_outbound_referrals = keen.success_message()
            if success_message_of_outbound_referrals.is_displayed():
                assert True
            else:
                assert False
            keen.close()
            keen.practice_directory()
            time.sleep(5)
            log.info("***** Validating the associated record *****")
            selected_practice_record = keen_create.validation_of_records()
            for i in selected_practice_record:
                if i.text == "Test Directory":
                    print("Test Pass")
                else:
                    print("Test Fail")
            time.sleep(5)
            keen.close()
            log.info("***** Validation is completed *****")
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Assosicate Practices to Member
    @pytest.mark.order(16)
    @allure.description("Associate outbound_referrals practices records to member")
    def test_edit_outbound_referrals(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        try:
            log.info("***** Select outbound_referral to associate a records to member *****")
            keen.select_outbound_referral().click()
            time.sleep(5)
            pop_up_of_outbound = keen.pop_up()
            if pop_up_of_outbound.text == "Outbound Referral Practices":
                assert True
            else:
                assert False
            present_count = keen.count_records()
            count = len(present_count)
            print(count)
            time.sleep(10)
            keen.new()
            time.sleep(5)
            pop_up_of_new_outbound = keen.pop_up_new_members()
            if pop_up_of_new_outbound.text == "New Outbound Referral: Practice":
                assert True
            else:
                assert False
            time.sleep(5)
            log.info("***** Search outbound referral practice record ******")
            keen.search_practice_directory().send_keys("Test")
            time.sleep(5)
            select_practice_directory = keen.Select_record()
            log.info("***** Select outbound referral practice record ******")
            for directory in select_practice_directory:

                if directory.text == "Test Practice":
                    action.move_to_element(directory).click().perform()
                    break
            keen.save()
            log.info("***** Outbound referral practice record is associated ******")
            success_message_of_outbound_referrals = keen.success_message()
            if success_message_of_outbound_referrals.is_displayed():
                assert True
            else:
                assert False
            added_count = keen.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            log.info("***** Select outbound referral practice record to delete******")
            selected_physicians_record = keen_create.validation_of_records()
            for i in selected_physicians_record:
                if i.text == "Test Practice":
                    i.click()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_delete().click()
                    keen.click_delete_button().click()
                    log.info("***** Selected outbound referral practice record is deleted ******")
                    pop_delete = keen.success_message_delete()
                    print(pop_delete.text)
                    if pop_delete.is_displayed():
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                        if guid != parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            log.info("***** Validating the deleted outbound referral practice ******")
                            deleted_physicians_record = keen_create.validation_of_records()
                            for i in deleted_physicians_record:
                                if i.text != "Test Practice":
                                    assert True
                                else:
                                    assert False
                            keen.close()
                            break
            log.info("***** Validation is completed ******")
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click onPharmacies
    ## Add Pharmacies to Member

    @pytest.mark.order(17)
    @allure.description("Associate Pharmacies records to member")
    def test_add_pharmacies(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        try:
            log.info("***** Select Pharmacy to associate records *****")
            keen.select_pharmacy()
            time.sleep(5)
            pop_up_of_pharmacies = keen.pop_up()
            if pop_up_of_pharmacies.text == "Member's Pharmacies":
                assert True
            else:
                assert False
            keen.new()
            time.sleep(5)
            pop_up_of_New_member_pharmacies = keen.pop_up_new_members()
            if pop_up_of_New_member_pharmacies.text == "New Member's pharmacy":
                assert True
            else:
                assert False
            log.info("***** Search pharmacy records to associate *****")
            keen.pharmacy_directory().send_keys("Test Pharmacy")
            time.sleep(5)
            select_pharmacies = keen.Select_record()
            time.sleep(5)
            log.info("***** Select pharmacy records to associate *****")
            for i in select_pharmacies:
                if i.text == "Test Pharmacy":
                    i.click()
            keen.save()
            log.info("***** Pharmacy records is associated to member *****")
            success_message_pharmacies = keen.success_message()
            if success_message_pharmacies.is_displayed():
                assert True
            else:
                assert False
            keen.close()
            time.sleep(5)
            keen.select_pharmacy()
            time.sleep(5)
            log.info("***** Validationg the associate pharmacy *****")
            selected_pharmacies = keen_create.validation_of_records()
            for i in selected_pharmacies:
                if i.text == "Test Pharmacy":
                    assert True
                else:
                    assert False
            time.sleep(5)
            log.info("***** Validation is completed *****")
            keen.close()
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Pharmacies
    ## Edit Pharmacies to Member
    @pytest.mark.order(18)
    @allure.description("***** Associate and Delete the Pharmacy records *****")
    def test_edit_pharmacies(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        try:
            log.info("***** Select Pharmacy to associate records *****")
            keen.select_pharmacy()
            time.sleep(5)
            pop_up_of_pharmacies = keen.pop_up()
            if pop_up_of_pharmacies.text == "Member's Pharmacies":
                assert True
            else:
                assert False
            present_count = keen.count_records()
            count = len(present_count)
            print(count)
            time.sleep(10)
            keen.new()
            time.sleep(5)
            pop_up_of_New_member_pharmacies = keen.pop_up_new_members()
            if pop_up_of_New_member_pharmacies.text == "New Member's pharmacy":
                assert True
            else:
                assert False
            log.info("***** Search Pharmacy record to associate *****")
            keen.pharmacy_directory().send_keys("Test Pharmacy")
            time.sleep(5)
            select_pharmacies = keen.Select_record()
            time.sleep(5)
            log.info("***** Select Pharmacy record to associate *****")
            for i in select_pharmacies:
                if i.text == "Test Pharmacy CVS":
                    i.click()
            keen.save()
            log.info("***** Pharmacy record is associated *****")
            success_message_pharmacies = keen.success_message()
            if success_message_pharmacies.is_displayed():
                assert True
            else:
                assert False
            added_count = keen.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            log.info("***** Select Pharmacy record to delete *****")
            selected_physicians_record = keen_create.validation_of_records()
            for i in selected_physicians_record:
                if i.text == "Test Pharmacy CVS":
                    i.click()
                    break
            log.info("***** Pharmacy record is slected to delete *****")
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_delete().click()
                    keen.click_delete_button().click()
                    log.info("***** Selected Pharmacy record is deleted *****")
                    pop_delete = keen.success_message_delete()
                    print(pop_delete.text)
                    if pop_delete.is_displayed():
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                        if guid != parent_guid:
                            self.driver.switch_to.window(parent_guid)
                            log.info("***** Validating the deleted pharmacy record *****")
                            deleted_physicians_record = keen_create.validation_of_records()
                            for i in deleted_physicians_record:
                                if i.text != "Test Pharmacy CVS":
                                    assert True
                                else:
                                    assert False
                            keen.close()
                            log.info("***** Validation is completed *****")
                            break
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Referrals
    ## Add refferraks  to Member
    @pytest.mark.order(19)
    @allure.description("Associate Outbound referral organization records to member")
    def test_add_outbound_referral_organization(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        try:
            log.info("***** Select _outbound referral organization to associate a records*****")
            keen.select_outbound_organization().click()
            time.sleep(5)
            pop_up_of_outbound = keen.pop_up()
            if pop_up_of_outbound.text == "Outbound Referral Organization":
                assert True
            else:
                assert False
            time.sleep(5)
            keen.new()
            time.sleep(5)
            pop_up_of_New_organization = keen.pop_up_new_members()
            if pop_up_of_New_organization.text == "New Outbound Referral: Organization":
                assert True
            else:
                assert False

            time.sleep(5)
            log.info("***** Search outbound referral organization to associate a record *****")
            keen.search_Community_and_senior_organization().send_keys("Test Community")
            time.sleep(5)
            select_community_and_senior_organization = keen.Select_record()
            log.info("***** Select outbound referral organization to associate a record *****")
            for i in select_community_and_senior_organization:
                if i.text == "Test Community":
                    i.click()
                    break
            time.sleep(5)
            keen.save()
            log.info("***** Outbound referral organization record is associated *****")
            success_message_of_outbound_organization = keen.success_message()
            if success_message_of_outbound_organization.is_displayed():
                assert True
            else:
                assert False
            keen.close()
            time.sleep(5)
            keen.select_outbound_organization()
            time.sleep(5)
            log.info("***** Validating the associated outbound referral organization record *****")
            selected_record_of_organization = keen_create.validation_of_records()
            for i in selected_record_of_organization:
                print(i.text)
                if i.text == "Test Community":
                    print("Test Pass")
                else:
                    print("Test fail")
            log.info("***** Validation is completed *****")
            time.sleep(5)
            keen.close()
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Organization
    ## Edit Organization to Member
    @pytest.mark.order(20)
    @allure.description("Associate and Delete Outbound referral organization records")
    def test_edit_outbound_referral_organization(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        try:
            log.info("***** Select outbound Organization to associate records *****")
            keen.select_outbound_organization().click()
            time.sleep(5)
            pop_up_of_outbound = keen.pop_up()
            if pop_up_of_outbound.text == "Outbound Referral Organization":
                assert True
            else:
                assert False
            present_count = keen.count_records()
            count = len(present_count)
            print(count)
            keen.new()
            time.sleep(5)
            pop_up_of_New_organization = keen.pop_up_new_members()
            if pop_up_of_New_organization.text == "New Outbound Referral: Organization":
                assert True
            else:
                assert False

            time.sleep(5)
            log.info("***** Search outbound Organization record to associate *****")
            keen.search_Community_and_senior_organization().send_keys("Test Organization")
            time.sleep(5)
            select_community_and_senior_organization = keen.Select_record()
            log.info("***** Select outbound Organization records to associate *****")
            for i in select_community_and_senior_organization:
                if i.text == "Test Organization":
                    i.click()
                    break
            time.sleep(5)
            keen.save()
            log.info("***** record is associated to Outbound referral organization *****")
            success_message_of_outbound_organization = keen.success_message()
            if success_message_of_outbound_organization.is_displayed():
                assert True
            else:
                assert False
            added_count = keen.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            keen.close()
            time.sleep(5)
            keen.select_outbound_organization().click()
            time.sleep(5)
            log.info("***** Select outbound Organization to delete *****")
            selected_record_of_organization = keen_create.validation_of_records()
            for i in selected_record_of_organization:
                print(i.text)
                if i.text == "Test Organization":
                    i.click()
                    break
                parent_guid = self.driver.current_window_handle
                handle = self.driver.window_handles
                for guid in handle:
                    if guid != parent_guid:
                        self.driver.switch_to.window(guid)
                        keen.click_delete().click()
                        keen.click_delete_button().click()
                        log.info("***** Selected outbound Organization record is deleted *****")
                        pop_delete = keen.success_message_delete()
                        print(pop_delete.text)
                        if pop_delete.is_displayed():
                            assert True
                        else:
                            assert False
                        if guid == guid:
                            self.driver.close()
                            if guid != parent_guid:
                                self.driver.switch_to.window(parent_guid)
                                deleted_organization_record = keen_create.validation_of_records()
                                for i in deleted_organization_record:
                                    if i.text != "Test Organization":
                                        assert True
                                    else:
                                        assert False
                                keen.close()
                                break
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Events
    ## Add events to Member
    @pytest.mark.sanity
    @pytest.mark.order(21)
    @allure.description("Associate Events to a Member")
    def test_add_events(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        try:
            log.info("***** Select events to associate a records *****")
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0, 200)")
            keen.events()
            pop_up_of_events = keen.pop_up()
            if pop_up_of_events.text == "Member's Event":
                assert True
            else:
                assert False
            keen.new()
            pop_of_New_member_events = keen.pop_up_new_members()
            if pop_of_New_member_events.text == "New Member at event":
                assert True
            else:
                assert False
            log.info("***** Search events to associate *****")
            keen.keen_event().send_keys("Test Event")
            select_event = keen.Select_record()
            log.info("***** Select event to associate *****")
            for i in select_event:
                if i.text == "Test Event":
                    i.click()
                    break
            keen.save()
            log.info("***** Selected event record is associated to member *****")
            success_message_of_events = keen.success_message()
            if success_message_of_events.is_displayed():
                assert True
            else:
                assert False
            keen.close()
            time.sleep(5)

            keen.events()
            time.sleep(5)
            log.info("***** Validating the selected record *****")
            selected_keen_event = keen_create.validation_of_records()
            for i in selected_keen_event:
                if i.text == "Test Even":
                    assert True
                else:
                    assert False
            time.sleep(5)
            keen.close()
            log.info("***** Validation is completed *****")
        except Exception as ex:
            print(ex)

    ##Test Case Description: Edit a Associated Practices to a Particular Member
    ##TestCase Steps:1.Login to SFDC--->Click on Keen Leads and Members--->Click Keen Lead-----> Click on Practices
    ## Edit Events to Member
    @pytest.mark.order(22)
    @allure.description("Associate and Delete the Events record")
    def test_edit_events(self):
        keen = Associate_Capture_full_Member_details(self.driver)
        keen_create = Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        action = ActionChains(self.driver)
        keen_login = Keen_login(self.driver)
        keen_login.keen_leads_members()
        keen.select_member()
        time.sleep(10)
        keen.Capture_Full_Member()
        try:
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0, 200)")
            log.info("***** Select Events option to associate records *****")
            keen.events()
            pop_up_of_events = keen.pop_up()
            if pop_up_of_events.text == "Member's Event":
                assert True
            else:
                assert False
            present_count = keen.count_records()
            count = len(present_count)
            print(count)
            keen.new()
            time.sleep(5)
            pop_of_New_member_events = keen.pop_up_new_members()
            if pop_of_New_member_events.text == "New Member at event":
                assert True
            else:
                assert False
            log.info("***** Search events records to associate *****")
            keen.keen_event().send_keys("Event")
            select_event = keen.Select_record()
            log.info("***** Select events records to associate *****")
            for i in select_event:
                if i.text == "Event":
                    i.click()
                    break
            keen.save()
            log.info("*****  Selected Event record is associated *****")
            success_message_of_events = keen.success_message()
            if success_message_of_events.is_displayed():
                assert True
            else:
                assert False
            added_count = keen.count_records()
            count_a = len(added_count)
            print(count)
            if count + 1 == count_a:
                assert True
            else:
                assert False
            keen.close()
            time.sleep(5)

            keen.events()
            time.sleep(5)
            log.info("***** Select the event record to delete *****")
            selected_keen_event = keen_create.validation_of_records()
            for i in selected_keen_event:
                if i.text == "Test Event":
                    i.click()
                    break
            parent_guid = self.driver.current_window_handle
            handle = self.driver.window_handles
            for guid in handle:
                if guid != parent_guid:
                    self.driver.switch_to.window(guid)
                    keen.click_delete().click()
                    keen.click_delete_button().click()
                    log.info("***** Selected event record is deleted *****")
                    pop_delete = keen.success_message_delete()
                    print(pop_delete.text)
                    if pop_delete.is_displayed():
                        assert True
                    else:
                        assert False
                    if guid == guid:
                        self.driver.close()
                        if guid != guid:
                            self.driver.switch_to.window(parent_guid)
                            log.info("***** Validating the deleted record *****")
                            deleted_events_record = keen_create.validation_of_records()
                            for i in deleted_events_record:
                                if i.text != "Test Organization":
                                    assert True
                                else:
                                    assert False
                            log.info("***** Validation is completed *****")
                            keen.close()
                            break
        except Exception as ex:
            print(ex)










