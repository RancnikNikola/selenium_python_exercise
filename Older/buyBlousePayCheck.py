from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Login import site_login, wait, driver
from selenium.webdriver import ActionChains

# ADD FUNCTIONALITY TO PRINT ORDER CONFIRMATION ITD ITD.....
# ADD click() AT THE END OF EVERY LINE


def buy_blouse():
    site_login()

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    # Find TOPS link in navbar and wait for it to be clickable
    tops = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="subcategories"]/ul/li[1]/div[1]/a')))
    # Click on TOPS
    tops.click()

    # Find BLOUSES and wait for it to be clickable
    blouses = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="subcategories"]/ul/li[2]/div[1]/a')))
    # Click on BLOUSES
    blouses.click()

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li/div/div/div[3]/div/div[2]/a[1]')))
    # Click ADD TO CART button
    add_to_cart.click()

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_1 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')))
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

    # Find PAY BY CHECK button and wait for it to be clickable
    pay_by_check = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')))
    # Click PAY BY CHECK
    pay_by_check.click()

    # Find I CONFIRM MY ORDER button and wait for it to be clickable
    confirm_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button/span')))
    # Click PAY WITH BANK WIRE
    confirm_order.click()

buy_blouse()
