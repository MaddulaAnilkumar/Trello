from selenium.webdriver.common.by import By

from utilities.action_utils import ActionUtils


class Wishes_Message(ActionUtils):
    def __init__(self,driver):
        super.__init__(self,driver)
        self.driver=driver
    edit=(By.XPATH,"(//button[@class='slds-button slds-button_neutral'])[15]")
    birthday=(By.XPATH,"(//div[@class='slds-rich-text-area__content slds-grow slds-text-color-weak standin'])[1]")
    anniversary=(By.XPATH,"(//div[@class='slds-rich-text-area__content slds-grow slds-text-color-weak standin'])[2]")
    save=(By.XPATH,"//button[@name='submit']")
    validating=(By.XPATH,"//lightning-formatted-rich-text[@class='slds-form-element__static slds-rich-text-editor__output']")
    ## Add Plans
    def click_on_edit(self):
        return self.click_element(*Wishes_Message.edit)
    def enter_Birthday_wishes(self,text):
        return self.enter_text(text,*Wishes_Message.birthday)
    def enter_Anniversary_Message(self,text):
        return self.enter_text(text,*Wishes_Message.anniversary)
    def save_messages(self):
        return self.find_element(*Wishes_Message.save)
    def validation_of_wishes(self):
        return self.Find_Elements(*Wishes_Message.validating)
