from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
driver.get(url)


def site_login():
    # Find Sign in button and wait for it to be clickable
    sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')))
    # Click Sign in button
    sign_in.click()
    # Find Email address field and wait for it to be clickable
    email_address_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    # Click on Email address field
    email_address_field.click()
    # Type email that is set in Email address field
    email_address_field.send_keys(user_email)
    # Find Password field and wait for it to be clickable
    password_field = wait.until(EC.element_to_be_clickable((By.NAME, "passwd")))
    # Click on Email address field
    password_field.click()
    # Type email that is set in Email address field
    password_field.send_keys(user_password)
    # Find Sign in button (Login) and wait for it to be clickable
    sign_in_login = wait.until(EC.element_to_be_clickable((By.NAME, 'SubmitLogin')))
    # Click Sign in button
    sign_in_login.click()














