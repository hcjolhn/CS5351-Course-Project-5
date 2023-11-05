from selenium.webdriver.common.by import By
import time
from Features.Pages.BasePage import BasePage


class NetworkTrafficValidatePage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context

    def me(self):
        print("hihi")