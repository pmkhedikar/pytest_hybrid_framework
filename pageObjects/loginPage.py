from selenium.webdriver.common.by import By

class LoginPage():
    #locator
    login_xpath="//*[@name='email']"
    password_xpath = "//*[@name='password']"
    login_button_xpath = "//*[@type='submit']"
    msg_myaccount_xpath = "//h2[text()='My Account']"

    #construtor
    def __init__(self, driver):
        self.driver = driver

    #actions
    def setloginEmail(self,email):
        self.driver.find_element(By.XPATH, self.login_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def loginSubmit(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        except:
            return False




