import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()

# Open the website
driver.get("http://automationpractice.com/index.php")

driver.maximize_window()

# Click on sign in button
signIn = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
signIn.click()

time.sleep(3)

# Find forgot password and click on it
forgotPasswd = driver.find_element_by_xpath('//*[@id="login_form"]/div/p[1]/a')
forgotPasswd.click()

time.sleep(3)

# Find email address field and enter address
forgotEmail = driver.find_element_by_name('email')
forgotEmail.send_keys("brucewayne@mailinator.com")

time.sleep(1)

# Find Retrieve Password button and click on it
retrievePass = driver.find_element_by_xpath('//*[@id="form_forgotpassword"]/fieldset/p/button/span')
retrievePass.click()

time.sleep(3)

driver.quit()