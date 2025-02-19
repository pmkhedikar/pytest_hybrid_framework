import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup():
    if browser=='chrome':
        driver= webdriver.Chrome(ChromeDriverManager.install())
        print("Launching Chrome")

    elif browser=='edge':
        driver= webdriver.Edge(EdgeChromiumDriverManager.install())
        print("Launching Edge")

    else:
        driver= webdriver.Firefox(GeckoDriverManager.install())
        print("Launching Firefox")
    return driver


def pytest_addoption(parser):   # this will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()                #this will return browser value to setup method
def browser(request):
    return request.config.getoption("--browser")

### hooks for adding info in HTML report
def pytest_config(config):
    config._metadat["Project Name"] ="Python Selenim Hybrid framework"
    config._metadat["Module Name"] = "Customer Registration"
    config._metadat["Author"] ="Parag Khedikar"

### hooks for delete/modify the info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


### specify the report folder location & save the report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%y_%H-%M-%S")+".html"