from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Login import site_login, wait

# ADD FUNCTIONALITY TO PRINT ORDER CONFIRMATION ITD ITD.....


def buy_tshirt():
    site_login()
    # Find T-SHIRTS link in navbar and wait for it to be clickable
    t_shirts = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')))
    # Click T-SHIRTS button
    t_shirts.click()
    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()
    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li/div/div/div[3]/div/div[2]/a[1]')))
    # Click ADD TO CART button
    add_to_cart.click()

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_1.click()

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_3.click()

    # Find Terms of service checkbox and wait for it to be clickable
    terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span')))
    # Agree on Terms of service
    terms_of_service.click()

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_4.click()

    # Find PAY WITH BANK WIRE button and wait for it to be clickable
    pay_with_bank_wire = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')))
    # Click PAY WITH BANK WIRE
    pay_with_bank_wire.click()

    # Find I CONFIRM MY ORDER button and wait for it to be clickable
    confirm_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button/span')))
    # Click PAY WITH BANK WIRE
    confirm_order.click()


buy_tshirt()


