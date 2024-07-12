from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from XLUtilities import Excel_data
import time
chrome_driver_path = "/chromedriver.exe"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
path="C:\\Users\\amaddula\\PycharmProjects\\Keen_Automation\\Keen_data (1).xlsx"
readdata_tasks=Excel_data(path, "Keen_leads")
write_data=Excel_data(path, "Keen_leads")
driver.get("https://www.sunfirematrix.com/app/agent/yourmedicare")
for data in range(6,64):
    First_Name=readdata_tasks.readdata(data, 1)
    Second_Name=readdata_tasks.readdata(data,2)
    Month=readdata_tasks.readdata(data, 3)
    Date=readdata_tasks.readdata(data, 4)
    Year=readdata_tasks.readdata(data, 5)
    advisor=readdata_tasks.readdata(data,6)
    Id=readdata_tasks.readdata(data, 7)
    Password=readdata_tasks.readdata(data, 8)
    time.sleep(4)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys(Id)
    time.sleep(4)
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(Password.strip())
    print("password:",Password)
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@type='submit']//span[text()='Login']").click()
    try:
        time.sleep(6)
        driver.find_element(By.XPATH,"//h3[text()='Quick links']/following::span[text()='Search contacts']").click()
    except Exception as ex:
        print("Search is not displayed because of same advisor",advisor)
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys(First_Name)
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys(Second_Name)
    time.sleep(1)
    #month
    driver.find_element(By.XPATH,"//input[@name='dobmm']").send_keys(Month)
    time.sleep(2)
    #data
    driver.find_element(By.XPATH,"//input[@name='dobdd']").send_keys(Date)
    time.sleep(2)
    ## year
    driver.find_element(By.XPATH,"//input[@name='dobyy']").send_keys(Year)
    time.sleep(2)
    driver.find_element(By.XPATH,"//label[text()='Disposition']/parent::div//button[@class='not-selected dropdown-toggle btn btn-tertiary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[text()='Enrolled']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[text()='Search']").click()
    time.sleep(3)
    try:
        time.sleep(6)
        driver.find_element(By.XPATH,"//button[@id='Popover1']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//li[@data-test='viewEnrollment']//a").click()
        time.sleep(2)
        plan=driver.find_element(By.XPATH,"//div[@class='enrollment-container block-container']//h2")
        plan_name=plan.text
        ### I
        print("Plane_name:",plan_name)
        write_data.write_result_in_to_excel_sheet(data, "Keen_leads", "I",plan_name)
        time.sleep(3)
        plan_date=driver.find_element(By.XPATH,"//div[@data-test='test-summary-effectiveDate']//p")
        plan_date_text=plan_date.text
        ### J
        print("Plane_date:",plan_date_text)
        write_data.write_result_in_to_excel_sheet(data, "Keen_leads", "J",plan_date_text)
    except Exception as ex:
        print("Enrollment is not found",Second_Name)
        write_data.write_result_in_to_excel_sheet(data, "Keen_leads", "I","NO_DATA")
        write_data.write_result_in_to_excel_sheet(data, "Keen_leads", "J","NO_DATA")
    driver.find_element(By.XPATH,"//a[@href='#']//span").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[@href='#/logout']").click()


        ### write to excel sheet












#         # self.log.info("***** Login in to Gmail to verify docusign *****")
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("anilkumar688@myyahoo.com")
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@name='signin']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Nani@1234")
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[@name='verifyPassword']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//li//a[@href='https://mail.yahoo.com/']").click()
# time.sleep(5)
# click_mail="//span[@title='Medicare Scope of Appointment: eSignature Request']"
# review_document=(//span[text()=' REVIEW DOCUMENT '])
# continu_buuton=(//button[text()='Continue'])
# date_signed=(//label[text()='DateSigned']/parent::div//span)





#####################################################################
# Keen_test_soa.test_docusing(row_soa_number)
        # # action_utils.wait_for_elements((Create_capture_member_details.Member))
        # # member=keen_Create.select_member()
        # # member[0].click()
        # # Keen_test_soa.test_createSOA_for_Member(row_soa_number)
        # self.driver.execute_script("window.open('', '_blank');")
        #
        # # Switch to the new tab/window
        # self.driver.switch_to.window(self.driver.window_handles[1])
        #
        # # Perform actions in the new tab/window (e.g., logging into email)
        # self.driver.get("https://www.yourmailservice.com")
        # self.driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
        #            'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
        #            '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        # self.driver.find_element(By.XPATH, "//input[@name='identifier']").send_keys("anilkumarmaddula05@gmail.com")
        # time.sleep(3)
        # next_button = self.driver.find_element(By.XPATH, "//div[@id='identifierNext']//button")
        # next_button.click()
        # print("hi")
        # self.driver.switch_to.window(self.driver.window_handles[0])

        # keen_generate = Test_GenerateQuote(self.driver)
         # kee_Create = Create_capture_member_details(self.driver)
         # action = ActionChains(self.driver)
         # keen_account = Keen_Account_creation(self.driver)
         # action_utils = ActionUtils(self.driver)
         # row_account = number.get_random_number("Account_Creation")
         # self.log.info("***** Verifying the Keen lead in Salesforce *****")
         # keen_generate.test_new_for_generate_quote(row_account)
         # action_utils.wait_for_elements((Create_capture_member_details.Member))
         # keen_member = kee_Create.select_member()
         # Existing_account = None
         # for member in keen_member:
         #     keen_member = member.get_attribute('title')
         #     print("existing members:", keen_member)
         #     if keen_member == 'Test Sean firstaugust':
         #         Existing_account = member
         #         print("Length of title:", len(keen_member))
         # if Existing_account is not None:
         #     Existing_account.click()
         #     self.log.info("***** Selected the Keen Member to initiate the generate Quote *****")
         #     self.log.info(("***** Generating the Quote for selected member *****"))
         #     keen_browser.test_examplegeneratequote_newaccount(row_account)
         # else:
         #     print("Account is not present")
         #     self.log.info("***** Keen Member is not exists in salesforce *****")
         #     keen_generate.test_new_for_generate_quote(row_account)
         #     keen_browser.test_examplegeneratequote_newaccount(row_account)
#################################################################################################