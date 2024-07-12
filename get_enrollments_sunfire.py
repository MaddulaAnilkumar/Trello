import requests
from requests.auth import HTTPBasicAuth
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from datetime import datetime
import time
from fetch_amendments import amdetails
class SunfireProcessor:
    def __init__(self):
        self.wait_time = 10
        self.options = Options()
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36")
        self.driver = None
    def login_to_sunfire(self, username, password):
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.sunfirematrix.com/app/agent/yourmedicare")
        print("Started processing SunfireLogin page ...")
        WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_element_located((By.NAME, 'username')))
        self.driver.implicitly_wait(15)
        user_box = self.driver.find_element(By.NAME, 'username')
        user_box.send_keys(username)
        pass_box = self.driver.find_element(By.NAME, 'password')
        pass_box.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//button[@class='auth0-lock-submit']")
        login_button.click()
        print("Login page processing")
    def process_search_page(self, first_name, last_name, mem_dob):
        if self.driver is None:
            print("Driver not initialized. Please call login_to_sunfire method first.")
            return
        wait_time = 10
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.LINK_TEXT, "Search contacts")))
        self.driver.implicitly_wait(15)
        searchcontact_field = self.driver.find_element(By.LINK_TEXT, value="Search contacts")
        searchcontact_field.click()
        print("Search Contact Page processing")
        F_Name = self.driver.find_element(By.NAME, "firstName")
        F_Name.send_keys(first_name)
        L_Name = self.driver.find_element(By.NAME, "lastName")
        L_Name.send_keys(last_name)
        Dob_M = self.driver.find_element(By.NAME, "dobmm")
        Dob_M.send_keys(mem_dob.split('/')[0])
        Dob_D = self.driver.find_element(By.NAME, "dobdd")
        Dob_D.send_keys(mem_dob.split('/')[1])
        Dob_Y = self.driver.find_element(By.NAME, "dobyy")
        Dob_Y.send_keys(mem_dob.split('/')[2])
        disposition_button = self.driver.find_element(By.XPATH, "//*[@id='contact-search-disposition-wrapper']/div/div/button")
        disposition_button.click()
        time.sleep(7)
        enrolled_option = self.driver.find_element(By.XPATH, "//*[@id='14']")
        enrolled_option.click()
        time.sleep(5)
        search_button = self.driver.find_element(By.XPATH,
                                                    "//button[text()='Search']")
        search_button.click()
        time.sleep(5)
        # Search results
        result_blocks = self.driver.find_elements(By.XPATH, "//*[@id='app']/div/div/main/div/div/div/div/div[2]")
        table_responsive = result_blocks[0].find_element(By.XPATH, "//div[contains(@class, 'table-responsive')]")
        buttons = table_responsive.find_elements(By.XPATH, "//tr[contains(@class, 'customer-table-row')]/td/button")
        # Process each customer block
        if buttons:
            for button in buttons:
                     print("started into loop ******")
                     try:
                    # Find the button within each result block using the XPath relative to the block
                         button.click()
                         time.sleep(10)
                         view_enrollment_button_xpath = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/ul/li[5]/a")
                         view_enrollment_button_xpath.click()
                         time.sleep(5)
                         Pdf_blocks = self.driver.find_elements(By.XPATH, "//*[@id='app']/div/div/main/div/div/div/div[5]")
                        # Get the current year
                         current_year = datetime.now().year
                        # Get the last day of the current year
                         last_date_of_year = datetime(current_year, 12, 31).date()
                         future_date_element = self.driver.find_element(By.XPATH, "//label[text()='Proposed effective date']/following-sibling::p").text
                         print("future_date:",future_date_element)
                         date_object = datetime.strptime(future_date_element, "%d/%m/%Y")
                         date_eff = date_object.date()
                         print(date_eff)
                         print(date_eff, last_date_of_year)
                         if date_eff> last_date_of_year:
                            save_as_pdf_button = self.driver.find_element(By.XPATH,"//span[text()='Save as PDF']")
                            if save_as_pdf_button is not None:
                                save_as_pdf_button.click()
                                print("save_as_pdf found")
                            else:
                                print("Save as PDF button not found. Check the element's XPath or the page structure.")
                            save_as_pdf_button.click()
                            print("future proposed date met Specified Condition and Enrolment file downloded for",first_name,last_name)
                         else:
                            print("The Proposed date condition doesn't satisfy")
                         time.sleep(5)
                     except Exception as e:
                          print("Results/Button not found in the result block:", e)
        else :
                        print('Results Not found for',first_name,last_name)
    def close_driver(self):
        if self.driver is not None:
            self.driver.quit()
