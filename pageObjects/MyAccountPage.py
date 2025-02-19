from selenium.webdriver.common.by import By

class MyAccountPage():
    logout_xpath = "//*[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver= driver

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

    

