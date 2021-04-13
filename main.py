from selenium import webdriver
from LoginPage import LoginPage
from Credentials import email,password
from selenium.webdriver.common.keys import Keys
import time

from MainPage import MainPage

driver = webdriver.Chrome()

page = LoginPage(driver)
page.go()

page.input_email.input_text(email)
page.input_password.input_text(password)
page.signin_button.click_button()
time.sleep(15)
mainpage = MainPage(driver)
mainpage.search.input_text('Mobile Phone')
mainpage.search.input_text(Keys.ENTER)
message = "This is just an automated test please ignore this message"

mainpage.contact_supllier(message)

