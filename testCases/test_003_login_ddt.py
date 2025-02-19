import os.path
import time

import pytest
from webdriver_manager.core import driver

from pageObjects import HomePage
from pageObjects import loginPage
from pageObjects import MyAccountPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlUtilities


class Test_Login_Ddt():
    baseUrl= ReadConfig.getAppUrl()
    logger = LogGen.loggen()


    path = os.path.abspath(os.curdir)+"\\testdata\\loginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        lst_status = []
        self.logger.info("Testcase test_003_login_ddt started")
        self.rows = xlUtilities.getRowCount(self.path, "Sheet1")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        #create the object for pageobject classes
        self.hp = HomePage(self,driver)
        self.lp = loginPage(self,driver)
        self.mp = MyAccountPage(self,driver)


        for r in range(2, self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = xlUtilities.readData(self.path, "Sheet1",r,1)
            self.password = xlUtilities.readData(self.path, "Sheet1",r,2)
            self.exp = xlUtilities.readData(self.path, "Sheet1",r,3)
            self.lp.setloginEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.loginSubmit()
            time.sleep(5)
            self.targetPage = self.lp.isMyAccountPageExists()

            if self.exp=="Valid":
                if self.targetPage==True:
                    lst_status.append("Pass")
                    self.mp.clicklogout()

                else:
                    lst_status.append("Failed")

            elif self.exp=="Invalid":
                if self.targetPage==True:
                    lst_status.append("Failed")
                    self.mp.clicklogout
                else:
                    lst_status.append("Pass")
            self.driver.close()

            if "Fail" not in lst_status:
                assert True
            else:
                assert False

            self.logger("Testcase test_003_login_ddt End")










