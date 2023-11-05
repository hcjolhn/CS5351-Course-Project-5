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

        self.INDEX = 3 # used for find the first 3 columns 
        self.EDIT_BTN_INDEX = 3 # used for find the edit button
        self.DEL_BTN_INDEX = 4 # used for find the delete button

        self.editbtn_xpath = f"//a[@href='/form_input/']"
        self.backbtn_xpath = "//a[@href='/']"
        self.table_xpath = "//table"

    def createbtn_click(self):
        Createbtn = self.driver.find_element(By.XPATH, self.createbtn_xpath)
        Createbtn.click()
        time.sleep(3)

    def submitbtn_click(self):
        Submitbtn = self.driver.find_element(By.XPATH, self.submitbtn_xpath)
        Submitbtn.click()
        time.sleep(3)

    def editbtn_click(self, order):
        try:
            table = self.driver.find_element(By.XPATH, self.table_xpath)
        except:
            assert False, "Table not found. editbtn_click failed."

        rows = table.find_elements(By.TAG_NAME, "tr")
        
        if len(rows) > 1:
            try:
                row = rows[int(order)]
            except:
                assert False, f"The {order}-th row not found. editbtn_click failed."
            cells = row.find_elements(By.TAG_NAME, "td")
            Editbtn = cells[self.EDIT_BTN_INDEX]
            Editbtn.click()
            time.sleep(3)
        else:
            assert False, f"Empty Table. editbtn_click failed."

    def delbtn_click(self, order):
        try:
            table = self.driver.find_element(By.XPATH, self.table_xpath)
        except:
            assert False, "Table not found. delbtn_click failed."

        rows = table.find_elements(By.TAG_NAME, "tr")
        original_len = len(rows)
        print(f"original_len: {original_len}")

        if len(rows) > 1:
            try:
                row = rows[int(order)]
            except:
                assert False, f"The {order}-th row not found. delbtn_click failed."
            cells = row.find_elements(By.TAG_NAME, "td")
            Delbtn = cells[self.DEL_BTN_INDEX]
            Delbtn.click()
            time.sleep(3)
            new_table = self.driver.find_element(By.XPATH, self.table_xpath)
            new_rows = new_table.find_elements(By.TAG_NAME, "tr")
            print(f"new_rows: {len(new_rows)}")
            if len(new_rows) + 1 == original_len:
                pass
            else:
                assert False, f"The {order}-th row have not deleted. delbtn_click failed."
        else:
            assert False, f"Empty Table. delbtn_click failed."

    def backbtn_click(self):
        Backbtn = self.driver.find_element(By.XPATH, self.backbtn_xpath)
        print("clicked on back btn")
        Backbtn.click()
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

    def clear(self, field):
        match field:
            case "name":
                Input = self.driver.find_element(By.XPATH, self.name_xpath)
            case "email":
                Input = self.driver.find_element(By.XPATH, self.email_xpath)
            case "message":
                Input = self.driver.find_element(By.XPATH, self.message_xpath)
        # Input.clear() # THIS IS NOT OKAY
        Input.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        Input.send_keys(Keys.DELETE)
        time.sleep(3)

    def check_edit_input(self, order, name, email, message):
        try:
            table = self.driver.find_element(By.XPATH, self.table_xpath)
        except:
            assert False, "Table not found. check_edit_input failed."

        rows = table.find_elements(By.TAG_NAME, "tr")
        
        if len(rows) > 1:
            try:
                row = rows[int(order)]
            except:
                assert False, f"The {order}-th row not found. check_edit_input failed."
            cells = row.find_elements(By.TAG_NAME, "td")[:self.INDEX]
            texts = [x.text for x in cells]
            if [name, email, message] == texts:
                pass
            else:
                assert False, "The new data do not match the input. check_edit_input failed."
        else:
            assert False, "There is no data in the table. check_edit_input failed."

    def check_new_input(self, name, email, message):
        try:
            table = self.driver.find_element(By.XPATH, self.table_xpath)
        except:
            assert False, "Table not found. check_new_input failed."

        rows = table.find_elements(By.TAG_NAME, "tr")
        
        if len(rows) > 1:
            new_row = rows[-1]
            cells = new_row.find_elements(By.TAG_NAME, "td")[:self.INDEX]
            texts = [x.text for x in cells]
            if [name, email, message] == texts:
                pass
            else:
                assert False, "The new data do not match the input. check_new_input failed."
        else:
            assert False, "There is no data in the table. check_new_input failed."

    def wait(self):
        time.sleep(3)
