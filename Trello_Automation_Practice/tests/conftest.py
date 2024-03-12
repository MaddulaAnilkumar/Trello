import os
import shutil
import allure
import pytest
from allure_commons.types import AttachmentType
from utilities.Webdriver import WebDriverFactory
from utilities import logger_utils
from utilities.action_utils import ActionUtils
from utilities.base_test import BaseTest
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_argument("--disable-notifications")
# option.add_argument("--headless")
log = logger_utils.get_logger()
driver = None
@pytest.fixture(scope="session")
def actions_utils(request):
    request.action_utils = ActionUtils(driver)


def pytest_addoption(parser):
    parser.addoption('--browser',action='store', default='chrome', help='Browser to execute tests'
    )

@pytest.fixture(scope="session")
def oneTimeSetup(request,get_browser):
    # try:
        global driver
        print("This is one time setup")
        wdf = WebDriverFactory(get_browser)
        driver = wdf.get_browser_instance()
        session = request.node
        for item in session.items:
            cls = item.getparent(pytest.Class)
            setattr(cls.obj, "driver", driver)
    # except Exception as ex:
    #     print("Webdriver version is changed")

    # yield driver
    # driver.quit()

@pytest.fixture(scope="session")
def get_browser(request):
    return request.config.getoption('--browser')

@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    ###report.when == "setup"
    if (report.when == 'call') and (report.failed or report.skipped):
        try:
            allure.attach(driver.get_screenshot_as_png(), name='Screnshot', attachment_type=AttachmentType.PNG)
        except Exception as e:
            log.error('Fail to take screenshot: ' .format(e))
            # allure.attach(driver.get_screenshot_as_png(), name = 'method of test case', attachement_type = AttachmentType.PNG)


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    path = BaseTest.ROOT_PATH + '/allure-results'
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)
        with open(os.path.join(path, 'environment.properties'), 'w') as temp_file:
            # temp_file.write("Browser=" + os.environ['browser'] + '\n' + "Environment=" + os.environ['testenv'] + '\n' + "Url=" + os.environ['url'])
            temp_file.write(
                "Browser=" + os.environ.get('browser') + '\n' + "Environment=" + os.environ.get('testenv') + '\n' + "Url=" + os.environ.get('url'))
    except OSError as e:
        log.error("Error: %s - %s." % (e.filename, e.strerror))


