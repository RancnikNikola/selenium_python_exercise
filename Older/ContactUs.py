from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Login import site_login, wait, driver

# ADD FUNCTIONALITY TO PRINT ORDER CONFIRMATION ITD ITD.....
# ADD click() AT THE END OF EVERY LINE


def contact_us():
    site_login()

    # Find WOMEN link in navbar and wait for it to be clickable
    contact = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contact-link"]/a')))
    # Click on WOMEN in navbar
    contact.click()

    # Find Subject Heading and wait for it to be clickable
    subject_heading = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_contact"]/option[2]')))
    # Click on subject heading and select Customer Service
    subject_heading.click()

    # Find Order reference and wait for it to be clickable
    order_reference = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/fieldset/div[1]/div[1]/div[2]/div/select/option[2]')))
    # Click on order reference and select first on the list
    order_reference.click()

    # Find Product and wait for it to be clickable
    product = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="253601_order_products"]/option[2]')))
    # Click on Product and select the first product on list
    product.click()

    # Find Attach File and wait for it to be clickable
    # attach_file = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fileUpload"]')))
    # Click on attach file
    # attach_file.click()
    # Upload file an locate it on you drive
    # attach_file.send_keys('/Users/nikolarancnik/Downloads/IN027828.pdf')

    # Find Message Textbox and wait for it to be clickable
    message = wait.until(EC.element_to_be_clickable((By.ID, 'message')))
    # Click on message textbox
    message.click()
    # Type in message you want to write
    message.send_keys("This is the message I want to write in textbox")

    # Find SEND button and wait for it to be clickable
    send = wait.until(EC.element_to_be_clickable((By.ID, 'submitMessage')))
    # Click SEND button
    send.click()


contact_us()

