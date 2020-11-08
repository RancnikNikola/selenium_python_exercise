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

# Find T-SHIRTS button and click on it
tshirtsButton = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a')
tshirtsButton.click()

time.sleep(3)

# Find List button and click on it
listButton = driver.find_element_by_xpath('//*[@id="list"]/a/i')
listButton.click()

time.sleep(1)

# Find T-SHIRT and click on it
# tshirtSelect = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')
moreButton = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div/div[3]/div/div[2]/a[2]')
moreButton.click()

time.sleep(3)

# Find size field and select it
sizeField = driver.find_element_by_name("group_1")
sizeField.click()
# Select the desired size
desiredSize = driver.find_element_by_xpath('//*[@id="group_1"]/option[2]')
desiredSize.click()

time.sleep(1)

# Find blue color and select it
blueColor = driver.find_element_by_name("Blue")
blueColor.click()

time.sleep(1)

# Find add to cart button and click it
addToCart = driver.find_element_by_xpath('//*[@id="add_to_cart"]/button')
addToCart.click()

time.sleep(2)

# Find proceed to checkout and click on it
checkoutButton = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')
checkoutButton.click()

time.sleep(2)

# Find proceed to checkout and click on it
checkoutButton2 = driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]')
checkoutButton2.click()

time.sleep(2)

# Find proceed to checkout and click on it
checkoutButton3 = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button/span')
checkoutButton3.click()

time.sleep(2)

# Find terms of service and checkout it
checkTerms = driver.find_element_by_name("cgv")
checkTerms.click()

time.sleep(1)

# Find proceed to checkout and click on it
checkoutButton4 = driver.find_element_by_xpath('//*[@id="form"]/p/button/span')
checkoutButton4.click()

time.sleep(1)

# Find Pay with bank wire and click on it
payWithBankWire = driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
payWithBankWire.click()

time.sleep(1)

# Find I confirm my order and click on it
payWithBankWire = driver.find_element_by_xpath('//*[@id="cart_navigation"]/button/span')
payWithBankWire.click()

time.sleep(2)

# Find I confirm my order button and click it
confirmOrder = driver.find_element_by_xpath('//*[@id="cart_navigation"]/button')
confirmOrder.click()

time.sleep(5)

driver.quit()




