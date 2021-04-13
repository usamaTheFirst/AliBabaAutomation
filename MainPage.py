from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BaseElement import BaseElement
from BasePage import BasePage
from Locator import Locator


class MainPage(BasePage):
    url = None

    @property
    def search(self):
        locator = Locator(By.CSS_SELECTOR, "input[class = 'ui-searchbar-keyword'][name = 'SearchText']")
        return BaseElement(self.driver, locator=locator)

    @property
    def next_page(self):
        locator = Locator(By.CSS_SELECTOR, "i.ui2-icon.ui2-icon-arrow-right.ui2-icon-xs")
        return BaseElement(self.driver, locator=locator)

    def contact_supllier(self, message):
        locator = Locator(By.CSS_SELECTOR, "div a.contact-supplier-btn.organic-gallery-offer__bottom-v2-item.small")
        elements = BaseElement(self.driver, locator).contact_elements
        elements[0].click()

        inp = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div textarea#inquiry-content')))
        print(inp)
        inp.send_keys(message)
        # for element in elements:
        #     element.click()
        #     self.enter_message(message)
        #     # self.send_message()

    def enter_message(self, message):
        locator = Locator(By.CSS_SELECTOR, "div textarea#inquiry-content")
        elements = BaseElement(self.driver, locator)
        elements.input_text(message)

    def send_message(self):
        locator = Locator(By.CSS_SELECTOR, "input.ui2-button.ui2-button-default.ui2-button-primary.ui2-button-large")
        element = BaseElement(self.driver, locator)
        element.click_button()

    def submit_RFQ(self):
        locator = Locator(By.CSS_SELECTOR, "button.next-btn.next-medium.next-btn-primary.submit-btn")
        element = BaseElement(self.driver, locator)
        element.click_button()
        self.driver.close()
