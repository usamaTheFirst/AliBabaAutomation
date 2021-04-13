from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver

        self.web_element = None
        self.locator = locator
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def input_text(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.send_keys(text)
        return None

    @property
    def contact_elements(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator=self.locator))
        self.web_element = element
        return self.web_element

    @property
    def text(self):
        text = self.web_element.text
        return text



