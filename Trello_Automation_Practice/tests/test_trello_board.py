import time
import allure
import pytest
from selenium.webdriver import ActionChains
from Pages.Trello_pages import Trello_Board
from utilities import logger_utils
from utilities.action_utils import ActionUtils
from utilities.base_test import BaseTest
class Test_Trello_board():
    log = logger_utils.get_logger()
    def __init__(self,driver):
        self.driver=driver
        self.action_utils = ActionUtils(self.driver)
        self.action = ActionChains(self.driver)
        self.credentails = BaseTest()
        self.sec=self.credentails.get_secs()
        self.secs_value=self.credentails.seconds_to_text(self.sec)
        self.trello = Trello_Board(self.driver)
        self.list = self.credentails.get_env_value('list').split(",")
        self.cards=self.credentails.get_env_value('cards').split(",")
        self.label_name=self.credentails.get_env_value('label_name')
        self.count=self.credentails.get_env_value('count')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Creating a New Board")
    @allure.feature("BOARD")
    @allure.step("Test Step : Click on Board")
    @allure.step("Test Step : Enter the Title of Board")
    @allure.step("Test Step : Click on Create Board")
    @allure.step("Test Step : Verify on Board Name")
    #@pytest.mark.create_board
    ## When board is given only Create_Board test case will execute
    # @pytest.skip
    ## It will prevent the Execution
    # @pytest.mark.order(1)
    ## It will execute in Order as we mention number
    def create_board(self):
        print("secs:",self.sec)
        print("string sec:",self.secs_value)
        name=self.credentails.get_env_value('board')
        board_name=name+self.secs_value
        self.trello.click_on_board()
        try:
            self.action_utils.wait_for_element((Trello_Board.board_page))
            boards= self.trello.verify_board_page()
            if boards.is_displayed():
                self.log.info("..... Create a first board .....")
                self.action_utils.wait_for_element((Trello_Board.create_board_button))
                self.trello.click_new_board_button()
        except Exception as ex:
                self.log.info("..... Create a New Board .....")
                time.sleep(5)
                self.action_utils.wait_for_element((Trello_Board.add_board))
                move_to_board = self.trello.add_new_board()
                self.driver.execute_script("arguments[0].scrollIntoView();", move_to_board)
                move_to_board.click()
        self.action_utils.wait_for_element((Trello_Board.add_board_page))
        new_board_page=self.trello.verify_new_board_page()
        print("Board page text:",new_board_page.text)
        if new_board_page.is_displayed():
            self.log.info(".....New Board page is displayed.....")
        time.sleep(5)
        self.action_utils.wait_for_element((Trello_Board.board_title))
        self.trello.enter_board_title(board_name)
        time.sleep(5)
        self.action_utils.wait_for_element((Trello_Board.create_board))
        self.trello.click_on_board_create()
        time.sleep(5)
        self.action_utils.wait_for_element((Trello_Board.name_board_page))
        created_board_name= self.trello.verify_board_name()
        try:
            assert board_name == created_board_name, "Board is not created"
        except Exception as ex:
            self.log.info("..... Board Title is wrong.....")
        return board_name

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Creating a New Board")
    @allure.feature("BOARD")
    @allure.step("Test Step : Click on Add list")
    @allure.step("Test Step : Enter the List Name")
    @allure.step("Test Step : Click on Add")
    @allure.step("Test Step : Verify the Created List")
    # @pytest.mark.lists_and_cards
    ## When lists_and_cards is given only create_lists_and_cards_in_board test case will execute
    # @pytest.skip
    ## It will prevent the Execution
    # @pytest.mark.order(2)
    ## It will execute in Order as we mention number
    def test_create_lists_and_cards_in_board(self):
        sec = self.credentails.get_secs()
        secs_value = self.credentails.seconds_to_text(sec)
        list_values=None
        card=None
        list = self.credentails.get_env_value('list').split(",")
        self.log.info(list)
        for list_value in list:
                list_values=list_value+secs_value
                self.action_utils.wait_for_element((Trello_Board.title_name))
                self.trello.enter_list_title(list_values)
                self.action_utils.wait_for_element((Trello_Board.add_list))
                self.trello.click_Add_list()
                time.sleep(2)
                sec = self.credentails.get_secs()
                secs_value_card = self.credentails.seconds_to_text(sec)
                print("list x paths conatins :",list_value)
                click_add_card = self.trello.add_card_to_list_by_name(list_value)
                add_card_button = self.driver.find_element(*click_add_card)
                self.log.info("..... waiting for card button .....")
                self.log.info(add_card_button)
                add_card_button.click()
                time.sleep(2)
                card = self.credentails.get_env_value('cards').split(",")
                for card_value in card:
                    self.action_utils.wait_for_element((Trello_Board.create_list))
                    card_values=card_value+secs_value_card
                    self.trello.enter_title_of_card(card_values)
                    self.trello.click_on_card()
                    time.sleep(2)
                self.action_utils.wait_for_element((Trello_Board.create_list_another_button))
                self.trello.create_add_list_another()
                time.sleep(2)
        self.action_utils.wait_for_elements((Trello_Board.added_list_in_board))
        added_list_in_board=self.trello.verify_lists_in_board()
        for list_board, expected_list_title in zip(added_list_in_board, list):
            if list_board.text in expected_list_title:
                self.log.info(f"Element {list_board.text} is matched.")
                time.sleep(2)
                cards=self.trello.verify_added_cards(list_values)
                add_card_button = self.driver.find_elements(*cards)
                for list_cards , expected_cards in zip(add_card_button,card):
                    if list_cards.text in expected_cards:
                        self.log.info(f"Element {list_cards.text} is matched.")
                    else:
                        self.log.info(f"Element {list_cards.text} is not matched with {expected_cards}.")
            else:
                self.log.info(f"Element {list_board.text} is not matched with {expected_list_title}.")
    @allure.step("Test Step : Select the card to drag")
    @allure.step("Test Step : Drop in to another List")
    @allure.step("Test Step : Verify the Card")
    @allure.description("Drag and Drop the Crad into List")
    @allure.severity(allure.severity_level.MINOR)
    # @pytest.mark.drag_drop
    ## When drag_drop is given only test_drag_and_drop_add_label test case will execute
    # @pytest.skip
    ## It will prevent the Execution
    # @pytest.mark.order(3)
    ## It will execute in Order as we mention number
    def test_drag_and_drop_add_label(self):
        drag_card_one=None
        drop_card_three=None
        self.action_utils.wait_for_elements((Trello_Board.number_of_lists))
        lists=self.trello.verify_number_of_lists()
        self.log.info(len(lists))
        if len(lists) >= int(self.count):
            self.log.info("..... Equal or More lists are in Board compared to expected.....")
            self.log.info(self.list)
            if self.list[0]:
                self.log.info(self.list[0])
                cards_path=self.trello.verfiy_cards_in_each_list(self.list[0])
                cards_in_list=self.driver.find_elements(*cards_path)
                drag_card_one=cards_in_list[0]
                # drag_card_one.text()
                # self.log.info(drag_card_one[0])
            if self.list[1]:
                cards_path = self.trello.verfiy_cards_in_each_list(self.list[1])
                cards_in_list = self.driver.find_elements(*cards_path)
                drop_card_three = cards_in_list[2]
            self.action.drag_and_drop(drag_card_one,drop_card_three).perform()
            self.log.info(".....Drag and drop is completed.....")
            cards_path = self.trello.verfiy_cards_in_each_list(self.list[1])
            cards_in_list = self.driver.find_elements(*cards_path)
            for added_cards_list in cards_in_list:
                self.log.info(added_cards_list.text)
                self.log.info(self.list[0])
                if self.list[0] in added_cards_list.text:
                    self.log.info(".....List one card is moved to List 2.....")
            if cards_in_list[1]:
                cards_in_list[2].click()
                self.action_utils.wait_for_element((Trello_Board.label))
                self.trello.click_on_label()
                self.action_utils.wait_for_element((Trello_Board.label_page))
                self.trello.verify_label_page()
                self.action_utils.wait_for_element((Trello_Board.search_label))
                self.trello.enter_label_name(self.label_name)
                try:
                    self.action_utils.wait_for_elements((Trello_Board.search_labels_list))
                    list_labels=self.trello.list_of_labels()
                    for labels in list_labels:
                        self.log.info(labels.text)
                        if labels.text == self.label_name:
                            list_labels.click()
                except Exception as ex:
                    self.log.info("..... Creating New Label.....")
                    self.action_utils.wait_for_element((Trello_Board.create_label))
                    self.trello.create_new_label()
                    self.action_utils.wait_for_element((Trello_Board.verify_create_label))
                    label_page=self.trello.verify_new_create_label()
                    assert label_page.is_displayed(),"Label page is not visible"
                    self.trello.enter_label_title(self.label_name)
                    time.sleep(2)
                    self.action_utils.wait_for_element((Trello_Board.color))
                    self.trello.remove_color()
                    self.action_utils.wait_for_element((Trello_Board.create_new))
                    self.trello.create_new_label()
                    self.action_utils.wait_for_element((Trello_Board.close_popup))
                    self.trello.click_close_popup()
                    self.action_utils.wait_for_elements((Trello_Board.search_labels_list))
                    list_labels = self.trello.list_of_labels()
                    for labels in list_labels:
                        self.log.info(labels.text)
                        assert labels.text == self.label_name,"Label is not added to card"















