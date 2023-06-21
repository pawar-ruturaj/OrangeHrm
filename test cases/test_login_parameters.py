# we create this file to parameters.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options

from pageObjects.test_AddEmp_Page import Add_emp
from pageObjects.test_loginpage import loginpage  # we are importing pageobject.
from utilities.readproperties import Readconfig  # for importing logs.
from utilities.Logger import logGenerate


class Test_login_Parameters:
    # we test the correct url is open or not by using page title. page title is used for page validations, in realtime
    # the page title is different than you can tell a developer to change the page title.
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = logGenerate.log_gen()

    def test_login_param_04(self, setup, getDataforLogin):
        self.driver = setup
        self.log.info("test_login_param_04 is started")
        self.log.info("Opening browser")
        self.log.info("Go to this url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_username(getDataforLogin[0])
        self.log.info("Entering username-->" + getDataforLogin[0])
        self.lp.Enter_Password(getDataforLogin[1])
        self.log.info("Entering Password-->" + getDataforLogin[1])
        self.lp.Click_login()
        self.log.info("Click on login button")

        if self.lp.Login_status() == True:
            if getDataforLogin[2] == "Pass":
                time.sleep(2)
                self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRMlogin.png")
                self.lp.Click_menu()
                self.log.info("click on Menu button")
                self.lp.Click_Logout()
                self.log.info("click on Logout button")
                self.log.info("test_login_param_04 is Passed")
                assert True
            else:
                self.log.info("test_login_param_04 is Failed")
                self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRMlogin.png")
                assert False

        else:
            if getDataforLogin[2] == "Fail":
                assert True
            else:
                self.log.info("test_login_param_04 is Failed")
                self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRMlogin.png")
                assert False

        self.driver.close()
        self.log.info("test_login_param_04 is Completed")

# when we run this testcase and false parameter given to username and password and it should fail the condition but
# the status of test case is Passed

    # def test_add_emp_03(self, setup):
    #     self.driver = setup
    #     self.log.info("test_add_emp_03 is started")
    #     self.log.info("Opening browser")
    #     self.log.info("Go to this url-->" + self.Url)
    #     self.lp = loginpage(self.driver)
    #     self.lp.Enter_username(self.Username)
    #     self.log.info("Entering username-->" + self.Username)
    #     self.lp.Enter_Password(self.Password)
    #     self.log.info("Entering Password-->" + self.Password)
    #     self.lp.Click_login()
    #     self.log.info("Click on login button")
    #
    #     self.ae = Add_emp(self.driver)
    #     self.ae.Click_PIM()
    #     self.log.info("Click on PIM button")
    #     self.ae.Click_Add()
    #     self.log.info("Click on Add button")
    #     self.ae.Enter_Firstname("Ruturaj")
    #     self.log.info("Entering Firstname")
    #     self.ae.Enter_Middlename("S")
    #     self.log.info("Entering Middlename")
    #     self.ae.Enter_Lastname("P")
    #     self.log.info("Entering Lastname")
    #     time.sleep(2)
    #     self.ae.Click_Save()
    #     self.log.info("Click on save button")
    #
    #     if self.ae.Add_Status() == True:
    #         self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRM_add_emp.png")
    #         self.lp.Click_menu()
    #         self.log.info("Click on Menu button")
    #         self.lp.Click_Logout()
    #         self.log.info("Click on Logout button")
    #         self.log.info("test_add_emp_03 is Passed")
    #         assert True
    #     else:
    #         self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRM_add_emp.png")
    #         assert False
    #
    #     self.driver.close()
    #     self.log.info("test_add_emp_03 is completed")
