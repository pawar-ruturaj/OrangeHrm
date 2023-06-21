import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options

from pageObjects.test_AddEmp_Page import Add_emp
from pageObjects.test_loginpage import loginpage  # we are importing pageobject.
from utilities.readproperties import Readconfig  # for importing logs.
from utilities.Logger import logGenerate


class Test_login:
    # we test the correct url is open or not by using page title. page title is used for page validations, in realtime
    # the page title is different than you can tell a developer to change the page title.
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = logGenerate.log_gen()

    def test_page_title_01(self, setup):
        self.driver = setup
        self.log.info("test_page_title_01 is started")
        self.log.info("Opening browser")
        self.log.info("Go to this url-->" + self.Url)
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(5)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        if self.driver.title == "OrangeHRM":
            time.sleep(2)
            self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRM_page_title.png")
            assert True
            self.log.info("test_page_title_01 is Passed")
            self.log.info("Page title is" + self.driver.title)
        else:
            self.log.info("test_page_title_01 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_page_title_01 is Completed")

        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")
        # maintain this sequence same.

    def test_login_02(self, setup):
        self.driver = setup
        self.log.info("test_login_02 is started")
        self.log.info("Opening browser")
        self.log.info("Go to this url-->" + self.Url)
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(5)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        self.lp = loginpage(self.driver)

        self.lp.Enter_username(self.Username)
        self.log.info("Entering username-->" + self.Username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")

        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password-->" + self.Password)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")

        self.lp.Click_login()
        self.log.info("Click on login button")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        # try:
        #     self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        #     # this Xpath of menu button, if this find means log in successful.
        #     # when we enter incorrect credentials, this element is not found and assertion error shown.
        #     print("test_Login_01 is pass")  # if a case is pass then logout perform.
        #     self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #     login = True
        #     # assert True
        #     print(login)
        # except:
        #     print("test_Login_01 is Failed")
        #     login = False
        #     print(login)
        #     # assert False
        # if login == True:
        #     assert True
        # else:
        #     assert False

        if self.lp.Login_status() == True:
            time.sleep(2)
            self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRMlogin.png")
            self.lp.Click_menu()
            self.log.info("click on Menu button")
            self.lp.Click_Logout()
            self.log.info("click on Logout button")
            self.log.info("test_login_02 is Passed")
            assert True
        else:
            self.log.info("test_login_02 is Failed")
            self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRMlogin.png")

            assert False
        self.driver.close()
        self.log.info("test_login_02 is Completed")

    # test case for add employee.
    # login->click on PIM->

    def test_add_emp_03(self, setup):
        self.driver = setup
        self.log.info("test_add_emp_03 is started")
        self.log.info("Opening browser")
        self.log.info("Go to this url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_username(self.Username)
        self.log.info("Entering username-->" + self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password-->" + self.Password)
        self.lp.Click_login()
        self.log.info("Click on login button")

        self.ae = Add_emp(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click on PIM button")
        self.ae.Click_Add()
        self.log.info("Click on Add button")
        self.ae.Enter_Firstname("Ruturaj")
        self.log.info("Entering Firstname")
        self.ae.Enter_Middlename("S")
        self.log.info("Entering Middlename")
        self.ae.Enter_Lastname("P")
        self.log.info("Entering Lastname")
        time.sleep(2)
        self.ae.Click_Save()
        self.log.info("Click on save button")

        if self.ae.Add_Status() == True:
            self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRM_add_emp.png")
            self.lp.Click_menu()
            self.log.info("Click on Menu button")
            self.lp.Click_Logout()
            self.log.info("Click on Logout button")
            self.log.info("test_add_emp_03 is Passed")
            assert True
        else:
            self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRM_add_emp.png")
            assert False

        self.driver.close()
        self.log.info("test_add_emp_03 is completed")

        # # driver = webdriver.Firefox()
        # # driver.implicitly_wait(5)
        # # driver.get("https://opensource-demo.orangehrmlive.com/")
        #
        # self.lp=loginpage(self.driver)
        #
        # self.lp.Enter_username("Admin")
        # # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # self.lp.Enter_Password("admin123")
        # # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        # self.lp.Click_login()
        # # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # self.driver.find_element(By.XPATH,
        #                          "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space("
        #                          ")='PIM']").click()
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Ruturaj")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("S")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("P")
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,
        #                          "//button[@class='oxd-button oxd-button--medium oxd-button--secondary "
        #                          "orangehrm-left-space']").click()
        # print(self.driver.find_element(By.XPATH,
        #                                "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']").text)
        #
        # try:
        #     self.driver.find_element(By.XPATH,
        #                              "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']")
        #     # this Xpath of menu button, if this find means log in successful.
        #     # when we enter incorrect credentials, this element is not found and assertion error shown.
        #     print("test_addemp_02 is passed")  # if a case is pass then logout perform.
        #     # assert True
        #     addemp = True
        # except:
        #     print("test_addemp_02 is Failed")
        #     # assert False
        #     addemp = False
        #
        # if addemp == True:
        #     assert True
        # else:
        #     assert False
        # self.driver.close()

# we can addemp=True and addemp=False instead of assert true and false, in assert if the first assert condition is
# satisfied it will stop execution of the remaining code of that test case, means it not check assert false condition,
# but in addemp=True and false case it will execute both conditions. but we use tag in try and except and use assert
# in if else condition for good practice because it checks both true and false condition in try and except,
# and after that we use assert.

# in above test cases, we observed that some functionality like login functionality we use repeatedly in each test
#  case, so to hande such condition we create new python file conftest where we store common files, if we change in
# conftest that changes apply on all file/testcase.


# we create new folder pageObject.
# here we create page objects. files in pageobject also start with prefix test_.
# if test_ not taken, test case directly run but not run in the terminal.
# we can use pageobject class and its methods in our test cases. any changes in pageobject reflect in test cases.
# because of pageobject test code is minimized, and any changes in code can be done through a page object.

# for good practice, perform logout after each test case execution.

# we can also take screenshots of our test cases for proof of testing (POT). we create new directory Screenshots to
# store screenshots.

# we can also save common and repeatedly used data in test cases.we create configuration folder. in that folder,
# we create config.ini file. we create another folder utility, and in that folder we create readproperties.py file.
# and create methods for common files. utilities folder created to store supporting files for your code

# use print in realtime code is not a good practice, we can use logs to track your activity.
# logs--> logs are nothing but whichever activity you perform, to track that activity.
# it tracks date,time, which class and method are used, line number, message etc. activities are tracked in logs.
# report and logs are different.
# we create logger.py file in utilities.

# without changing the code we can open browser in which we want to run testcases, we define browser in the terminal
# while executing test cases. for that we use hookup functions, we create that function in conftest file.
# hookup function--> it will extend/modify/ customise the behaviour of pytest run. we tell pytest to run test as
# we said in command
# we define method in conftest for hoockup.
# now we can run in the terminal with browser name.
# e.g. pytest -v --browser chrome
#      pytest -v --browser edge
#      pytest -v --browser firefox
#      pytest -v      --> for headless execution.

# by using this method we're done cross-browser testing.
# cross-browser testing by manual testing is not good practice, we use automation for that testing

# when we create a html report, in an environment section, we can modify that environment section my using pytest
# metadata function. and this is onetime activity.

# we can pass multiple values through parameters. consider login test,there are four scenarios,
# But every time we cants change code for each scenario, so we use parameters for that.
# we're defining parameters in conftest file.and crete new file test_login_parameters.py for test that scenario.
# when we only use parameters, and there are 3 scenarios for to fail the test case, that 3 case report shows
# assert fail, but in real that fail result means your test case is pass, to give status pass we use nested if in our
# test case.

# we can create test case data by using Excel.
# we create a new XLutils.py file in utilities, and in that file we create method about exel.
# now we create new test case file test_addemp_ddt file for data-driven run to add employee test case.
# we create another method in XLutils.py file for ditect rows and columns of that excel file sheet.

# while executing in terminal -p no:warnings used, then it will no show warnings in your result.
