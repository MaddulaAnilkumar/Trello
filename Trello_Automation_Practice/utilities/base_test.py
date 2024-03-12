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
    ROOT_PATH = str(Path(__file__).parent.parent)
    CONSTANTS_PATH = ROOT_PATH+"/constants.json"
    CONSTANTS = None
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
    def get_secs(self):
        from datetime import datetime
        current_time = datetime.now()
        current_seconds = current_time.second
        print("Current seconds:", current_seconds)
        return current_seconds

    def seconds_to_text(self,seconds):
        seconds_mapping = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
            20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty"
        }
        if seconds in seconds_mapping:
            print("Text of sec:",seconds_mapping[seconds])
            return seconds_mapping[seconds]
        tens = seconds // 10 * 10
        units = seconds % 10
        if tens > 0:
            if units > 0:
                return f"{seconds_mapping[tens]}-{seconds_mapping[units]}"
            else:
                return seconds_mapping[tens]
        else:
            return seconds_mapping[units]

