from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
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