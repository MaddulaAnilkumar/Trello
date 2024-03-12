import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utilities import logger_utils

class ActionUtils():
    log = logger_utils.get_logger()
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def find_element(self, *element):
        return self.driver.find_element(*element)

    def Find_Elements(self,*web_element):
        self.log.info("Finding web elements... {}".format(web_element))
        return self.driver.find_elements(*web_element)

    def verify_link_text_presence(self, text):
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, text, *web_element):
        self.log.info("# Select an option from dropdown... {}".format(web_element))
        sel = Select(self.find_element(*web_element))
        sel.select_by_visible_text(text)

    def web_driver_wait(self, timeout):
        return WebDriverWait(self.driver, timeout)

    def wait_for_element(self, *web_element):
        self.log.info("Wait for element to appear...{}".format(web_element))
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(*web_element))

    def wait_for_element_selected(self,web_element):
        self.log.info("Wait for element to appear...{}".format(web_element))
        WebDriverWait(self.driver, 60).until(EC.element_located_to_be_selected(web_element))

    def wait_for_elements(self,*web_element):
        self.log.info("Wait for element to appear...{}".format(web_element))
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(*web_element))
    def click_element(self, *web_element):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((web_element)))
        element=self.find_element(*web_element)
        self.log.info("Finding web element to click....{}".format(web_element))
        self.driver.execute_script("arguments[0].click();", element)
    # without finding element, perform click action
    # def enter_text(self, web_element, text):
    #     self.log.info("....{}".format(web_element))
    #     web_element.send_keys(text)
    def enter_text(self,text,*web_element):
        self.log.info("Finding web element to enter the text ....{}".format(web_element))
        self.find_element(*web_element).clear()
        self.find_element(*web_element).send_keys(text)
    def get_text(self, *web_element):
        self.log.info("Finding web element to get text ....{}".format(web_element))
        return self.find_element(*web_element).text
    def open(self, url):
        self.log.info("Open url ...{}".format(url))
        self.driver.get(url)
    def user_enter(self,*web_element,user):
        self.log.info("Enter username ....{}".format(user))
