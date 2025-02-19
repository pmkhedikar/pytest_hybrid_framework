import os

import pytest
from webdriver_manager.core import driver
from pageObjects.HomePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_login():
    pass

    baseURL = ReadConfig.getAppUrl()
    logger = LogGen.loggen()

    user = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("test_login method started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self,driver)     #created the object of homepage
        self.hp.clickMyAccount()
        self.hp.login_link()

        self.lp = LoginPage(self,driver)
        self.lp.setloginEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.loginSubmit()

        self.targetpage = self.lp.isMyAccountPageExists()
        if self.targetpage == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_002_login **********")


