import os
import json
import openpyxl
from pathlib import Path
import pytest
from utilities import logger_utils
from utilities.XLUtilities import Excel_data
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
@pytest.mark.usefixtures("oneTimeSetup", "actions_utils")
class BaseTest:
    path = "../test_data/Keen_Testdata.xlsx"
    workbook = openpyxl.load_workbook(path)
    ROOT_PATH = str(Path(__file__).parent.parent)
    # CONSTANTS_PATH = ROOT_PATH+"/constants.json"
    # CONSTANTS = None
    log = logger_utils.get_logger()
    def get_env_var_username(self):
        self.log.info('Fetching environment variables')
        user = os.environ['user']
        return user
    def get_env_var_url(self):
        self.log.info("Fetching url from environment variables")
        url = os.environ['url']
        return url
    def get_env_var_pwd(self):
        self.log.info('Fetching environment variables')
        pwd = os.environ['password']
        return pwd
    def get_env_value(self, param):
        self.log.info('Fetching environment variable '+ param)
        return os.environ.get(param)
    def get_data(self):
        self.log.info('Loading data from JSON file')
        config_file = open(self.CONSTANTS_PATH)
        self.CONSTANTS = json.load(config_file)
        return self.CONSTANTS
    def get_random_number(self,sheet_name):
        readdata_account = Excel_data(self.path, sheet_name)
        rows = readdata_account.rowcount()
        number = random.randint(3, rows)
        return number
    def convert_Fulldate_to_Month(self,date):
        date_str = date
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        month_name = date_obj.strftime('%b')
        return month_name

    def extract_month_and_year(self,date):
        date_obj = datetime.strptime(date, "%b %d, %Y")
        month = date_obj.strftime('%b')
        year = date_obj.year
        return month, year

    def convert_Full_date_to_year(self,year):
        date_string = year
        date_obj = datetime.strptime(date_string, "%m/%d/%Y")
        year = date_obj.strftime("%Y")
        return year
    def calculate_age(self,birthdate):
        current_date = datetime.now().date()
        birthdate_obj = datetime.strptime(birthdate, "%m/%d/%Y").date()
        age = relativedelta(current_date, birthdate_obj)
        age_str = f"{age.years} years {age.months} months {age.days} days"
        return age_str
    def convert_date(self,date_value):
        parsed_date = datetime.strptime(date_value, "%m/%d/%Y")
        expected_date_format = parsed_date.strftime("%b %d, %Y")
        return expected_date_format
    def write_result_in_to_excel_sheet(self,row_account,sheet_name,column_code):
        sheet = self.workbook[sheet_name]
        random_row = row_account
        column = column_code
        cell_reference = f"{column}{random_row}"
        sheet[cell_reference] = 'YES'
        self.workbook.save(self.path)
    def retrieve_value(self, row_number, column_name, sheet_name,column_index):
        sheet_parent = self.workbook[sheet_name]
        print("Row number:", row_number)
        data_row = sheet_parent[row_number]
        for cell in data_row:
            if cell.column_letter == column_name and cell.value == "YES":
                Name = data_row[column_index].value
                return Name
    def get_sheet_name(self,sheet_name):
        workbook = openpyxl.load_workbook(self.path)
        sheet=workbook[sheet_name]
        return sheet

    def retrieve_row_number(self,sheet_name, name, column_letter):
        sheet = self.workbook[sheet_name]
        column = sheet[column_letter]
        for row, cell in enumerate(column, start=1):
            if cell.value == name:
                print(f"The parent organization '{name}' is found at row {row}.")
                return row
        else:
            print(f"The parent organization '{name}' is not found in the Excel sheet.")

    def convert_date_to_string(self,date):
        numbers_mapping = {0: 'zero',
                           1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
                           7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth",
                           13: "thirteenth", 14: "fourteenth", 15: "fifteenth", 16: "sixteenth", 17: "seventeenth",
                           18: "eighteenth", 19: "nineteenth", 20: "twentieth", 21: "twentyfirst", 22: "twentysecond",
                           23: "twenty-third", 24: "twentyfourth", 25: "twentyfifth", 26: "twentysixth",27: "twentyseventh",
                           28: "twentyeighth", 29: "twentyninth", 30: "thirtieth", 31: "thirtyfirst",
                           20: "twenty", 21: "twentyfirst", 22: "twentysecond", 23: "twentythird", 24: "twentyfourth",
                           25: "twentyfifth", 26: "twentysixth", 27: "twentyseventh", 28: "twentyeighth",
                           29: "twentyninth", 30: "thirtieth", 31: "thirtyfirst"
                           }

        month_mapping = {
            1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
            7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"
        }
        day = numbers_mapping[date.day]
        month = month_mapping[date.month]
        result = day + month
        return result
