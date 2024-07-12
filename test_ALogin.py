import time
from selenium.webdriver import ActionChains
import pytest
import allure
from Pages.Keen_Login import Keen_login
from utilities.action_utils import ActionUtils
from utilities import logger_utils
from utilities.base_test import BaseTest
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Login to SFDC")
@allure.description("Adivsor login to SFDC with valid credentials")
class Test_login():
    def __int__(self,driver):
        self.driver=driver
    @pytest.fixture(scope="session" , autouse=True)
    @pytest.mark.order(1)
    def test_login(self, oneTimeSetup):
        log = logger_utils.get_logger()
        keen = Keen_login(self.driver)
        action = ActionUtils(self.driver)
        action_move = ActionChains(self.driver)
        log.info("***** Login started *****")
        credentials = BaseTest()
        action.open(credentials.get_env_value('url'))
        keen.enter_email(credentials.get_env_var_username())
        print("url:",credentials.get_env_var_url())
        action.wait_for_element((Keen_login.password))
        keen.enter_password(credentials.get_env_var_pwd())
        keen.login_to_sandbox()
        log.info("***** User logged to SFDC *****")
        try:
            action.wait_for_element((Keen_login.app))
            Select_App=keen.Verify_App()
            if Select_App.text != "Keen App Beta":
                keen.options()
                keen.search_App("Keen App Beta")
                choose_app=keen.select_app()
                for app in choose_app:
                    if app .text == "Keen App Beta":
                        action_move.move_to_element(app).click().perform()
                time.sleep(10)
                keen.keen_leads_members()
            else:
                time.sleep(10)
                keen.keen_leads_members()
                log.info("***** Keen Leads and Members Tab is displayed *****")
        except Exception as ex:
            log.info("First time user is not logged")
            action.open(credentials.get_env_value('url'))
            keen.enter_email(credentials.get_env_var_username())
            action.wait_for_element((Keen_login.password))
            keen.enter_password(credentials.get_env_var_pwd())
            keen.login_to_sandbox()
            action.wait_for_element((Keen_login.app))
            Select_App = keen.Verify_App()
            if Select_App.text != "Keen App Beta":
                keen.options()
                keen.search_App("Keen App Beta")
                choose_app = keen.select_app()
                for app in choose_app:
                    if app.text == "Keen App Beta":
                        action_move.move_to_element(app).click().perform()
                time.sleep(10)
                keen.keen_leads_members()
            else:
                time.sleep(10)
                keen.keen_leads_members()
                log.info("***** Keen Leads and Members Tab is displayed *****")





