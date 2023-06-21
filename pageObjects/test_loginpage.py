from selenium.webdriver.common.by import By


class loginpage:
    Text_username_XPATH = (By.XPATH, "//input[@placeholder='Username']")
    Text_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Click_Login_Button = (By.XPATH, "//button[normalize-space()='Login']")
    Click_Menu_Button_XPATH = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_username(self, Username):
        self.driver.find_element(*loginpage.Text_username_XPATH).send_keys(
            Username)  # * is used for take variable from class.

    def Enter_Password(self, password):
        self.driver.find_element(*loginpage.Text_Password_XPATH).send_keys(password)

    def Click_login(self):
        self.driver.find_element(*loginpage.Click_Login_Button).click()

    def Click_menu(self):
        self.driver.find_element(*loginpage.Click_Menu_Button_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*loginpage.Click_Logout_XPATH).click()

    def Login_status(self):
        try:
            self.driver.find_element(*loginpage.Click_Menu_Button_XPATH)
            return True
        except:
            return False
