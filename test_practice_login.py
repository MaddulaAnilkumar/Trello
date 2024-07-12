from selenium import webdriver
chrome_driver_path = "C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\chromedriver-win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("www.gmail.com")
driver.quit()