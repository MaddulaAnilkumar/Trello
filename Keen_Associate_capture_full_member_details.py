from selenium.webdriver.common.by import By

from utilities.action_utils import ActionUtils

class Associate_Capture_full_Member_details(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    ## Add Plans
    Member=(By.XPATH,"//a[@title='Test Automation']")
    organizatino_records=(By.XPATH,"//div[@class='primaryLabel slds-truncate slds-lookup__result-text']")
    Member_Details=(By.XPATH,"//span[@title='Capture Full Member Detail']")
    plans_option=(By.XPATH, "//button[@title='Plans']")
    click_new=(By.XPATH,"//button[@name='New']")
    plan_record=(By.XPATH,"//input[@placeholder='Search PlanDetailsList...']")
    existing_records=(By.XPATH,"//span[@class='slds-media__body']")
    associated_records=(By.XPATH,"//th[@data-label]")
    enrolledby_keen=(By.XPATH,"//input[@name='Enrolled_by_Keen__c']")
    member_id=(By.XPATH,"//input[@name='Carrier_member_ID__c']")
    plan_hra=(By.XPATH,"//input[@name='HRA_completed__c']")
    plan_hra_date=(By.XPATH,"//input[@name='HRA_completed_date__c']")
    plan_effectiveDate=(By.XPATH,"//input[@name='Effective_date__c']")
    enroll_number=(By.XPATH,"//input[@name='Enrollment_confirmation_number__c']")
    plan_endDate=(By.XPATH,"//input[@name='Plan_end_date__c']")
    enroll_type=(By.XPATH,"//button[@aria-label='Enrollment type, --None--']")
    list_enrollTypes=(By.XPATH,"lightning-base-combobox-item")
    submission_date=(By.XPATH,"//input[@name='App_submission_date__c']")
    approve_date=(By.XPATH,"//input[@name='App_approval_date__c']")
    end_date=(By.XPATH,"//input[@name='Disenrollment_date__c']")
    savebutton_popup=(By.XPATH,"//button[@name='SaveEdit']")
    close_popup=(By.XPATH,"//button[@title='Close']")
    count=(By.XPATH,"//th[@data-label='Name']")
    def select_member(self):
        return self.click_element(*Associate_Capture_full_Member_details.Member)
    def Capture_Full_Member(self):
        return self.click_element(*Associate_Capture_full_Member_details.Member_Details)
    def Select_Plans(self):
        return self.click_element(*Associate_Capture_full_Member_details.plans_option)
    def new(self):
        return self.click_element(*Associate_Capture_full_Member_details.click_new)
    def search_plan_detail(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.plan_record)

    #select Existing account
    def select_existing_records(self):
        return self.Find_Elements(*Associate_Capture_full_Member_details.existing_records)
        # return self.driver.find_elements(By.XPATH,"//ul[@role='group']//li")
    def validation_of_plan(self):
        return self.Find_Elements(*Associate_Capture_full_Member_details.associated_records)
    def Enrolled_by_Keen(self):
        return self.click_element(*Associate_Capture_full_Member_details.enrolledby_keen)
    def Carrier_member_ID(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.member_id)
    def hra_completd(self):
        return self.click_element(*Associate_Capture_full_Member_details.plan_hra)
    def HRA_completed_date(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.plan_hra_date)
    def Effective_date__c(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.plan_effectiveDate)
    def Enrollment_confirmation_number(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.enroll_number)
    def plan_end_date(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.plan_endDate)
    def enrollment_type(self):
        return self.click_element(*Associate_Capture_full_Member_details.enroll_type)
    def select_enrollment_type(self):
        return self.Find_Elements(*Associate_Capture_full_Member_details.list_enrollTypes)
    def App_submission_date(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.submission_date)
    def App_approval_date(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.approve_date)
    def Disenrollment_date(self,text):
        return self.enter_text(text,*Associate_Capture_full_Member_details.end_date)
    def save(self):
        return self.click_element(*Associate_Capture_full_Member_details.savebutton_popup)
    def close(self):
        return self.driver.find_element(*Associate_Capture_full_Member_details.close_popup)
    def count_records(self):
        return self.driver.find_elements(*Associate_Capture_full_Member_details.count)

    ##### Edit Plans


    def list_plans(self):
        plans=self.driver.find_element(By.XPATH,"//a[text()='Test Plan3']")
        return self.driver.execute_script("arguments[0].click();", plans)
    def edit_appsubmission_date(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Edit App submission date']")
    def edit_plan(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Clear Selection']")
    def validation_plan(self):
        return self.driver.find_element(By.XPATH,"(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[1]")

    def validation_Enrolled_by(self):
        return self.driver.find_element(By.XPATH,"(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[2]")

    def validation_Carrier_member_ID(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[3]")

    def validation_HRA_completed(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[4]")

    def validation_HRA_completed_date(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[5]")
    def valiadtion_Effective_date(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[6]")

    def validation_Enrollment_confirmation_number(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[7]")

    def validation_Plan_enddate(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[8]")

    def validation_Enrollment_type(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[9]")

    def validation_App_submissiondate(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[10]")


    def validation_App_approvaldate(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[11]")

    def validation_Disenrollmentdate(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[12]")



    ### Add Practices
    capture_popup=(By.XPATH,"//h2[@class='slds-text-heading_medium slds-hyphenate']")
    popup_newmembers=(By.XPATH,"//h2[@class='slds-modal__title slds-hyphenate slds-text-heading--medium']")
    def pop_up(self):
        return self.driver.find_element(*Associate_Capture_full_Member_details.capture_popup)
    def pop_up_new_members(self):
        return self.driver.find_element(*Associate_Capture_full_Member_details.popup_newmembers)
    ##### == 'Member's practices'
    ##### == 'New Member's practice'

    def practice_directory(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Practice directory...']")
### Add Hospitals
    def hospitals(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Hospitals']")
    def Hospital_directory(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Hospitals and health systems...']")
    ##### Add Physicians

    def physicians(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Physicians']")
    def physician_directory(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Physician directory...']")
    def Is_Primary_Care_Physician(self):
        return self.driver.find_element(By.XPATH,"//input[@name='Is_Primary_Care_Physician__c']")
    def city(self):
        return self.driver.find_element(By.XPATH,"//input[@name='City__c']")
    def state(self):
        return self.driver.find_element(By.XPATH,"//button[@aria-label='State, --None--']")
    def select_state(self):
        return self.driver.find_elements(By.XPATH,"//lightning-base-combobox-item[@class='slds-media slds-listbox__option slds-media_center slds-media_small slds-listbox__option_plain']")
    def zipcode(self):
        return self.driver.find_element(By.XPATH,"//input[@name='Zipcode__c']")

    #### Add Events
    # def select_events(self):
    #     return self.driver.find_element(By.XPATH,"//button[@title='Member's Events']")

    def events(self):
        return self.driver.find_element(By.XPATH,"//lightning-button[@data-id='MemberEvents']//button")
    def keen_event(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Keen Events...']")
    ### Related Persons
    related_persons=(By.XPATH,"//button[@title='Related Persons']")
    caregiver_person=(By.XPATH,"//input[@placeholder='Search Caregivers Directory...']")
    keen_leads_member=(By.XPATH,"//input[@placeholder='Search Keen leads and members Directory']")
    relation=(By.XPATH,"//button[@name='relationship']")
    caregiver_yes=(By.XPATH,"(//span[text()='Yes'])[1]")
    caregiver_no=(By.XPATH,"(//span[text()='No'])[1]")
    power_of_attorney_yes=(By.XPATH,"(//span[text()='Yes'])[2]")
    power_of_attorney_no=(By.XPATH,"(//span[text()='No'])[2]")
    save_related_person=(By.XPATH,"//button[@name='submit']")
    selected_person=(By.XPATH,"//input[@name='keenMember']")
    listrecords=(By.XPATH,"//span[@class='slds-truncate']")
    poa_selector=(By.XPATH,"(//span[@part='indicator'])[1]")
    caregiver_selector=(By.XPATH,"(//span[@part='indicator'])[2]")
    select_soa=(By.XPATH,"//li[@data-name='Test Test']")
    enable_caregiver=(By.XPATH,"//input[@placeholder='Search Caregivers Directory']")
    enable_keen_leads=(By.XPATH,"//input[@placeholder='Search Keen leads and members Directory']")
    related_person_save_message=(By.XPATH,"//div[@class='toastTitle slds-text-heading--small']")
    new_caregiver_relatedpersons=(By.XPATH,"//li[@data-name='New Caregiver']")
    def click_related_persons(self):
        return self.click_element(*Associate_Capture_full_Member_details.related_persons)
    def search_caregiver_person(self):
        return self.find_element(*Associate_Capture_full_Member_details.caregiver_person)
    def check_caregiver_person(self):
        return self.find_element(*Associate_Capture_full_Member_details.enable_caregiver)
    def check_caregiver_member(self):
        return self.find_element(*Associate_Capture_full_Member_details.enable_keen_leads)
    def click_newcaregiver_relatedperson(self):
        return self.click_element(*Associate_Capture_full_Member_details.new_caregiver_relatedpersons)
    def search_keen_leads(self):
        return self.find_element(*Associate_Capture_full_Member_details.keen_leads_member)
    def click_realtion(self):
        return self.click_element(*Associate_Capture_full_Member_details.relation)
    def click_caregiver_yes(self):
        return self.click_element(*Associate_Capture_full_Member_details.caregiver_yes)
    def click_caregiver_no(self):
        return self.click_element(*Associate_Capture_full_Member_details.caregiver_no)
    def click_power_of_attorney_yes(self):
        return self.click_element(*Associate_Capture_full_Member_details.power_of_attorney_yes)
    def click_power_of_attorney_no(self):
        return self.click_element(*Associate_Capture_full_Member_details.power_of_attorney_no)
    def click_save_related_person(self):
        return self.click_element(*Associate_Capture_full_Member_details.save_related_person)
    def Selected_person(self):
        return self.get_text(*Associate_Capture_full_Member_details.selected_person)
    def Select_record(self):
        return self.Find_Elements(*Associate_Capture_full_Member_details.listrecords)
    def Select_SOA_Member(self):
        return self.click_element(*Associate_Capture_full_Member_details.select_soa)
    def check_poa(self):
        return self.find_element(*Associate_Capture_full_Member_details.poa_selector)
    def check_caregiver(self):
        return self.find_element(*Associate_Capture_full_Member_details.caregiver_selector)
    def success_message_related_persons(self):
        return self.get_text(*Associate_Capture_full_Member_details.related_person_save_message)
    #### Edit Caregivers
    def select_saved_record(self):
        return self.driver.find_element(By.XPATH,"//span[@id='window']")
    def click_delete(self):
        return self.driver.find_element(By.XPATH,"//button[@name='Delete']")
    def success_message_delete(self):
        return self.driver.find_element(By.XPATH,"//span[@class=toastMessage slds-text-heading--small forceActionsText']")
    def click_delete_button(self):
        return self.driver.find_element(By.XPATH,"//span[text()='Delete']")

    def validation_of_edit_caregiver(self):
        return self.driver.find_element(By.XPATH,"(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[1]")

    def validation_edit_Caregiver_Name(self):
        return self.driver.find_element(By.XPATH,"(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[1]")

    def validation_edit_Date_of_birth(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[2]")

    def validation_edit_Do_not_call(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[3]")

    def validation_edit_Email(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[4]")
    def valiadtion_edit_Email_opt_out(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[5]")

    def validation_phone(self):
        return self.driver.find_element(By.XPATH, "//lightning-click-to-dial[@slot='outputField']//span[2]")

    def validation_edit_Phonetype(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[7]")

    def validation_edit_otherphone(self):
        return self.driver.find_element(By.XPATH,"(//lightning-click-to-dial[@slot='outputField']//span[2])[2]")


    def validation_edit_Address(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[9]")


    def validation_edit_city(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[10]")

    def validation_edit_state(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[11]")
    def validation_edit_relationship(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[12]")
    def validation_edit_zipcode(self):
        return self.driver.find_element(By.XPATH,
                                        "(//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11'])[13]")



    ##### Add Medications

    def Medication_option(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Medications']")
    def medication_search(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Medication Directory...']")
    def Quantity_per_fill(self):
        return self.driver.find_element(By.XPATH,"//input[@name='Quantity_per_refill__c']")
    def Refill_frequency(self):
        return self.driver.find_element(By.XPATH,"//button[@aria-label='Refill frequency, --None--']")
    def select_frequency(self):
        return self.driver.find_elements(By.XPATH,"//lightning-base-combobox-item[@class='slds-media slds-listbox__option slds-media_center slds-media_small slds-listbox__option_plain']")
    ### Add Campaigns

    def select_campaigns(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Campaigns']")
    def search_keen_campaign(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Keen campaigns...']")

    ### Add Pharmacies
    def select_pharmacy(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Pharmacies']")
    def pharmacy_directory(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Pharmacy directory...']")
    def is_primary_physician(self):
        return self.driver.find_element(By.XPATH,"//span[text()='Is Pharmacy Primary']")

    ### Add outboundreferral Practice

    def select_outbound_referral(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Outbound Referrals Practice']")

    def search_practice_directory(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Practice directory...']")
    ### Add outbound referral organization

    def select_outbound_organization(self):
        return self.driver.find_element(By.XPATH,"//button[@title='Outbound Referrals Organization']")
    def search_Community_and_senior_organization(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Community and senior organizations...']")
    def success_message(self):
        return self.driver.find_element(By.XPATH,"//div[contains(@id,'toastDescription')]//span")

