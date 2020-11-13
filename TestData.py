from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# PATH to chromium driver
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