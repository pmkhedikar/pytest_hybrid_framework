from selenium.webdriver.common import By


class AccountRegristrationPage():

    firstName_xpath = "//*[@placeholder = 'First Name']"
    lastname_xpath = "//*[@placeholder = 'Last Name']"
    email_xpath= "//*[@placeholder = 'E-Mail']"
    password_xpath = "//*[@placeholder = 'Password']"
    agree_button_xpath = "//*[@name= 'agree']"
    continue_button_xpath = "//*[text()[contains(.,'Continue')]]"
    conf_txt_message_xpath = "//*[text()[contains(.,'Your Account Has Been Created!')]]"

    def __init__(self,driver):
        self.driver= driver

    #actions
    def setFirstname(self,Fname):
        self.driver.find_element(By.XPATH,self.firstName_xpath).send_keys(Fname)

    def setLastname(self,Lname):
        self.driver.find_element(By.XPATH,self.lastname_xpath).send_keys(Lname)

    def setEmail(self, Email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(Email)

    def setPassword(self, Password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(Password)

    def setAgree(self):
        self.driver.find_element(By.XPATH, self.agree_button_xpath).click()

    def clcikContinue(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def getConfMessage(self):
        try:
            self.driver.find_element(By.XPATH, self.conf_txt_message_xpath).text
        except:
            None









