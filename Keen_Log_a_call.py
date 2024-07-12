from selenium.webdriver.common.by import By

from utilities.action_utils import ActionUtils


class New_Log(ActionUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    log_a_call=(By.XPATH, "//span[text()='Log a Call']")
    log_subject=(By.XPATH,"//input[@class='slds-combobox__input slds-input slds-combobox__input-value']")
    pick_subject=(By.XPATH,"//lightning-base-combobox-item")
    select_dispositions=(By.XPATH,"//span[@title]")
    log_start_date=(By.XPATH,"(//div[@class='dateTime-inputDate form-element form-element__control']//input)[3]")
    log_start_time=(By.XPATH,"(//label[text()='Time'])[3]")
    log_end_date=(By.XPATH,"(//div[@class='dateTime-inputDate form-element form-element__control']//input)[4]")
    log_end_time=(By.XPATH,"(//label[text()='Time'])[4]")
    log_satisfaction_score=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content slds-p-top--none']/div/div[2]/div[2]/div/div/div//div/div/div/a")
    select_score=(By.XPATH,"//ul//li[@role='presentation']/a")
    log_status=(By.XPATH,"//div[@class='test-id__section-content slds-section__content section__content slds-p-top--none']/div/div[5]/div/div/div/div//div/div/div/a")
    pick_status=(By.XPATH,"//li[@class='uiMenuItem uiRadioMenuItem']")
    log_save=(By.XPATH,"(//span[text()='Save'])[5]")
    verify_call=(By.XPATH,"//a[@class='subjectLink slds-truncate']")
    verify_fields=(By.XPATH,"//span[@class='test-id__field-value slds-form-element__static slds-grow ']")
    call_dispositions=(By.XPATH,"//div[text()='Dispositions']")
    move_to_choosen=(By.XPATH,"(//section[@class='tabs__content active uiTab']//div[@class='slds-form-element slds-hint-parent'])[2]//button[@title='Move selection to Chosen']")
    def click_log_a_call(self):
        keen_log = self.driver.find_element(*New_Log.log_a_call)
        return self.driver.execute_script("arguments[0].click();", keen_log)
    def subject(self,text):
        return self.enter_text(text,*New_Log.log_subject)
    def select_subject(self):
        return self.Find_Elements(*New_Log.pick_subject)
    def dispositions(self):
        return self.Find_Elements(*New_Log.select_dispositions)
    def click_move_to_choosen(self):
        return self.click_element(*New_Log.move_to_choosen)
    def start_date(self,text):
        return self.enter_text(text,*New_Log.log_start_date)
    def start_time(self,text):
        return self.enter_text(text,*New_Log.log_start_time)
    def End_date(self,text):
        return self.enter_text(text,*New_Log.log_end_date)
    def End_Time(self,text):
        return self.enter_text(text,*New_Log.log_end_time)
    def satisfaction_score(self):
        return self.click_element(*New_Log.log_satisfaction_score)
    def select_satisfaction_score(self):
        return self.Find_Elements(*New_Log.select_score)
    def status(self):
        return self.click_element(*New_Log.log_status)
    def select_status(self):
        return self.Find_Elements(*New_Log.pick_status)
    def save(self):
        return self.click_element(*New_Log.log_save)
    ### validation
    def validation_of_call(self):
        return self.Find_Elements(*New_Log.verify_call)
    def validation_of_data(self):
        return self.Find_Elements(*New_Log.verify_fields)
