import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.EmolyeeSearchPage import EmployeeSearch
from pageObjects.test_AddEmp_Page import Add_emp
from pageObjects.test_loginpage import loginpage  # we are importing pageobject.
from utilities.readproperties import Readconfig  # for importing logs.
from utilities.Logger import logGenerate


class Test_Search_Emp:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = logGenerate.log_gen()

    def test_search_emp_05(self, setup):
        self.log.info("test_search_emp_05 is started")
        self.driver = setup
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

        self.es = EmployeeSearch(self.driver)
        self.es.Enter_EmpName("David")
        self.log.info("Entering Emp Name")
        time.sleep(2)
        self.es.Click_SearchButton()
        time.sleep(5)
        self.log.info("Click on Search button")
        print(self.es.Search_Result())
        if self.es.Search_Result() == True:
            self.log.info("Search Found")
            self.log.info("test_search_emp_05 is Passed")
            self.lp.Click_menu()
            self.log.info("click on Menu button")
            self.lp.Click_Logout()
            self.log.info("click on Logout button")
            assert True
            self.log.info("test_search_emp_05 is Passed")
        else:
            self.log.info("No Search Found")
            self.lp.Click_menu()
            self.log.info("click on Menu button")
            self.lp.Click_Logout()
            self.log.info("click on Logout button")
            self.log.info("test_search_emp_05 is Failed")
            assert False

        self.driver.close()



