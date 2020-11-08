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

# Find email field for login purposes and enter email
emailField = driver.find_element_by_name("email")
emailField.send_keys("brucewayne@mailinator.com")

time.sleep(1)

# Find password field and enter password
passwdField = driver.find_element_by_name("passwd")
passwdField.send_keys("brucewayne94")

time.sleep(1)

# Find sign in button
loginButton = driver.find_element_by_name("SubmitLogin")
loginButton.click()

time.sleep(3)

driver.quit()