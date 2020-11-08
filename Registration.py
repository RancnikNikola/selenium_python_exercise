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

# Find email field and enter email "brucewayne@mail.com"
emailField = driver.find_element_by_name("email_create")
# emailField.send_keys("brucewayne@mailinator.com")
emailField.send_keys("brucewayne10@mailinator.com")

# Click on create an account button
emailFieldButton = driver.find_element_by_xpath('//*[@id="SubmitCreate"]/span')
emailFieldButton.click()

time.sleep(3)

# YOUR PERSONAL INFORMATION
# Find radio button with Mr. and click on it
radioButtonGender = driver.find_element_by_xpath('//*[@id="id_gender1"]')
radioButtonGender.click()

time.sleep(1)

# Find First name input field and type in "Bruce"
firstNamePersonal = driver.find_element_by_name("customer_firstname")
firstNamePersonal.send_keys("Bruce")

time.sleep(1)

# Find Last name input field and type in "Wayne"
lastNamePersonal = driver.find_element_by_name("customer_lastname")
lastNamePersonal.send_keys("Wayne")

time.sleep(1)

# Find Password field and type in "brucewayne94"
passField = driver.find_element_by_name("passwd")
passField.send_keys("brucewayne94")

time.sleep(1)

# Find drop down element ( for day of birth)
birthDayBox = driver.find_element_by_xpath('//*[@id="days"]')
birthDayBox.click()
# Select the day in dropdown and click on right
birthDay = driver.find_element_by_xpath('//*[@id="days"]/option[18]')
birthDay.click()

time.sleep(1)

# Find drop down element ( for month of birth)
monthDayBox = driver.find_element_by_xpath('//*[@id="months"]')
monthDayBox.click()
# Select the month in dropdown and click on right
monthDay = driver.find_element_by_xpath('//*[@id="months"]/option[6]')
monthDay.click()

time.sleep(1)

# Find drop down element ( for year of birth)
yearDayBox = driver.find_element_by_xpath('//*[@id="years"]')
yearDayBox.click()
# Select the year in dropdown and click on right
yearDay = driver.find_element_by_xpath('//*[@id="years"]/option[28]')
yearDay.click()

time.sleep(1)

# Find newsletter checkbox and click on it
newsletterBox = driver.find_element_by_name("newsletter")
newsletterBox.click()

time.sleep(1)

# Find optin checkbox and click on it ( Receive special offers...)
yearDayBox = driver.find_element_by_name("optin")
yearDayBox.click()

time.sleep(1)

# YOUR ADDRESS
# Find Company field and enter "Wayne"
companyField = driver.find_element_by_name("company")
companyField.send_keys("Wayne")

time.sleep(1)

# Find Address field and enter "Doverska"
addressField = driver.find_element_by_name("address1")
addressField.send_keys("Doverska 23")

time.sleep(1)

# Find Address (Line 2) field and enter "Doverska 2"
addressField2 = driver.find_element_by_name("address2")
addressField2.send_keys("Doverska 2")

time.sleep(1)

# Find Address field and enter "Doverska"
cityField = driver.find_element_by_name("city")
cityField.send_keys("Split")

# Find State field and click on it
stateField = driver.find_element_by_name("id_state")
stateField.click()
# Find the desired state
stateFieldstate = driver.find_element_by_xpath('//*[@id="id_state"]/option[6]')
stateFieldstate.click()

time.sleep(1)

# Find Zip/Postal Code field
zipPostal = driver.find_element_by_name("postcode")
zipPostal.send_keys("21000")

time.sleep(1)

# Find Additional information field and enter "Some additional information"
additionalInfo = driver.find_element_by_name("other")
additionalInfo.send_keys("Some additional information")

time.sleep(1)

# Find Mobile phone field
homephoneField = driver.find_element_by_name("phone")
homephoneField.send_keys("12345678")

time.sleep(1)

# Find Mobile phone field
mobileField = driver.find_element_by_name("phone_mobile")
mobileField.send_keys("099999999")

# Find Assign an address alias field
aliasField = driver.find_element_by_name("alias")
aliasField.send_keys("Address")

time.sleep(1)

# Find Register button
registerPerson = driver.find_element_by_name("submitAccount")
registerPerson.click()

time.sleep(3)

driver.quit()



