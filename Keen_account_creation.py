from selenium.webdriver.common.by import By
from utilities.action_utils import ActionUtils

class Keen_Account_creation(ActionUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    select_keen_lists=(By.XPATH,"(//lightning-icon[@icon-name='utility:down'])[3]")
    close_popup=(By.XPATH,"//button[@title='Close']")
    new_button=(By.XPATH, "//a[@title='New']")
    enter_firstName=(By.XPATH, "//input[@name='FirstName']")
    verify_firstName=(By.XPATH,"//flexipage-component2[@data-target-selection-name='c_customAccountCmp']//div[@part='body']//input[@name='FirstName']")
    enter_middleName=(By.XPATH,"//input[@name='MiddleName']")
    enter_lastName=(By.XPATH,"//input[@name='LastName']")
    verify_LastName=(By.XPATH,"//flexipage-component2[@data-target-selection-name='c_customAccountCmp']//div[@part='body']//input[@name='LastName']")
    enter_dob=(By.XPATH,"//input[@name='dob']")
    veridy_member=(By.XPATH,"(//div[@class='slds-media__body']//span)[1]")
    click_source=(By.XPATH,"//button[@name='AccountSource']")
    options_source=(By.XPATH,"//lightning-base-combobox-item[@class='slds-media slds-listbox__option slds-media_center slds-media_small slds-listbox__option_plain']//span[@class='slds-truncate']")
    source_icon=(By.XPATH,"(//lightning-icon[@title='source detail'])[2]")
    icon_source=(By.XPATH,"//flexipage-component2[@data-target-selection-name='c_customAccountCmp']/slot/c-custom-account-cmp/div/lightning-card/article/div[2]/slot/div/lightning-record-view-form/div/slot/div/div[2]/span/label/lightning-icon")
    error_message_source=(By.XPATH,"//div[@class='slds-form-element__help']")
    source_popup=(By.XPATH,"//h2[text()='Source Type and Source Name the member came from.']")
    ok_button_sourcepopup=(By.XPATH,"//button[text()='Ok']")
    cancel_button_sourcepopup=(By.XPATH,"//button[@title='Cancel']")
    enter_email=(By.XPATH, "//input[@inputmode='email']")
    enter_PTC=(By.XPATH, "//input[@name='Permission_to_contact_date__c']")
    enter_SOA=(By.XPATH, "//input[@name='Scope_of_appointment_date__c']")
    select_gender=(By.XPATH, "//button[@name='GenderIdentity__c']")
    gender_options=(By.XPATH,"//div[@role='listbox']//lightning-base-combobox-item")
    status=(By.XPATH, "//button[@name='Status__c']")
    status_options=(By.XPATH,"//lightning-base-combobox-item//span[@class='slds-truncate']")
    language = (By.XPATH, "//div[@part='dual-listbox']//div[text()='Preferred Language']")
    language_choosen = (By.XPATH,"(//div[@part='dual-listbox']//div[@class='slds-dueling-list__column slds-dueling-list__column_responsive'])[2]//ul//li//div//span[@class='slds-truncate']")
    warning=(By.XPATH,"//h2[text()='Warning!']")
    edit=(By.XPATH,"//button[text()='Back to Edit']")
    enter_phone=(By.XPATH, "//input[@name='Phone']")
    enter_Address_newcreation=(By.XPATH,"//textarea[@name='PersonMailingStreet']")
    verify_streetaddress=(By.XPATH,"//label[contains(text(), 'Mailing Street')]/following-sibling::div//textarea[@name='PersonMailingStreet']")
    enter_newcreationaddress_line_2=(By.XPATH,"//input[@name='Address_Line_2__c']")
    verify_address_line_2=(By.XPATH,"//label[contains(text(), 'Address Line 2')]/following-sibling::div//input[@name='Address_Line_2__c']")
    enter_city_newcreation=(By.XPATH,"//input[@name='PersonMailingCity']")
    verify_city=(By.XPATH,"//label[contains(text(), 'Mailing City')]/following-sibling::div//input[@name='PersonMailingCity']")
    select_state_newcreation=(By.XPATH,"//button[@name='PersonMailingState']")
    verify_state=(By.XPATH,"//button[@name='PersonMailingState']")
    enter_zipcode_newcreation=(By.XPATH,"//input[@name='PersonMailingPostalCode']")
    verify_zipcode=(By.XPATH,"//label[contains(text(), 'ZIP code')]/following::div//input[@name='zipCode']")
    enter_county_newcreation=(By.XPATH,"//button[@name='county']")
    verify_county=(By.XPATH,"//label[text()='County']/parent::span/parent::div//input")
    enter_address=(By.XPATH,"//textarea[@name='PersonMailingStreet']")
    address_details=(By.XPATH,"//lightning-icon[@title='address detail']")
    enter_mailing_street=(By.XPATH,"//textarea[@name='street']")
    enter_zipcode=(By.XPATH,"//input[@name='postalCode']")
    enter_city=(By.XPATH,"//input[@name='city']")
    click_state=(By.XPATH,"//button[@name='PersonMailingState']")
    state_options=(By.XPATH, "//lightning-base-combobox-item//span[2]")
    other_details_icon=(By.XPATH,"//lightning-icon[@title='Other Details']")
    origin=(By.XPATH,"//button[@name='CountryOfOrigin__c']")
    country_options=(By.XPATH,"//lightning-base-combobox-item")
    select_militaryVet=(By.XPATH,"//input[@name='Military_Vet__c']")
    options=(By.XPATH,"//li[@role='presentation']")
    click_choosen=(By.XPATH,"//button[@title='Move selection to Chosen']")
    ok_button=(By.XPATH,"//button[text()='Ok']")
    medication_details_popup=(By.XPATH,"(//lightning-icon[@title='Medicare/ Medicaid Details'])[1]")
    medication_details=(By.XPATH,"//flexipage-component2[@data-target-selection-name='c_customAccountCmp']/slot/c-custom-account-cmp/div/lightning-card/article/div[2]/slot/div/lightning-record-view-form/div/slot/div/div[16]/span/label/lightning-icon")
    medicare_id=(By.XPATH,"//input[@name='MedicareID__c']")
    member_id=(By.XPATH,"//input[@name='Keen_Member_ID__c']")
    low_income_subsidy=(By.XPATH,"//label[text()='Low Income Subsidy']/following-sibling::div//button[@name='Low_Income_Subsidy__c']")
    medicaid_category=(By.XPATH,"//label[text()='Eligible Medicaid Category']/following-sibling::div//button[@name='Eligible_Medicaid_Category__c']")
    part_A=(By.XPATH,"//input[@name='Part_A_enrollment_date__c']")
    part_B=(By.XPATH,"//input[@name='Part_B_enrollment_date__c']")
    SSN=(By.XPATH,"//input[@name='SSN__c']")
    medicaid_id=(By.XPATH,"//input[@name='MedcaidID__c']")
    medicare_popup=(By.XPATH,"//button[@title='Close']")
    verification_date=(By.XPATH,"//input[@name='Medicaid_status_verification_date__c']")
    ok_2=(By.XPATH,"(//button[@name='submit'])[2]")
    save=(By.XPATH,"//button[@name='submit']")
    warning_popup=(By.XPATH,"//h2[@class='slds-text-heading_medium slds-hyphenate']")
    toast_message=(By.XPATH,"//div[text()='Success']")
    member_options = (By.XPATH, "//span[@class='slds-truncate']")
    member=(By.XPATH,"//th[@class='slds-cell-edit cellContainer']/span//a")
    edit_owner=(By.XPATH,"//button[@title='Remove']")
    cancel_edit=(By.XPATH,"(//button[text()='Cancel'])[2]")
    cancel_in_member_page=(By.XPATH,"//flexipage-component2//button[text()='Cancel']")
    delete_record=(By.XPATH,"(//span[@class='slds-icon_container slds-icon-utility-down'])[1]")
    delete_option=(By.XPATH,"//a[@title='Delete']")
    delete_popup=(By.XPATH,"//h2[@class='title slds-text-heading--medium slds-hyphenate']")
    delete_lead=(By.XPATH,"//span[text()='Delete']")
    ptc_popup=(By.XPATH,"//lightning-icon[@title='ptc detail']")
    ptc_option=(By.XPATH,"//button[@name='Permission_to_contact_source__c']")
    med=(By.XPATH,"//div[@class='slds-m-around_medium']//div[16]//lightning-icon[@title='medicare detail']")
    verify_invalid_data_entered_fields=(By.XPATH,"//label[contains(text(), 'Contact Info')]/following-sibling::lightning-layout//div[text()]")
    enter_nickname=(By.XPATH,"//input[@name='Nickname__c']")
    disposition_field=(By.XPATH,"//button[@name='Disposition__c']")
    do_no_text=(By.XPATH,"//input[@name='Do_not_text__c']/following-sibling::label//span[@class='slds-checkbox_faux']")
    ##### Account Login
    setup_settings=(By.XPATH,"//lightning-icon[@icon-name='utility:setup']")
    setup_option=(By.XPATH,"//li[@id='related_setup_app_home']")
    quick_find=(By.XPATH,"//input[@placeholder='Quick Find']")
    select_users=(By.XPATH,"//a[@href='/one/one.app#/setup/ManageUsers/home']")
    users_page=(By.XPATH,"//span[text()='Users']")
    login_advisor=(By.XPATH,"//a[@title='Login - Record 18 - Vijayaraghavan, Arthi' and text()='Login']")
    all_keen_members=(By.XPATH,"(//span[text()='All Keen leads and members'])[1]")
    gender_label=(By.XPATH,"//input[@value='Male']")

    ##login
    def click_gender_label(self):
        return self.click_element(*Keen_Account_creation.gender_label)
    def click_all_keen_members(self):
        return self.click_element(*Keen_Account_creation.all_keen_members)
    ## driver.find_elem(Xpath).click() or send_keys()
    def click_keen_list(self):
        return self.find_element(*Keen_Account_creation.select_keen_lists)
    def click_setup_settings(self):
        return self.click_element(*Keen_Account_creation.setup_settings)
    def click_setup_option(self):
        return self.find_element(*Keen_Account_creation.setup_option)
    def search_users_in_quickfind(self,text):
        return self.enter_text(text,*Keen_Account_creation.quick_find)
    def click_users(self):
        return self.click_element(*Keen_Account_creation.select_users)
    def verify_usres_page(self):
        return self.find_element(*Keen_Account_creation.users_page)
    def click_advisor(self):
        return self.click_element(*Keen_Account_creation.login_advisor)
    def verify_errors(self):
        return self.Find_Elements(*Keen_Account_creation.verify_invalid_data_entered_fields)
    def keen_member(self):
        return self.get_text(*Keen_Account_creation.veridy_member)
    def enter_field_value(self, field_name, value):
        # Find the input field element corresponding to the field name
        field_element = self.driver.find_element(By.ID, field_name)  # Replace with the appropriate locator method

        # Clear the existing value (if any) from the field
        field_element.clear()

        # Enter the value in the input field
        field_element.send_keys(value)
    def delete_keen_lead(self):
        return self.click_element(*Keen_Account_creation.delete_record)
    def click_cancel_keen_page(self):
        return self.click_element(*Keen_Account_creation.cancel_in_member_page)
    def click_delete(self):
        return self.click_element(*Keen_Account_creation.delete_option)
    def verify_delete_popup(self):
        return self.find_element(*Keen_Account_creation.delete_popup)
    def click_delete_lead(self):
        return self.click_element(*Keen_Account_creation.delete_lead)
    def select_member(self):
        return self.Find_Elements(*Keen_Account_creation.member)
    def Click_close_popup(self):
        return self.click_element(*Keen_Account_creation.close_popup)
    def New(self):
        return self.click_element(*Keen_Account_creation.new_button)
    def first_name(self):
        return self.find_element(*Keen_Account_creation.enter_firstName)
    def verify_first_name(self):
        return self.find_element(*Keen_Account_creation.verify_firstName)
    def middle_name(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_middleName)
    def last_name(self):
        return self.find_element(*Keen_Account_creation.enter_lastName)
    def verify_last_name(self):
        return self.find_element(*Keen_Account_creation.verify_LastName)
    def DoB(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_dob)
    def source(self):
        return self.click_element(*Keen_Account_creation.click_source)
    def select_source(self):
        return self.Find_Elements(*Keen_Account_creation.options_source)
    def select_source_details(self):
        return self.click_element(*Keen_Account_creation.icon_source)
    def Error_messageof_soruce_popup(self):
        return self.find_element(*Keen_Account_creation.error_message_source)
    def pop_up_sourceType(self):
        return self.find_element(*Keen_Account_creation.source_popup)
    def ok(self):
        return self.click_element(*Keen_Account_creation.ok_button_sourcepopup)
    def cancel_sourcetype_popup(self):
        return self.click_element(*Keen_Account_creation.cancel_button_sourcepopup)
    def email(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_email)
    def premession_to_contact(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_PTC)
    def click_ptc_popup(self):
        return self.click_element(*Keen_Account_creation.ptc_popup)
    def click_permission_to_contact_filed(self):
        return self.click_element(*Keen_Account_creation.ptc_option)
    def scope_of_appointment_date(self):
        return self.find_element(*Keen_Account_creation.enter_SOA)
    def gender(self):
        return self.click_element(*Keen_Account_creation.select_gender)
    def select_gender_in_list(self):
        return self.Find_Elements(*Keen_Account_creation.gender_options)
    def click_status(self):
        return self.click_element(*Keen_Account_creation.status)
    def select_status(self):
        return self.Find_Elements(*Keen_Account_creation.status_options)
    def warning_pop_up(self):
        return self.find_element(*Keen_Account_creation.warning)
    def back_edit(self):
        return self.click_element(*Keen_Account_creation.edit)
    def phone(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_phone)
    def street_address(self):
        return self.find_element(*Keen_Account_creation.enter_address)
    def enter_address_line2(self):
        return self.find_element(*Keen_Account_creation.enter_newcreationaddress_line_2)
    def enter_city_newLead(self):
        return self.find_element(*Keen_Account_creation.enter_city_newcreation)
    def enter_zipcode_newlead(self):
        return self.find_element(*Keen_Account_creation.enter_zipcode_newcreation)
    def click_state_newLead(self):
        return self.find_element(*Keen_Account_creation.select_state_newcreation)
    def select_state_newlead(self):
        return self.Find_Elements(*Keen_Account_creation.member_options)
    def enter_county_newlead(self):
        return self.find_element(*Keen_Account_creation.enter_county_newcreation)
    def click_address_Details(self):
        return self.click_element(*Keen_Account_creation.address_details)
    def mailing_street(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_mailing_street)
    def mailing_zipcode(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_zipcode)
    def mailing_city(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_city)
    def mailing_state(self):
        return self.click_element(*Keen_Account_creation.click_state)
    def select_state(self):
        return self.driver.Find_Elements(*Keen_Account_creation.state_options)
    def click_cancel(self):
        return self.click_element(*Keen_Account_creation.cancel_edit)
    def other_details(self):
        return self.click_element(*Keen_Account_creation.other_details_icon)
    def Country_of_origin(self):
        return self.find_element(*Keen_Account_creation.origin)
    def select_Country_of_origin(self):
        return self.Find_Elements(*Keen_Account_creation.country_options)
    def Military_vet(self):
         return self.click_element(*Keen_Account_creation.select_militaryVet)
    def preferred_language(self):
         return  self.Find_Elements(*Keen_Account_creation.options)
    def select_to_chosen(self):
         return  self.click_element(*Keen_Account_creation.click_choosen)
    def choosen_language(self):
        return self.driver.Find_Elements(*Keen_Account_creation.language_choosen)
    def click_ok_button(self):
        return self.click_element(*Keen_Account_creation.ok_button)
    def select_medication_details(self):
        return self.click_element(*Keen_Account_creation.medication_details_popup)
    def select_medication_popup(self):
        return self.click_element(*Keen_Account_creation.medication_details)
    def enter_medicare_ID(self):
        return self.find_element(*Keen_Account_creation.medicare_id)
    def enter_Part_A_enrollment_date(self):
        return self.find_element(*Keen_Account_creation.part_A)
    def enter_Part_B_enrollment_date(self):
        return self.find_element(*Keen_Account_creation.part_B)
    def enter_SSN(self):
        return self.find_element(*Keen_Account_creation.SSN)
    def enter_Medcaid_ID(self):
        return self.find_element(*Keen_Account_creation.medicaid_id)
    def close_medicaredetails_popup(self):
        return self.click_element(*Keen_Account_creation.medicare_popup)
    def enter_Medicaid_status_verification_date(self):
        return self.find_element(*Keen_Account_creation.verification_date)
    def Click_Ok(self):
        return self.click_element(*Keen_Account_creation.ok_2)
    def click_save(self):
        return self.click_element(*Keen_Account_creation.save) ##//button[text()='Save']
    def Warning_popup(self):
        return self.find_element(*Keen_Account_creation.warning_popup)
    def Back_To_Edit(self):
        return self.click_element(*Keen_Account_creation.edit)
    def Success_Message(self):
        return self.find_element(*Keen_Account_creation.toast_message)

    # validations
    verify_field_DoB=(By.XPATH,"//label[text()='DoB:']/following-sibling::div//lightning-output-field//div//lightning-formatted-text")
    verify_field_02=(By.XPATH, "//label[text()='Source:']/following-sibling::lightning-output-field//div//lightning-formatted-text")
    verify_field_03=(By.XPATH, "//label[text()='PTC:']/following-sibling::lightning-output-field//div//lightning-formatted-text")
    verify_field_04=(By.XPATH, "//label[text()='SOA:']/following-sibling::lightning-output-field//div//lightning-formatted-text")
    verify_field_05=(By.XPATH, "//label[text()='Gender and other demographics:']/following-sibling::lightning-output-field//div//lightning-formatted-text")
    verify_field_06=(By.XPATH, "//label[text()='Status:']/following-sibling::lightning-output-field//div//lightning-formatted-text")
    verify_field_07=(By.XPATH, "(//lightning-formatted-text[@class='slds-form-element__static'])[7]")
    verify_email=(By.XPATH,"//label[text()='Email:']/following-sibling::lightning-output-field//div//lightning-formatted-email//a")
    verify_address=(By.XPATH,"//p[@data-id='addressOutput']")
    verify_phone=(By.XPATH,"//label[text()='Phone:']/following-sibling::p//lightning-click-to-dial//span[2]")
    verify_total_address=(By.XPATH,"//div[@class='slds-col slds-size_3-of-12']//p")
    verrify_name=(By.XPATH,"(//span[@class='slds-text-heading_small slds-truncate'])[3]")
    verify_dispositions=(By.XPATH,"//label[text()='Disposition:']/following-sibling::lightning-output-field//div//lightning-formatted-text")
    verfiy_text_source=(By.XPATH,"//lightning-output-field[@data-id='source']//lightning-formatted-text")
    def validation_source_text(self):
        self.get_text(*Keen_Account_creation.verfiy_text_source)
    def validation_name(self):
        return self.get_text(*Keen_Account_creation.verrify_name)
    def validation_of_email(self):
        return self.get_text(*Keen_Account_creation.verify_email)
    def validation_of_DoB(self):
        return self.get_text(*Keen_Account_creation.verify_field_DoB)
    def validation_member_address(self):
        return self.get_text(*Keen_Account_creation.verify_total_address)
    def validation_of_source(self):
        return self.get_text(*Keen_Account_creation.source)
    def validation_of_PTC(self):
        return self.get_text(*Keen_Account_creation.verify_field_03)
    def validation_of_SOA(self):
        return self.get_text(*Keen_Account_creation.verify_field_04)
    def validation_of_Gender(self):
        return self.get_text(*Keen_Account_creation.verify_field_05)
    def validation_of_status(self):
        return self.get_text(*Keen_Account_creation.verify_field_06)
    def validation_of_street_Address(self):
        return self.get_text(*Keen_Account_creation.verify_field_07)
    def validation_of_Phone(self):
        return self.get_text(*Keen_Account_creation.verify_phone)
    def validation_of_street(self):
        return self.find_element(*Keen_Account_creation.verify_streetaddress)
    def validation_of_addressline_2(self):
        return self.find_element(*Keen_Account_creation.verify_address_line_2)
    def validation_of_city(self):
        return self.find_element(*Keen_Account_creation.verify_city)
    def validation_of_state(self):
        return self.find_element(*Keen_Account_creation.verify_state)
    def validation_of_zipcode(self):
        return self.find_element(*Keen_Account_creation.verify_zipcode)
    def validation_of_county(self):
        return self.find_element(*Keen_Account_creation.verify_county)


    ### For SOurce Pop-ups
    community_record=(By.XPATH,"//input[@placeholder='Search Community and senior organizations...']")
    validate_popup_record_01=(By.XPATH,"//input[@data-value][1]")
    validate_popup_record_02 = (By.XPATH, "//input[@data-value][2]")
    validate_popup_record_03 = (By.XPATH, "//input[@data-value][3]")
    validate_popup_record_04 = (By.XPATH,"(//button[@data-value])[4]")
    records=(By.XPATH,"//ul[@role='group']//li//lightning-base-combobox-item//span[2]//span")
    for_practice_records=(By.XPATH,"//lightning-input-field[@data-id='Practice_directory__c']//lightning-base-combobox-formatted-text[@class='slds-truncate']")
    for_events_records=(By.XPATH,"//lightning-input-field[@data-id='Ev']//lightning-base-combobox-formatted-text[@class='slds-truncate']")
    error_message_sourcepopup=(By.XPATH,"//div[@class='slds-form-element__help']")
    practice_record=(By.XPATH,"//input[@placeholder='Search Practice directory...']")
    referral_member=(By.XPATH,"//input[@placeholder='Search Keen leads and members...']")
    click_relation=(By.XPATH,"//button[@name='Referring_member_s_relationship__c']")
    campaign_record=(By.XPATH,"//input[@placeholder='Search Campaigns...']")
    event_record=(By.XPATH,"//input[@placeholder='Search Keen Events...']")
    keen_other=(By.XPATH,"//input[@name='Source_Other__c']")
    #### For community_organization
    def select_community_organization(self):
        return self.find_element(*Keen_Account_creation.community_record)
    def validating_community_organization(self):
        return self.find_element(*Keen_Account_creation.validate_popup_record_01)
    def select_record(self):
        return self.Find_Elements(*Keen_Account_creation.records)
    def select_directory_records(self):
        return self.Find_Elements(*Keen_Account_creation.for_practice_records)
    def select_events_records(self):
        return self.Find_Elements(*Keen_Account_creation.for_events_records)
    def error_messagepopup_source(self):
        return self.driver.Find_Elements(*Keen_Account_creation.error_message_sourcepopup)
    ### Provider: Aledade,Provider: Archwell,Provider: Centerwell,Provider: ChenM / Ded Call center,Provider: ChenM / Ded MCG
    ### Aledade Website Directory,  Aledade T-65/MAI
    def select_practice_directory(self):
        return self.find_element(*Keen_Account_creation.practice_record)
    def validating_practice_directory(self):
        return self.find_element(*Keen_Account_creation.validate_popup_record_02)
    ### for Member Referral
    def click_referring_member(self,text):
        return self.enter_text(text,*Keen_Account_creation.referral_member)
    def member_relationship(self):
        return self.click_element(*Keen_Account_creation.click_relation)
    def relation_member(self):
        return self.Find_Elements(*Keen_Account_creation.member_options)
    ## For Campaign
    def select_campaign(self):
        return self.find_element(*Keen_Account_creation.campaign_record)
    ### Community Event
    def event(self):
        return self.find_element(*Keen_Account_creation.event_record)
    def validating_event(self):
        return self.find_element(*Keen_Account_creation.validate_popup_record_03)
    def validating_referral_meber(self):
        return self.find_element(*Keen_Account_creation.validate_popup_record_01)
    def validating_member_relationship(self):
        return self.find_element(*Keen_Account_creation.validate_popup_record_04)
    def Lead_other(self):
        return self.find_element(*Keen_Account_creation.keen_other)

    ### Referrals from Redesign
    ## Practice , Referring member, member relationship

    ### Editing the Keen Leads and Members Account
    existing_account=(By.XPATH, "//a[@title='Anil Kumar Kumar']")
    edit_record=(By.XPATH,"//button[@title='Edit']")
    search_owner=(By.XPATH,"(//input[@placeholder='Search Users'])[2]")
    permission_to_contact=(By.XPATH,"//button[@name='Permission_to_contact_source__c']")
    other_permission=(By.XPATH,"//input[@name='Other_Permission_to_contact_Details__c']")
    gender_popup=(By.XPATH,"(//div[@class='slds-grid slds-gutters slds-wrap'])[2]/div[11]/span/label/lightning-icon")
    address_popup=(By.XPATH,"(//div[@class='slds-grid slds-gutters slds-wrap'])[2]/div[16]/span/label/lightning-icon")
    def select_keen_member(self):
        return self.click_element(*Keen_Account_creation.existing_account)
    def click_on_edit(self):
        return self.click_element(*Keen_Account_creation.edit_record)
    def click_permession_to_contact(self):
        return self.click_element(*Keen_Account_creation.permission_to_contact)
    def enter_other_permission(self,text):
        return self.enter_text(text,*Keen_Account_creation.other_permission)
    def click_edit_owner(self):
        return self.click_element(*Keen_Account_creation.edit_owner)
    def click_search_owner(self):
        return self.click_element(*Keen_Account_creation.search_owner)
    def select_owner(self):
        return self.find_element(*Keen_Account_creation.options)
    def click_gender_popup(self):
        return self.click_element(*Keen_Account_creation.gender_popup)
    def click_address_popuop(self):
        return self.click_element(*Keen_Account_creation.address_popup)
    def edit_stress_address(self,text):
        return self.enter_text(text,*Keen_Account_creation.enter_Address_newcreation)
    ### Keen Duplicate records
    duplicate=(By.XPATH,"//div[@class='slds-modal__content slds-p-around_small']")
    existing_names=(By.XPATH,"//th[@data-label='Name']")
    existing_dob=(By.XPATH,"//td[@data-label='DoB']")
    duplicate_record=(By.XPATH,"//button[text()='Create Record']")
    more_tab=(By.XPATH,"(//span[text()='More'])[1]")
    reports_tab=(By.XPATH,"(//a[@href='/lightning/o/Report/home'])[2]")
    options_in_list=(By.XPATH,"//span[@class='slds-truncate']")
    options_for_county=(By.XPATH,"//button[@name='county']/following::div//lightning-base-combobox-item")
    report_options=(By.XPATH,"//a[@title='All Reports']")
    search_reports=(By.XPATH,"//input[@placeholder='Search all reports...']")
    data=(By.XPATH,"//lightning-primitive-cell-factory[@class='slds-cell-wrap']")
    verify_data=(By.XPATH,"//td[@class='data-grid-table-cell lightning-table-detail-cell data-grid-table-cell-even data-grid-table-cell-wrap']")
    cancel_record=(By.XPATH,"//button[text()='Cancel']")
    save_duplicate_record=(By.XPATH,"(//button[@name='submit'])[2]")
    def select_county(self):
        return self.Find_Elements(*Keen_Account_creation.options_for_county)
    def pop_up_Duplicate(self):
        return self.find_element(*Keen_Account_creation.duplicate)
    def Name_existing_record(self):
        return self.Find_Elements(*Keen_Account_creation.existing_names)
    def dob_existing_record(self):
        return self.Find_Elements(*Keen_Account_creation.existing_dob)
    def create_Duplicate_record(self):
        return self.click_element(*Keen_Account_creation.duplicate_record)
    def click_more(self):
        return self.click_element(*Keen_Account_creation.more_tab)
    def click_reports(self):
        Reports = self.find_element(*Keen_Account_creation.reports_tab)
        return self.driver.execute_script("arguments[0].click();", Reports)
    def tab_reports(self):
        tab=self.driver.find_element(By.XPATH,"//a[@href='/lightning/o/Report/home']")
        return self.driver.execute_script("arguments[0].click();", tab)
    def tabs_options(self):
        return self.Find_Elements(*Keen_Account_creation.options_in_list)
    def click_AllReports(self):
        return self.click_element(*Keen_Account_creation.report_options)
    def search_allreports(self,text):
        return self.enter_text(text,*Keen_Account_creation.search_reports)
    def click_Duplicate_reports(self):
        report=self.driver.find_element(By.XPATH,"//a[@title='Duplicate Report Data']")
        return self.driver.execute_script("arguments[0].click();", report)
    def duplicate_recorddata(self):
        return self.Find_Elements(*Keen_Account_creation.data)
    def validation_recorddata(self):
        return self.Find_Elements(*Keen_Account_creation.verify_data)
    ### //td[@class='data-grid-table-cell lightning-table-detail-cell data-grid-table-cell-odd data-grid-table-cell-wrap']
    def cancel_record_creation(self):
        return self.click_element(*Keen_Account_creation.cancel_record)
    def save_popup(self):
        return self.driver.find_element(*Keen_Account_creation.save_duplicate_record)
        ###### Verifing selected record

    # def verify_community_input(self):
    #     return self.driver.find_element(By.XPATH, "//input[@class='slds-combobox__input slds-input slds-combobox__input-value']")
    # def verify_practice_input(self):
    #     return self.driver.find_element(By.XPATH,"(//input[@class='slds-combobox__input slds-input slds-combobox__input-value'])[2]")
    # def verify_event_input(self):
    #     return self.driver.find_element(By.XPATH,"(//input[@class='slds-combobox__input slds-input slds-combobox__input-value'])[3]")


class Test_Generate_Quote(ActionUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    choose_member=(By.XPATH,"//a[@title]")
    generate_quote=(By.XPATH,"//button[@title='Generate Quote']")
    generate_popup=(By.XPATH,"//h2[@class='slds-text-heading_medium slds-hyphenate']")
    first_name_generate=(By.XPATH,"//input[@name='firstName']")
    last_name_generate=(By.XPATH,"//input[@name='lastName']")
    zipcode_generate=(By.XPATH,"//input[@name='shippingPostalCode']")
    dob_generate=(By.XPATH,"//input[@name='DoB__c']")
    email_generate=(By.XPATH,"//input[@name='email']")
    phone_generate=(By.XPATH,"//input[@name='phone']")
    plans=(By.XPATH,"(//span[@class='slds-form-element__label'])[5]")
    pharmacy=(By.XPATH,"(//button[@name='New'])[1]")
    doctors=(By.XPATH,"(//button[@name='New'])[3]")
    physicians_generatequote=(By.XPATH,"//button[@title='Physicians']")
    physician_record=(By.XPATH,"//input[@placeholder='Search Physician directory...']")
    primary_physician=(By.XPATH,"//input[@name='Is_Primary_Care_Physician__c']")
    physician_city=(By.XPATH,"//input[@name='City__c']")
    state_physician=(By.XPATH,"//button[@aria-label='State, --None--']")
    physicians_state_options=(By.XPATH,"//lightning-base-combobox-item[@class='slds-media slds-listbox__option slds-media_center slds-media_small slds-listbox__option_plain']")
    physicians_zipcode=(By.XPATH,"//input[@name='Zipcode__c']")
    medication_generatequote=(By.XPATH,"(//button[@name='New'])[2]")
    save_in_generatequote=(By.XPATH,"//button[@name='SaveEdit']")
    generate_records=(By.XPATH,"//span[@class='slds-media__body']//span/span")
    generate_pharmacy=(By.XPATH,"//input[@placeholder='Search Pharmacy directory...']")
    primary_pharmacy=(By.XPATH,"//span[text()='Is Pharmacy Primary']")
    def select_member(self):
        return self.Find_Elements(*Test_Generate_Quote.choose_member)
    def click_GenerateQuote(self):
        return self.click_element(*Test_Generate_Quote.generate_quote)
    def pop_up_GenerateQuote(self):
        return self.find_element(*Test_Generate_Quote.generate_popup)
    def elements(self):
        return self.driver.find_elements(By.XPATH,"lightning-layout-item")
    def firstName_Generate_Quote(self):
        return self.find_element(*Test_Generate_Quote.first_name_generate)
    def enter_lastname_GenerateQuote(self):
        return self.find_element(*Test_Generate_Quote.last_name_generate)
    def zipcode_GenerateQuote(self):
        return self.find_element(*Test_Generate_Quote.zipcode_generate)
    def DoB_GenerateQuote(self):
        return self.find_element(*Test_Generate_Quote.dob_generate)
    def Email_GenerateQuote(self):
        return self.driver.find_element(*Test_Generate_Quote.email_generate)
    def Phone_GenerateQuote(self):
        return self.find_element(*Test_Generate_Quote.phone_generate)
    def select_plans(self):
        return self.find_element(*Test_Generate_Quote.plans)
    def select_pharmacy(self):
        return self.click_element(*Test_Generate_Quote.pharmacy)
    def select_Doctors(self):
        return self.click_element(*Test_Generate_Quote.doctors)

    def physicians(self):
        return self.click_element(*Test_Generate_Quote.physicians_generatequote)
    def select_physician_directory(self,text):
        return self.enter_text(text,*Test_Generate_Quote.physician_record)
    def Is_Primary_Care_Physician(self):
        return self.click_element(*Test_Generate_Quote.primary_physician)
    def city(self,text):
        return self.enter_text(text,*Test_Generate_Quote.physician_city)
    def state(self):
        return self.click_element(*Test_Generate_Quote.state_physician)
    def select_state(self):
        return self.Find_Elements(*Test_Generate_Quote.physicians_state_options)
    def zipcode(self,text):
        return self.enter_text(text,*Test_Generate_Quote.physicians_zipcode)
    def select_medication(self):
        return self.click_element(*Test_Generate_Quote.medication_generatequote)
    def save(self):
        return self.driver.find_element(Test_Generate_Quote.save_in_generatequote)
    def select_record(self): ##### //lightning-base-combobox-item//span[2]  //span[@class='slds-media__body']
        return self.driver.find_elements(*Test_Generate_Quote.generate_records)
    #### Pharmacies

    def select_pharmacy_directory(self,text):
        return self.enter_text(text,Test_Generate_Quote.generate_pharmacy)
    def is_primary_pharmacy(self):
        return self.click_element(*Test_Generate_Quote.primary_pharmacy)

    #### Medications
    medicine_generatequote=(By.XPATH,"//input[@placeholder='Search Medication Directory...']")
    generatequote_fill=(By.XPATH,"//input[@name='Quantity_per_refill__c']")
    generatequote_frequency=(By.XPATH,"//button[@aria-label='Refill frequency, --None--']")
    popup_members=(By.XPATH,"//h2[@class='slds-modal__title slds-hyphenate slds-text-heading--medium']")
    frequency_options=(By.XPATH,"//lightning-base-combobox-item[@class='slds-media slds-listbox__option slds-media_center slds-media_small slds-listbox__option_plain']")
    priority_options=(By.XPATH,"//span[@class='slds-form-element__label']")
    generate_medicare=(By.XPATH,"//span[@class='slds-radio_faux']")
    subsidy=(By.XPATH,"//span[@class='slds-radio_faux']")
    sunfire=(By.XPATH,"//button[@title='Transfer to Sunfire']")
    def medication_search(self,text):
        return self.enter_text(text,*Test_Generate_Quote.medicine_generatequote)
    def Quantity_per_fill(self,text):
        return self.enter_text(text,*Test_Generate_Quote.generatequote_fill)
    def Refill_frequency(self):
        return self.click_element(*Test_Generate_Quote.generatequote_frequency)
    def select_frequency(self):
        return self.Find_Elements(*Test_Generate_Quote.frequency_options)
    def pop_up_new_members(self):
        return self.find_element(*Test_Generate_Quote.popup_members)

    def Patient_priority(self):
        return self.Find_Elements(*Test_Generate_Quote.priority_options)
    def medical_care_visit(self):
        return self.Find_Elements(*Test_Generate_Quote.generate_medicare)
    def  Low_Income_Subsidy(self):
        return self.click_element(*Test_Generate_Quote.subsidy)
    def click_TransferToSunfire(self):
        return self.click_element(*Test_Generate_Quote.sunfire)










