import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from utilities import logger_utils

class ActionUtils():

    log = logger_utils.get_logger()
    path="../test_data/Keen_Testdata.xlsx"

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
    def add_list(self,number):
        list = []
        list.append(number)
        return list
    def convert_string(self,result):
        output_SF = []
        for i in result:
            if i.isalnum():
                output_SF.append(i)
        validation = "".join(output_SF)
        return validation
    def record_verification(self,row_number,sheet_name,column_name):
        workbook = openpyxl.load_workbook(self.path)
        sheet = workbook[sheet_name]
        # Find the column index based on the column name
        column_index = None
        for row in sheet.iter_rows(min_row=2, max_row=2):
            for cell in row:
                if cell.value == column_name:
                    column_index = cell.column_letter
                    break
            if column_index is not None:
                break

        if column_index is None:
            print(f"Column '{column_name}' not found in the sheet.")
        else:
            # Get the value from the specified row and column
            cell = sheet[column_index + str(row_number)]
            cell_value = cell.value
            print(f"Value in row {row_number}, column '{column_name}': {cell_value}")
            return cell_value
    def test_identify_yes(self,least_row,last_row,column_code):
        workbook = openpyxl.load_workbook('your_file.xlsx')

        # Select the specific worksheet
        worksheet = workbook['Sheet1']

        # Find the row where the cell in the Status column contains "YES"
        for row in worksheet.iter_rows(min_row=least_row, max_row=last_row):  # Only check the 3rd row
            for cell in row:
                if cell.column_letter == column_code and cell.value == "YES":
                    # Get the value of the First_Name column in the same row (column A)
                    first_name = row[0].value
                    print("First Name:", first_name)
                    break
            else:
                continue
            break

    def validate_excel_data(file_path, row_number, field_column_map):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=row_number):  # Assuming the data starts from the second row
            for field, column in field_column_map.items():
                field_value = row[column - 1].value  # Adjusting column index to 0-based index
                if field_value != field:
                    print("Test failed for row:",
                          row[0].row)  # Assuming the first column contains unique identifiers for each row
                    return False

        print("All tests passed")
        return True
