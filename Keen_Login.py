from selenium.webdriver.common.by import By

from utilities.action_utils import ActionUtils


class Keen_login(ActionUtils):
    email=(By.ID,"username")
    password=(By.ID,"password")
    login=(By.ID,"Login")
    app =(By.XPATH,"//span[@class='appName slds-context-bar__label-action slds-context-bar__app-name']")
    view_options=(By.XPATH,"//div[@class='slds-icon-waffle']")
    search=(By.XPATH,"//input[@placeholder='Search apps and items...']")
    choose_app=(By.XPATH,"//div[@class='slds-size_small']")
    close_popup=(By.XPATH,"//button[@title='Close']")
    select_parentapp = (By.XPATH, "//p[@class='slds-truncate']")
    parent_records = (By.XPATH, "//span[@class='slds-grid slds-grid--align-spread forceInlineEditCell']//a")
    community_object = (By.XPATH, "//span[@title='Community and senior organizations']")
    community_records = (By.XPATH, "//th[@data-label='Organization name']//a//span")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def Click_close_popup(self):
        return self.click_element(*Keen_login.close_popup)
    def enter_email(self,text):
        return self.enter_text(text,*Keen_login.email)
    def enter_password(self,text):
        return self.enter_text(text,*Keen_login.password)
    def login_to_sandbox(self):
        return self.click_element(*Keen_login.login)
    def Verify_App(self):
        return self.driver.find_element(*Keen_login.app)
    def options(self):
        return self.click_element(*Keen_login.view_options)
    def search_App(self,text):
        return self.enter_text(text,*Keen_login.search)
    def select_app(self):
        return self.Find_Elements(*Keen_login.choose_app)
    def keen_leads_members(self):
        keen_leads = self.driver.find_element(By.XPATH, "(//span[text()='Keen leads and members'])[1]")
        return self.driver.execute_script("arguments[0].click();", keen_leads)
    def click_Parent_organization(self):
        return self.click_element(*Keen_login.select_parentapp)
    def List_existing_Parent_Records(self):
        return self.Find_Elements(*Keen_login.parent_records)
    def Community_Organization_ParentOrganization(self):
        return self.find_element(*Keen_login.community_object)
    def Associated_CommunityOrganization_records(self):
        return self.Find_Elements(*Keen_login.community_records)
