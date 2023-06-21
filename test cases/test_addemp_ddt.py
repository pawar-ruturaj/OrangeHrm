import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options

from pageObjects.test_AddEmp_Page import Add_emp
from pageObjects.test_loginpage import loginpage  # we are importing pageobject.
from utilities import XLutils
from utilities.readproperties import Readconfig  # for importing logs.
from utilities.Logger import logGenerate


class Test_Add_Emp_DDT:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = logGenerate.log_gen()
    path = "D:\\Ruturaj\\OrangeHRM\\test cases\\TestData\\EmployeeList.xlsx"

    # get this path from test data folders absolute path of Excel file.

    def test_add_emp_ddt_06(self, setup):
        self.log.info("test_add_emp_ddt_06 is started")
        self.driver = setup
        self.log.info("Opening browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_username(self.Username)
        self.log.info("Entering username-->" + self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password-->" + self.Password)
        self.lp.Click_login()
        self.log.info("Click on login button")

        self.ae = Add_emp(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')  # it will get Excel file
        print("Number of rows are-->", self.rows)  # it will print no. of rows in that Excel file.
        self.ae.Click_PIM()
        self.log.info("Click on PIM button")
        self.ae.Click_Add()
        self.log.info("Click on Add button")
        status_list = []

        for r in range(2, self.rows + 1):
            self.FirstName = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.MiddleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.LastName = XLutils.readData(self.path, 'Sheet1', r, 4)
            time.sleep(2)
            self.ae.Enter_Firstname(self.FirstName)
            self.log.info("Entering Firstname-->" + self.FirstName)
            self.ae.Enter_Middlename(self.MiddleName)
            self.log.info("Entering MiddleName-->" + self.MiddleName)
            self.ae.Enter_Lastname(self.LastName)
            self.log.info("Entering Lastname-->" + self.LastName)
            time.sleep(2)
            self.ae.Click_Save()
            self.log.info("Click on save button")

            if self.ae.Add_Status() == True:
                self.ae.Click_AddEmployee()
                time.sleep(2)
                status_list.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Pass")
                self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRM_add_emp.png")
                self.log.info("test_add_emp_ddt_06 is Passed")

            else:
                status_list.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Fail")
                self.driver.save_screenshot("D:\\Ruturaj\\OrangeHRM\\Screenshots\\HRM_add_emp.png")

        print(status_list)

        time.sleep(2)
        self.lp.Click_menu()
        self.log.info("Click on Menu button")
        time.sleep(2)
        self.lp.Click_Logout()
        self.log.info("Click on Logout button")
        self.driver.close()
        if "Fail" not in status_list:
            self.log.info("test_add_emp_ddt_06 is Passed")
            assert True
        else:
            self.log.info("test_add_emp_ddt_06 is Failed")
            assert False

        self.log.info("test_add_emp_03 is completed")

# when open with a browser case is successful, but when open in headless mode it will fail,why??
