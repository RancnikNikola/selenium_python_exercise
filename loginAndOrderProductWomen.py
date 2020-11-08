
from selenium import webdriver
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

time.sleep(2)

# Find password field and enter password
passwdField = driver.find_element_by_name("passwd")
passwdField.send_keys("brucewayne94")

time.sleep(2)

# Find sign in button
loginButton = driver.find_element_by_name("SubmitLogin")
loginButton.click()

time.sleep(3)

# Find WOMEN button and click on it
womenButton = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')
womenButton.click()

time.sleep(3)

# Find DRESSES button and click on it
dressesButton = driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[2]/div[1]/a')
dressesButton.click()

time.sleep(2)

# Find CASUAL DRESSES and click it
casualDresses = driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[1]/div[1]/a')
casualDresses.click()

time.sleep(2)

# Find List button and click on it
listButton = driver.find_element_by_xpath('//*[@id="list"]/a/i')
listButton.click()

time.sleep(2)

# Find Add to Cart button and click on it
addToCart = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div/div[3]/div/div[2]/a[1]')
addToCart.click()

time.sleep(2)

# Find continue shopping button and click on it
continueShopping = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')
continueShopping.click()

time.sleep(2)

# Find DRESSES button and click on it
dressesButton = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a')
dressesButton.click()

time.sleep(3)

# Find EVENING DRESSES and click on it
eveningDresses = driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[2]/div[1]/a')
eveningDresses.click()

time.sleep(3)

# Find a choose pink color dress
pinkColor = driver.find_element_by_xpath('//*[@id="color_43"]')
pinkColor.click()

time.sleep(3)

# Find and click Add to Cart Button
addToCartevening = driver.find_element_by_name('Submit')
addToCartevening.click()

time.sleep(2)

# Find Continue shopping button and click it
continueShopping2 = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')
continueShopping2.click()

time.sleep(2)

# Find DRESSES button and click on it
dressesButton2 = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a')
dressesButton2.click()

time.sleep(3)
# driver.quit()