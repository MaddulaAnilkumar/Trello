from selenium.webdriver.common.by import By
from utilities.action_utils import ActionUtils


class Create_capture_member_details(ActionUtils):
    #### For All Capture Full Members Details
    Member=(By.XPATH,"//th[@class='slds-cell-edit cellContainer']/span//a[@title]")
    Member_details=(By.XPATH,"//span[@title='Capture Full Member Detail']")
    Members_Popup = (By.XPATH, "//h2[@class='slds-text-heading_medium slds-hyphenate']")
    new=(By.XPATH,"//header//button[@name='New']")
    members_deatils_save=(By.XPATH,"//button[@name='save']")
    pop_up_new_members = (By.XPATH, "//h2[@class='slds-modal__title slds-hyphenate slds-text-heading--medium']")
    pop_up_of_medications=(By.XPATH,"//h2[text()='New Member Medication']")
    popup_realted_person=(By.XPATH,"//h2[text()='New Related Person']")
    popup_of_related_members=(By.XPATH,"(//h2[@class='slds-text-heading_medium slds-hyphenate'])[2]")
    new_medication_popup=(By.XPATH,"//h2[@class='slds-text-heading_medium slds-hyphenate']")
    new_creation=(By.XPATH,"//lightning-base-combobox-item[@data-value='actionCreateNew']")
    pop_up_creation=(By.XPATH,"//h2[@class='title slds-text-heading--medium slds-hyphenate']")
    pop_up_creation_new=(By.XPATH,"(//h2[@class='title slds-text-heading--medium slds-hyphenate'])[2]")
    Add=(By.XPATH,"//button[@name='SaveEdit']")
    Success_message_creation=(By.XPATH,"//span[@class='toastMessage slds-text-heading--small forceActionsText']")
    Creation=(By.XPATH,"//div[@class='modal-footer slds-modal__footer']//button//span[text()='Save']")
    Success_message_Added=(By.XPATH,"//div[contains(@id,'toastDescription')]//span")
    Close=(By.XPATH,"//button[@title='Close']")
    created_record_for_validation_plans=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.MemberPlanDetail__c.PlanDetailList__c']//a")
    existing_records=(By.XPATH, "//div[@class='slds-truncate']//a")
    move_carriers=(By.XPATH,"//span[text()='Available']")
    move_carriers_event=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Accepted_Carrier__c']")
    save_popup=(By.XPATH,"(//span[text()='Save'])[3]")
    new_popup=By.XPATH,"//button[@name='SaveEdit']"
    related_save=(By.XPATH,"//button[@name='submit']")
    save_parent_organization=(By.XPATH,"//h2[text()='New Parent organization']/following::*[self::span[text()='Save']]")
    save_practice_directroy=(By.XPATH,"//h2[text()='New Practice directory']/following::*[self::span[text()='Save']]")
    save_community_organization=(By.XPATH,"//h2[text()='New Community and senior organization']/following::*[self::span[text()='Save']]")
    #### For select options(Picklist)
    options_in_list=(By.XPATH,"//ul[@class='scrollable']//li//a")
    ### For a Creation of New Records
    newoptions_type=(By.XPATH,"//span[@class='slds-media__body']//a")
    #### For Typefields
    available_options=(By.XPATH,"//li[@class='slds-listbox__item']")
    follow_up_link=(By.XPATH,"//a[@class='subjectLink slds-truncate']")
    keen_campaign=(By.XPATH,"//input[@class='slds-combobox__input slds-input']")
    CommunityOrganization=(By.XPATH,"//a[@title='Community and senior organizations']")
    Keen_Events_CommunityOrganization=(By.XPATH,"//span[@title='Keen Events']")
    parent_organization=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Parent_organization_directory__c']//div[@class='contentWrapper slds-box--border']")
    # main_contact=(By.XPATH,'(//input[@placeholder="Search Keen's contacts..."])')
    ###  For creation of newrecords common fields for All Capture full Member Details
    ### field is for first div
    Field_01 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[1]")
    Field_02 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[2]")
    Field_03 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[3]")
    Field_04 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[4]")
    Field_05 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[5]")
    Field_06 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[6]")
    Field_07 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[7]")
    Field_08 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[8]")
    Field_09 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[9]")
    ### filed_d for second div
    Field_D_01=  (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/input)[1]")
    Field_D_02 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/input)[2]")
    Field_D_03 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/input)[3]")
    Field_D_04 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/input)[4]")
    Field_D_05 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/input)[5]")
    Field_D_06 = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/input)[6]")
    ### for select options
    Field_S_01=(By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/div/div/div/div/a)[1]")
    Field_S_02=(By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/div/div/div/div/a)[2]")
    Field_S_03=(By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/div/div/div/div/a)[3]")
    Field_S_04=(By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/div/div/div/div/a)[4]")
    Field_S_05=(By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/div/div/div/div/a)[5]")
    Field_S_06=(By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/div/div/div/div/a)[6]")
    ### For select options second div
    Field_SD_01=(By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/div/div/div/div/a)[1]")
    Field_SD_02 = (By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/div/div/div/div/a)[2]")
    Field_SD_03 = (By.XPATH,"(//div[@class ='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/div/div/div/div/a)[3]")
    Verify_Phone = (By.XPATH,"(//lightning-click-to-dial//span[2])[2]")
    Verify_Phone2=(By.XPATH,"//lightning-click-to-dial//span[2]")
    ### New keens Contact
    keen_contact_name=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div/div/div/div/div/input")
    contact_role=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[2]/div/div/div/div/input")
    contact_address=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div/div[2]/div/div/div/input")
    contact_address_line_2=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[2]/div[2]/div/div/div/input")
    contact_city=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[3]/div[2]/div/div/div/input")
    contact_title=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[3]/div/div/div/div/input")
    contact_phone=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[4]/div/div/div/div/input")
    contact_mobile=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[5]/div/div/div/div/input")
    contact_zipcode=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[5]/div[2]/div/div/div/input2")
    contact_fax=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[6]/div/div/div/div/input")
    contact_email=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[3]/div/div[7]/div/div/div/div/input")
    contact_move_to_choosen=(By.XPATH,"(//span[text()='Move selection to Chosen'])[2]")
    contact_move_to_available=(By.XPATH,"(//span[text()='Move selection to Available'])[2]")
    ##### New Parent Organization
    click_new_parent_organization=(By.XPATH,"//span[@title='New Parent organization']")
    parent_organizationname=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Name']//input")
    ## //div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Name']//input
    parent_organization_Address_line_1=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Address_line_1__c']//input")
    parent_organization_Address_line_2=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Address_line_2__c']//input")
    parent_organization_TaxId=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Tax_ID__c']//input")
    parent_organization_Email=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Email__c']//input")
    parent_organization_city=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.City__c']//input")
    parent_organization_phone=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Phone__c']//input")
    parent_organization_state=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.State__c']//a")
    parent_organization_zipcode=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Zip_code__c']//input")
    parent_organization_website=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Website__c']//input")
    parent_organization_status=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Parent_organization__c.Status__c']//a")
    parent_organization_popup=(By.XPATH,"//h2[text()='New Parent organization']")
    parent_organization_save=(By.XPATH,"(//button[@title='Save'])[2]")
    event_community=(By.XPATH,"//span[@title='New Community and senior organization']")
    def save_creation_parent_organization(self):
        return self.click_element(*Create_capture_member_details.parent_organization_save)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    row=(By.XPATH,"//td[@data-label='Strength']//span[1]")
    def click_organization(self):
        return self.click_element(*Create_capture_member_details.click_new_parent_organization)
    def new_parent_organization_popup(self):
        return self.get_text(*Create_capture_member_details.parent_organization_popup)
    def first_row(self):
        return self.driver.find_element(*Create_capture_member_details.row)
    ### For All options in Capture Full Member Details
    def select_member(self):
        return self.Find_Elements(*Create_capture_member_details.Member)
    def Capture_Full_Member(self):
        Capture_details= self.driver.find_element(*Create_capture_member_details.Member_details)
        return self.driver.execute_script("arguments[0].click();", Capture_details)
    def pop_up(self):
        return self.find_element(*Create_capture_member_details.Members_Popup)
    def click_new(self):
        return self.click_element(*Create_capture_member_details.new)
    def click_new_member(self):
        return self.click_element(*Create_capture_member_details.new_creation)
    def select_options_in_list(self):
        return self.Find_Elements(*Create_capture_member_details.options_in_list)
    def save_button_creation(self):
        return self.click_element(*Create_capture_member_details.Creation)
    def save_button_Add(self):
        return self.click_element(*Create_capture_member_details.Add)
    def save_related_person(self):
        return self.click_element(*Create_capture_member_details.related_save)
    def close(self):
        return self.click_element(*Create_capture_member_details.Close)
    def click_record(self):
        return self.click_element(*Create_capture_member_details.created_record_for_validation_plans)
    def pop_up_of_New_Members(self):
        return self.find_element(*Create_capture_member_details.pop_up_new_members)
    def popup_of_new_medication(self):
        return self.find_element(*Create_capture_member_details.new_medication_popup)
    def popup_related_persons(self):
        return self.find_element(*Create_capture_member_details.popup_realted_person)
    def pop_up_Newcreation(self):
        return self.find_element(*Create_capture_member_details.pop_up_creation)
    def select_optionsType(self):
        return self.Find_Elements(*Create_capture_member_details.available_options)
    def Click_Move_to_choosen_2(self):
        return self.click_element(*Create_capture_member_details.Move_to_chosen_2)
    def move_to_carriers(self):
        return self.find_element(*Create_capture_member_details.move_carriers)
    def select_options_type(self):
        return self.Find_Elements(*Create_capture_member_details.newoptions_type)
    def validation_of_records(self):
        return self.Find_Elements(*Create_capture_member_details.existing_records)
    def pop_up_Newcreation_event(self):
        return self.find_element(*Create_capture_member_details.pop_up_creation_new)
    def click_save_parent_organization(self):
        return self.click_element(*Create_capture_member_details.save_parent_organization)
    def click_save_practice_directroy(self):
        return self.click_element(*Create_capture_member_details.save_practice_directroy)
    def click_save_community_organization(self):
        return self.click_element(*Create_capture_member_details.save_community_organization)
    def click_new_event_community(self):
        return self.click_element(*Create_capture_member_details.event_community)
    def click_members_details_save(self):
        return self.click_element(*Create_capture_member_details.members_deatils_save)

### creation_of_plans
    associated_plans_for_member=(By.XPATH,"//th[@data-label='Members Physcian Name']//a")
    existing_record = (By.XPATH, "//lightning-base-combobox-formatted-text[@class='slds-truncate']")
    plans_record=(By.XPATH,"//lightning-base-combobox-formatted-text[@class='slds-truncate']")
    existing_record_practice_parent=(By.XPATH,"")
    plans_option=(By.XPATH,"//button[@title='Plans']")
    plans_records=(By.XPATH,"//input[@placeholder='Search PlanDetailsList...']")
    plan_contractnumber=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[2]/div/div/div/input)[2]")
    plan_producttype=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[2]/div/div/div/div/div/div/div/div/a")
    plan_carrier=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[3]/div/div/div/div/div/div/div/div/a")
    plan_options=(By.XPATH ,"//li[@class='uiMenuItem uiRadioMenuItem']//a")
    plan_state=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[5]/div/div/div/div/div/div/div/div/a")
    plan_verify=(By.XPATH ,"(//input[@data-value])")
    plan_hra_eligibility=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.PlanDetailList__c.HRA_Eligibility__c']//input")
    plan_offer_D=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.PlanDetailList__c.Offers_Part_D__c']//input")
    def verify_associated_plans_for_member(self):
        return self.Find_Elements(*Create_capture_member_details.associated_plans_for_member)
    def select_plans_record(self):
        return self.Find_Elements(*Create_capture_member_details.plans_record)
    def select_existing_records(self):
        return self.Find_Elements(*Create_capture_member_details.existing_record)
    def click_plans(self):
        return self.click_element(*Create_capture_member_details.plans_option)
    def click_plan_detail_list(self):
        return self.find_element(*Create_capture_member_details.plans_records)
    def enter_member_plan_details_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def  enter_PlanID(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_02)
    def click_carrier_name(self):
        return self.click_element(*Create_capture_member_details.plan_carrier)
    def click_product_type(self):
        return self.click_element(*Create_capture_member_details.plan_producttype)
    def enter_product_othertype(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_01)
    def select_product_type(self):
        return self.Find_Elements(*Create_capture_member_details.plan_options)
    def click_State(self):
        return self.click_element(*Create_capture_member_details.plan_state)
    def enter_carrier_other(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_03)
    def offers_planD(self):
        return self.click_element(*Create_capture_member_details.plan_offer_D)
    def click_Parent_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_06)
    def enter_contract_number(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_contractnumber)
    def enter_PBP(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_03)
    def enter_county(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_04)
    def enter_segment(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_04)
    def enter_Plan_year(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_05)
    def click_HRA_eligibility(self):
        return self.click_element(*Create_capture_member_details.plan_hra_eligibility)
    def validation_of_plan(self):
        return self.find_element(*Create_capture_member_details.plan_verify)
    ### New Members Plan popup
    plan_enrolled_keen=(By.XPATH,"//input[@name='Enrolled_by_Keen__c']")
    plan_carrier_member_id=(By.XPATH,"//input[@name='Carrier_member_ID__c']")
    plan_hra_completed=(By.XPATH,"//input[@name='HRA_completed__c']")
    plan_hra_date=(By.XPATH,"//input[@name='HRA_completed_date__c']")
    plan_effective_date=(By.XPATH,"//input[@name='Effective_date__c']")
    plan_number=(By.XPATH,"//input[@name='Enrollment_confirmation_number__c']")
    plan_enddate=(By.XPATH,"//input[@name='Plan_end_date__c']")
    plan_enrollmenttype=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.MemberPlanDetail__c.Enrollment_type__c']//button")
    plan_appsubmission_date=(By.XPATH,"//input[@name='App_submission_date__c']")
    plan_app_approvaldate=(By.XPATH,"//input[@name='App_approval_date__c']")
    plan_enrollment_date=(By.XPATH,"")
    plan_disenrollmentdate=(By.XPATH,"//input[@name='Disenrollment_date__c']")
    plan_beneficiary=(By.XPATH,"//textarea[@class='slds-textarea']")
    plan_amount=(By.XPATH,"//input[@name='Premium_Amount__c']")
    plan_policynumber=(By.XPATH,"//input[@name='Policy_Number__c']")
    plan_premium_frequency = (By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content align-with-title']//records-record-layout-row[17]//button")
    available_list_options=(By.XPATH,"//span[@class='slds-truncate']")
    app_declined=(By.XPATH,"//input[@name='App_declined__c']")
    physician_record=(By.XPATH,"//lightning-base-combobox-formatted-text[@title='NATASHA']")
    physician_record_list=(By.XPATH,"//h2[text()='Physician directory']/parent::slot/parent::lightning-layout-item/parent::div//div[@data-value]//span")
    physicians_records=(By.XPATH,"//h2[text()='Medication']/following::lightning-layout-item//div[@data-value]")
    def new_physcians_list(self):
        return self.Find_Elements(*Create_capture_member_details.physician_record_list)
    def select_physicians_records(self):
        return self.Find_Elements(*Create_capture_member_details.physicians_records)
    def click_physician_record(self):
        return self.click_element(*Create_capture_member_details.physician_record)
    def Enrolled_by_Keen(self):
        return self.click_element(*Create_capture_member_details.plan_enrolled_keen)
    def click_app_diclined(self):
        return self.click_element(*Create_capture_member_details.app_declined)
    def Carrier_member_ID(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_carrier_member_id)
    def hra_completd(self):
        return self.click_element(*Create_capture_member_details.plan_hra_completed)
    def HRA_completed_date(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_hra_date)
    def Effective_date__c(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_effective_date)
    def Enrollment_confirmation_number(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_number)
    def plan_end_date(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_enddate)
    def enrollment_type(self):
        return self.click_element(*Create_capture_member_details.plan_enrollmenttype)
    def App_submission_date(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_appsubmission_date)
    def App_approval_date(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_app_approvaldate)
    def Disenrollment_date(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_disenrollmentdate)
    def enter_Beneficiary(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_beneficiary)
    def click_premium_frequency(self):
        return self.click_element(*Create_capture_member_details.plan_premium_frequency)
    def select_options(self):
        return self.Find_Elements(*Create_capture_member_details.available_list_options)
    def enter_premium_ammount(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_amount)
    def enter_policy_number(self,text):
        return self.enter_text(text,*Create_capture_member_details.plan_policynumber)



    ###Edit plans

    new_plan=(By.XPATH,"//button[@title='Edit Member Plan Details Name']")
    new_plan_id=(By.XPATH, "//input[@name='PlanID__c']")
    new_carrier=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[2]")
    new_plan_offers_D=(By.XPATH,"//input[@name='Offers_Part_D__c']")
    new_county=(By.XPATH,"//input[@name='County__c']")
    new_producttype=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[1]")
    new_product_type_other=(By.XPATH,"//input[@name='ProductType_Other__c']")
    new_contract_number=(By.XPATH,"//input[@name='Contract_number__c']")
    new_PBP=(By.XPATH,"//input[@name='PBP__c']")
    new_plan_state=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[3]")
    new_segment=(By.XPATH,"//input[@name='Segment__c']")
    new_planyear=(By.XPATH,"//input[@name='Planyear__c']")
    click_save=(By.XPATH,"//button[@name='SaveEdit']")
    new_hra_eligibility=(By.XPATH,"//input[@name='HRA_Eligibility__c']")

    def edit_memberplan_name(self):
        return self.click_element(*Create_capture_member_details.new_plan)

    def edit_planID(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_plan_id)
    def edit_Carrier_Name(self):
        return self.click_element(*Create_capture_member_details.new_carrier)
    def edit_state(self):
        return self.click_element(*Create_capture_member_details.new_plan_state)
    def edit_county(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_county)
    def edit_product_type(self):
        return self.click_element(*Create_capture_member_details.new_producttype)
    def edit_ContractNumber(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_contract_number)
    def edit_PBP(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_PBP)
    def edit_segment(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_segment)
    def edit_planyear(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_planyear)
    def edit_save(self):
        return self.click_element(*Create_capture_member_details.click_save)
    ### Validation of Entered TestData
    verify_plan=(By.XPATH,"//records-record-layout-item[@field-label='Member Plan Details Name']//lightning-formatted-text")
    verify_planid=(By.XPATH,"//records-record-layout-item[@field-label='PlanID']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_carrier_name=(By.XPATH,"//records-record-layout-item[@field-label='Carrier Name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_carrier_other=(By.XPATH,"//records-record-layout-item[@field-label='Carrier_Other']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_state=(By.XPATH,"//records-record-layout-item[@field-label='State']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_county=(By.XPATH,"//records-record-layout-item[@field-label='County']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_product_type=(By.XPATH,"//records-record-layout-item[@field-label='Product Type']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_producttype_other=(By.XPATH,"//records-record-layout-item[@field-label='Product Type_Other']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_contract_number=(By.XPATH,"//records-record-layout-item[@field-label='Contract Number']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_pbp=(By.XPATH,"//records-record-layout-item[@field-label='PBP']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_segment=(By.XPATH,"//records-record-layout-item[@field-label='Segment']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_plan_year=(By.XPATH,"//records-record-layout-item[@field-label='Plan year']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_parent_organization=(By.XPATH,"//records-record-layout-item[@field-label='Parent Organization']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_offers_d=(By.XPATH,"//records-record-layout-item[@field-label='Offers Part D']/div/div/div[2]/span/slot/lightning-input")
    verify_app_approvaldate=(By.XPATH,"//records-record-layout-item[@field-label='App approval date']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_disnrollment_date=(By.XPATH,"//records-record-layout-item[@field-label='Disenrollment date']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_plan_detaillist=(By.XPATH,"//records-record-layout-item[@field-label='Plan Detail List']/div/div/div[2]/span/slot/force-lookup/div/records-hoverable-link/div//a")
    verify_member_id=(By.XPATH,"//records-record-layout-item[@field-label='Account number/Member ID']//lightning-formatted-text")
    verify_hradate=(By.XPATH,"//records-record-layout-item[@field-label='HRA completed date']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_effective_date=(By.XPATH,"//records-record-layout-item[@field-label='Effective date']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_enroll_number=(By.XPATH,"//records-record-layout-item[@field-label='Enrollment confirmation number']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_plan_enddate=(By.XPATH,"//records-record-layout-item[@field-label='Plan end date']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_enrollment_type=(By.XPATH,"//records-record-layout-item[@field-label='Enrollment type']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_app_submission_date=(By.XPATH,"//records-record-layout-item[@field-label='App submission date']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_beneficary=(By.XPATH,"//records-record-layout-item[@field-label='Beneficiary']/div/div/div[2]/span/slot/lightning-formatted-text")
    verfiy_premiumammount=(By.XPATH,"//records-record-layout-item[@field-label='Premium Amount']//lightning-formatted-text")
    verify_premium_frequency=(By.XPATH,"//records-record-layout-item[@field-label='Premium frequency']//lightning-formatted-text")
    verfiy_policy_number=(By.XPATH,"//records-record-layout-item[@field-label='Policy Number']//lightning-formatted-text")
    def validation_plan_name(self):
        return self.get_text(*Create_capture_member_details.verify_plan)
    def validation_planId(self):
        return self.get_text(*Create_capture_member_details.verify_planid)
    def validation_Carrier_Name(self):
        return self.get_text(*Create_capture_member_details.verify_carrier_name)
    def validation_Carrier_other(self):
        return self.get_text(*Create_capture_member_details.verify_carrier_other)
    def validation_state(self):
        return self.get_text(*Create_capture_member_details.verify_state)
    def validation_county(self):
        return self.get_text(*Create_capture_member_details.verify_county)
    def valiadtion_product_type(self):
        return self.get_text(*Create_capture_member_details.verify_product_type)
    def validation_producttype_other(self):
        return self.get_text(*Create_capture_member_details.verify_producttype_other)
    def validation_contract_number(self):
        return self.get_text(*Create_capture_member_details.verify_contract_number)
    def validation_PBP(self):
        return self.get_text(*Create_capture_member_details.verify_pbp)
    def validation_segment(self):
        return self.get_text(*Create_capture_member_details.verify_segment)
    def validation_Planyear(self):
        return self.get_text(*Create_capture_member_details.verify_plan_year)
    def validation_organization(self):
        return self.get_text(*Create_capture_member_details.verify_parent_organization)
    def validation_premium_frequency(self):
        return self.get_text(*Create_capture_member_details.verify_premium_frequency)
    def validation_policy_number(self):
        return self.get_text(*Create_capture_member_details.verfiy_policy_number)
    #### creation_of_Caregiver
    related_person=(By.XPATH,"//button[@title='Related Persons']")
    caregiver=(By.XPATH,"//button[@title='Care Givers']")
    search_record=(By.XPATH,"//input[@placeholder='Search Caregivers Directory...']")
    caregiver_city = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)8]")
    caregiver_zipcode = (By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content']/div/div/div[1]/div/div/div/input)[9]")
    caregiver_dob=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[2]/div/div/div/div/div/input")
    caregiver_phone_type=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Phone_type__c']//button")
    caregiver_options=(By.XPATH,"//li[@class='uiMenuItem uiRadioMenuItem']")
    caregiver_state=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[11]/div/div/div/div/div/div/div/div/a")
    caregiver_relationship=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[12]/div/div/div/div/div/div/div/div/a")
    verify_data=(By.XPATH,"//span[@class='test-id__field-value slds-form-element__static slds-grow word-break-ie11']")
    new_caregiver_creation=(By.XPATH,"//li[@data-name='New Caregiver']")
    list_keen_members=(By.XPATH,"//li[@data-name]")
    save_caregiver_creation=(By.XPATH,"//div[@class='center-align-buttons']//button[@name='SaveEdit']")
    def existing_list_caregivers(self):
        self.Find_Elements(*Create_capture_member_details.list_keen_members)
    def click_related_persons(self):
        return self.click_element(*Create_capture_member_details.related_person)
    def click_caregiver_option(self):
        return self.click_element(*Create_capture_member_details.caregiver)
    def click_Caregiver(self):
        return self.find_element(*Create_capture_member_details.search_record)
    def click_new_caregiver(self):
        return self.find_element(*Create_capture_member_details.new_caregiver_creation)
    def click_save_caregiver_creation(self):
        return self.click_element(*Create_capture_member_details.save_caregiver_creation)
    ##New Caregiver Directory
    def enter_caregiver_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def enter_date_of_birth(self,text):
        return self.enter_text(text,*Create_capture_member_details.caregiver_dob)
    def click_do_not_call(self):
        return self.click_element(*Create_capture_member_details.Field_02)
    def enter_email(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_03)
    def click_email_opt_out(self):
        return self.click_element(*Create_capture_member_details.Field_04)
    def enter_phone(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_05)
    def click_phone_type(self):
        return self.click_element(*Create_capture_member_details.caregiver_phone_type)
    def enter_other_phone(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_06)
    def enter_address_line_1(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_07)
    def enter_city(self,text):
        return self.enter_text(text,*Create_capture_member_details.caregiver_city)
    def click_state(self):
        return self.click_element(*Create_capture_member_details.caregiver_state)
    def click_relationship(self):
        return self.click_element(*Create_capture_member_details.caregiver_relationship)
    def select_Caregiver_options(self):
        return self.Find_Elements(*Create_capture_member_details.caregiver_options)
    def enter_zipcode(self,text):
        return self.enter_text(text,*Create_capture_member_details.caregiver_zipcode)

    def validation_of_record_data(self):
        return self.Find_Elements(*Create_capture_member_details.verify_data)
    def validation_phone(self):
        return self.get_text(*Create_capture_member_details.Verify_Phone2)
    def save_button(self):
        return self.click_element(*Create_capture_member_details.save_popup)
    def save_button_in_New_member_pop_up(self):
        return self.driver.find_element(*Create_capture_member_details.new_popup)
    ## Edit CareGivers
    edit_field=(By.XPATH,"//button[@title='Edit Date of birth']")
    new_name=(By.XPATH,"//input[@name='Name']")
    new_caregiver_dob=(By.XPATH,"//input[@name='Date_of_birth__c']")
    new_email=(By.XPATH,"//input[@name='Email__c']")
    new_email_optout=(By.XPATH,"//input[@name='Email_opt_out__c']")
    new_do_not_call=(By.XPATH,"//input[@name='Do_not_call__c']")
    new_phone=(By.XPATH,"//input[@name='Phone__c']")
    new_phonetype=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Phone_type__c']//button")
    new_otherphone=(By.XPATH,"//input[@name='Other_phone__c']")
    new_addressline=(By.XPATH,"//input[@name='Address_line_1__c']")
    new_caregiver_state=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.State__c']//button")
    #### Validation of caregiver record
    verify_name=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Name']//lightning-formatted-text")
    verify_email = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Email__c']//emailui-formatted-email-wrapper")
    verify_caregiver_dob = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Date_of_birth__c']//lightning-formatted-text")
    verify_caregiver_phone = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Phone__c']//lightning-formatted-phone")
    verify_caregiver_phone_type = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Phone_type__c']//lightning-formatted-text")
    verify_caregiver_otherphone = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Other_phone__c']//lightning-formatted-phone")
    verify_caregiver_addressline = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Address_line_1__c']//lightning-formatted-text")
    verify_caregiver_city = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.City__c']//lightning-formatted-text")
    verify_caregiver_state = (By.XPATH, "//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.State__c']//lightning-formatted-text")
    verify_caregiver_relationship=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Relationship__c']//lightning-formatted-text")
    verify_caregiver_zipcode=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Zipcode__c']//lightning-formatted-number")
    email_opt_out_check_box=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Email_opt_out__c']//lightning-input")
    ### is_checked = driver.execute_script("return arguments[0].checked;", checkbox)

    ## For all Capture Full Member Details
    new_city=(By.XPATH,"//input[@name='City__c']")
    new_Caregiverstate=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[2]")
    new_relationship=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Caregiver__c.Relationship__c']//button")
    new_zipcode=(By.XPATH,"//input[@name='Zipcode__c']")
    verify_cargiverphone=(By.XPATH, "//lightning-click-to-dial[@slot='outputField']//span[2]")
    verify_otherphone=(By.XPATH,"(//lightning-click-to-dial[@slot='outputField']//span[2])[2]")
    def edit_caregiver(self):
        return self.click_element(*Create_capture_member_details.edit_field)
    def edit_caregiver_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_name)
    def edit_Caregiverdate_of_birth(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_caregiver_dob)
    def edit_Caregiverdo_not_call(self):
        return self.click_element(*Create_capture_member_details.new_do_not_call)
    def edit_Caregiveremail(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_email)
    def edit_email_opt_out(self):
        return self.click_element(*Create_capture_member_details.new_email_optout)
    def edit_Caregiverphone(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_phone)
    def edit_Caregiverphone_type(self):
        return self.click_element(*Create_capture_member_details.new_phonetype)
    def edit_Caregiverother_phone(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_otherphone)
    def edit_Caregiveraddress_line_1(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_addressline)
    def edit_Caregivercity(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_city)
    def edit_Caregiver_state(self):
        return self.click_element(*Create_capture_member_details.new_Caregiverstate)
    def edit_Caregiverrelationship(self):
        return self.click_element(*Create_capture_member_details.new_relationship)
    def edit_Caregiverzipcode(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_zipcode)

    ### validation of Caregiver
    def validation_Caregiver_Name(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_01)

    def validation_Date_of_birth(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_02)

    def validation_Do_not_call(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_03)
    def validation_Email(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_04)
    def valiadtion_Email_opt_out(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_05)

    def validation_phone_caregiver(self):
        return self.driver.find_element(*Create_capture_member_details.verify_cargiverphone)

    def validation_edit_Phonetype(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_07)

    def validation_otherphone(self):
        return self.driver.find_element(*Create_capture_member_details.verify_otherphone)
    def validation__Address(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_09)
    def validation__city(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_10)
    def validation_state_caregiver(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_11)
    def validation_relationship(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_12)
    def validation_zipcode(self):
        return self.driver.find_element(*Create_capture_member_details.Verify_Field_13)
    ### Web_Elements for Practice Directory
    ### Creation of Practice for a Particular Member
    practice_record=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Member_practices__c.Practice_directory__c']//a")
    select_practices=(By.XPATH,"(//lightning-button[@data-id='practices'])[1]")
    create_record=(By.XPATH,"//input[@placeholder='Search Practice directory...']")
    NewAccount_creation = (By.XPATH, "//lightning-base-combobox-item[@data-value='actionCreateNew']")
    prcatice_name=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Name']//input")
    practice_NPI=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Practice_NPI__c']//input")
    practice_taxid=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.TaxID__c']//input")
    practice_phone=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Phone__c']//input")
    practice_email=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Practice_email__c']//input")
    practice_zipcode=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Zip_code__c']//input")
    practice_status=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Status__c']//a")
    practice_addressline1=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Address_line_1__c']//input")
    practice_city=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.City__c']//input")
    practice_state=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.State__c']//a")
    practice_aledade=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Aledade_Practice_Type__c']//a")
    practice_url=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Practice_URL__c']//input")
    Practice_organization = (By.XPATH, " //input[@title='Search Parent organization']")
    Practice_Main_contact = (By.XPATH, "//span[text()='Main contact']")
    Practice_Available_option = (By.XPATH, "//li[@class='slds-listbox__item']")
    Move_to_chosen = (By.XPATH, "(//button[@title='Move selection to Chosen'])[1]")
    Move_to_chosen_2=(By.XPATH,"(//button[@title='Move selection to Chosen'])[2]")
    Move_to_available = (By.XPATH, "//button[@title='Move selection to Available']")
    edit_practices=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Practice_directory__c.Name']//button")

   #### creation of New Practice Directory
    def click_practice_verify(self):
        return self.click_element(*Create_capture_member_details.practice_record)
    def click_edit_practices(self):
        return self.click_element(*Create_capture_member_details.edit_practices)
    def click_practices(self):
        return self.click_element(*Create_capture_member_details.select_practices)
    def click_practice_directory(self):
        return self.find_element(*Create_capture_member_details.create_record)
    def new_practice_directory(self):
        return self.click_element(*Create_capture_member_details.NewAccount_creation)
    def enter_practice_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.prcatice_name)
    def enter_practice_NPI(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_02)
    def enter_taxID(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_03)
    def enter_practice_email(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_05)
    def click_practice_organization(self):
        return self.find_element(*Create_capture_member_details.Practice_organization)
    def click_status(self):
        return self.click_element(*Create_capture_member_details.Field_S_02)
    def click_main_contact(self):
        return self.click_element(*Create_capture_member_details.Practice_Main_contact)
    def click_move_to_chosen(self):
        return self.click_element(*Create_capture_member_details.Move_to_chosen)
    def click_to_available(self):
        return self.click_element(*Create_capture_member_details.Practice_Available_option)
    def click_Aledade_Practice_Type(self):
        return self.click_element(*Create_capture_member_details.Field_S_04)
    def enter_practice_url(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_06)
    def enter_Address_line_1(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_01)
    def Address_line_2(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_02)
    def enter_City(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_03)
    def click_state_of_practice(self):
        return self.click_element(*Create_capture_member_details.Field_SD_01)
    def enter_Practice_Phone(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_04)
    def enter_Zipcode(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_04)
    ####Web Elements for Practices
    ### New Creation and Edit of Practice Records in Practice Tab
    PracticesNew_NPI = (By.XPATH, "//input[@name='Practice_NPI__c']")
    PracticesNew_taxID = (By.XPATH, "//input[@name='TaxID__c']")
    PracticesNew_email = (By.XPATH, "//input[@name='Practice_email__c']")
    PracticesNew_phone = (By.XPATH, " (//input[@name='Phone__c'])[2]")
    PracticesNew_status = (
    By.XPATH, "(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[5]")
    PracticesNew_main_contact = (By.XPATH, "//span[text()='Main contact']")
    PracticesNewselect_Available_option = (By.XPATH, "//li[@class='slds-listbox__item']")
    PracticesNew_Aledade_Practice_Type = (
    By.XPATH, "(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[6]")
    PracticesNew_url = (By.XPATH, "//input[@name='Practice_URL__c']")
    New_Address_line_2 = (By.XPATH, "//input[@name='Address_line_2__c']")
    PracticesNew_City = (By.XPATH, "//input[@name='City__c']")
    PracticesNew_state = (By.XPATH, "(//div[@class='uiPopupTrigger']//a)[2]")
    PracticesNew_Zipcode = (By.XPATH, "(//input[@data-aura-class='uiInputSmartNumber'])[3]")
    ### Edit Practice Records
    def edit_practices_NPI(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_NPI)
    def edit_taxID(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_taxID)
    def edit_practice_email(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_email)
    def edit_practice_phone(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_phone)
    def edit_practice_status(self):
        return self.click_element(*Create_capture_member_details.PracticesNew_status)
    def edit_main_contact(self):
        return self.click_element(*Create_capture_member_details.PracticesNew_main_contact)
    def edit_select_Available_option(self):
        return self.Find_Elements(*Create_capture_member_details.available_options)
    def edit_Aledade_Practice_Type(self):
        return self.click_element(*Create_capture_member_details.PracticesNew_Aledade_Practice_Type)
    def edit_practice_url(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_url)
    def edit_Address_line_1(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_addressline)
    def edit_Address_line_2(self,text):
        return self.enter_text(text,*Create_capture_member_details.New_Address_line_2)
    def edit_City(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_City)
    def edit_state_of_practice(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_state)
    def edit_Zipcode(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticesNew_Zipcode)
    ##### Validation of Practice directory
    verify_practicename=(By.XPATH,"//records-record-layout-item[@field-label='Practice name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_practiceNPI=(By.XPATH,"//records-record-layout-item[@field-label='Practice NPI']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_practiceTaxId=(By.XPATH,"//records-record-layout-item[@field-label='TaxID']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_practiceEmail=(By.XPATH,"//records-record-layout-item[@field-label='Practice email']/div/div/div[2]/span/slot/emailui-formatted-email-wrapper")
    verify_practice_organization=(By.XPATH,"//records-record-layout-item[@field-label='Parent organization directory']/div/div/div[2]/span/slot/force-lookup/div")
    verify_practice_status=(By.XPATH,"//records-record-layout-item[@field-label='Status']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_acceptedcarriers=(By.XPATH,"//records-record-layout-item[@field-label='Accepted Carriers']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_contact_main=(By.XPATH,"//records-record-layout-item[@field-label='Main contact']/div/div/div[2]/span/slot/force-lookup/div")
    verify_practice_type=(By.XPATH,"//records-record-layout-item[@field-label='Aledade Practice Type']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_practice_url=(By.XPATH,"//records-record-layout-item[@field-label='Practice URL']/div/div/div[2]/span/slot/lightning-formatted-text")
    def validation_practice_name(self):
        return self.get_text(*Create_capture_member_details.verify_practicename)
    def validation_practice_NPI(self):
        return self.get_text(*Create_capture_member_details.verify_practiceNPI)
    def validation_practice_taxID(self):
        return self.get_text(*Create_capture_member_details.verify_practiceTaxId)
    def validation_practice_email(self):
        return self.get_text(*Create_capture_member_details.verify_practiceEmail)
    def validation_practice_organization(self):
        return self.get_text(*Create_capture_member_details.verify_practice_organization)
    def validation_Practice_status(self):
        return self.get_text(*Create_capture_member_details.verify_practice_status)
    def validation_Practicemain_contact(self):
        return self.get_text(*Create_capture_member_details.verify_contact_main)
    def validation_Practiceacceptedcarriers(self):
        return self.get_text(*Create_capture_member_details.verify_acceptedcarriers)
    def validation_Aledade_Practice_Type(self):
        return self.get_text(*Create_capture_member_details.verify_practice_type)
    def validation_practice_url(self):
        return self.get_text(*Create_capture_member_details.verify_practice_url)
    def validation_PracticeAddress_line_1(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_1)
    def validation_practiceAddress_line_2(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_2)
    def validation_PracticeCity(self):
        return self.get_text(*Create_capture_member_details.verify_City)
    def validation_PracticePhone(self):
        return self.get_text(*Create_capture_member_details.Verify_Phone2)
    def validation_state_practice(self):
        return self.get_text(*Create_capture_member_details.verify_state)
    def validation_practice_zipcode(self):
        return self.get_text(*Create_capture_member_details.verify_zipcode)

    #### Web Elements of Medictions
    medication=(By.XPATH, "//button[@title='Medications']")
    search_medication=(By.XPATH, "//input[@placeholder='Search Medication directory..']")
    medication_ValidUntil=(By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[9]/div[1]/div/div/div/div/input")
    pharmaClass=(By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[11]/div/div/div/div/textarea")
    medication_record=(By.XPATH, "(//input[@class='slds-combobox__input slds-input slds-combobox__input-value'])[2]")
    quantityperfill=(By.XPATH, "//input[@name='Quantity_per_refill__c']")
    refillfrequency=(By.XPATH, "//button[@name='Refill_frequency__c']")
    options=(By.XPATH, "//lightning-base-combobox-item[@data-value]")
    drug_form=(By.XPATH,"//button[@name='DrugForm__c']")
    drug_strength=(By.XPATH,"//button[@name='Strength__c']")
    select_first_option=(By.XPATH,"//button[@name='DrugForm__c']/parent::div/parent::div//div//lightning-base-combobox-item")
    select_first_option_strength = (By.XPATH,"(//h2[text()='Strength']/following::lightning-layout-item//span[@title])[1]")
    #### creation_of_Medications

    def Medication_option(self):
        return self.click_element(*Create_capture_member_details.medication)
    def medication_search(self):
        return self.find_element(*Create_capture_member_details.search_medication)
    def Member_medication_popup(self):
        return self.find_element(*Create_capture_member_details.pop_up_of_medications)
    def enter_medication(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_01)
    def click_Branded_generic(self):
        return self.click_element(*Create_capture_member_details.Field_S_01)
    def click_Drug_form(self):
        return self.click_element(*Create_capture_member_details.Field_S_02)
    def enter_strength(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_02)
    def enter_strength_units(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_03)
    def enter_packaging(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_04)
    def enter_daily_frequency(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_05)
    def enter_daily_quantity(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_06)
    def enter_valid_until(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_ValidUntil)
    def enter_drug_form_other(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_07)
    def enter_pharm_class(self,text):
        return self.enter_text(text,*Create_capture_member_details.pharmaClass)
    def enter_refill_quantity(self,text):
        return self.enter_text(text,*Create_capture_member_details. Field_08)
    def click_refill_frequency(self):
        return self.click_element(*Create_capture_member_details.Field_S_03)
    def validation_of_created(self):
        return self.driver.find_element(*Create_capture_member_details.medication_record)
    def Quantity_per_fill(self,text):
        return self.enter_text(text,*Create_capture_member_details.quantityperfill)
    def Refill_frequency(self):
        return self.click_element(*Create_capture_member_details.refillfrequency)
    def select_frequency(self):
        return self.Find_Elements(*Create_capture_member_details.options)
    def verify_drug_form(self):
        return self.find_element(*Create_capture_member_details.drug_form)
    def verify_strength(self):
        return self.click_element(*Create_capture_member_details.drug_strength)
    def click_firstoption_strength(self):
        return self.click_element(*Create_capture_member_details.select_first_option_strength)
    def click_first_element(self):
        return self.Find_Elements(*Create_capture_member_details.select_first_option)
    #### Validation of Medications
    medication_name=(By.XPATH,"//records-record-layout-item[@field-label='Medication']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_Brand=(By.XPATH,"//records-record-layout-item[@field-label='Branded Generic']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_drug=(By.XPATH,"//records-record-layout-item[@field-label='Drug Form']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_strength=(By.XPATH,"//records-record-layout-item[@field-label='Strength']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_strength_units=(By.XPATH,"//records-record-layout-item[@field-label='Strength_units']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_packaging=(By.XPATH,"//records-record-layout-item[@field-label='Packaging']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_dailyfrequency=(By.XPATH,"//records-record-layout-item[@field-label='Daily Frequency']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_dailyquantity=(By.XPATH,"//records-record-layout-item[@field-label='Daily Quantity']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_valid=(By.XPATH,"//records-record-layout-item[@field-label='Valid Until']/div/div/div[2]/span/slot/lightning-formatted-text")
    medication_refill=(By.XPATH,"(//records-record-layout-item[@field-label='Refill frequency']/div/div/div[2]/span/slot/lightning-formatted-text)[2]")
    medication_quantity=(By.XPATH,"//records-record-layout-item[@field-label='Refill quantity']/div/div/div[2]/span/slot/lightning-formatted-number")
    def validation_MedicationName(self):
        return self.get_text(*Create_capture_member_details.medication_name)
    def validation_BrandedGenric(self):
        return self.get_text(*Create_capture_member_details.medication_Brand)
    def validation_DrugForm(self):
        return self.get_text(*Create_capture_member_details.medication_drug)
    def validation_Strength(self):
        return self.get_text(*Create_capture_member_details.medication_strength)
    def validation_StrengthUnits(self):
        return self.get_text(*Create_capture_member_details.medication_strength_units)
    def validation_Packaging(self):
        return self.get_text(*Create_capture_member_details.medication_packaging)
    def validation_DailyFrequency(self):
        return self.get_text(*Create_capture_member_details.medication_dailyfrequency)
    def validation_DailyQuantity(self):
        return self.get_text(*Create_capture_member_details.medication_dailyquantity)
    def validation_ValidUntil(self):
        return self.get_text(*Create_capture_member_details.medication_valid)
    def validation_RefillFrequency(self):
        return self.get_text(*Create_capture_member_details.medication_refill)
    def validation_RefillQuantity(self):
        return self.get_text(*Create_capture_member_details.medication_quantity)

    ### New Creation of Medication and Editing the Medications
    medication_Newedit_branded=(By.XPATH,"//button[@title='Edit Branded Generic']")
    medication_Newdrugform=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[2]")
    medication_Newstrength=(By.NAME,"Strength__c")
    medication_Newstrengthunits=(By.NAME,"Strength_units__c")
    medication_options=By.XPATH,"//lightning-base-combobox-item"
    medication_Newpackaging=(By.NAME,"Packaging__c")
    medication_NewDailyfrequency=(By.NAME,"Daily_Frequency__c")
    pharmaclass_New=By.XPATH,"//textarea[contains(@id,';a')]"
    medication_NewDailQuantity=(By.NAME,"Daily_Quantity__c")
    medication_NewValidUntil=(By.NAME,"ValidUntil__c")
    medication_NewDrugFormOther=(By.NAME,"DrugFormOther__c")
    medication_NewRefillQuantity=(By.NAME,"Refill_quantity__c")
    medication_NewrefillFrequency=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[3]")
    def click_NewBranded_generic(self):
        return self.click_element(*Create_capture_member_details.medication_Newedit_branded)
    def select_Options(self):
        return self.Find_Elements(*Create_capture_member_details.medication_options)
    def click_NewDrug_form(self):
        return self.click_element(*Create_capture_member_details.medication_Newdrugform)
    def enter_Newstrength(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_Newstrength)
    def enter_Newstrength_units(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_Newstrengthunits)
    def enter_Newpackaging(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_Newpackaging)
    def enter_Newdaily_frequency(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_NewDailyfrequency)
    def enter_Newdaily_quantity(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_NewDailQuantity)
    def enter_Newvalid_until(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_NewValidUntil)
    def enter_Newdrug_form_other(self,text):
        return self.enter_text(text,*Create_capture_member_details.medication_NewDrugFormOther)
    def enter_Newpharm_class(self,text):
        return self.find_element(text,*Create_capture_member_details.pharmaclass_New)
    def enter_Newrefill_quantity(self,text):
        return self.find_element(text,*Create_capture_member_details.medication_NewRefillQuantity)
    def click_Newrefill_frequency(self):
        return self.click_element(*Create_capture_member_details.medication_NewrefillFrequency)

    ### Creation of Hospitals
    hospital_record=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Member_s_hospitals__c.Hospital_directory__c']//a")
    select_hospitals=(By.XPATH,"//button[@title='Hospitals']")
    new_hospital=(By.XPATH,"//input[@placeholder='Search Hospitals and health systems...']")
    hospital_location=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[2]/div/div/div/div/input")
    hospital_addressline_1=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[3]/div/div/div/div/input")
    hospital_addressline_2=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[4]/div/div/div/div/input")
    hospital_city=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[5]/div/div/div/div/input")
    hospital_zipcode=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[7]/div/div/div/div/input")
    hospital_npi=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[8]/div/div/div/div/input")
    hospital_taxid=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[9]/div/div/div/div/input")
    hospital_phone=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[14]/div/div/div/div/input")
    hospital_contactname=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[15]/div/div/div/div/input")
    hospital_contactemail=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[16]/div/div/div/div/input")
    hospital_contactphone=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[17]/div/div/div/div/input")
    hospital_website=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[18]/div/div/div/div/input")
    def click_hospital_verify(self):
        return self.click_element(*Create_capture_member_details.hospital_record)
    def click_hospitals(self):
        return self.click_element(*Create_capture_member_details.select_hospitals)
    def click_Hospital_directory(self):
        return self.find_element(*Create_capture_member_details.new_hospital)
    def enter_hospital_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def enter_hospital_location(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_location)
    def enter_address_line1_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_addressline_1)
    def enter_address_line2_hospital(self,text):
        return self.enter_text(*Create_capture_member_details.hospital_addressline_2)
    def enter_city_hospitals(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_city)
    def click_state_hospitals(self):
        return self.click_element(*Create_capture_member_details.Field_S_01)
    def enter_zipcode_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_zipcode)
    def enter_NPI(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_npi)
    def enter_TaxId_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_taxid)
    def click_status_hospitals(self):
        return self.driver.find_element(*Create_capture_member_details.Field_S_02)
    def enter_phone_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_phone)
    def enter_contact_name_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_contactname)
    def enter_contact_email_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_contactemail)
    def enter_contact_phone_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_contactphone)
    def enter_website_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.hospital_website)

    def success_message_of_records(self):
        return self.driver.find_element(*Create_capture_member_details.Success_message_creation)


    #### Creation and Editing the Hospitals in a Hospital Tab
    click_eidt_hospitals=(By.XPATH,"//button[@title='Edit Hospital location']")
    new_hospital_location=(By.XPATH,"//input[@name='Hospital_location__c']")
    new_hospital_city=(By.XPATH,"//input[@name='City__c']")
    new_hospital_state=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[1]")
    new_hospital_zipcode=(By.XPATH,"//input[@name='Zip_code__']")
    new_hospital_npi=(By.XPATH,"//input[@name='NPI__c']")
    new_hospital_taxid=(By.XPATH,"//input[@name='Tax_ID__c']")
    new_hospital_status=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[2]")
    new_hospital_contactname=(By.XPATH,"//input[@name='Contact_name__c']")
    new_hospital_contactemail=(By.XPATH,"//input[@name='Contact_email__c']")
    new_hospital_contactphone=(By.XPATH,"//input[@name='Contact_phone__c']")
    new_hospital_website=(By.XPATH,"//input[@name='Website__c']")
    def edit_hospitals(self):
        return self.click_element(*Create_capture_member_details.click_eidt_hospitals)
    def edit_hospital_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_name)
    def edit_hospital_location(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_location)
    def edit_address_line1_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_addressline)
    def edit_address_line2(self,text):
        return self.enter_text(text,*Create_capture_member_details.New_Address_line_2)
    def edit_city_hospitals(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_city)
    def edit_state_hospitals(self):
        return self.click_element(*Create_capture_member_details.new_hospital_state)
    def edit_zipcode_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_zipcode)
    def edit_NPI(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_npi)
    def edit_TaxId_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_taxid)
    def edit_status_hospitals(self):
        return self.click_element(*Create_capture_member_details.new_hospital_status)
    def edit_phone_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_phone)
    def edit_contact_name_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_contactname)
    def edit_contact_email_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_contactemail)
    def edit_contact_phone_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_contactphone)
    def edit_website_hospital(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_hospital_website)
    def success_message(self):
        return self.driver.find_element(*Create_capture_member_details.Success_message_Added)
    ### Validation of Hospitals
    verify_hospital_name=(By.XPATH,"//records-record-layout-item[@field-label='Hospital Name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_hospital_location=(By.XPATH,"//records-record-layout-item[@field-label='Hospital location']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_addressline_1=(By.XPATH,"//records-record-layout-item[@field-label='Address line 1']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_addressline_2=(By.XPATH,"//records-record-layout-item[@field-label='Address line 2']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_City=(By.XPATH,"//records-record-layout-item[@field-label='City']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_zipcode=(By.XPATH,"//records-record-layout-item[@field-label='Zip code']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_hospital_npi=(By.XPATH,"//records-record-layout-item[@field-label='NPI']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_hospital_taxid=(By.XPATH,"//records-record-layout-item[@field-label='Tax ID']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_status=(By.XPATH,"//records-record-layout-item[@field-label='Status']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_hospital_parent_organization=(By.XPATH,"//records-record-layout-item[@field-label='Parent organization directory']/div/div/div[2]/span/slot/force-lookup")
    verify_phone=(By.XPATH,"//records-record-layout-item[@field-label='Phone']/div/div/div[2]/span/slot/lightning-click-to-dial")
    verify_hospital_contactname=(By.XPATH,"//records-record-layout-item[@field-label='Contact name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_hospital_contactphone=(By.XPATH,"//records-record-layout-item[@field-label='Contact phone']/div/div/div[2]/span/slot/lightning-click-to-dial")
    verify_hospital_contactemail=(By.XPATH,"//records-record-layout-item[@field-label='Contact email']/div/div/div[2]/span/slot/emailui-formatted-email-wrapper")
    verify_website=(By.XPATH,"//records-record-layout-item[@field-label='Website']/div/div/div[2]/span/slot/lightning-formatted-url")
    def validation_HospitalName(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_name)
    def validation_HospitalLocation(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_location)
    def validation_HospitalAddress(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_1)
    def validation_hospitaladdress_line_2(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_2)
    def validation_HospitalCity(self):
        return self.get_text(*Create_capture_member_details.verify_City)
    def validation_HospitalState(self):
        return self.get_text(*Create_capture_member_details.verify_state)
    def validation_HospitalZipcode(self):
        return self.get_text(*Create_capture_member_details.verify_zipcode)
    def validation_HospitalNPI(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_npi)
    def validation_HospitalTaxID(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_taxid)
    def validation_HospitalStatus(self):
        return self.get_text(*Create_capture_member_details.verify_status)
    def validation_HospitalParentOrganization(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_parent_organization)
    def validation_HospitalPhone(self):
        return self.get_text(*Create_capture_member_details.verify_phone)
    def validation_HospitalContactName(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_contactname)
    def validation_HospitalContact_Email(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_contactemail)
    def validation_HospitalContact_Phone(self):
        return self.get_text(*Create_capture_member_details.verify_hospital_contactphone)
    def validation_Hospital_Website(self):
        return self.get_text(*Create_capture_member_details.verify_website)

    #### Members Campaigns
    click_campaigns=(By.XPATH,"//button[@title='Campaigns']")
    campaign=(By.XPATH,"//input[@placeholder='Search Keen campaigns...']")
    campaign_startdate=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[4]/div/div/div/fieldset/div/div/input")
    campaign_starttime=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[4]/div/div/div/fieldset/div/div/div/input")
    campaign_enddate=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[5]/div/div/div/fieldset/div/div/input")
    campaign_endtime=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content']/div/div[5]/div/div/div/fieldset/div/div/div/input")

    def select_campaigns(self):
        return self.click_element(*Create_capture_member_details.click_campaigns)
    def search_keen_campaign(self):
        return self.find_element(*Create_capture_member_details.campaign)
    def enter_campaign_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def enter_startdate(self,text):
        return self.enter_text(text,*Create_capture_member_details.campaign_startdate)
    def enter_starttime(self,text):
        return self.enter_text(text,*Create_capture_member_details.campaign_starttime)
    def enter_enddate(self,text):
        return self.enter_text(text,*Create_capture_member_details.campaign_enddate)
    def enter_endtime(self,text):
        return self.enter_text(text,*Create_capture_member_details.campaign_endtime)
    def enter_budget(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_02)
    def enter_member_contacted(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_03)
    ### Edit Campaigns
    new_campaigns=(By.XPATH,"//button[@title='Edit Type']")
    new_options=(By.XPATH,"//li[@class='slds-listbox__item']")
    new_startname=(By.XPATH,"(//input[@name='Start_Date__c'])[1]")
    new_starttime=(By.XPATH,"(//input[@name='Start_Date__c'])[2]")
    new_enddate=(By.XPATH,"(//input[@name='End_Date__c'])[1]")
    new_endtime=(By.XPATH,"(//input[@name='End_Date__c'])[2]")
    def edit_campaigns(self):
        return self.click_element(*Create_capture_member_details.new_campaigns)
    def eidt_available(self):
        return self.Find_Elements(*Create_capture_member_details.new_options)
    def edit_StartDate(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_startname)
    def edit_StartTime(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_starttime)
    def edit_EndDate(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_enddate)
    def edit_EndTime(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_endtime)
    ### Validation of Campaigns
    verify_campaignname=(By.XPATH,"//records-record-layout-item[@field-label='Campaign Name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_type=(By.XPATH,"//records-record-layout-item[@field-label='Type']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_start_date=(By.XPATH,"//records-record-layout-item[@field-label='Start Date']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_end_date=(By.XPATH,"//records-record-layout-item[@field-label='End Date']/div/div/div[2]/span/slot/lightning-formatted-text")
    def validation_CampaignName(self):
        return self.get_text(*Create_capture_member_details.verify_campaignname)
    def validation_StartTime_Date(self):
        return self.get_text(*Create_capture_member_details.verify_start_date)
    def validation_EndTime_Date(self):
        return self.get_text(*Create_capture_member_details.verify_end_date)
    def validation_Campaign_Type(self):
        return self.get_text(*Create_capture_member_details.verify_type)
    ##### create Physicians
    click_physicians=(By.XPATH,"//button[@title='Physicians']")
    physician_record_select=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Member_s_physician__c.Physician_directory__c']//a")
    physician=(By.XPATH,"//input[@placeholder='Search Physician directory..']")
    primary_physician=(By.XPATH,"//input[@name='Is_Primary_Care_Physician__c']/parent::span//span[@class='slds-checkbox_faux']")
    state_members_popup=(By.XPATH,"//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value']")
    moveto_subspecialty=(By.XPATH,"//div[text()='Subspecialty']")
    physician_lastname=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[1]/div/div/div/div/input")
    physician_firstname=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[2]/div/div/div/div/input")
    physician_npi=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[3]/div/div/div/div/input")
    physician_city=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[3]/div[2]/div/div/div/input")
    physician_state=(By.XPATH,"//div[@class='slds-form form-horizontal slds-is-editing']/div[4]/div[2]//a")
    physician_address_line2=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[2]/div[2]/div/div/div/input")
    physician_address=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div/div[2]/div/div/div/input")
    physician_phone=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[4]/div/div/div/div/input")
    physician_email=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[5]/div/div/div/div/input")
    physician_zipcode=(By.XPATH,"(//div[@class='test-id__section-content slds-section__content section__content'])[2]/div/div[5]/div[2]/div/div/div/input")
    physician_move_to_choosen=(By.XPATH,"(//button[@title='Move selection to Chosen'])[4]")
    physician_move_to_available=(By.XPATH,"(//button[@title='Move selection to Available'])[4]")
    new_member_physician_state=(By.XPATH,"//div[@class='slds-form']//records-record-layout-row[6]//button")
    member_physician_state=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Member_s_physician__c.State__c']//button")
    def select_physicians(self):
        return self.click_element(*Create_capture_member_details.click_physicians)
    def select_physician_record(self):
        return self.click_element(*Create_capture_member_details.physician_record_select)
    def click_physician_directory(self):
        return self.find_element(*Create_capture_member_details.physician)
    def enter_last_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def enter_address_line_1_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_01)
    def enter_firstname_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_02)
    def enter_NPI_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_03)
    def enter_city_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_03)
    def state_physicians(self):
        return self.click_element(*Create_capture_member_details.Field_SD_01)
    def Subspecialty(self):
        return self.find_element(*Create_capture_member_details.moveto_subspecialty)
    def enter_phone_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_04)
    def enter_Email_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_05)
    def enter_zipcode_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_04)
    def click_Is_Primary_Care_Physician(self):
        return self.click_element(*Create_capture_member_details.primary_physician)
    def enter_city_physician(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_city)
    def click_state_physicians(self):
        return self.click_element(*Create_capture_member_details.physician_state)
    def click_new_member_physician_state(self):
        return self.click_element(*Create_capture_member_details.new_member_physician_state)
    def select_state_physicians(self):
        return self.Find_Elements(*Create_capture_member_details.options)
    def zipcode_pysicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_zipcode)
    def click_Physician_move_to_choosen(self):
        return self.click_element(*Create_capture_member_details.physician_move_to_choosen)
    def click_Physician_move_to_available(self):
        return self.click_element(*Create_capture_member_details.physician_move_to_available)
    #### Edit Physicians
    new_physicians=(By.XPATH,"//button[@title='Edit First name']")
    new_physiciansaddress=(By.XPATH,"//input[@name='Address_line__c']")
    new_physicians_firstname=(By.XPATH,"//input[@name='First_name__c']")
    new_physiciansnpi=(By.XPATH,"//input[@name='NPI__c']")
    new_physicianstate=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[1]")
    new_subspecialty=(By.XPATH,"//span[@class='slds-media__body']")
    def edit_physicians(self):
        return self.click_element(*Create_capture_member_details.new_physicians)
    def edit_last_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_name)
    def edit_address_line_1_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_physiciansaddress)
    def edit_firstname_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_physicians_firstname)
    def edit_NPI_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_physiciansnpi)
    def edit_city_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_city)
    def edit_state_physicians(self):
        return self.click_element(*Create_capture_member_details.new_physicianstate)
    def edit_Subspecialty(self):
        return self.Find_Elements(*Create_capture_member_details.new_subspecialty)
    def edit_superspecialty(self):
        return self.Find_Elements(*Create_capture_member_details.new_subspecialty)
    def edit_phone_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_phone)
    def edit_Email_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_email)
    def edit_zipcode_physicians(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_zipcode)
    ### Validation of Physicians
    verify_physician_lastname=(By.XPATH,"//records-record-layout-item[@field-label='Last Name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_physician_firstname=(By.XPATH,"//records-record-layout-item[@field-label='First name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_physician_npi=(By.XPATH,"//records-record-layout-item[@field-label='NPI']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_physician_address_line_1=(By.XPATH,"//records-record-layout-item[@field-label='Address line']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_physician_email=(By.XPATH,"//records-record-layout-item[@field-label='Email']/div/div/div[2]/span/slot/emailui-formatted-email-wrapper")
    verify_physician_speciality=(By.XPATH,"//records-record-layout-item[@field-label='Specialty']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_physician_subspeciality=(By.XPATH,"//records-record-layout-item[@field-label='Subspecialty']/div/div/div[2]/span/slot/lightning-formatted-text")
    def validation_Physician_LastName(self):
        return self.get_text(*Create_capture_member_details.verify_physician_lastname)
    def validation_Physician_Firstname(self):
        return self.get_text(*Create_capture_member_details.verify_physician_firstname)
    def validation_Physician_Addressline(self):
        return self.get_text(*Create_capture_member_details.verify_physician_address_line_1)
    def validation_Physician_NPI(self):
        return self.get_text(*Create_capture_member_details.verify_physician_npi)
    def validation_Physician_City(self):
        return self.get_text(*Create_capture_member_details.verify_City)
    def validation_Physicain_Phone(self):
        return self.get_text(*Create_capture_member_details.verify_phone)
    def validation_Physician_State(self):
        return self.get_text(*Create_capture_member_details.verify_state)
    def validation_Physician_Email(self):
        return self.get_text(*Create_capture_member_details.verify_physician_email)
    def validation_Physician_Zipcode(self):
        return self.get_text(*Create_capture_member_details.verify_zipcode)
    def validation_Physician_Specialty(self):
        return self.get_text(*Create_capture_member_details.verify_physician_speciality)
    def validation_Physician_Subspecialty(self):
        return self.get_text(*Create_capture_member_details.verify_physician_subspeciality)
    ### outbound referral Practice
    click_outbound=(By.XPATH, "//button[@title='Outbound Referrals Practice']")
    practice=(By.XPATH, "//input[@placeholder='Search Practice directory...']")
    def select_outbound_referral(self):
        return self.click_element(*Create_capture_member_details.click_outbound)
    def search_practice_directory(self):
        return self.driver.find_element(*Create_capture_member_details.practice)
    ## Creation of Members Pharmacies
    ### For New Pharmacy directory
    pharmacies=(By.XPATH, "//button[@title='Pharmacies']")
    search_pharmacy=(By.XPATH, "//input[@placeholder='Search Pharmacy directory...']")
    primary_pharmacy=(By.XPATH, "//span[text()='Is Pharmacy Primary']")
    cancel_pharmacy=(By.XPATH,"//li[@data-target-selection-name='sfdc:StandardButton.Member_s_pharmacy__c.CancelEdit']//button")
    def select_pharmacies(self):
        return self.click_element(*Create_capture_member_details.pharmacies)
    def pharmacy_directory(self):
        return self.find_element(*Create_capture_member_details.search_pharmacy)
    def enter_pharmacy_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def enter_Address_pharmacy(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_01)
    def enter_phone_pharmacy(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_02)
    def click_Pharmacy_chain(self):
        return self.click_element(*Create_capture_member_details.Field_S_01)
    def enter_City_pharmacy(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_03)
    def click_mail_order_pharmacy(self):
        return self.click_element(*Create_capture_member_details.Field_S_02)
    def click_state_pharmacy(self):
        return self.click_element(*Create_capture_member_details.Field_SD_01)
    def click_status_pharmacy(self):
        return self.click_element(*Create_capture_member_details.Field_S_03)
    def enter_zipcode_pharmacy(self,text):
        return self.driver.find_element(text,*Create_capture_member_details.Field_D_04)
    def is_primary_pharmacy(self):
        return self.driver.find_element(*Create_capture_member_details.primary_pharmacy)
    def click_cancel_pharcmacy(self):
        return self.click_element(*Create_capture_member_details.cancel_pharmacy)
    ### creation and Edit the Pharmacies from Pharmacy Directory
    edit_pharmacies=(By.XPATH,"//button[@title='Edit Pharmacy name']")
    new_pharmacy_chain=(By.XPATH,"//button[@aria-label='Pharmacy chain, --None--']")
    new_mail_order_pharmacy=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[2]")
    new_Status_pharmacy=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[4]")
    new_addressline_Pharmacy=(By.XPATH,"//input[@name='Address_Line1__c']")
    new_state_pharmacy=(By.XPATH,"(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[3]")
    def click_edit_pharmecies(self):
        return self.click_element(*Create_capture_member_details.edit_pharmacies)
    def enter_New_pharmacy_Name(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_name)
    def enter_New_Pharamacy_Phone(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_phone)
    def click_New_pharmacy_chain(self):
        return self.click_element(*Create_capture_member_details.new_pharmacy_chain)
    def click_New_mail_order_Pharmacy(self):
        return self.click_element(*Create_capture_member_details.new_mail_order_pharmacy)
    def clik_New_Status_Pharmacy(self):
        return self.click_element(*Create_capture_member_details.new_Status_pharmacy)
    def enter_NewZipcode_pharmacy(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_zipcode)
    def enter_NewAddressline_pharmacy(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_addressline_Pharmacy)
    def enter_NewCity_pharmacy(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_city)
    def click_Newstate_pharmacy(self):
        return self.click_element(*Create_capture_member_details.new_state_pharmacy)

    ## Validation of Pharmacies
    verify_pharmacy_name=(By.XPATH,"//records-record-layout-item[@field-label='Pharmacy name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_pharmacy_chain=(By.XPATH,"//records-record-layout-item[@field-label='Pharmacy chain']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_pharmacy_address_line_1=(By.XPATH,"//records-record-layout-item[@field-label='Address Line1']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_pharmacy_mailorder=(By.XPATH,"//records-record-layout-item[@field-label='Mail Order']/div/div/div[2]/span/slot/lightning-formatted-text")
    def validation_Pharmacy_name(self):
        return self.get_text(*Create_capture_member_details.verify_pharmacy_name)
    def validation_Pharmacy_phone(self):
        return self.get_text(*Create_capture_member_details.verify_phone)
    def validation_Pharmacy_primarychain(self):
        return self.get_text(*Create_capture_member_details.verify_pharmacy_name)
    def validation_Pharmacy_Mailorder(self):
        return self.get_text(*Create_capture_member_details.verify_pharmacy_mailorder)
    def validation_Pharmacy_status(self):
        return self.get_text(*Create_capture_member_details.verify_status)
    def validation_Pharmacy_Addressline_1(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_1)
    def validation_Pharmacy_Addressline_2(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_2)
    def validation_Pharmacy_city(self):
        return self.get_text(*Create_capture_member_details.verify_City)
    def validation_Pharmacy_State(self):
        return self.get_text(*Create_capture_member_details.verify_state)


    #### Create Outbound Referral Organization
    ### Outbound Referral Organization Creation and Edit
    ### For Creation
    outbound_organization = (By.XPATH, "//button[@title='Outbound Referrals Organization']")
    search_community = (By.XPATH, "//input[@placeholder='Search Community and senior organizations...']")
    event_associate_to_organization=(By.XPATH,"//a[@class='flex-wrap-ie11 slds-truncate']")
    associate_records=(By.XPATH, "//th[@class='slds-cell-edit cellContainer']")
    organization_service_available=(By.XPATH,"(//span[text()='Available'])[1]")
    Organization_type_Available=(By.XPATH,"(//span[text()='Available'])[2]")
    organization_name=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Name']//input")
    organization_Address_line_1=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Address_line_1__c']//input")
    organization_city=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.City__c']//input")
    oragnization_state=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.State__c']//a")
    organization_zipcode=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Zip_code__c']//input")
    organization_phone=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Phone__c']//input")
    organization_website=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Website__c']//input")
    organization_email=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Email__c']//input")
    organization_service_region=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Servicing_region__c']//input")
    organization_status=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Organizations__c.Status__c']//a")
    #### Create Outbound Referral Organization
    def select_outbound_organization(self):
        return self.click_element(*Create_capture_member_details.outbound_organization)
    def search_Community_and_senior_organization(self):
        return self.find_element(*Create_capture_member_details.search_community)
    def enter_organization_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def enter_address_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_02)
    def enter_city_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_04)
    def click_state_organization(self):
        return self.click_element(*Create_capture_member_details.Field_S_01)
    def enter_zipcode_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_05)
    def enter_phone_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_06)
    def enter_website_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_07)
    def enter_email_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_08)
    def enter_county_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_09)
    def click_status_organization(self):
        return self.click_element(*Create_capture_member_details.Field_S_04)
    def click_CommunityOrganization_Tab(self):
        return self.click_element(*Create_capture_member_details.CommunityOrganization)
    def select_AssosicateRecords(self):
        return self.Find_Elements(*Create_capture_member_details.associate_records)
    def click_EventsModule(self):
        return self.click_element(*Create_capture_member_details.Keen_Events_CommunityOrganization)
    def Event_Organization(self):
        return self.Find_Elements(*Create_capture_member_details.event_associate_to_organization)

    ### Edit Outbound Referral Organization
    ### For New Directory Creation and Edit
    edit_organizationName = (By.XPATH, "//button[@title='Edit Organization name']")
    edit_City_organization = (By.NAME, "City__c")
    edit_State_organization = (By.XPATH, "(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[1]")
    edit_Zipcode_organization = (By.NAME, "Zip_code__c")
    edit_Parent_organization = (By.XPATH, "//input[@class='slds-combobox__input slds-input slds-combobox__input-value']")
    edit_clearSection_Pranet = (By.XPATH, "//button[@title='Clear Selection']")
    edit_Phone_organization = (By.NAME, "Phone__c")
    edit_Website_organization = (By.NAME, "Website__c")
    edit_Email_organization = (By.NAME, "Email__c")
    edit_services_OrganizationType = (By.XPATH, "//span[@class='slds-media__body']")
    edit_KeenContacts = (By.XPATH, "//input[@class='slds-combobox__input slds-input']")
    edit_Servicing_region_county = (By.NAME, "Servicing_region__c")
    edit_Status_organization = (By.XPATH, "(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[4]")

    def edit_OrganizationName(self):
        return self.click_element(*Create_capture_member_details.edit_organizationName)
    def Edit_address_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_addressline)
    def Edit_city_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.edit_City_organization)
    def Edit_state_organization(self):
        return self.click_element(*Create_capture_member_details.edit_State_organization)
    def Edit_zipcode_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.edit_Zipcode_organization)
    def Edit_phone_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.edit_Phone_organization)
    def Edit_website_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.edit_Website_organization)
    def Edit_email_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.edit_Email_organization)
    def Edit_county_organization(self,text):
        return self.enter_text(text,*Create_capture_member_details.edit_Servicing_region_county)
    def Edit_status_organization(self):
        return self.click_element(*Create_capture_member_details.edit_Status_organization)
    ### Validation of Outbound Referrals Organization
    verify_organizationname=(By.XPATH,"//records-record-layout-item[@field-label='Organization name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_zipcode_text=(By.XPATH,"//records-record-layout-item[@field-label='Zip code']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_organization_parent_organization=(By.XPATH,"//records-record-layout-item[@field-label='Parent organization']/div/div/div[2]/span/slot/force-lookup/div")
    verify_organization_county=(By.XPATH,"//records-record-layout-item[@field-label='Servicing region (county)']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_maincontact=(By.XPATH,"//records-record-layout-item[@field-label='Main contact']/div/div/div[2]/span/slot/force-lookup/div")
    verify_organization_services=(By.XPATH,"//records-record-layout-item[@field-label='Services']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_organization_type=(By.XPATH,"//records-record-layout-item[@field-label='Organization type']/div/div/div[2]/span/slot/lightning-formatted-text")
    def validation_OrganizationName(self):
        return self.get_text(*Create_capture_member_details.verify_organizationname)
    def validation_address_organization(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_1)
    def validation_organizationaddress_line_2(self):
        return self.get_text(*Create_capture_member_details.verify_addressline_2)
    def validation_city_organization(self):
        return self.get_text(*Create_capture_member_details.verify_City)
    def validation_state_organization(self):
        return self.get_text(*Create_capture_member_details.verify_state)
    def validation_zipcode_organization(self):
        return self.get_text(*Create_capture_member_details.verify_zipcode_text)
    def validation_organization_parentorganization(self):
        return self.get_text(*Create_capture_member_details.verify_organization_parent_organization)
    def validation_organization_phone(self):
        return self.get_text(*Create_capture_member_details.verify_phone)
    def validation_website_organization(self):
        return self.get_text(*Create_capture_member_details.verify_website)
    def validation_email_organization(self):
        return self.get_text(*Create_capture_member_details.edit_Email_organization)
    def validation_county_organization(self):
        return self.get_text(*Create_capture_member_details.verify_organization_county)
    def validation_status_organization(self):
        return self.get_text(*Create_capture_member_details.verify_status)
    def validation_maincontact_organization(self):
        return self.get_text(*Create_capture_member_details.verify_maincontact)
    def validation_organization_services(self):
        return self.get_text(*Create_capture_member_details.verify_organization_services)
    def validation_organization_type(self):
        return self.get_text(*Create_capture_member_details.verify_organization_type)

    ### Creation of EVents for a Member
    select_event = (By.XPATH, "//lightning-button[@data-id='MemberEvents']//button")
    keen_event = (By.XPATH, "//input[@placeholder='Search Keen Events...']")
    start_date = (By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[2]/div/div/div/fieldset/div/div/input")
    start_time = (By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[2]/div/div/div/fieldset/div/div/div/input")
    End_date = (By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[3]/div/div/div/fieldset/div/div/input")
    End_time = (By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[3]/div/div/div/fieldset/div/div/div/input")
    state_events = (By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[4]/div/div/div/div/div/div/div/div/a")
    reportdate_events = (By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[8]/div[2]/div/div/div/div/input")
    status_event = (By.XPATH, "//div[@class='test-id__section-content slds-section__content section__content']/div/div[10]/div/div/div/div/div/div/div/div/a")
    Community_Organization_Events = (By.XPATH, "//input[@title='Search Community and senior organizations']")
    PracticeDirectory_Event = (By.XPATH, "//input[@title='Search Practice directory']")
    PracticeRecords = (By.XPATH, "//th[@scope='row']")
    eventspractice = (By.XPATH, "(//h2[@class='slds-card__header-title'])[15]")
    New_records=(By.XPATH,"//div[@class='primaryLabel slds-truncate slds-lookup__result-text']")
    carrires=(By.XPATH,"//div[text()='Carriers submitted to']")
    type_avaliable=(By.XPATH,"//div[text()='Type']")
    evp = (By.XPATH, "//span[@title='Events at practice']")  ### //th[@scope='row'] events at practice
    new_practice=(By.XPATH,"//span[@title='New Practice directory']")
    practice_records=(By.XPATH,"//div[@title]")
    ### Creat Events for Members
    def type_field(self):
        return self.find_element(*Create_capture_member_details.type_avaliable)
    def select_events(self):
        return self.click_element(*Create_capture_member_details.select_event)
    def click_keen_event(self):
        return self.find_element(*Create_capture_member_details.keen_event)
    def enter_event_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_01)
    def enter_start_date_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.start_date)
    def enter_start_time_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.start_time)
    def enter_End_date_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.End_date)
    def enter_End_time_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.End_time)
    def enter_Adress_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_01)
    def click_type_choosen(self):
        return self.click_element(*Create_capture_member_details.Move_to_chosen)
    def enter_Number_of_Attendees_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_02)
    def enter_RegistartionCost_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_03)
    def enter_FoodCost_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_04)
    def enter_CommunityOrganization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Community_Organization_Events)
    def enter_PracticeDirectory_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticeDirectory_Event)
    def click_new_practice_event(self):
        return self.click_element(*Create_capture_member_details.new_practice)
    def select_practice_records(self):
        return self.Find_Elements(*Create_capture_member_details.practice_records)
    def select_records(self):
        return self.Find_Elements(*Create_capture_member_details.New_records)
    def click_carrier_choosen(self):
        return self.click_element(*Create_capture_member_details.Move_to_chosen_2)
    def click_state_event(self):
        return self.click_element(*Create_capture_member_details.state_events)
    def enter_city_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_03)
    def enter_zipcode_events(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_04)
    def enter_Phone_events(self,text):
        return self.enter_text(text,*Create_capture_member_details.Field_D_05)
    def enter_Report_date_events(self,text):
        return self.enter_text(text,*Create_capture_member_details.reportdate_events)
    def click_status_events(self):
        return self.click_element(*Create_capture_member_details.status_event)
    def click_Report_as_marketing_event(self):
        return self.click_element(*Create_capture_member_details.Field_05)
    def click_Submitted_to_carrier(self):
        return self.click_element(*Create_capture_member_details.Field_06)
    def click_Recurring_event(self):
        return self.click_element(*Create_capture_member_details.Field_07)
    def click_Community_Organization_Tab(self):
        return self.click_element(*Create_capture_member_details.CommunityOrganization)

    ### Creation and Edit the Events in Events Tab
    Newstart_date = (By.XPATH, "(//input[@name='Start_date_time__c'])[1]")
    Newstart_time = (By.XPATH, "(//input[@name='Start_date_time__c'])[2]")
    NewEnd_date = (By.XPATH, "(//input[@name='End_date_time__c'])[1]")
    NewEnd_time = (By.XPATH, "(//input[@name='End_date_time__c'])[2]")
    Newcity_event = (By.XPATH, "//input[@name='Event_City__c']")
    Newstate_events = (By.XPATH, "(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[1]]")
    Newreportdate_events = (By.XPATH, "//input[@name='Report_date__c']")
    Newstatus_event = (By.XPATH, "(//button[@class='slds-combobox__input slds-input_faux slds-combobox__input-value'])[2]")
    NewReport_as_marketing_event = (By.XPATH, "//input[@name='Report_as_marketing_event__c']")
    NewSubmitted_to_carrier = (By.XPATH, "//input[@name='Submitted_to_carrier__c']")
    NewRecurring_Event = (By.XPATH, "//input[@name='Recurring_event__c']")
    NewNumberAttendees = (By.XPATH, "//input[@name='Number_of_attendees__c']")
    NewCost_RegistrationEvent = (By.XPATH, "//input[@name='Registration_Cost__c']")
    NewCost_FoodEvent = (By.XPATH, "//input[@name='Food_and_drink_cost__c']")
    NewCommunity_Organization_Events = (By.XPATH, "//input[@title='Search Community and senior organizations']")
    NewPracticeDirectory_Event = (By.XPATH, "//input[@title='Search Practice directory']")
    associate_event_records=(By.XPATH,"//th[@scope='row']")
    ### Creation and Edit on Events

    def enter_Newevent_name(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_name)
    def enter_Newstart_date_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.start_date)
    def enter_Newstart_time_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.start_time)
    def enter_NewEnd_date_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.End_date)
    def enter_NewEnd_time_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.End_time)
    def enter_NewAddress_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_addressline)
    def enter_NewAddress_line2_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.New_Address_line_2)
    def enter_Newtype_choosen(self):
        return self.click_element(*Create_capture_member_details.Move_to_chosen)
    def enter_NewNumber_of_Attendees_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.NewNumberAttendees)
    def enter_NewRegistartionCost_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.NewCost_RegistrationEvent)
    def enter_NewFoodCost_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.NewCost_FoodEvent)
    def enter_NewCommunityOrganization(self,text):
        return self.enter_text(text,*Create_capture_member_details.Community_Organization_Events)
    def enter_NewPracticeDirectory_Event(self,text):
        return self.enter_text(text,*Create_capture_member_details.PracticeDirectory_Event)
    def selectNew_records(self):
        return self.Find_Elements(*Create_capture_member_details.New_records)
    def click_Newcarrier_choosen(self):
        return self.click_element(*Create_capture_member_details.Move_to_chosen_2)
    def click_Newstate_event(self):
        return self.click_element(*Create_capture_member_details.state_events)
    def enter_Newcity_event(self,text):
        return self.enter_text(text,*Create_capture_member_details.Newcity_event)
    def enter_Newzipcode_events(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_zipcode)
    def enter_NewPhone_events(self,text):
        return self.enter_text(text,*Create_capture_member_details.new_phone)
    def enter_NewReport_date_events(self,text):
        return self.enter_text(text,*Create_capture_member_details.reportdate_events)
    def enter_Newstatus_events(self):
        return self.click_element(*Create_capture_member_details.status_event)
    def New_Report_as_marketing_event(self):
        return self.click_element(*Create_capture_member_details.NewReport_as_marketing_event)
    def New_Submitted_to_carrier(self):
        return self.click_element(*Create_capture_member_details.NewSubmitted_to_carrier)
    def enter_NewRecurring_event(self):
        return self.click_element(*Create_capture_member_details.NewRecurring_Event)
    def enter_NewCommunity_Organization_Tab(self):
        return self.click_element(*Create_capture_member_details.CommunityOrganization)
    def community_SeniorOrganization(self):
        return self.click_element(*Create_capture_member_details.Community_Organization_Events)
    def PracticeDirectory(self):
        return self.click_element(*Create_capture_member_details.PracticeDirectory_Event)
    def list_PracticeDirectory(self):
        return self.driver.find_elements(*Create_capture_member_details.PracticeRecords)
    def Events_IN_Practice(self):
        return self.click_element(*Create_capture_member_details.eventspractice)
    def Records_Events(self):
        return self.driver.find_elements(*Create_capture_member_details.associate_event_records)
    ### validation of Events
    verify_eventname=(By.XPATH,"//records-record-layout-item[@field-label='Event Name']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_startdate = (By.XPATH, "//records-record-layout-item[@field-label='Start date time']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_enddate = (By.XPATH, "//records-record-layout-item[@field-label='End date time']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_address = (By.XPATH, "//records-record-layout-item[@field-label='Address Line 1']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_type = (By.XPATH, "//records-record-layout-item[@field-label='Type']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_numberof_attendees = (By.XPATH, "//records-record-layout-item[@field-label='Number of attendees']/div/div/div[2]/span/slot/lightning-formatted-number")
    verify_event_registrationcost = (By.XPATH, "//records-record-layout-item[@field-label='Registration Cost']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_foodcost = (By.XPATH, "//records-record-layout-item[@field-label='Food and drink cost']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_community_organization =(By.XPATH,"//records-record-layout-item[@field-label='Community and senior organization']/div/div/div[2]/span/slot/force-lookup/div")
    verify_event_practice_directory=(By.XPATH,"//records-record-layout-item[@field-label='Practice directory']/div/div/div[2]/span/slot/force-lookup/div")
    verify_event_status = (By.XPATH, "//records-record-layout-item[@field-label='Status']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_reporting = (By.XPATH, "//records-record-layout-item[@field-label='Report as marketing event']/div/div/div[2]/span/slot/lightning-input")
    verify_event_submitted_carriers = (By.XPATH, "//records-record-layout-item[@field-label='Submitted to carrier']/div/div/div[2]/span/slot/lightning-input")
    verify_event_carriers_submitted = (By.XPATH, "//records-record-layout-item[@field-label='Carriers submitted to']/div/div/div[2]/span/slot/lightning-formatted-text")
    verify_event_recurring = (By.XPATH, "//records-record-layout-item[@field-label='Recurring Event']/div/div/div[2]/span/slot/lightning-input")
    verify_event_report_date=(By.XPATH,"//records-record-layout-item[@field-label='Report date']/div/div/div[2]/span/slot/lightning-formatted-text")
    def Validation_event_name(self):
        return self.get_text(*Create_capture_member_details.verify_eventname)
    def Validation_start_Date_Timeevent(self):
        return self.get_text(*Create_capture_member_details.verify_event_startdate)
    def Validation_End_Date_Timeevent(self):
        return self.get_text(*Create_capture_member_details.verify_event_enddate)
    def Validation_Adress_event(self):
        return self.get_text(*Create_capture_member_details.verify_event_address)
    def Validation_type_choosen(self):
        return self.get_text(*Create_capture_member_details.verify_event_type)
    def Validation_state_event(self):
        return self.get_text(*Create_capture_member_details.verify_state)
    def Validation_Number_Attendees(self):
        return self.get_text(*Create_capture_member_details.verify_event_numberof_attendees)
    def Validation_city_event(self):
        return self.get_text(*Create_capture_member_details.verify_City)
    def Validation_zipcode_events(self):
        return self.get_text(*Create_capture_member_details.verify_zipcode_text)
    def Validation_RegistrationCost(self):
        return self.get_text(*Create_capture_member_details.verify_event_registrationcost)
    def Validation_Phone_events(self):
        return self.get_text(*Create_capture_member_details.Verify_Phone)
    def Validation_food_Cost_Event(self):
        return self.get_text(*Create_capture_member_details.verify_event_foodcost)
    def Validation_Community_Organization(self):
        return self.get_text(*Create_capture_member_details.verify_event_community_organization)
    def Validation_Report_date_events(self):
        return self.get_text(*Create_capture_member_details.verify_event_report_date)
    def Validation_PracticeDirectory(self):
        return self.get_text(*Create_capture_member_details.verify_event_practice_directory)
    def Validation_status_events(self):
        return self.get_text(*Create_capture_member_details.verify_event_status)
    def Validation_Report_as_marketing_event(self):
        return self.get_text(*Create_capture_member_details.verify_event_reporting)
    def Validation_Submitted_to_carrier(self):
        return self.get_text(*Create_capture_member_details.verify_event_submitted_carriers)
    def Validation_Carriers_Submitted(self):
        return self.get_text(*Create_capture_member_details.verify_event_carriers_submitted)
    def Validation_Recurring_event(self):
        return self.get_text(*Create_capture_member_details.verify_event_recurring)

    ###### Assosicate a New Keen advisor for a member
    advisor = (By.XPATH, "(//button[@name='New'])[2]")
    advisor_page = (By.XPATH, "//h1[@class='slds-page-header__title listViewTitle slds-truncate']")
    new_advisor = (By.XPATH, "(//a[@title='New'])[3]")
    search_advisor = (By.XPATH, "//input[@placeholder='Search People...']")
    select_advisor = (By.XPATH, "//span[@class='slds-listbox__option-text slds-listbox__option-text_entity']")
    keed_advisor = (By.XPATH, "//td//lightning-primitive-cell-factory//span/div")
    lead_Name = (By.XPATH, "//a[@class='flex-wrap-ie11 slds-truncate']//slot/slot/span")
    return_member = (By.XPATH, "(//li[@class='slds-breadcrumb__item slds-line-height--reset'])[1]")

    def click_New_Keen_advisor_for_a_member(self):
        keen_leads = self.driver.find_element(*Create_capture_member_details.advisor)
        return self.driver.execute_script("arguments[0].click();", keen_leads)
    def Advisor_Page(self):
        return self.find_element(*Create_capture_member_details.advisor_page)
    def click_New(self):
        return self.click_element(*Create_capture_member_details.new_advisor)
    def Search_advisor(self,text):
        return self.enter_text(text,*Create_capture_member_details.search_advisor)
    def Select_advisor(self):
        return self.Find_Elements(*Create_capture_member_details.select_advisor)
    def Keen_Advisor_for_a_Lead(self):
        return self.Find_Elements(*Create_capture_member_details.lead_Name)
    def Associate_Keen_Adivsor(self):
        return self.driver.find_elements(*Create_capture_member_details.keed_advisor)
    def Return_to_Keen_lead_and_Member(self):
        return self.click_element(*Create_capture_member_details.return_member)


    #### Associate Files to a Member
    add_files=(By.XPATH,"//div[@title='Add Files']")
    list_files=(By.XPATH,"//span[@class='slds-checkbox--faux']")
    list=(By.XPATH,"//div[@class='slds-size_12-of-12 slds-grid slds-nowrap']")
    popup_file=(By.XPATH,"//h2[@class='title slds-text-heading--medium slds-hyphenate']")
    add=(By.XPATH,"//button[@class='slds-button slds-button--neutral attach uiButton--default uiButton--brand uiButton']")
    files=(By.XPATH,"//div[@class='leftPanel']/div/div[1]/div/div/button")
    done=(By.XPATH,"//span[text()='Done']")
    verify_file=(By.XPATH,"(//span[@class='itemTitle desktop outputTextOverride uiOutputText'])[1]")
    view_all=(By.XPATH,"//a[@href='/lightning/r/Account/0017800000IStSHAA1/related/AttachedContentDocuments/view']/div/span")
    files_tab=(By.XPATH,"//h1[@title='Files']")
    def Associate_Files(self):
        return self.click_element(*Create_capture_member_details.add_files)
    def Select_files(self):
        return self.Find_Elements(*Create_capture_member_details.list)
    def Popup_title_files(self):
        return self.get_text(*Create_capture_member_details.popup_file)
    def associate_files_to_member(self):
        return self.click_element(*Create_capture_member_details.add)
    def Upload_files(self):
        return self.click_element(*Create_capture_member_details.files)
    def click_done(self):
        return self.click_element(*Create_capture_member_details.done)
    def click_view_all(self):
        return self.click_element(*Create_capture_member_details.view_all)
    def Validation_File(self):
        return self.get_text(*Create_capture_member_details.verify_file)












