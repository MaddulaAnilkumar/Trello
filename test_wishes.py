import allure
import pytest
from tests.test_ALogin import Test_login
from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
import time
from Pages.Keen_Wishes_Message import Wishes_Message
from utilities import logger_utils

@allure.description("Birtday and Anniversary Messages")
class Test_messages(Test_login):

    def test_wishes_messages(self):
        keen = Wishes_Message(self.driver)
        keen_create=Create_capture_member_details(self.driver)
        log = logger_utils.get_logger()
        keen_create.select_member()
        log.info("*****Wishes message****")
        time.sleep(10)
        self.driver.execute_script("scroll(0,700);")
        keen.click_on_edit().click()
        time.sleep(10)
        keen.enter_Birthday_wishes("Birthday Wishes")
        time.sleep(15)
        keen.enter_Anniversary_Message("Anniversary Wishes")
        keen.save_messages().click()
        log.info("*****Messages are saved*****")
        list_of_validations = keen.validation_of_wishes()
        for i in list_of_validations:
            if i.text == "Birthday Wishes":
                print("Test Pass")
            else:
                print("Test fail")
                break
        for i in list_of_validations:
            if i.text == "Anniversary Wishes":
                print("Test Pass")
            else:
                print("Test fail")
                break
