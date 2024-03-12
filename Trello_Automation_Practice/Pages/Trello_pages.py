from selenium.webdriver.common.by import By
from utilities.action_utils import ActionUtils
class Trello_Board(ActionUtils):
    #### Login Web Eleemnts   ###
    list_name=None
    username = (By.ID, "user")
    continue_button = (By.ID,"login")
    password = (By.XPATH, "//input[@placeholder='Enter password']")
    login = (By.ID, "login-submit")
    ##### Board Web Elements ###
    create_board_button=(By.XPATH,"//button[text()='Create your first board']")
    board = (By.XPATH, "//a[@data-testid='home-team-boards-tab']")
    board_page=(By.XPATH,"//h2[text()='Trello Workspace']")
    existing_board_page = (By.XPATH, "//h2[text()='Most popular templates']")
    add_board = (By.CSS_SELECTOR, "div.board-tile.mod-add")
    add_board_page = (By.XPATH, "//h2[@title='Create board']")
    board_title = (By.XPATH, "//input[@data-testid='create-board-title-input']")
    create_board = (By.XPATH, "//button[text()='Create']")
    name_board_page = (By.CSS_SELECTOR, "[data-testid='board-name-display']")
    ### List Related Web Elements ###
    title_name = (By.NAME, "Enter list title…")
    add_list = (By.XPATH, "//button[text()='Add list']")
    added_list_in_board=(By.XPATH,"//h2[@data-testid='list-name']")
    add_cart_to_list=(By.XPATH,"//h2[@data-testid='list-name']")
    card_and_selected_list=(By.XPATH,"//h2[@data-testid='list-name']/parent::div/parent::div/parent::div//button[@data-testid='list-add-card-button']")
    create_list = (By.XPATH, "//textarea[@placeholder='Enter a title for this card…']")
    create_list_another_button=(By.XPATH,"//button[@data-testid='list-composer-button']")
    add_card = (By.XPATH, "//button[text()='Add card']")
    created_board = "//h2[text()='Your boards ']/parent::div/parent::div//a"
    number_of_lists = (By.XPATH, "//ol[@id='board']//li[@data-list-id]")

    def __int__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def enter_user_name(self,text):
        return self.enter_text(text,*Trello_Board.username)
    def click_on_continue(self):
        return self.click_element(*Trello_Board.continue_button)
    def enter_password(self,text):
        return self.enter_text(text,*Trello_Board.password)
    def click_login(self):
        return self.click_element(*Trello_Board.login)
    def click_on_board(self):
        return self.click_element(*Trello_Board.board)
    def verify_existing_boards(self):
        return self.find_element(*Trello_Board.existing_board_page)
    def click_new_board_button(self):
        return self.click_element(*Trello_Board.create_board_button)
    def verify_board_page(self):
        return self.find_element(*Trello_Board.board_page)
    def add_new_board(self):
        return self.find_element(*Trello_Board.add_board)
    def verify_new_board_page(self):
        return self.find_element(*Trello_Board.add_board_page)
    def verify_board_title(self):
        return self.get_text(*Trello_Board.board_title)
    def enter_board_title(self,text):
        return self.enter_text(text,*Trello_Board.board_title)
    def click_on_board_create(self):
        return self.click_element(*Trello_Board.create_board)
    def verify_board_name(self):
        return self.get_text(*Trello_Board.name_board_page)
    def enter_list_title(self,text):
        return self.enter_text(text,*Trello_Board.title_name)
    def click_Add_list(self):
        return self.click_element(*Trello_Board.add_list)
    def verify_lists_in_board(self):
        return self.Find_Elements(*Trello_Board.added_list_in_board)
    def enter_title_of_card(self,text):
        return self.enter_text(text,*Trello_Board.create_list)
    def create_add_list_another(self):
        return self.click_element(*Trello_Board.create_list_another_button)
    def lists_in_board(self):
        return self.Find_Elements(*Trello_Board.add_cart_to_list)
    def click_on_created_board(self):
        return self.Find_Elements(*Trello_Board.created_board)
    def add_card_to_list_by_name(self, list_name):
        element = f"//h2[contains(text(),'{list_name}')]/parent::div/parent::div/parent::div//button[@data-testid='list-add-card-button']"
        return (By.XPATH, element)
    def verify_added_cards(self,list_name):
        added_cards_lists = (By.XPATH,
                             f"//textarea[contains(text(),'{list_name}')]/parent::div/parent::div/parent::div[@data-testid='list']//li")
        return (By.XPATH,added_cards_lists)

    def click_on_card(self):
        return self.click_element(*Trello_Board.add_card)
    def verify_number_of_lists(self):
        return self.Find_Elements(*Trello_Board.number_of_lists)
    def verfiy_cards_in_each_list(self,list_name):
        cards_in_lists = (f"//h2[contains(text(),'{list_name}')]/parent::div/parent::div/parent::div//li")
        return (By.XPATH, cards_in_lists)
###### Label Related web elements #####
    label_page = (By.XPATH, "//h2[@title='Labels']")
    search_label = (By.XPATH, "//input[@placeholder='Search labels…']")
    label=(By.XPATH,"//a[@title='Labels']")
    create_label=(By.XPATH,"//button[text()='Create a new label']")
    search_labels_list=(By.XPATH,"//span[@data-testid='card-label']")
    create_new=(By.XPATH,"//button[text()='Create']")
    verify_label_field=(By.XPATH,"//h3[text()='Labels']")
    added_label=(By.XPATH,"//h3[text()='Labels']/parent::div//span")
    label_title=(By.XPATH,"//p[text()='Title']/parent::div//input")
    verify_create_label=(By.XPATH,"//h2[@title='Create label']")
    color=(By.XPATH,"(//p[text()='Select a color']/parent::div//button)[1]")
    close_popup=(By.XPATH,"//button[@aria-label='Close popover']")
    close_card=(By.XPATH,"//a[@aria-label='Close dialog']")
    def click_on_label(self):
        return self.click_element(*Trello_Board.label)
    def verify_label_page(self):
        return self.find_element(*Trello_Board.label_page)
    def enter_label_name(self,text):
        return self.enter_text(text,*Trello_Board.search_label)
    def list_of_labels(self):
        return self.Find_Elements(*Trello_Board.search_labels_list)
    def create_new_label(self):
        return self.click_element(*Trello_Board.create_new)
    def verify_new_create_label(self):
        return self.find_element(*Trello_Board.verify_create_label)
    def enter_label_title(self,text):
        return self.enter_text(text,*Trello_Board.label_title)
    def remove_color(self):
        return self.click_element(*Trello_Board.color)
    def click_close_popup(self):
        return self.click_element(*Trello_Board.close_popup)
    def click_close_card(self):
        return self.click_element(*Trello_Board.close_card)
if __name__  ==  '__main__':
    print("This class holdes the Web Elements")




