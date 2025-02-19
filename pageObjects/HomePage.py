from selenium.webdriver.common.by import By


class HomePage():
    # locators
    myaccount_link = "//span[text()[contains(.,'My Account')]]"
    register_link = "//*[@class='dropdown-item' and contains(text(),'Register')]"
    login_link = "//*[@class='dropdown-item' and contains(text(),'Login')]"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action steps
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.myaccount_link).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.register_link).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_link)

