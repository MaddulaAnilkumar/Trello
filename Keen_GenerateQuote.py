from selenium.webdriver.common.by import By

from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
from utilities.action_utils import ActionUtils


class Keen_Quote_Generation(ActionUtils,Create_capture_member_details):
    close_plan_popuop=(By.XPATH,"//button[@name='CancelEdit']")
    edit = (By.XPATH, "//button[@title='Edit']")
    member_firstname = (By.XPATH, "//input[@name='FirstName']")
    member_lastname = (By.XPATH, "//input[@name='LastName']")
    cancel=(By.XPATH,"//button[text()='Cancel']")
    account_cancel=(By.XPATH,"(//button[@class='slds-button slds-button_neutral'])[2]")
    associated_records=(By.XPATH, "//th[@data-label='Members Physcian Name']")
    row_number=(By.XPATH,"//tr[@data-row-number]")
    generate_quote=(By.XPATH,"//button[text()='Generate Quote']")
    click_elements=(By.XPATH,"lightning-layout-item")
    first_name=(By.XPATH,"//input[@name='firstName']")
    last_name=(By.XPATH,"//input[@name='lastName']")
    zipcode=(By.XPATH,"//label[text()='Zip Code']/following::div//input[@name='shippingPostalCode']")
    dob=(By.XPATH,"//input[@name='dob']")
    click_plans=(By.XPATH,"(//span[@class='slds-form-element__label'])[5]")
    plans_type_checkboxes=(By.XPATH,"//div[@class='slds-modal__content slds-scrollable_y slds-p-around_large']//lightning-layout-item//lightning-checkbox-group//span[@class='slds-checkbox_faux']")
    medicar_advantage=(By.XPATH,"(//div[@class='slds-modal__content slds-scrollable_y slds-p-around_large']//lightning-layout-item//lightning-checkbox-group//span[@class='slds-checkbox_faux'])[1]")
    plans_types_name=(By.XPATH,"//label[text()='Please select the plan types to discuss with consumer']/following-sibling::lightning-checkbox-group//span[@class='slds-form-element__label']")
    pharmacy_new=(By.XPATH,"(//button[@name='New'])[1]")
    new=(By.XPATH,"(//button[@name='New'])[2]")
    doctors_new=(By.XPATH,"(//button[@name='New'])[3]")
    medicareid=(By.XPATH,"//input[@name='medicareId']")
    medicaidid=(By.XPATH,"//input[@name='medicaidId']")
    ssn=(By.XPATH,"//input[@name='ssn']")
    addressline2=(By.XPATH,"//input[@name='addressLineTwo']")
    address=(By.XPATH,"//textarea[@name='streetAddress']")
    generate_city=(By.XPATH,"//input[@name='city']")
    generate_state=(By.XPATH,"//button[@name='state']")
    generate_zipcode=(By.XPATH,"//input[@name='shippingPostalCode']")
    generate_county=(By.XPATH,"//input[@name='county']")
    doctors_vist_yes=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-grid slds-wrap slds-m-top_x-small']//lightning-layout-item//span//span)[1]")
    doctors_vist_no=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-grid slds-wrap slds-m-top_x-small']//lightning-layout-item//span//span)[2]")
    medication_yes=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-grid slds-wrap slds-m-top_x-small']//lightning-layout-item//span//span)[3]")
    medication_no=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-grid slds-wrap slds-m-top_x-small']//lightning-layout-item//span//span)[4]")
    pharmacy_yes=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-grid slds-wrap slds-m-top_x-small']//lightning-layout-item//span//span)[5]")
    pharmacy_no=(By.XPATH,"//label[text()='Do you want to add a preferred pharmacy?']/following-sibling::lightning-layout-item//span[text()='No']")
    doctor_visit_or_receive_medicalcare=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-m-top_x-small'])[1]//span//label/span")
    extra_help_or_low_income=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-m-top_x-small'])[2]//span//label/span")
    medicare_suplimentary=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-m-top_x-small'])[3]//span//label/span")
    important_to_patient=(By.XPATH,"//fieldset[@class='slds-form-element box-shadow slds-box slds-box_small slds-m-top_x-small']//div/div/div/label/span[@class='slds-checkbox_faux']")
    doctors_add=(By.XPATH,"(//label[text()='Do you want to add any doctors that you would like to be covered?']/following::button[@name='New'])[1]")
    medication_add=(By.XPATH,"(//label[text()='Do you want to add a prescription medication?']/following::button[@name='New'])[1]")
    pharmacy_add=(By.XPATH,"(//label[text()='Do you want to add a preferred pharmacy?']/following::button[@name='New'])[1]")
    phone=(By.XPATH,"//input[@name='phone']")
    county=(By.XPATH,"//label[text()='County']/following::div//button[@name='county']")
    medicare_label=(By.XPATH,"//label[text()='Do you want to add any doctors that you would like to be covered?']")
    verify_physician_record=(By.XPATH,"//th[@data-label='Name']//lightning-primitive-cell-factory//span//div")
    created_physician=(By.XPATH,"(//input[@data-value])[2]")
    state_physician=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content align-with-title']//records-record-layout-row[6]//button")
    select_state_physician=(By.XPATH,"//lightning-base-combobox-item[@class='slds-media slds-listbox__option slds-media_center slds-media_small slds-listbox__option_plain']")
    physician_zipcode=(By.XPATH,"//input[@name='Zipcode__c']")
    save_popup=(By.XPATH,"//button[@name='SaveEdit']")
    search_mediaction_field=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-grid slds-wrap slds-m-top_x-small'])[2]")
    search_pharmacy_field=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-grid slds-wrap slds-m-top_x-small'])[3]")
    quantity_new_medication=(By.XPATH,"//input[@name='Quantity_per_refill__c']")
    move_to_extra=(By.XPATH,"//h2[text()='Do you want to add Hospital Indemnity or Medicare Supplement information?']")
    drug_pay=(By.XPATH,"//h2[text()='Drug co-pay/co-insurance']")
    pick_drug_option=(By.XPATH,"//lightning-radio-group[@class='checkboxClass slds-m-top_x-small slds-form-element']//label/span")
    quote_medicare_supplementary=(By.XPATH,"//h2[text()='Do you want to add Hospital Indemnity or Medicare Supplement information?']")
    medicare_options=(By.XPATH,"//div[@class='slds-box slds-box_small box-shadow slds-m-top_x-small']//span//span")
    medicare_yes=(By.XPATH,"//label[text()='Customer details']")
    effective_date=(By.XPATH,"//button[@name='effectiveDate']")
    pick_effectivedate=(By.XPATH,"(//label[contains(text(), 'Customer details')]/following-sibling::lightning-layout//lightning-base-combobox-item[@class='slds-media slds-listbox__option slds-media_center slds-media_small slds-listbox__option_plain'])[1]")
    pick_date=(By.XPATH,"//lightning-base-combobox-item//span[@class='slds-truncate']")
    PartA_month=(By.XPATH,"//button[@name='partA_enrollmentMonth']")
    PartA_year=(By.XPATH,"//button[@name='partA_enrollmentYear']")
    PartB_month=(By.XPATH,"//button[@name='partB_EffectiveMonth']")
    PartB_year=(By.XPATH,"//button[@name='partB_EffectiveYear']")
    tobacco_use=(By.XPATH,"//input[@name='tobaccoUse']/following-sibling::label//span[text()]")
    household_discount=(By.XPATH,"//input[@name='householdDiscount']/following-sibling::label//span[text()]")
    transfer_to_sunfire_success_message=(By.XPATH,"//span[@class='toastMessage forceActions Text']")
    transfer_to_sunfire=(By.XPATH,"//button[@title='Transfer to Sunfire']")
    quote_created=(By.XPATH,"//h2[text()='Quote created in Sunfire!']")
    close_quote_created_popup=(By.XPATH,"//button[text()='Close']")
    generate_email=(By.XPATH,"//input[@name='email']")
    Supplement_yes=(By.XPATH,"(//div[@class='slds-box slds-box_small box-shadow slds-m-top_x-small'])[3]//span//label/span")
    Supplement_no=(By.XPATH,"(//span[@class='slds-radio_faux'])[24]")
    data_failure_message=(By.XPATH,"//div[@class='toastTitle slds-text-heading--small']")
    verify_invalid_data_entered_fields = (
    By.XPATH, "//label[contains(text(), 'Contact Info')]/following-sibling::lightning-layout//div[text()]")
    error_message_quote=(By.XPATH,"//span[text()]")
    error_toast_message=(By.XPATH,"//div[text()]")
    move_to_plans=(By.XPATH,"//label[text()='Please select the plan types to discuss with consumer']")
    network_preference=(By.XPATH,"//button[@name='Provider_Network_Preference__c']")
    network_preference_list=(By.XPATH,"//button[@name='Provider_Network_Preference__c']/following::div//lightning-base-combobox-item//span[@title]")
    recieve_extra_help=(By.XPATH,"//h2[text()='Do you receive Extra Help / Low Income Subsidy (optional)?']")
    gender=(By.XPATH,"//input[@value='Female']/parent::span//span[text()='Female']")
    def __init__(self,driver):
            super().__init__(driver)
            self.driver = driver
            # self.move_to_plans = (By.XPATH, "//label[text()='Please select the plan types to discuss with consumer']")
    def click_gender(self):
        return self.click_element(*Keen_Quote_Generation.gender)
    def move_to_extra_help_section(self):
        return self.find_element(*Keen_Quote_Generation.recieve_extra_help)
    def smart_quote_plan_close(self):
        return self.click_element(*Keen_Quote_Generation.close_plan_popuop)
    def quote_status_errror(self):
        return self.Find_Elements(*Keen_Quote_Generation.error_message_quote)
    def verify_error_toast_message(self):
        return self.Find_Elements(*Keen_Quote_Generation.error_toast_message)
    def click_on_edit(self):
        move_to_edit=self.driver.find_element(*Keen_Quote_Generation.edit)
        return self.driver.execute_script("arguments[0].click();", move_to_edit)
    def verify_toast_message(self):
        return self.find_element(*Keen_Quote_Generation.data_failure_message)
    def click_supplement(self):
        return self.Find_Elements(*Keen_Quote_Generation.Supplement_yes)
    def click_no_supplement(self):
        return self.click_element(*Keen_Quote_Generation.Supplement_no)
    def selected_Members_FirstName(self):
        return self.driver.find_element(*Keen_Quote_Generation.member_firstname)
    def selected_Members_LastName(self):
        return self.driver.find_element(*Keen_Quote_Generation.member_lastname)
    def click_on_cancel(self):
        return self.driver.find_element(*Keen_Quote_Generation.account_cancel)
    def validation_of_records(self):
        return self.driver.find_elements(*Keen_Quote_Generation.associated_records)
    def validation_fields(self):
        return self.driver.find_elements(*Keen_Quote_Generation.row_number)
    def click_GenerateQuote(self):
        return self.click_element(*Keen_Quote_Generation.generate_quote)
    def elements(self):
        return self.driver.Find_Elements(*Keen_Quote_Generation.click_elements)
    def firstName_Generate_Quote(self):
        return self.find_element(*Keen_Quote_Generation.first_name)
    def enter_lastname_GenerateQuote(self):
        return self.find_element(*Keen_Quote_Generation.last_name)
    def zipcode_GenerateQuote(self):
        return self.driver.find_element(*Keen_Quote_Generation.zipcode)
    def DoB_GenerateQuote(self):
        return self.find_element(*Keen_Quote_Generation.dob)
    def enter_medicareid(self):
        return self.find_element(*Keen_Quote_Generation.medicareid)
    def enter_medicaidid(self):
        return self.find_element(*Keen_Quote_Generation.medicaidid)
    def enter_ssn(self):
        return self.find_element(*Keen_Quote_Generation.ssn)
    def street_address(self):
        return self.find_element(*Keen_Quote_Generation.address)
    def enter_addressline2(self):
        return self.find_element(*Keen_Quote_Generation.addressline2)
    def enter_city(self):
        return self.find_element(*Keen_Quote_Generation.generate_city)
    def click_plan_types(self):
        return self.Find_Elements(*Keen_Quote_Generation.plans_types_name)
    def verify_medicare_advantage(self):
        return self.find_element(*Keen_Quote_Generation.medicar_advantage)
    def verify_medicare_label(self):
        return self.find_element(*Keen_Quote_Generation.medicare_label)
    def click_doctor_yes(self):
        return self.click_element(*Keen_Quote_Generation.doctors_vist_yes)
    def Email_GenerateQuote(self):
        return self.find_element(*Keen_Quote_Generation.generate_email)
    def Phone_GenerateQuote(self):
        return self.find_element(*Keen_Quote_Generation.phone)
    def select_plans(self):
        return self.driver.find_element(*Keen_Quote_Generation.click_plans)
    def select_pharmacy_GenerateQuote(self):
        return self.driver.find_element(*Keen_Quote_Generation.pharmacy_new)
    def move_to_extra_help_subsidy(self):
        return self.find_element(*Keen_Quote_Generation.move_to_extra)
    def click_extra_help_or_subsidy(self):
        return self.Find_Elements(*Keen_Quote_Generation.extra_help_or_low_income)
    def verify_drug_pay(self):
        return self.find_element(*Keen_Quote_Generation.drug_pay)
    def select_drug_pay(self):
        return self.Find_Elements(*Keen_Quote_Generation.pick_drug_option)
    def select_important_to_patient(self):
        return self.Find_Elements(*Keen_Quote_Generation.important_to_patient)
    def select_generate_state(self):
        return self.find_element(*Keen_Quote_Generation.generate_state)
    def select_Doctors_Generate(self):
        return self.click_element(*Keen_Quote_Generation.doctors_add)
    def validation_associated_physician(self):
        return self.get_text(*Keen_Quote_Generation.verify_physician_record)
    def verify_created_physician(self):
        return self.find_element(*Keen_Quote_Generation.created_physician)
    def state(self):
        return self.click_element(*Keen_Quote_Generation.state_physician)
    def select_state(self):
        return self.driver.find_elements(*Keen_Quote_Generation.select_state_physician)
    def enter_physician_zipcode(self,text):
        return self.enter_text(text,*Keen_Quote_Generation.physician_zipcode)
    def enter_physcian(self,text):
        return self.enter_text(text,*Keen_Quote_Generation.Drug)
    def member_doctor_vist(self):
        return self.Find_Elements(*Keen_Quote_Generation.doctor_visit_or_receive_medicalcare)
    def select_medication_GenerateQuote(self):
        return self.click_element(*Keen_Quote_Generation.medication_add)
    def save(self):
        return self.click_element(*Keen_Quote_Generation.save_popup)
    def move_to_medication(self):
        return self.find_element(*Keen_Quote_Generation.search_mediaction_field)
    def move_to_pharmacy(self):
        return self.find_element(*Keen_Quote_Generation.pharmacy_add)
    def click_pharmacy_no(self):
        return self.click_element(*Keen_Quote_Generation.pharmacy_no)
    def verify_medicare_supplimentary(self):
        return self.find_element(*Keen_Quote_Generation.quote_medicare_supplementary)
    def medicare_supplimetary_options(self):
        return self.Find_Elements(*Keen_Quote_Generation.medicare_options)
    def verify_medicare_yes(self):
        return self.find_element(*Keen_Quote_Generation.medicare_yes)
    def click_Effective_Date(self):
        return self.click_element(*Keen_Quote_Generation.effective_date)
    def select_effective_date(self):
        return self.click_element(*Keen_Quote_Generation.pick_effectivedate)
    def select_PratA_enrollment_date(self):
        return self.find_element(*Keen_Quote_Generation.PartA_month)
    def select_PartA_enrollment_year(self):
        return self.find_element(*Keen_Quote_Generation.PartA_year)
    def select_PartB_enrollment_month(self):
        return self.find_element(*Keen_Quote_Generation.PartB_month)
    def select_PartB_enrollment_year(self):
        return self.find_element(*Keen_Quote_Generation.PartB_year)
    def select_medicare_Tobacco_use(self):
        return self.Find_Elements(*Keen_Quote_Generation.tobacco_use)
    def select_Household_Discount(self):
        return self.Find_Elements(*Keen_Quote_Generation.household_discount)
    def click_pharamcy(self):
        return self.click_element(*Keen_Quote_Generation.pharmacy_add)
    def Quantity_per_fill(self,text):
        return self.enter_text(text,*Keen_Quote_Generation.quantity_new_medication)
    def click_TransferToSunfire(self):
        return self.click_element(*Keen_Quote_Generation.transfer_to_sunfire)
    def Member_county(self):
        return self.find_element(*Keen_Quote_Generation.county)
    def verify_success_quote(self):
        return self.find_element(*Keen_Quote_Generation.quote_created)
    def Quote_close(self):
        return self.click_element(*Keen_Quote_Generation.close_quote_created_popup)
    def Quote_success_message(self):
        return self.driver.find_element(*Keen_Quote_Generation.transfer_to_sunfire_success_message)
    def Failure_Quote(self):
        return self.driver.find_element(By.XPATH,"//div[@class='slds-theme--error slds-notify--toast slds-notify slds-notify--toast forceToastMessage']")

    def verify_errors(self):
        return self.Find_Elements(*Keen_Quote_Generation.verify_invalid_data_entered_fields)
    def scroll_plans(self):
        return self.find_element(*Keen_Quote_Generation.move_to_plans)
    def click_network_preference(self):
        return self.click_element(*Keen_Quote_Generation.network_preference)
    def select_network_options(self):
        return self.Find_Elements(*Keen_Quote_Generation.network_preference_list)
################################### SMART QUOTE FEATURE
    smart_quote=(By.XPATH,"//button[@title='Smart Quote']")
    bna_tab=(By.XPATH,"//button[@name='basicNeedsAssessment']")
    tobacco_label=(By.XPATH,"//p[text()=' Tobacco Consumption']")
    tobacco_consumption_yes=(By.XPATH,"//input[@name='tobaccoUse' and @value='y']/parent::span//span")
    tobacco_consumption_no=(By.XPATH,"//input[@name='tobaccoUse' and @value='n']/parent::span//span")
    question_1=(By.XPATH,"//button[@name='UQ_Times_you_visit_PCP__c']")
    question_options=(By.XPATH,"//lightning-base-combobox-item[@data-value]")
    question_2=(By.XPATH,"//button[@name='UQ_Times_you_visit_Specialist__c']")
    question_3=(By.XPATH,"//button[@name='UQ_Times_admitted_to_hospital__c']")
    current_plan_no=(By.XPATH,"//input[@name='isPlanDetailsRequired' and @value='n']//parent::span//span")
    current_plan_verification=(By.XPATH,"//div[text()='Please select a current plan.']")
    current_plan_new=(By.XPATH,"//label[contains(text(),'plan information?')]/parent::div//button[@name='New']")
    def click_smart_Quote(self):
        return self.click_element(*Keen_Quote_Generation.smart_quote)
    ##### New tab
    def smart_quote_tab(self):
        return self.find_element(*Keen_Quote_Generation.bna_tab)
    def move_to_tobaccco_label(self):
        return self.find_element(*Keen_Quote_Generation.tobacco_label)
    def click_tobacco_yes(self):
        return self.find_element(*Keen_Quote_Generation.tobacco_consumption_yes)
    def click_tobacco_no(self):
        return self.click_element(*Keen_Quote_Generation.tobacco_consumption_no)
    def verify_current_plan(self):
        return self.find_element(*Keen_Quote_Generation.current_plan_verification)
    def click_current_plan_no(self):
        return self.click_element(*Keen_Quote_Generation.current_plan_no)
    def click_current_plan_new(self):
        return self.click_element(*Keen_Quote_Generation.current_plan_new)
        ############### Medicare Supplimentary Tab ##########
    error_message = (By.XPATH, "//h2[text()]")
        ### if "Failed to get plan recommendations"
    close_button_error_popup = (By.XPATH, "//button[text()='Close']")
    def verify_message(self):
        return self.get_text(*Keen_Quote_Generation.error_message)
    def click_close(self):
        return self.click_element(*Keen_Quote_Generation.close_button_error_popup)
    medicare_supplimentary_tab=(By.XPATH,"//button[@name='medSuppUnderwriting']")
    guaranteed_issue_yes=(By.XPATH,"//input[@name='GI_Is_Eligible_Guaranteed_Issue__c' and @value='Yes']/parent::span//span")
    guaranteed_issue_no=(By.XPATH,"//input[@name='GI_Is_Eligible_Guaranteed_Issue__c' and @value='No']/parent::span//span")
    overall_health=(By.XPATH,"//button[@name='GI_Members_Overall_Health__c']")
    surgeries_yes=(By.XPATH,"//input[@name='GI_Any_surgeries_in_past_yr__c' and @value='Yes']/parent::span//span")
    surgeries_no=(By.XPATH,"//input[@name='GI_Any_surgeries_in_past_yr__c' and @value='No']/parent::span//span")
    move_mobility=(By.XPATH,"//label[text()='Do you have any mobility limitations? If yes, select the limitation(s) and its last occurrence.']")
    mobility_limitations_yes=(By.XPATH,"//input[@name='Any_Mobility_Limitations__c' and @value='Yes']/parent::span//span")
    mobility_limitations_no=(By.XPATH,"//input[@name='Any_Mobility_Limitations__c' and @value='No']/parent::span//span")
    ### if yes
    limitation_input=(By.XPATH,"//div[text()='Limitation']/parent::div/parent::div//input")
    limitations_option=(By.XPATH,"//span[text()]")
    med_supp_options=(By.XPATH,"//div[@data-label]")
    experienced_year=(By.XPATH,"//div[text()='Limitation']/parent::div/parent::div//button[@data-value]")
    move_to_major_health=(By.XPATH,"//label[text()='Do you have any major health conditions or have you been medically diagnosed, treated, or had surgery for any of the following? If yes, select the condition(s) and its last occurrence?']")
    major_health_condition_yes=(By.XPATH,"//input[@name='Any_Major_Health_Conditions__c' and @value='Yes']")
    major_health_condition_no=(By.XPATH,"//input[@name='Any_Major_Health_Conditions__c' and @value='No']")
    major_health_input=(By.XPATH,"//div[text()='Condition']/parent::div/parent::div//input")
    major_health_experienced_year=(By.XPATH,"//div[text()='Condition']/parent::div/parent::div//button[@data-value]")
    ## select options
    move_psa=(By.XPATH,"//label[text()='Do you have a pacemaker or high PSA test result?']")
    pacemaker_highpsa_yes = (By.XPATH, "//input[@name='Any_Other_Limitations__c' and @value='Yes']/parent::span//span")
    pacemaker_highpsa_no = (By.XPATH, "//input[@name='Any_Other_Limitations__c' and @value='No']/parent::span//span")
    pacemaker_search = (By.XPATH, "//input[@name='Any_Other_Limitations__c' and @value='Yes']/parent::span/parent::div/parent::div/parent::fieldset/parent::lightning-radio-group/parent::div/parent::div/parent::div//div[text()='Limitation']/parent::div/parent::div//input")
    pacemaker_experience_year = (By.XPATH, "//input[@name='Any_Other_Limitations__c' and @value='Yes']/parent::span/parent::div/parent::div/parent::fieldset/parent::lightning-radio-group/parent::div/parent::div/parent::div//div[text()='Limitation']/parent::div/parent::div//button[@data-value]")
    move_hospital=(By.XPATH,"//label[text()='Have you been confined in a hospital three or more times in the past two years for a same or similar condition?']")
    confined_hospital_last_two_year_yes = (By.XPATH, "//input[@name='Have_you_been_hospital_confined__c' and @value='Yes']/parent::span//span")
    confined_hospital_last_two_year_no = (By.XPATH,  "//input[@name='Have_you_been_hospital_confined__c' and @value='No']/parent::span//span")
    move_medical_professional=(By.XPATH,"//label[text()='Have you been advised by a medical professional to have treatment, further diagnostic evaluation, diagnostic testing, follow up visits or any surgery that has not been performed?']")
    advised_by_a_medical_professional_yes = (By.XPATH, "//input[@name='Any_advise_by_med_Professional__c' and @value='Yes']/parent::span//span")
    advised_by_a_medical_professional_no = (By.XPATH, "//input[@name='Any_advise_by_med_Professional__c' and @value='No']/parent::span//span")
    drug_usage_section=(By.XPATH,"//label[text()='Have you used any form of tobacco, an electronic cigarette (e-cig) or other nicotine product in past 12 months?']")
    tobacco_electronic_cigarette_consumption_yes = (By.XPATH,"//input[@name='Used_any_form_of_tobacco__c' and @value='Yes']/parent::span//span")
    tobacco_electronic_cigarette_consumption_no = (By.XPATH,"//input[@name='Used_any_form_of_tobacco__c' and @value='No']/parent::span//span")
    success_toast_message=(By.XPATH,"//div[text()='Success!']")
    plan_proceed=(By.XPATH,"//button[text()='Proceed']")
    ## select_options
    def verify_toast_message_success(self):
        return self.find_element(*Keen_Quote_Generation.success_toast_message)
    def click_medicaretab(self):
        return self.click_element(*Keen_Quote_Generation.medicare_supplimentary_tab)
    def member_eligible_for_guaranteed_issue_yes(self):
        return self.find_element(*Keen_Quote_Generation.guaranteed_issue_yes)
    def member_eligible_for_guaranteed_issue_no(self):
        return self.find_element(*Keen_Quote_Generation.guaranteed_issue_no)
    def click_overall_health(self):
        return self.click_element(*Keen_Quote_Generation.overall_health)
    def click_surgeries_yes(self):
        return self.click_element(*Keen_Quote_Generation.guaranteed_issue_yes)
    def move_to_mobility_limitations(self):
        return self.find_element(*Keen_Quote_Generation.move_mobility)
    def click_surgeries_no(self):
        return self.click_element(*Keen_Quote_Generation.guaranteed_issue_no)
    def click_mobility_limitations_yes(self):
        return self.click_element(*Keen_Quote_Generation.mobility_limitations_yes)
    def click_mobility_limitations_no(self):
        return self.click_element(*Keen_Quote_Generation.mobility_limitations_no)
    def search_limitation(self,text):
        return self.enter_text(text,*Keen_Quote_Generation.limitation_input)
    def click_medsupp_options(self):
        return self.Find_Elements(*Keen_Quote_Generation.med_supp_options)
    def click_experienced_years(self):
        return self.click_element(*Keen_Quote_Generation.experienced_year)
    ## select options
    def move_to_major_health_conditions(self):
        return self.find_element(*Keen_Quote_Generation.move_to_major_health)
    def click_major_health_conditions_yes(self):
        return self.click_element(*Keen_Quote_Generation.major_health_condition_yes)
    def enter_major_health_condition(self):
        return self.find_element(*Keen_Quote_Generation.major_health_input)
    def click_major_health_condition_experienced_year(self):
        return self.click_element(*Keen_Quote_Generation.major_health_experienced_year)
    def click_major_health_conditions_no(self):
        return self.click_element(*Keen_Quote_Generation.major_health_condition_no)
    def move_high_psa(self):
        return self.find_element(*Keen_Quote_Generation.move_psa)
    def click_pacemaker_highpsa_yes(self):
        return self.click_element(*Keen_Quote_Generation.pacemaker_highpsa_yes)
    def pacemaker_search_input(self):
        return self.find_element(*Keen_Quote_Generation.pacemaker_search)
    def click_pacemaker_experience_year(self):
        return self.click_element(*Keen_Quote_Generation.pacemaker_experience_year)
    def click_pacemaker_highpsa_no(self):
        return self.click_element(*Keen_Quote_Generation.pacemaker_highpsa_no)
    def move_confined_hospital(self):
        return self.find_element(*Keen_Quote_Generation.move_hospital)
    def click_confined_hospital_last_two_year_yes(self):
        return self.click_element(*Keen_Quote_Generation.confined_hospital_last_two_year_yes)
    def click_confined_hospital_last_two_year_no(self):
        return self.click_element(*Keen_Quote_Generation.confined_hospital_last_two_year_no)
    def move_medical_professional_advice(self):
        return self.find_element(*Keen_Quote_Generation.move_medical_professional)
    def click_advised_by_a_medical_professional_yes(self):
        return self.click_element(*Keen_Quote_Generation.advised_by_a_medical_professional_yes)
    def click_advised_by_a_medical_professional_no(self):
        return self.click_element(*Keen_Quote_Generation.advised_by_a_medical_professional_no)
    def move_drug_usage_section(self):
        return self.find_element(*Keen_Quote_Generation.drug_usage_section)
    def click_tobacco_electronic_cigarette_consumption_yes(self):
        return self.click_element(*Keen_Quote_Generation.tobacco_electronic_cigarette_consumption_yes)
    def click_tobacco_electronic_cigarette_consumption_no(self):
        return self.click_element(*Keen_Quote_Generation.tobacco_electronic_cigarette_consumption_no)
    def click_plan_proceed(self):
        return self.click_element(*Keen_Quote_Generation.plan_proceed)




    ###### Advance Needs Assessment
    advanced_needs_assessment=(By.XPATH,"//button[@name='advanceNeedsAssessment']")
    ##### Greaterthan 80years age
    alert_message=(By.XPATH,"//c-basic-needs-assessment-cmp//h2[text()='Message!']")
    proceed_button=(By.XPATH,"//c-basic-needs-assessment-cmp//button[@type='button' and text()='Proceed']")
    financial_concerns_yes=(By.XPATH,"//input[@name='FC_Any_Trouble_Making_Payments__c' and @value='Yes']/parent::span//span")
    financial_concerns_no=(By.XPATH,"//input[@name='FC_Any_Trouble_Making_Payments__c' and @value='No']/parent::span//span")
    yes_to_previousquestion=(By.XPATH,"//input[@name='FC_Trouble_paying_bills__c' and @value='Yes']/parent::span//span")
    no_to_previousquestion=(By.XPATH,"//input[@name='FC_Trouble_paying_bills__c' and @value='No']/parent::span//span")
    dental_options=(By.XPATH,"//label[text()='Do you have any major dental issues like needing an extraction or untreated tooth ache?']")
    dental_vision_hearing=(By.XPATH,"//button[@name='DVH_How_often_dentist_per_year__c']")
    #### use options for this x path ='question_options'
    move_to_dental_services=(By.XPATH,"//label[text()=', what dental services do you need?']")
    major_dental_issues_yes=(By.XPATH,"//input[@name='DVH_any_major_dental_issues__c' and @value='Yes']/parent::span//span")
    dental_services_need=(By.XPATH,"//p[text()='Dental/Vision/Hearing']/parent::div//input[@placeholder='Select an Option']")
    major_dental_issues_no=(By.XPATH,"//input[@name='DVH_any_major_dental_issues__c' and @value='No']/parent::span//span")
    ##### if yes
    services_you_need=(By.XPATH,"(//input[@placeholder='Select an Option'])[1]")
    ### title options
    lenses_or_glases_field=(By.XPATH,"//label[text()='Do you wear glasses or lenses?']")
    do_you_wearglasses_or_lenses_yes=(By.XPATH,"//input[@name='DVH_Wear_glasses_or_lense__c' and @value='Yes']/parent::span//span")
    do_you_wearglasses_or_lenses_no=(By.XPATH,"//input[@name='DVH_Wear_glasses_or_lense__c' and @value='No']/parent::span//span")
    move_to_hearing_field=(By.XPATH,"//label[text()='Do you have trouble hearing?']")
    do_you_have_trouble_hearing_yes=(By.XPATH,"//input[@name='DVH_Trouble_hearing__c' and @value='Yes']/parent::span//span")
    do_you_have_trouble_hearing_no = (By.XPATH, "//input[@name='DVH_Trouble_hearing__c' and @value='No']/parent::span//span")
    move_to_hearing_aids=(By.XPATH,"//label[text()='Do you use hearing aids?']")
    do_you_use_hearing_aids_yes = (By.XPATH, "//input[@name='DVH_Use_hearing_aids__c' and @value='Yes']/parent::span//span")
    do_you_use_hearing_aids_no= (By.XPATH, "//input[@name='DVH_Use_hearing_aids__c' and @value='No']/parent::span//span")
    move_to_drive_need_drive=(By.XPATH,"//label[text()='How do you get to the doctor today? Do you drive or does a family member or a caregiver take you?']")
    do_you_drive_or_does_a_family_member=(By.XPATH,"//button[@name='SS_who_drive_you_to_doctor__c']")
    move_to_ride_fields=(By.XPATH,"//label[text()='If answer to previous question is has help or needs a ride: Do you want us to find you a plan that gives you free rides to the doctor?']")
    #### use options for this x path ='question_options'
    free_rides_to_the_doctor_yes=(By.XPATH,"//input[@name='SS_Need_plan_for_free_rides_to_doctor__c' and @value='Yes']")
    free_rides_to_the_doctor_no=(By.XPATH,"//input[@name='SS_Need_plan_for_free_rides_to_doctor__c' and @value='No']")
    move_to_meals=(By.XPATH,"//label[text()=' Do you typically eat healthy meals?']")
    do_you_typically_eat_healthy_meals_yes=(By.XPATH,"//input[@name='SS_Typically_eat_healthy_meals__c'and @value='Yes']/parent::span//span")
    do_you_typically_eat_healthy_meals_no=(By.XPATH,"//input[@name='SS_Typically_eat_healthy_meals__c'and @value='No']/parent::span//span")
    move_to_daily_meals=(By.XPATH,"//label[text()=' Do you have trouble getting healthy meals daily?']")
    do_you_have_trouble_getting_healthy_meals_daily_yes=(By.XPATH,"//input[@name='SS_Trouble_getting_healthy_meals__c'and @value='Yes']/parent::span//span")
    do_you_have_trouble_getting_healthy_meals_daily_no= (By.XPATH, "//input[@name='SS_Trouble_getting_healthy_meals__c'and @value='No']/parent::span//span")
    food_card=(By.XPATH,"//label[text()=' Do you currently have a OTC card, food card or flex card?']")
    have_otccard_foodcard_yes=(By.XPATH,"//input[@name='SS_Have_card__c'and @value='Yes']/parent::span//span")
    food_card_type=(By.XPATH,"//button[@name='SS_Card_type__c']")
    have_otccard_foodcard_no = (By.XPATH, "//input[@name='SS_Have_card__c'and @value='No']/parent::span//span")
    plan_ference=(By.XPATH,"//p[text()='Plan preference']")
    insurance_carriers=(By.XPATH, "//p[text()='Plan preference']/parent::div//input[@placeholder='Select an Option']")
    move_to_preference_plans=(By.XPATH,"//label[text()=' Do you have a preference between a HMO and a PPO plan?']")
    preference_hmo=(By.XPATH,"//input[@name='PP_Preference_HMO_or_PPO_plan__c' and @value='HMO']/parent::span//span")
    preference_ppo = (By.XPATH, "//input[@name='PP_Preference_HMO_or_PPO_plan__c' and @value='PPO']/parent::span//span")
    move_to_part_b=(By.XPATH,"//label[text()=' Did the client specifically asks for a Part B give back?']")
    part_b_give_back_yes=(By.XPATH,"//input[@name='PP_Client_Part_B_giveback__c' and @value='Yes']/parent::span//span")
    part_b_give_back_no= (By.XPATH, "//input[@name='PP_Client_Part_B_giveback__c' and @value='No']/parent::span//span")

    def click_advanced_need_assessment(self):
        self.click_element(*Keen_Quote_Generation.advanced_needs_assessment)
    def verify_alert(self):
        return self.find_element(*Keen_Quote_Generation.alert_message)
    def click_proceed(self):
        return self.click_element(*Keen_Quote_Generation.proceed_button)
    def click_financial_concerns_yes(self):
        return self.click_element(*Keen_Quote_Generation.financial_concerns_yes)
    def click_financial_concerns_no(self):
        return self.click_element(*Keen_Quote_Generation.financial_concerns_no)
    def click_yes_to_previousquestion(self):
        return self.click_element(*Keen_Quote_Generation.yes_to_previousquestion)
    def click_no_to_previousquestion(self):
        return self.click_element(*Keen_Quote_Generation.no_to_previousquestion)
    def move_to_dental_options(self):
        return self.find_element(*Keen_Quote_Generation.dental_options)
    def click_dental_vision_hearing(self):
        return self.click_element(*Keen_Quote_Generation.dental_vision_hearing)
    #### select_frequency from capture_member
    def move_dental_services_need(self):
        return self.find_element(*Keen_Quote_Generation.move_to_dental_services)
    def click_major_dental_issues_yes(self):
        return self.click_element(*Keen_Quote_Generation.major_dental_issues_yes)
    def click_dental_services_need(self):
        return self.click_element(*Keen_Quote_Generation.dental_services_need)
    def click_major_dental_issues_no(self):
        return self.click_element(*Keen_Quote_Generation.major_dental_issues_no)
    ### if yes dental
    def click_services_you_need(self):
        return self.click_element(*Keen_Quote_Generation.services_you_need)
    #### select_frequency from capture_member
    def move_to_lenses(self):
        return self.find_element(*Keen_Quote_Generation.lenses_or_glases_field)
    def click_do_you_wearglasses_or_lenses_yes(self):
        return self.click_element(*Keen_Quote_Generation.do_you_wearglasses_or_lenses_yes)
    def click_do_you_wearglasses_or_lenses_no(self):
        return self.click_element(*Keen_Quote_Generation.do_you_wearglasses_or_lenses_no)
    def move_to_hearing(self):
        return self.find_element(*Keen_Quote_Generation.move_to_hearing_field)
    def click_do_you_have_trouble_hearing_yes(self):
        return self.click_element(*Keen_Quote_Generation.do_you_have_trouble_hearing_yes)
    def click_do_you_have_trouble_hearing_no(self):
        return self.click_element(*Keen_Quote_Generation.do_you_have_trouble_hearing_no)
    def move_to_hearing_aids_field(self):
        return self.find_element(*Keen_Quote_Generation.move_to_hearing_aids)
    def click_do_you_use_hearing_aids_yes(self):
        return self.click_element(*Keen_Quote_Generation.do_you_use_hearing_aids_yes)
    def click_do_you_use_hearing_aids_no(self):
        return self.click_element(*Keen_Quote_Generation.do_you_use_hearing_aids_no)
    def move_to_ride(self):
        return self.find_element(*Keen_Quote_Generation.move_to_drive_need_drive)
    def click_do_you_drive_or_does_a_family_member(self):
        return self.click_element(*Keen_Quote_Generation.do_you_drive_or_does_a_family_member)
    def click_free_rides_to_the_doctor_yes(self):
        return self.click_element(*Keen_Quote_Generation.free_rides_to_the_doctor_yes)
    def click_free_rides_to_the_doctor_no(self):
        return self.click_element(*Keen_Quote_Generation.free_rides_to_the_doctor_no)
    def move_to_need_ride_field(self):
        return self.find_element(*Keen_Quote_Generation.move_to_ride_fields)
    def move_to_meals_fields(self):
        return self.find_element(*Keen_Quote_Generation.move_to_meals)
    def click_do_you_typically_eat_healthy_meals_yes(self):
        return self.click_element(*Keen_Quote_Generation.do_you_typically_eat_healthy_meals_yes)
    def click_do_you_typically_eat_healthy_meals_no(self):
        return self.click_element(*Keen_Quote_Generation.do_you_typically_eat_healthy_meals_no)
    def move_to_meals_daily_fields(self):
        return self.find_element(*Keen_Quote_Generation.move_to_daily_meals)
    def click_do_you_have_trouble_getting_healthy_meals_daily_yes(self):
        return self.click_element(*Keen_Quote_Generation.do_you_have_trouble_getting_healthy_meals_daily_yes)
    def click_do_you_have_trouble_getting_healthy_meals_daily_no(self):
        return self.click_element(*Keen_Quote_Generation.do_you_have_trouble_getting_healthy_meals_daily_no)
    def move_to_food_card(self):
        return self.find_element(*Keen_Quote_Generation.food_card)
    def click_have_otccard_foodcard_yes(self):
        return self.click_element(*Keen_Quote_Generation.have_otccard_foodcard_yes)
    def click_food_card_type(self):
        return self.click_element(*Keen_Quote_Generation.food_card_type)
    def click_have_otccard_foodcard_no(self):
        return self.click_element(*Keen_Quote_Generation.have_otccard_foodcard_no)
    def move_to_plans(self):
        return self.find_element(*Keen_Quote_Generation.plan_ference)
    def click_insurance_carriers(self):
        return self.click_element(*Keen_Quote_Generation.insurance_carriers)
    def move_to_part_B_field(self):
        return self.find_element(*Keen_Quote_Generation.move_to_part_b)
    def click_part_b_give_back_yes(self):
        return self.click_element(*Keen_Quote_Generation.part_b_give_back_yes)
    def click_part_b_give_back_no(self):
        return self.click_element(*Keen_Quote_Generation.part_b_give_back_no)
    #### title
    def move_to_preference_plan_field(self):
        return self.find_element(*Keen_Quote_Generation.move_to_preference_plans)
    def click_preference_hmo(self):
        return self.click_element(*Keen_Quote_Generation.preference_hmo)
    def click_preference_ppo(self):
        return self.click_element(*Keen_Quote_Generation.preference_ppo)

    ###### Plan recommendations Tab #####
    plans_failed_message=(By.XPATH,"//h2[text()='Failed to get plan recommendations']")
    close_failed_popup=(By.XPATH,"//button[text()='Close']")
    plan_recommendations_tab = (By.XPATH, "//button[@name='planRecommendations']")
    medicare_supplimentary_plans=(By.XPATH,"//p[text()='Medicare Supplement']")
    medicare_supplimentary_plans_list = (By.XPATH, "//p[text()='Medicare Supplement']/parent::div//p[@class='plan-name-style']")
    medicare_advantage_part_d_plan = (By.XPATH, "//div[@data-id='mapd']//div//p[@class='slds-text-title_bold' and contains(text(),'Medicare Advantage/Part D')]")
    medicare_advantage_part_d_plan_list = (By.XPATH , "//p[text()='Medicare Advantage/Part D']/parent::div//p[@class='plan-name-style']")
    medicare_advantage_plan = (By.XPATH , "//div[@data-id='ma']/parent::div//p[text()='Medicare Advantage']")
    medicare_advantage_plan_list = (By.XPATH , "//div[@data-id='ma']/parent::div//p[@class='plan-name-style']")
    part_d_plan=(By.XPATH,"//div[@data-id='pdp']//p[text()='Part D']")
    pard_d_plan_detail_list=(By.XPATH,"//div[@data-id='pdp']/parent::div//p[@class='plan-name-style']")
    def verfiy_plans_for_user(self):
        return self.find_element(*Keen_Quote_Generation.plans_failed_message)
    def click_close_failed_popup(self):
        return self.click_element(*Keen_Quote_Generation.close_failed_popup)
    def click_plan_recommendations_tab(self):
        return self.click_element(*Keen_Quote_Generation.plan_recommendations_tab)
    def verify_medicare_supplimentary_plans(self):
        return self.find_element(*Keen_Quote_Generation.medicare_supplimentary_plans)
    def verify_medicare_supplimentary_plans_list(self):
        return self.find_element(*Keen_Quote_Generation.medicare_supplimentary_plans_list)
    def verify_medicare_advantage_part_d_plan(self):
        return self.find_element(*Keen_Quote_Generation.medicare_advantage_part_d_plan)
    def verify_medicare_advantage_part_d_plan_list(self):
        return self.find_element(*Keen_Quote_Generation.medicare_advantage_part_d_plan_list)
    def verify_medicare_advantage_plan(self):
        return self.find_element(*Keen_Quote_Generation.medicare_advantage_plan)
    def verify_medicare_advantage_plan_list(self):
        return self.find_element(*Keen_Quote_Generation.medicare_advantage_plan_list)
    def verify_part_d(self):
        return self.find_element(*Keen_Quote_Generation.part_d_plan)
    def verify_part_d_list(self):
        return self.find_element(*Keen_Quote_Generation.pard_d_plan_detail_list)

    ############# Get aledade data ########################
    aledade_button=(By.XPATH,"//button[@title='Get Aledade Data']")
    message=(By.XPATH,"//h2[text()='Message!']")
    text_msg=(By.XPATH,"//h2[text()='Message!']/parent::header/parent::div//label")
    close_aledade_data=(By.XPATH,"//button[text()='Close']")
    data_accept=(By.XPATH,"//h2[text()='Consent to access patient data']")
    data_accept_yes=(By.XPATH,"//button[text()='Yes']")
    data_accept_no=(By.XPATH,"//button[text()='No']")
    success_message=(By.XPATH,"//div[text()='Success!]")
    def verfiy_aledade_button(self):
        return self.find_element(*Keen_Quote_Generation.aledade_button)
    def verify_member_is_aledade(self):
        return self.find_element(*Keen_Quote_Generation.text_msg)
    def click_close_aledade_message(self):
        return self.click_element(*Keen_Quote_Generation.close_aledade_data)
    def consent_member_data(self):
        return self.click_element(*Keen_Quote_Generation.data_accept)
    def consent_member_data_yes(self):
        return self.click_element(*Keen_Quote_Generation.data_accept_yes)
    def consent_member_data_no(self):
        return self.click_element(*Keen_Quote_Generation.data_accept_no)
    def verify_toast_message_aledade(self):
        return self.find_element(*Keen_Quote_Generation.success_message)


