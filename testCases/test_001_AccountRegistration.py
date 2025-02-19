import os.path

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegristrationPage
from utilities.randomString import random_str_generator
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountRegistartion():
    baseURL = ReadConfig.getAppUrl()
    logger= LogGen.loggen()

    def test_account_reg(self,setup):
        self.logger.info("********* Test AccountRegistartion Started")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # created the object of class
        self.hp.clickMyAccount()
        self.hp.register_link()

        self.regpg = AccountRegristrationPage(self.driver)
        self.regpg.setFirstname("Parag")
        self.regpg.setLastname("Khedikar")
        self.email = random_str_generator()+"@gmail.com"
        self.regpg.setEmail(self.email)
        self.regpg.setPassword("1234512345")
        self.regpg.setAgree()
        self.regpg.clcikContinue()
        self.confirMsg = self.regpg.getConfMessage()
        if self.confirMsg =="Your Account Has Been Created!":
            assert  True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenShots\\"+ "test_account_reg.png")
            self.driver.close()
            assert False
            self.logger.info("********* Test AccountRegistartion Finsihed")

