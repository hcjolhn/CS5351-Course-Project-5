import json
import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
from Pages.BasePage import BasePage
from Pages.TestPage import TestPage

data = json.load(open("Resources/config.json"))

def before_scenario(context, scenario):

    for tags in scenario.tags:
        (tag, browserVersion) = tags.split('_')
    print(browserVersion)
    match browserVersion:
        case "Chrome":
            context.driver = webdriver.Chrome()
        case "FireFox":
            context.driver = webdriver.Firefox()
        case "Edge":
            context.driver = webdriver.Edge()
        case "IE":
            context.driver = webdriver.Ie()
    time.sleep(5)
    basepage = BasePage(context.driver)
    context.testpage = TestPage(basepage)
