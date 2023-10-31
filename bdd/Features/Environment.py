import json
import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

from seleniumwire import webdriver


from Pages.BasePage import BasePage
from Pages.TestPage import TestPage
from selenium.webdriver.chrome.options import Options
data = json.load(open("Resources/config.json"))


def before_scenario(context, scenario):
    for tags in scenario.tags:
        (tag, browserVersion) = tags.split('_')
    print(browserVersion)
    match browserVersion:
        case "Chrome":
            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument('--disable-web-security')

            context.driver = webdriver.Chrome(options=chrome_options)
        case "FireFox":
            context.driver = webdriver.Firefox()
        case "Edge":
            context.driver = webdriver.Edge()
        case "IE":
            context.driver = webdriver.Ie()
    time.sleep(5)
    basepage = BasePage(context.driver)
    context.testpage = TestPage(basepage)

    context.stepid = 1
    if "api" not in tag:
        context.driver.get(data['WEBURL'])
        context.driver.maximize_window()
        context.driver.implicitly_wait(3)
    else:
        context.driver.get(data['APIURL'])
        context.driver.maximize_window()
        context.driver.implicitly_wait(3)

def after_step(context, step):
    print("hi")
    attach(context.driver.get_screenshot_as_png(), name=context.stepid, attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1


def after_scenario(context, scenario):
    print("After scenario", scenario)
    print(context.table)
    context.driver.close()
