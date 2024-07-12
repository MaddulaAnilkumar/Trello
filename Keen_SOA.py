from selenium.webdriver.common.by import By
from utilities.action_utils import ActionUtils
class Create_SOA_Form(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    member=(By.XPATH,"//a[@title='Test Williams']")
    edit=(By.XPATH,"//button[@title='Edit']")
    home=(By.XPATH,"//a[@title='Home']")
    address_details=(By.XPATH,"(//lightning-icon[@title='address detail'])")
    SOA = (By.XPATH, "//button[@title='Generate SOA']")
    SOA_Member=(By.XPATH,"//flexipage-component2[@data-target-selection-name='c_createSOAFormCmp']//span[text()='Scope of Appointment (SOA)']/following::button[text()='Generate SOA']")
    NewForm = (By.XPATH, "//flexipage-component2[@data-target-selection-name='c_createSOAFormCmp']//span[text()='Scope of Appointment (SOA)']/following::button[text()='Generate SOA']/following::div//lightning-menu-item[1]")
    SOA_TAb = (By.XPATH,"(//lightning-layout-item[@class='slds-p-vertical_x-small slds-size_12-of-12 slds-small-size_12-of-12'])[1]")
    Product_Types = (By.XPATH, "//span[@class='slds-checkbox_faux']")
    membersignature = (By.XPATH, "//input[@name='memberSignature']")
    date=(By.XPATH,"//input[@name='date']")
    agent_Name = (By.XPATH, "//input[@name='agentName']")
    agent_phone = (By.XPATH, "//input[@name='agentPhone']")
    agent_signature=(By.XPATH,"//input[@name='agentSignature']")
    members_SOAfirstname = (By.XPATH, "//input[@name='beneficiaryFirstName']")
    members_SOAlastname = (By.XPATH, "//input[@name='beneficiaryLastName']")
    members_phone = (By.XPATH, "//input[@name='beneficiaryPhone']")
    members_streetaddress = (By.XPATH, "//textarea[@name='streetAddress']")
    members_streetaddress2 = (By.XPATH, "//textarea[@name='addressLineTwo']")
    members_city = (By.XPATH, "//input[@name='city']")
    members_zipcode = (By.XPATH, "//input[@name='zipCode']")
    members_county = (By.XPATH, "//input[@name='county']")
    members_state = (By.XPATH, "//button[@name='state']")
    members_contact=(By.XPATH,"//button[@name='initialMethodOfContact']")
    method_contact=(By.XPATH,"//span[@class='slds-truncate']")
    dateofappointment=(By.XPATH,"//input[@name='dateOfAppointment']")
    explination=(By.XPATH,"//input[@name='explanation']")
    save_soa=(By.XPATH,"//button[text()='Save']")
    save_and_submit=(By.XPATH,"//span[text()='Save & Submit']")
    soa_records=(By.XPATH,"//tr[@class='slds-hint-parent']")
    soa_visible=(By.XPATH,"(//header[@class='slds-media slds-media_center slds-has-flexi-truncate'])[6]")
    options=(By.XPATH,"//lightning-base-combobox-item")
    #### Address of a selected Member
    profile = (By.XPATH, "//button[@class='slds-button branding-userProfile-button slds-button slds-global-actions__avatar slds-global-actions__item-action forceHeaderButton']")
    name_ad=(By.XPATH,"(//a[@class='profile-link-label'])[1]")
    settings = (By.XPATH, "(//a[@class='profile-link-label'])[2]")
    advisor_firstName = (By.XPATH, "(//input[@maxlength='40'])[1]")
    advisor_secondName = (By.XPATH, "(//input[@maxlength='80'])")
    adviosr_phone = (By.XPATH, "(//input[@maxlength='40'])[2]")
    member_firstname=(By.XPATH,"//input[@name='FirstName']")
    member_lastname=(By.XPATH,"//input[@name='LastName']")
    Street=(By.XPATH,"//textarea[@name='street']")
    phone=(By.XPATH,"//input[@name='Phone']")
    city=(By.XPATH,"//input[@name='city']")
    state=(By.XPATH,"//input[@name='province']")
    zipcode=(By.XPATH,"//input[@name='postalCode']")
    county=(By.XPATH,"//input[@name='County__c']")
    soa_saved_successmessage=(By.XPATH,"//h2[@class='slds-text-heading_small']")
    close=(By.XPATH,"//button[@title='Close']")
    cancel=(By.XPATH,"(//button[text()='Cancel'])[2]")
    soa_save=(By.XPATH,"//div[@class='slds-p-around_large buttons-container']//button[@part='button button-icon']")
    sent_signature=(By.XPATH,"//span[text()='Save & Send for Signature']")
    signature_errors=(By.XPATH,"//div[text()='Signature field should be empty']")
    contact_details_popup=(By.XPATH,"//h1[text()='Confirm Contact Details']")
    send_to_docusign=(By.XPATH,"//h1[text()='Confirm Contact Details']/following::div[@class='slds-modal__footer']//button[text()='Save & Send']")
    access_code=(By.XPATH,"//input[@name='DocuAccessCode']")
    verify_soa=(By.XPATH,"//label[text()='SOA:']/following-sibling::lightning-output-field//div//lightning-formatted-text")
    ok_soa_button=(By.XPATH,"//section[@aria-description='Please update ‘SOA’ date field on the member record to reflect the latest SOA.']//button")
    view_document=(By.XPATH,"//span[text()=' REVIEW DOCUMENT ']")
    verification_code=(By.XPATH,"//input[@name='ds$hldrBdy$txtAccessCode']")
    verify_accesscode_page=(By.XPATH,"//span[text()='Please enter the access code to view the document']")
    validate_button=(By.XPATH,"//button[text()='Validate']")
    review_document=(By.XPATH,"//h1[@class='title']//span[text()='Please Review & Act on These Documents']")
    signature_of_member=(By.XPATH,"//input[contains(@class,'signing-required ')]")
    finish_document=(By.XPATH,"(//div[@class='documents-finish-button-decoration']//button[@id='end-of-document-btn-finish' or text()='Finish'])[1]")
    verify_sign=(By.XPATH,"//h1[contains(text(),'Done Signing')]")
    continue_button=(By.XPATH,"//h1[contains(text(),'Done Signing')]/following::div[2]//button")
    sign_page=(By.XPATH,"//h1[contains(text(),' finished signing! ')]")
    select_docusign_document=(By.XPATH,"//div[@class='xT']//span[text()='***Test Document***Medicare Scope of Appointment: eSignature Request']")
    phone_security=(By.XPATH,"//div[text()='Security Check']")
    phone_security_continue=(By.XPATH,"//div[text()='Security Check']/following::button[1]")
    continue_document=(By.XPATH,"//button[text()='Continue']")
    soa_date_document=(By.XPATH,"//label[text()='DateSigned']/following-sibling::span")
    save_signature=(By.XPATH,"//button[text()='Save']/following::span[text()='Save & Send for Signature']")
    user_name=(By.XPATH, "//input[@name='identifier']")
    password=(By.XPATH,"//input[@name='Passwd']")
    next_button=(By.XPATH,"//div[@id='identifierNext']//button")
    refresh=(By.XPATH,"//div[@data-tooltip='Refresh']//div[@class='asa']")
    click_options_list=(By.XPATH,"//div[@gh='mtb']//div[@data-tooltip='Select']//div//div[@class='G-asx T-I-J3 J-J5-Ji']")
    unread_option=(By.XPATH,"//div[@id=':kh']//div[text()='Unread']")
    sign_request=(By.XPATH,"(//button[@class='lm']/div[text()='Medicare Scope of Appointment: eSignature Request'])[1]")
    ##### (//div[text()='Medicare Scope of Appointment: eSignature Request'])[1]
    prod_request=(By.XPATH,"(//span//span[text()='Medicare Scope of Appointment: eSignature Request'])[1]")
    validation_field=(By.XPATH,"//input[@name='ds$hldrBdy$txtAccessCode']/following::button[contains(@id,'ds_hldrBdy_btnDSAccessCode_btnInline')]")
    existing_soa_latest_record=(By.XPATH,"//lightning-primitive-cell-factory[@data-label='Created Date']//a")
    def select_soa_existing_records(self):
        return self.Find_Elements(*Create_SOA_Form.existing_soa_latest_record)
    def select_document_sign_request(self):
        return self.click_element(*Create_SOA_Form.prod_request)
    def select_unread_option(self):
        return self.click_element(*Create_SOA_Form.unread_option)
    def select_options(self):
        return self.click_element(*Create_SOA_Form.click_options_list)
    def enter_mail_user_name(self,text):
        return self.enter_text(text,*Create_SOA_Form.user_name)
    def click_next_button(self):
        return self.click_element(*Create_SOA_Form.next_button)
    def enter_mail_password(self,text):
        return self.enter_text(text,*Create_SOA_Form.password)
    def click_refresh_page(self):
        return self.click_element(*Create_SOA_Form.refresh)
    def verify_confirm_page(self):
        return self.find_element(*Create_SOA_Form.contact_details_popup)
    def click_sent_signature(self):
        return self.click_element(*Create_SOA_Form.sent_signature)
    def click_select_docusign_document(self):
        return self.click_element(*Create_SOA_Form.select_docusign_document)
    def verify_document_page(self):
        return self.find_element(*Create_SOA_Form.view_document)
    def click_document(self):
        return self.click_element(*Create_SOA_Form.view_document)
    def verify_access_code(self):
        return self.find_element(*Create_SOA_Form.access_code)
    def click_save_send_docusign(self):
        return self.click_element(*Create_SOA_Form.send_to_docusign)
    ### Window
    def verify_access_code_page(self):
        return self.find_element(*Create_SOA_Form.verify_accesscode_page)
    def enter_verification_code(self,text):
        return self.enter_text(text,*Create_SOA_Form.verification_code)
    def verify_validation_button(self):
        return self.find_element(*Create_SOA_Form.validation_field)
    def click_validate_button(self):
        return self.click_element(*Create_SOA_Form.validate_button)
    ###
    def verify_phone_security(self):
        return self.find_element(*Create_SOA_Form.phone_security)
    def verify_phone_security_continue(self):
        return self.click_element(*Create_SOA_Form.phone_security_continue)
    ## exception
    def verify_review_act_document(self):
        return self.find_element(*Create_SOA_Form.review_document)
    def click_continue_document(self):
        return self.click_element(*Create_SOA_Form.continue_document)
    def enter_member_signature(self,text):
        return self.enter_text(text,*Create_SOA_Form.signature_of_member)
    def click_finish(self):
        return self.click_element(*Create_SOA_Form.finish_document)

    def verify_sign_popup(self):
        return self.find_element(*Create_SOA_Form.verify_sign)
    def click_sign_continue(self):
        return self.click_element(*Create_SOA_Form.continue_button)
    def verify_successfull_sign(self):
        return self.find_element(*Create_SOA_Form.sign_page)
    ### close the mail driver and move to SOA form

    def verify_soa_date(self):
        return self.find_element(*Create_SOA_Form.soa_date_document)

    def click_ok_soa_button(self):
        return self.click_element(*Create_SOA_Form.ok_soa_button)
    def check_soa_date(self):
        return self.driver.find_element(*Create_SOA_Form.verify_soa)
    def click_soa_save(self):
        return self.find_element(*Create_SOA_Form.soa_save)
    def Click_profile(self):
        return self.click_element(*Create_SOA_Form.profile)
    def Click_Settings(self):
        return self.click_element(*Create_SOA_Form.settings)
    def NameAdvisor(self):
        return self.find_element(*Create_SOA_Form.name_ad)
    def Advisor_firstName(self):
        return self.find_element(*Create_SOA_Form.advisor_firstName)
    def Advisor_LastName(self):
        return self.find_element(*Create_SOA_Form.advisor_secondName)
    def Advisor_Phone(self):
        return self.find_element(*Create_SOA_Form.adviosr_phone)
    def Click_HomeTab(self):
        keen_leads = self.driver.find_element(*Create_SOA_Form.home)
        return self.driver.execute_script("arguments[0].click();", keen_leads)
    def Click_generateSOAHome(self):
        return self.click_element(*Create_SOA_Form.SOA)
    def select_member(self):
        return self.click_element(*Create_SOA_Form.member)
    def SOA_popup(self):
        return self.driver.find_element(*Create_SOA_Form.SOA_TAb)
    def click_GenerateSOA(self):
        return self.click_element(*Create_SOA_Form.SOA_Member)
    def click_New_Form(self):
        return self.click_element(*Create_SOA_Form.NewForm)
    def Click_Check_Types_Products_Discuss(self):
        return self.Find_Elements(*Create_SOA_Form.Product_Types)
    def Enter_MemberSignature(self):
        return self.find_element(*Create_SOA_Form.membersignature)
    def Verify_date(self):
        return self.driver.find_element(*Create_SOA_Form.date)
    def AgentName(self):
        return self.driver.find_element(*Create_SOA_Form.agent_Name)
    def AgentPhone(self):
        return self.driver.find_element(*Create_SOA_Form.agent_phone)
    def AgentSignature(self):
        return self.find_element(*Create_SOA_Form.agent_signature)
    def MemberFirstName(self):
        return self.driver.find_element(*Create_SOA_Form.members_SOAfirstname)
    def MemberLastName(self):
        return self.driver.find_element(*Create_SOA_Form.members_SOAlastname)
    def MemberPhone(self):
        return self.enter_text(*Create_SOA_Form.members_phone)
    def MemberSteertAddress(self):
        return self.driver.find_element(*Create_SOA_Form.members_streetaddress)
    def MemberStreetAddress2(self):
        return self.find_element(*Create_SOA_Form.members_streetaddress2)
    def MemberCity(self):
        return self.driver.find_element(*Create_SOA_Form.members_city)
    def MemberZipcode(self):
        return self.driver.find_element(*Create_SOA_Form.members_zipcode)
    def MemberCounty(self):
        return self.driver.find_element(*Create_SOA_Form.members_county)
    def MemberState(self):
        return self.driver.find_element(*Create_SOA_Form.members_state)
    def select_options(self):
        return self.Find_Elements(*Create_SOA_Form.options)
    def Initial_method_contact(self):
        return self.driver.find_element(*Create_SOA_Form.members_contact)
    def Select_Method_Contact(self):
        return self.Find_Elements(*Create_SOA_Form.method_contact)
    def Appointment_Date(self):
        return self.find_element(*Create_SOA_Form.dateofappointment)
    def PlanExplination(self):
        return self.driver.find_element(*Create_SOA_Form.explination)
    def Click_save(self):
        return self.click_element(*Create_SOA_Form.save_soa)
    def Click_Save_and_Submit(self):
        return self.find_element(*Create_SOA_Form.save_and_submit)
    def View_file(self):
        return self.Find_Elements(By.XPATH,"//td[@data-label='File']//span//div")
    save_message=(By.XPATH,"//h2[@class='slds-text-heading_small']")
    def Save_Success_Message(self):
        return self.find_element(*Create_SOA_Form.save_message)
    check_advisor=(By.XPATH,"//td[@data-label='Created By']//span//div")
    def Verify_Advisor(self):
        return self.Find_Elements(*Create_SOA_Form.check_advisor)
    check_signature=(By.XPATH,"//td[@data-label='Signature Status']//span//div")
    check_date=(By.XPATH,"//th[@data-label='Created Date']//span//div")
    save_options_soa=(By.XPATH,"//div[@id='LightningComponentid']//div[@class='slds-p-around_large buttons-container']//button[@class='slds-button slds-button_icon-container']")
    def Verify_Signature(self):
        return self.Find_Elements(*Create_SOA_Form.check_signature)
    def Verify_SOAdate(self):
        return self.Find_Elements(*Create_SOA_Form.check_date)
    def SOA_SAVE_SUBMIT_records(self):
        return self.driver.find_elements(*Create_SOA_Form.soa_records)
    def click_save_options(self):
        return self.click_element(*Create_SOA_Form.save_options_soa)
    def click_save_signature(self):
        return self.click_element(*Create_SOA_Form.save_signature)
    def Move_to_SOA(self):
        return self.driver.find_element(*Create_SOA_Form.soa_visible)
    def selected_SOA(self):
        return self.driver.find_elements(By.XPATH,"//td[@data-label='User']//div[@class='slds-truncate']")
    ### Existing Member
    def click_on_edit(self):
        return self.click_element(*Create_SOA_Form.edit)
    def wait_edit(self):
        return self.wait_for_element(*Create_SOA_Form.edit)
    def selected_Members_FirstName(self):
        return self.driver.find_element(*Create_SOA_Form.member_firstname)
    def selected_Members_LastName(self):
        return self.driver.find_element(*Create_SOA_Form.member_lastname)
    def selected_Members_phone(self):
        return self.driver.find_element(*Create_SOA_Form.phone)
    def selected_Member_Address(self):
        return self.click_element(*Create_SOA_Form.address_details)
    def selected_Members_street(self):
        return self.driver.find_element(*Create_SOA_Form.Street)
    def selected_Memebrs_City(self):
        return self.driver.find_element(*Create_SOA_Form.city)
    def selected_Members_state(self):
        return self.driver.find_element(*Create_SOA_Form.state)
    def selected_Members_county(self):
        return self.driver.find_element(*Create_SOA_Form.county)
    def selected_Members_zipcode(self):
        return self.driver.find_element(*Create_SOA_Form.zipcode)
    def close_AddressPopup(self):
        return self.click_element(*Create_SOA_Form.close)
    def click_on_cancel(self):
        return self.click_element(*Create_SOA_Form.cancel)

