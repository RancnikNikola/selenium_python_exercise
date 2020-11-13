from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Login import site_login, wait, driver

# ADD FUNCTIONALITY TO PRINT ORDER CONFIRMATION ITD ITD.....
# ADD click() AT THE END OF EVERY LINE


def change_personal_info():
    site_login()
    # Find MY PERSONAL INFORMATION and wait for it to be clickable
    my_personal_information = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[4]/a/span')))
    # Click on MY PERSONAL INFORMATION
    my_personal_information.click()

    # Find First name field and wait for it to be clickable
    firstname = wait.until(EC.element_to_be_clickable((By.ID, 'firstname')))
    # Clear firstname filed
    firstname.clear()
    # Click on firstname field
    firstname.click()
    # Type in firstname field
    firstname.send_keys("Nikola")

    # Find Last name field and wait for it to be clickable
    lastname = wait.until(EC.element_to_be_clickable((By.ID, 'lastname')))
    # Clear lastname filed
    lastname.clear()
    # Click on lastname field
    lastname.click()
    # Type in lastname field
    lastname.send_keys("Rancnik")

    # Find E-mail address field and clear it
    email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
    # Clear lastname filed
    email.clear()
    # Click on lastname field
    email.click()
    # Type in lastname field
    email.send_keys("waynebruce@mailinator.com")

    # Find Date of birth field set day to 1
    days = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="days"]/option[2]')))
    days.click()

    # Find Date of birth field set month to January
    month = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="months"]/option[2]')))
    month.click()

    # Find Date of birth field set month to January
    year = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="years"]/option[22]')))
    year.click()

    # Find Current Password field and click it
    old_pass = wait.until(EC.element_to_be_clickable((By.ID, 'old_passwd')))
    old_pass.click()
    # Type in current user password
    old_pass.send_keys("brucewayne94")

    # Find New Password field and click it
    new_pass = wait.until(EC.element_to_be_clickable((By.ID, 'passwd')))
    new_pass.click()
    # Type in current user password
    new_pass.send_keys("waynebruce94")

    # Confirmation field and click it
    confirmation = wait.until(EC.element_to_be_clickable((By.ID, 'confirmation')))
    confirmation.click()
    # Type in current user password
    confirmation.send_keys("waynebruce94")

    # Find SAVE button
    save_info = wait.until(EC.element_to_be_clickable((By.NAME, 'submitIdentity')))
    save_info.click()

    # Find BACK TO YOUR ACCOUNT
    back_to_acc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/a/span')))
    back_to_acc.click()


change_personal_info()
