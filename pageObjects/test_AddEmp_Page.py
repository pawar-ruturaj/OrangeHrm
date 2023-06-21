import time

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as Ec


class Add_emp:
    Click_PIM_XPATH = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space("
                                 ")='PIM']")
    Click_Add_Button_XPATH = (By.XPATH, "//button[normalize-space()='Add']")
    Text_Firstname_XPATH = (By.XPATH, "//input[@placeholder='First Name']")
    Text_Middlename_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_Lastname_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_Save_Button = (
    By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    Verify_Success_msg = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    Click_Add_Emp_XPATH = (By.XPATH, "//a[normalize-space()='Add Employee']")

    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*Add_emp.Click_PIM_XPATH).click()

    def Click_Add(self):
        self.driver.find_element(*Add_emp.Click_Add_Button_XPATH).click()

    def Enter_Firstname(self, firstname):
        self.driver.find_element(*Add_emp.Text_Firstname_XPATH).send_keys(firstname)

    def Enter_Middlename(self, middlename):
        self.driver.find_element(*Add_emp.Text_Middlename_XPATH).send_keys(middlename)

    def Enter_Lastname(self, lastname):
        self.driver.find_element(*Add_emp.Text_Lastname_XPATH).send_keys(lastname)

    def Click_Save(self):
        self.driver.find_element(*Add_emp.Click_Save_Button).click()

    def Click_AddEmployee(self):
        self.driver.find_element(*Add_emp.Click_Add_Emp_XPATH).click()

    def Add_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*Add_emp.Verify_Success_msg)
            return True
        except Ec:
            return False
