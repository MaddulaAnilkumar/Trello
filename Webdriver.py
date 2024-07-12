from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location("C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\chromedriver.exe")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-javascript")
# chrome_options.add_argument("user-agent=" + user_agent)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
class WebDriverFactory():
    def __init__(self,browser):
        self.browser = browser
    def get_browser_instance(self):
        if self.browser == "FF":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        elif self.browser == "Chrome":
            driver = webdriver.Chrome(options=chrome_options)

        elif self.browser == "Edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        else:
            driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver