from selenium.webdriver.common.by import By
from BaseElement import BaseElement
from BasePage import BasePage
from Locator import Locator
class LoginPage(BasePage):
    url = 'https://passport.alibaba.com/icbu_login.htm?tracelog=hd_signin'

    @property
    def input_email(self):
        locator = Locator(By.CSS_SELECTOR,"input#fm-login-id")
        return BaseElement(self.driver,locator= locator)

    @property
    def input_password(self):
        locator = Locator(By.CSS_SELECTOR, "input#fm-login-password")
        return BaseElement(self.driver, locator=locator)


    @property
    def signin_button(self):
        locator = Locator(By.CSS_SELECTOR, "input[type = 'submit']")
        return BaseElement(self.driver, locator=locator)


