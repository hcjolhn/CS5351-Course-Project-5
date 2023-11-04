from selenium.webdriver.common.by import By
import time
from Features.Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestPage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.createbtn_xpath = "//a[@href='/form_input']"
        self.submitbtn_xpath = "//button[text()='Submit']"
        self.name_xpath = "//input[@name='name']"
        self.email_xpath = "//input[@name='email']"
        self.message_xpath = "//textarea[@name='message']"

    def createbtn_click(self):
        Createbtn = self.driver.find_element(By.XPATH, self.createbtn_xpath)
        Createbtn.click()
        time.sleep(3)

    def submitbtn_click(self):
        Submitbtn = self.driver.find_element(By.XPATH, self.submitbtn_xpath)
        Submitbtn.click()
        time.sleep(3)

    def input(self, input, field):
        match field:
            case "name":
                Input = self.driver.find_element(By.XPATH, self.name_xpath)
            case "email":
                Input = self.driver.find_element(By.XPATH, self.email_xpath)
            case "message":
                Input = self.driver.find_element(By.XPATH, self.message_xpath)
        Input.send_keys(input)
        time.sleep(3)
    
    def inputValidation(self,field):
        # do onblur to trigger error message
        self.driver.find_element(By.CSS_SELECTOR,".input-fields-container").click()
        ele = self.driver.find_element(By.CSS_SELECTOR,"input[name='%s'] + .input-validate-error" % field)
        print(ele.text)
        assert(ele.text == "Please input correct "+field)
        time.sleep(3)
