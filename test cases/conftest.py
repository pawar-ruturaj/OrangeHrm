# here we store browser related and plugin-related files. we can use only conftest name for that file.
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# when we define testcase, use setup with self--> def test_add_emp_03(self,setup):
# and replace all driver into self.driver ( use notepad for that, copy code in notepad and use find and replace)
# here you change it will reflect in testcases.

def pytest_addoption(parser):  # parser is an inbuilt function
    parser.addoption("--browser")
    # here we customize run of pytest.while running pytest it will take argument 'browser'


# here wee give value to the browser.
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# in def setup no argument, but when we use hoockup, we need to give above browser argument in below setup def.

@pytest.fixture()
def setup(browser):  # setup is standard name.
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        driver = webdriver.Firefox()
        # driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    return driver

# when we create a html report, in an environment section, we can modify that environment section my using pytest
# metadata function. and this is onetime activity.

def pytest_metadata(metadata):
    # to add
    metadata["Environment"] = "test"
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Ruturaj"
    # to remove
    metadata.pop("Packages",None)
    metadata.pop("Plugins",None)

@pytest.fixture(params=[
    ("Admin","admin123","Pass"),   # correct username(CU), correct password(CP)
    ("Admin1","admin123","Fail"),  #IU,CP
    ("Admin","admin1234","Fail"),  #CU,IP
    ("Admin1","admin1231","Fail"), #IU,IP
])
def getDataforLogin(request):
    return request.param

# if an interviewer asks where you store test data, you can say that in configtest file we store test data.
