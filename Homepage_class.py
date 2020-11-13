from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators_class import Locators
import time

# PATH to chromium webdriver
PATH = '/Users/nikolarancnik/chromedriver'
# Set Chrome as driver
driver = webdriver.Chrome(executable_path=PATH)
# Define wait
wait = WebDriverWait(driver, 10)
# Define URL
url = "http://automationpractice.com/index.php"
# Define user email
user_email = "brucewayne@mailinator.com"
# Define user password
user_password = "waynebruce94"
# Go to
# driver.get(url)


class Login:

    def __init__(self, driver):
        self.driver = driver

    def site_login(self):

        # Open the page
        driver.get(url)
        # Find Sign in button and wait for it to be clickable then click it
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        time.sleep(2)
        # Find Email address field and send it the email address
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(user_email)
        time.sleep(2)
        # Find Password field and send it the password value
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(user_password)
        time.sleep(1)
        # Find Sign in button (Login) and wait for it to be clickable
        driver.find_element(*Locators.LOGIN_BUTTON).click()


Login.site_login(url)















