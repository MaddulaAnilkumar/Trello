from selenium.webdriver.common.by import By
from utilities.action_utils import ActionUtils
class New_Task(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    satisfaction_score=(By.XPATH,"(//div[@class='slds-p-around_small']//div//div//lightning-output-field)[1]")
    satisfaction_date=(By.XPATH,"(//div[@class='slds-p-around_small']//div//div//lightning-output-field)[2]")
    task=(By.XPATH,"//button[@title='Add']")
    task_subject=(By.XPATH,"//div[@data-target-selection-name='sfdc:RecordField.Task.Subject']//input")
    task_status=(By.XPATH,"//span[text()='Status']/following::a[1]")
    options=(By.XPATH,"(//div[@class='slds-dueling-list__options'])[1]//ul//li")
    task_start_date=(By.XPATH,"(//div[@data-target-selection-name='sfdc:RecordField.Task.Start_Date_Time__c']//following-sibling::input)[1]")
    task_start_time=(By.XPATH,"(//div[@data-target-selection-name='sfdc:RecordField.Task.Start_Date_Time__c']//following-sibling::input)[2]")
    task_end_date=(By.XPATH,"(//div[@data-target-selection-name='sfdc:RecordField.Task.End_Date_time__c']//following-sibling::input)[1]")
    task_end_time=(By.XPATH,"(//div[@data-target-selection-name='sfdc:RecordField.Task.End_Date_time__c']//following-sibling::input)[2]")
    task_select_time=(By.XPATH,"//ul[@class='datepicker--time__list']//li")
    task_subtype=(By.XPATH,"(//span[text()='Task Subtype']/following::a)[1]")
    task_type=(By.XPATH,"(//span[text()='Task Type']/following::a)[1]")
    select_satisfactionscore=(By.XPATH,"(//span[text()='Satisfaction Score']/following::a)[1]")
    move_to_choosen=(By.XPATH,"//button[@title='Move selection to Chosen']")
    dispositions=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content slds-p-top--none']/div/div[2]/div[2]//div[text()='Dispositions']")
    drop_down_options = (By.XPATH, "//span[@class='slds-truncate']")
    subtask_options=(By.XPATH,"//li[@role='presentation']//a[@title]")
    save_task=(By.XPATH,"//button[@title='Save']")
    def click_save(self):
        return self.click_element(*New_Task.save_task)
    def select_subtask_options(self):
        return self.Find_Elements(*New_Task.subtask_options)
    def Click_move_to_choosen(self):
        return self.click_element(*New_Task.move_to_choosen)
    def click_Task(self):
        return self.click_element(*New_Task.task)
    def check_satisfaction_score(self):
        return self.find_element(*New_Task.satisfaction_score)
    #### *New_Task.satisfaction_date
    def check_satisfaction_date(self):
        return self.find_element(*New_Task.satisfaction_score)
    def subject(self,text):
        return self.enter_text(text,*New_Task.task_subject)
    def status(self):
        return self.driver.find_element(*New_Task.task_status)
    def select_option(self):
        return self.driver.find_elements(*New_Task.options)
    def start_date(self,text):
        return self.enter_text(text,*New_Task.task_start_date)
    def start_time(self):
        return self.find_element(*New_Task.task_start_time)
    def select_time(self):
        return self.Find_Elements(*New_Task.task_select_time)
    def End_date(self,text):
        return self.enter_text(text,*New_Task.task_end_date)
    def End_time(self):
        return self.find_element(*New_Task.task_end_time)
    def click_satisfaction_score(self):
        return self.click_element(*New_Task.select_satisfactionscore)
    def Task_type(self):
        return self.click_element(*New_Task.task_type)
    def pick_options_list(self):
        return self.Find_Elements(*New_Task.drop_down_options)
    ## for new creation also
    task_satisfaction_score=(By.XPATH,"(//a[@class='select'])[2]")
    subtask=(By.XPATH,"(//a[@class='select'])[4]")
    save_task=(By.XPATH,"(//button[text()='Save'])[2]")
    task_validation=(By.CSS_SELECTOR, "a.subjectLink.slds-truncate")
    pick_task=(By.XPATH,"//a[title]")
    name=(By.XPATH,"(//ul[@class='orderedList'])[1]")
    pick_name=(By.XPATH,"//input[@title='Search DONOTUSEContacts']")
    pick_record=(By.XPATH,"//div[@class='primaryLabel slds-truncate slds-lookup__result-text']")
    module=(By.XPATH,"//a[@class='slds-button slds-button_reset slds-context-bar__label-action']")
    task_tab=(By.XPATH, "//span[@class='slds-truncate']")
    task_validate=(By.XPATH,"//span[@class='uiOutputText']")
    created_task=(By.XPATH,"//div[@class='slds-page-header__title slds-m-right--small slds-align-middle clip-text slds-line-clamp']")
    options_subject=(By.XPATH,"//lightning-base-combobox-item[@data-value]")
    def subject_options(self):
        return self.Find_Elements(*New_Task.options_subject)
    def select_satisfaction_score(self):
        return self.click_element(*New_Task.task_satisfaction_score)
    def Task_subtask(self):
        return self.click_element(*New_Task.subtask)
    def save(self):
        return self.driver.find_element(*New_Task.save_task)
    def new_task_validation(self):
        return self.Find_Elements(*New_Task.task_validation)
    def select_task(self):
        return self.Find_Elements(*New_Task.pick_task)
    def click_name(self):
        return self.driver.find_element(*New_Task.name)
    def select_name(self):
        return self.driver.find_element(*New_Task.pick_name)
    def select_record(self):
        return self.driver.find_elements(*New_Task.pick_record)
    def click_more_module(self):
        return self.driver.find_element(*New_Task.module)
    def tasks_tab(self):
        return self.Find_Elements(*New_Task.task_tab)
    def click_more(self):
        return self.driver.find_element(By.XPATH,"(//span[text()='More'])[1]")
    def Click_Tab_task(self):
        tab_task=self.driver.find_element(By.XPATH,"(//a[@href='/lightning/o/Task/home'])[2]")
        return self.driver.execute_script("arguments[0].click();", tab_task)
    def click_Task_module(self):
        tasks=self.driver.find_element(By.XPATH,"//a[@title='Tasks']")
        return self.driver.execute_script("arguments[0].click();", tasks)
    def click_task(self):
        return self.driver.find_elements(*New_Task.task_validate)
    verify_fields=(By.XPATH,"//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']//div[2]/span")
    verify_subject=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[1]")
    verify_relates_to=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[2]")
    verify_start_date_time=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[4]")
    verify_end_date_time=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[6]")
    verify_dispositions=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[5]")
    verify_satisfaction_score=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[7]")
    verify_comments=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[9]")
    verify_status=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[13]")
    verify_tasktype=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[3]")
    verify_name=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[16]")
    verify_due_date=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[11]")
    verify_priority=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[12]")
    verify_keencontact=(By.XPATH,"(//div[@class='slds-form-element slds-form-element_readonly slds-form-element_edit slds-grow slds-hint-parent override--slds-form-element']/div[2])[14]")
    def validation_Task(self):
        return self.get_text(*New_Task.created_task)
    def validation_fields(self):
        return self.Find_Elements(*New_Task.verify_fields)
    def validation_subject(self):
        return self.get_text(*New_Task.verify_subject)
    def validation_related_to(self):
        return self.find_element(*New_Task.verify_relates_to)
    def validation_start_data_time(self):
        return self.get_text(*New_Task.verify_start_date_time)
    def validation_dispositions(self):
        return self.get_text(*New_Task.verify_end_date_time)
    def validation_end_data_time(self):
        return self.get_text(*New_Task.verify_dispositions)
    def validation_satisfaction_score(self):
        return self.get_text(*New_Task.verify_satisfaction_score)
    def validation_comments(self):
        return self.get_text(*New_Task.verify_comments)
    def validation_Status(self):
        return self.get_text(*New_Task.verify_status)
    def validation_tasktype(self):
        return self.get_text(*New_Task.verify_tasktype)
    def validation_name(self):
        return self.get_text(*New_Task.verify_name)
    def validation_Due_date(self):
        return self.get_text(*New_Task.verify_due_date)
    def validation_priority(self):
        return self.get_text(*New_Task.verify_priority)
    def validation_keencontact(self):
        return self.driver.find_element(*New_Task.verify_keencontact)

    # // *[ @ id = "15895:0"] / div / div[1] / div[1] / div / div[2]
    # // *[ @ id = "15895:0"] / div / div[3] / div[1] / div / div[2] / span / span
    #//a[@class='subjectLink slds-truncate']


    ### Create New Task
    def click_on_showmore_button(self):
        return self.driver.find_element(By.XPATH,"//a[@title='Show one more action']")
    def click_new_task(self):
        return self.driver.find_element(By.XPATH,"//li[@class='uiMenuItem']//a")
    def new_task_subject(self):
        return self.driver.find_element(By.XPATH,"(//input[@type='text'])[6]")
    def select_subject(self):
        return self.driver.find_elements(By.XPATH," //lightning-base-combobox-item")
    def click_relates_to(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search Accepted plans by practce...']")
    def click_accepted_plansbypractices(self):
        return self.driver.find_element(By.XPATH,"//span[@title='New Accepted plans by practce']")
    def select_plans(self):
        return self.driver.find_element(By.XPATH,"//input[@title='Search PlanDetailsList']")
    def select_practicedirectory(self):
        return self.driver.find_element(By.XPATH,"//input[@title='Search Practice directory']")
    def click_save(self):
        return self.driver.find_element(By.XPATH,"(//span[text()='Save'])[3]")
    def click_task_type(self):
        return self.driver.find_element(By.XPATH,"(//a[@class='select'])[1]")
    def select_list_options(self):
        return self.driver.find_elements(By.XPATH,"//li[@class='uiMenuItem uiRadioMenuItem']")
    def new_task_priority(self):
        return self.driver.find_element(By.XPATH,"(//a[@class='select'])[3]")
    def new_tast_status(self):
        return self.driver.find_element(By.XPATH,"(//a[@class='select'])[4]")
    def new_task_subtype(self):
        return self.driver.find_element(By.XPATH,"(//a[@class='select'])[5]")
    def new_task_member(self):
        return self.driver.find_element(By.XPATH,"//input[@placeholder='Search DONOTUSEContacts...']")
    def add_member(self):
        return self.driver.find_elements(By.XPATH,"//div[@class='primaryLabel slds-truncate slds-lookup__result-text']")
    def add_task_member(self):
        return self.driver.find_element(By.XPATH,"//div[@title='Test Anil Kumar']")


    ###### Auto Task Updated

    def plans(self):
        return self.driver.find_element(By.XPATH, "//button[@title='Plans']")
    def pop_up(self):
        return self.driver.find_element(By.XPATH,"//h2[@class='slds-text-heading_medium slds-hyphenate']")
    def pop_up_new_members(self):
        return self.driver.find_element(By.XPATH,"//h2[@class='slds-modal__title slds-hyphenate slds-text-heading--medium']")
    def success_message(self):
        return self.driver.find_element(By.XPATH,"//div[contains(@id,'toastDescription')]//span")

    def new(self):
        return self.driver.find_element(By.XPATH, "//button[@name='New']")

    def search_plan_detail(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Search PlanDetailsList...']")
        # select Existing account

    def select_plan(self):
        return self.driver.find_elements(By.XPATH, "//span[@class='slds-media__body']")
        # return self.driver.find_elements(By.XPATH,"//ul[@role='group']//li")

    def validation_of_plan(self):
        return self.driver.find_elements(By.XPATH, "//th[@data-label]")

    def Enrolled_by_Keen(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Enrolled_by_Keen__c']")

    def Carrier_member_ID(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Carrier_member_ID__c']")

    def hra_completd(self):
        return self.driver.find_element(By.XPATH, "//input[@name='HRA_completed__c']")

    def HRA_completed_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='HRA_completed_date__c']")

    def Effective_date__c(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Effective_date__c']")

    def Enrollment_confirmation_number(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Enrollment_confirmation_number__c']")

    def plan_end_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Plan_end_date__c']")

    def enrollment_type(self):
        return self.driver.find_element(By.XPATH, "//button[@aria-label='Enrollment type, --None--']")

    def select_enrollment_type(self):
        return self.driver.find_elements(By.XPATH, "lightning-base-combobox-item")

    def App_submission_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='App_submission_date__c']")

    def App_approval_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='App_approval_date__c']")

    def Disenrollment_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Disenrollment_date__c']")

    def close(self):
        return self.driver.find_element(By.XPATH, "//button[@title='Close']")
    def verify_auto_generatedTask(self):
        return self.driver.find_elements(By.XPATH,"//a[@class='subjectLink slds-truncate']")
    def auto_task_start_date(self):
        return self.driver.find_element(By.XPATH,"(//span[@class='uiOutputDateTime'])[1]")
    def auto_task_end_date(self):
        return self.driver.find_element(By.XPATH,"(//span[@class='uiOutputDateTime'])[2]")
    def Auto_Commnets(self):
        return self.driver.find_element(By.XPATH,"//span[@class='uiOutputTextArea']")
    def Auto_priority(self):
        return self.driver.find_element(By.XPATH,"//span[text()='Normal']")
    def Auto_open(self):
        return self.driver.find_element(By.XPATH,"//span[text()='Open']")
    def Auto_task_subtype(self):
        return self.driver.find_element(By.XPATH,"(//span[text()='Call'])")
    def verify_auto_task_generated(self):
        return self.driver.find_element(By.XPATH,"(//span[@class='slds-grow slds-text-body--regular slds-text-color--default fade test-splitViewCardData'])[1]")

