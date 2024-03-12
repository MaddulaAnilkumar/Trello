import time
import pytest
import allure
from Pages.Trello_pages import Trello_Board
from utilities.action_utils import ActionUtils
from utilities.base_test import BaseTest
class Test_Login_Trello():
    def __int__(self,driver):
        self.driver=driver
    @pytest.fixture(scope="session" , autouse=True)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Login to Trello")
    @allure.step("Nagivate to URL")
    @allure.step("Enter Username")
    @allure.step("Click on Continue")
    @allure.step("Enter Password")
    @allure.step("Click on Login")
    def test_login(self, oneTimeSetup):
        trello = Trello_Board(self.driver)
        action = ActionUtils(self.driver)
        credentials = BaseTest()
        action.open(credentials.get_env_value('url'))
        time.sleep(10)
        name = credentials.get_env_var_username()
        print("Name:",name)
        trello.enter_user_name(credentials.get_env_var_username())
        trello.click_on_continue()
        # action.wait_for_element((Trello_Board.password))
        time.sleep(5)
        trello.enter_password(credentials.get_env_var_pwd())
        trello.click_login()
if __name__  ==  '__main__':
    print("This class holdes the login Method")