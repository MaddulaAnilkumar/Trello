import allure
from tests.test_login_to_trello import Test_Login_Trello
from tests.test_trello_board import Test_Trello_board
from utilities import logger_utils
class Test_suite_trello(Test_Login_Trello):
    log =logger_utils.get_logger()
    @allure.description("Test Suite")
    def test_run_script(self):
        board = Test_Trello_board(self.driver)
        self.log.info(".....User Logged into Trello.....")
        board.create_board()
        self.log.info(".....Board is Created abd Verified .....")
        board.create_lists_and_cards_in_board()
        self.log.info("..... Lists and Cards are Created and Verified ")
        board.test_drag_and_drop_add_label()
        self.log.info("..... Drag and Drop ,Add Label to Card is  completed and Verified .....")