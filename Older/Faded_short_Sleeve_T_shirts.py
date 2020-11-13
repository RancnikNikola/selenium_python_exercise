from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Login import site_login, wait, driver
import time

action = ActionChains(driver)

# ACTIONS
# Orange color
# Blue color
# Add to wishlist
# Add to compare
# Add to cart
# More
# Quick view


def faded_short_sleeve_t_shirts_add_to_cart():
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[1]')))
    # Click ADD TO CART button
    add_to_cart.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout.click()

    time.sleep(1)   # If quantity is more than 2 click - sign till it is 1 !!!!!!

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_1.click()

    time.sleep(1)

    # Find TEXTAREA
    # "If you would like to add a comment about your order, please write in the field below
    order_comment = wait.until(EC.element_to_be_clickable((By.NAME, 'message')))
    # Click to write into textbox
    order_comment.click()
    # Write your comment about order
    order_comment.send_keys("This is my comment about this order")

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find text link "(Read the Terms of Service)"
    read_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div/p[2]/a')))
    # Click to read terms of service
    read_terms_of_service.click()

    time.sleep(1)

    # Find close button (x) for window of "terms and conditions of use"
    close_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="order"]/div[2]/div/div/a')))
    # Close the window of terms of service
    close_terms_of_service.click()

    time.sleep(1)

    # Find Terms of service checkbox and wait for it to be clickable
    terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span')))
    # Agree\Click on Terms of service
    terms_of_service.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_3.click()

    time.sleep(1)

    # Find PAY WITH BANK WIRE button and wait for it to be clickable
    pay_with_bank_wire = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')))
    # Click PAY WITH BANK WIRE
    pay_with_bank_wire.click()

    time.sleep(1)

    # Find I CONFIRM MY ORDER button and wait for it to be clickable
    confirm_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button')))
    # Click PAY WITH BANK WIRE
    confirm_order.click()

    time.sleep(1)

    # Write out content here


def faded_short_sleeve_t_shirts_more():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_cart"]/button')))
    # Click ADD TO CART button
    add_to_cart.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find TEXTAREA
    # "If you would like to add a comment about your order, please write in the field below
    order_comment = wait.until(EC.element_to_be_clickable((By.NAME, 'message')))
    # Click to write into textbox
    order_comment.click()
    # Pause for 1 second
    time.sleep(1)
    # Write your comment about order
    order_comment.send_keys("This is my comment about this order")

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find text link "(Read the Terms of Service)"
    read_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div/p[2]/a')))
    # Click to read terms of service
    read_terms_of_service.click()

    time.sleep(3)

    # Find close button (x) for window of "terms and conditions of use"
    close_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="order"]/div[2]/div/div/a')))
    # Close the window of terms of service
    close_terms_of_service.click()

    time.sleep(1)

    # Find Terms of service checkbox and wait for it to be clickable
    terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span')))
    # Agree\Click on Terms of service
    terms_of_service.click()

    time.sleep(2)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_3.click()

    time.sleep(1)

    # Find PAY WITH BANK WIRE button and wait for it to be clickable
    pay_with_bank_wire = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')))
    # Click PAY WITH BANK WIRE
    pay_with_bank_wire.click()

    time.sleep(1)

    # Find I CONFIRM MY ORDER button and wait for it to be clickable
    confirm_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button')))
    # Click PAY WITH BANK WIRE
    confirm_order.click()

    time.sleep(1)

    # Write out content here


def faded_short_sleeve_t_shirts_add_to_wishlist():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find Add to wishlist button
    add_to_wishlist = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[3]/div[1]/a')))
    # Click on add to wishlist
    add_to_wishlist.click()

    time.sleep(2)

    # Find close button (x) of the popup
    popup_close = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="category"]/div[2]/div/div/a')))
    # Close the popup
    popup_close.click()

    time.sleep(1)


def faded_short_sleeve_t_shirts_orange_color():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find ORANGE color and wait for it to be clickable
    orange_color = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color_1"]')))
    # Click on ORANGE color
    orange_color.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_cart"]/button')))
    # Click ADD TO CART button
    add_to_cart.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find TEXTAREA
    # "If you would like to add a comment about your order, please write in the field below
    order_comment = wait.until(EC.element_to_be_clickable((By.NAME, 'message')))
    # Click to write into textbox
    order_comment.click()
    # Pause for 1 second
    time.sleep(1)
    # Write your comment about order
    order_comment.send_keys("This is my comment about this order")

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find text link "(Read the Terms of Service)"
    read_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div/p[2]/a')))
    # Click to read terms of service
    read_terms_of_service.click()

    time.sleep(3)

    # Find close button (x) for window of "terms and conditions of use"
    close_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="order"]/div[2]/div/div/a')))
    # Close the window of terms of service
    close_terms_of_service.click()

    time.sleep(1)

    # Find Terms of service checkbox and wait for it to be clickable
    terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span')))
    # Agree\Click on Terms of service
    terms_of_service.click()

    time.sleep(2)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_3.click()

    time.sleep(1)

    # Find PAY WITH BANK WIRE button and wait for it to be clickable
    pay_with_bank_wire = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')))
    # Click PAY WITH BANK WIRE
    pay_with_bank_wire.click()

    time.sleep(1)

    # Find I CONFIRM MY ORDER button and wait for it to be clickable
    confirm_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button')))
    # Click PAY WITH BANK WIRE
    confirm_order.click()

    time.sleep(1)

    # Write out content here


def faded_short_sleeve_t_shirts_blue_color():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find BLUE color and wait for it to be clickable
    blue_color = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="color_2"]')))
    # Click on BLUE color
    blue_color.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_cart"]/button')))
    # Click ADD TO CART button
    add_to_cart.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find TEXTAREA
    # "If you would like to add a comment about your order, please write in the field below
    order_comment = wait.until(EC.element_to_be_clickable((By.NAME, 'message')))
    # Click to write into textbox
    order_comment.click()
    # Pause for 1 second
    time.sleep(1)
    # Write your comment about order
    order_comment.send_keys("This is my comment about this order")

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find text link "(Read the Terms of Service)"
    read_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div/p[2]/a')))
    # Click to read terms of service
    read_terms_of_service.click()

    time.sleep(3)

    # Find close button (x) for window of "terms and conditions of use"
    close_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="order"]/div[2]/div/div/a')))
    # Close the window of terms of service
    close_terms_of_service.click()

    time.sleep(1)

    # Find Terms of service checkbox and wait for it to be clickable
    terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span')))
    # Agree\Click on Terms of service
    terms_of_service.click()

    time.sleep(2)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_3.click()

    time.sleep(1)

    # Find PAY WITH BANK WIRE button and wait for it to be clickable
    pay_with_bank_wire = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')))
    # Click PAY WITH BANK WIRE
    pay_with_bank_wire.click()

    time.sleep(1)

    # Find I CONFIRM MY ORDER button and wait for it to be clickable
    confirm_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button')))
    # Click PAY WITH BANK WIRE
    confirm_order.click()

    time.sleep(1)

    # Write out content here


def faded_short_sleeve_t_shirts_compare():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find first to compare button
    compare_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[3]/div[2]/a')))
    # Click on add to compare button
    compare_button.click()

    time.sleep(1)

    # Find second to compare button
    compare_button_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div/div[3]/div/div[3]/div[2]/a')))
    # Click on add to compare button
    compare_button_2.click()

    time.sleep(1)

    # Find COMPARE button
    compare_two = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/div[3]/div[2]/form/button')))
    # Click on COMPARE button
    compare_two.click()

    time.sleep(1)

    # Write results here


def faded_short_sleeve_t_shirts_more_write_a_review():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find WRITE A REVIEW textbox and wait for it to be clickable
    write_a_review_blouse = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="product_comments_block_extra"]/ul/li/a')))
    # Click on WRITE A REVIEW
    write_a_review_blouse.click()

    time.sleep(1)

    # Find QUALITY stars and wait for it to be clickable
    quality_star_5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="criterions_list"]/li/div[1]/div[6]')))
    # Click and rate the product with 5 stars
    quality_star_5.click()

    time.sleep(1)

    # Find TITLE input field for blouse and wait for it to be clickable
    review_blouse_title = wait.until(EC.element_to_be_clickable((By.NAME, 'title')))
    # Click on TITLE input field
    review_blouse_title.click()
    # Type in title
    review_blouse_title.send_keys("Title for blouse")

    time.sleep(1)

    # Find COMMENT input field for blouse and wait for it to be clickable
    review_blouse_comment = wait.until(EC.element_to_be_clickable((By.NAME, 'content')))
    # Click on COMMENT input field
    review_blouse_comment.click()
    # Type in COMMENT
    review_blouse_comment.send_keys("One big comment for blouse that is automated")

    time.sleep(1)

    # Find SEND button and wait for it to be clickable
    send_review = wait.until(EC.element_to_be_clickable((By.ID, 'submitNewMessage')))
    # Click SEND to send a review
    send_review.click()

    time.sleep(1)

    # Find OK button and wait for it to be clickable
    ok_button_review = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div/p[2]/button')))
    # Click OK button
    ok_button_review.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_cart"]/button')))
    # Click ADD TO CART button
    add_to_cart.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout.click()

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find TEXTAREA
    # "If you would like to add a comment about your order, please write in the field below
    order_comment = wait.until(EC.element_to_be_clickable((By.NAME, 'message')))
    # Click to write into textbox
    order_comment.click()
    # Pause for 1 second
    time.sleep(1)
    # Write your comment about order
    order_comment.send_keys("This is my comment about this order")

    time.sleep(1)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_2.click()

    time.sleep(1)

    # Find text link "(Read the Terms of Service)"
    read_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div/p[2]/a')))
    # Click to read terms of service
    read_terms_of_service.click()

    time.sleep(3)

    # Find close button (x) for window of "terms and conditions of use"
    close_terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="order"]/div[2]/div/div/a')))
    # Close the window of terms of service
    close_terms_of_service.click()

    time.sleep(1)

    # Find Terms of service checkbox and wait for it to be clickable
    terms_of_service = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniform-cgv"]/span')))
    # Agree\Click on Terms of service
    terms_of_service.click()

    time.sleep(2)

    # Find PROCEED TO CHECKOUT button and wait for it to be clickable
    proceed_to_checkout_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button')))
    # Click PROCEED TO CHECKOUT button
    proceed_to_checkout_3.click()

    time.sleep(1)

    # Find PAY WITH BANK WIRE button and wait for it to be clickable
    pay_with_bank_wire = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')))
    # Click PAY WITH BANK WIRE
    pay_with_bank_wire.click()

    time.sleep(1)

    # Find I CONFIRM MY ORDER button and wait for it to be clickable
    confirm_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button')))
    # Click PAY WITH BANK WIRE
    confirm_order.click()

    time.sleep(1)

    # Write out content here


def faded_short_sleeve_t_shirts_more_quantity_increase():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find QUANTITY and wait for it to be clickable
    increase_quantity = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]')))
    # Click on + sign one(1) time(s) to increase quantity
    increase_quantity.click()

    time.sleep(1)


def faded_short_sleeve_t_shirts_more_quantity_decrease():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find QUANTITY and wait for it to be clickable
    decrease_quantity = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quantity_wanted_p"]/a[1]/span')))
    # Click on - sign one(1) time(s) to decrease quantity
    decrease_quantity.click()

    time.sleep(1)


def faded_short_sleeve_t_shirts_more_size_large():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find SIZE dropdown and wait for it to be clickable
    size_large = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="group_1"]/option[3]')))
    # Select the size M and click it
    size_large.click()

    time.sleep(1)

def faded_short_sleeve_t_shirts_more_size_medium():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find SIZE dropdown and wait for it to be clickable
    size_large = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="group_1"]/option[2]')))
    # Select the size M and click it
    size_large.click()

    time.sleep(1)

def faded_short_sleeve_t_shirts_more_size_small():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find SIZE dropdown and wait for it to be clickable
    size_large = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="group_1"]/option[1]')))
    # Select the size M and click it
    size_large.click()

    time.sleep(1)

def faded_short_sleeve_t_shirts_more_add_to_wishlist():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find Add to wishlist button
    add_to_wishlist = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist_button"]')))
    # Click on add to wishlist
    add_to_wishlist.click()

    time.sleep(2)

    # Find close button (x) of the popup
    popup_close = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/a')))
    # Close the popup
    popup_close.click()

    time.sleep(1)


def faded_short_sleeve_t_shirts_more_send_to_a_friend():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find SEND TO A FRIEND button
    send_to_a_friend_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="send_friend_button"]')))
    # Click SEND TO A FRIEND button
    send_to_a_friend_button.click()

    time.sleep(1)

    # Find NAME OF YOUR FRIEND input field
    name_of_your_friend = wait.until(EC.element_to_be_clickable((By.NAME, 'friend_name')))
    # Click to write into input field
    name_of_your_friend.click()
    # Write your friend's name about order
    name_of_your_friend.send_keys("Jane Doe")

    time.sleep(2)

    # Find EMAIL ADDRESS OF YOUR FRIEND input field
    email_of_your_friend = wait.until(EC.element_to_be_clickable((By.NAME, 'friend_email')))
    # Click to write into input field
    email_of_your_friend.click()
    # Write your friend's email
    email_of_your_friend.send_keys("Janedoe@unknown.com")

    time.sleep(2)

    # Find SEND button
    send_button_friend = wait.until(EC.element_to_be_clickable((By.NAME, 'sendEmail')))
    # Click SEND button to send content to friend
    send_button_friend.click()

    time.sleep(2)

    # Find OK button
    friend_ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div/p[2]/input')))
    # Click OK button
    friend_ok.click()

    time.sleep(1)


def faded_short_sleeve_t_shirts_more_view_larger_swipe_right():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find VIEW LARGE button to see the picture in full size
    view_large_picture = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view_full_size"]')))
    # Click on picture VIEW LARGE button
    view_large_picture.click()

    time.sleep(1)

    # First level action to perform to acticate hover
    # before_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div[1]/a[2]')))
    # action.move_to_element(before_next_button).perform()

    # Find NEXT button
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div[1]/a[2]')))
    # action.move_to_element(next_button).perform()

    # Click NEXT button to see the next image
    next_button.click()
    time.sleep(2)

    # Find NEXT button 2
    next_button_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[2]')))
    # Click NEXT button 2 to see the next image
    next_button_2.click()
    time.sleep(2)

    # Find NEXT button 3
    next_button_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[2]')))
    # Click NEXT button 3 to see the next image
    next_button_3.click()

    time.sleep(2)

    # Find NEXT button 4
    next_button_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[2]')))
    # Click NEXT button 4 to see the next image
    next_button_4.click()

    time.sleep(2)

    # Find CLOSE button (x) to close the large picture
    close_large = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/a')))
    # Click to close the window
    close_large.click()


def faded_short_sleeve_t_shirts_more_view_larger_swipe_left():
    driver.maximize_window()
    # Log in into website
    site_login()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find LIST button to change view of products wait for it to be clickable
    list_view = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list"]/a')))
    # Click LIST button
    list_view.click()

    time.sleep(1)

    # Find MORE button
    more_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]/span')))
    # Click on button
    more_button.click()

    time.sleep(1)

    # Find VIEW LARGE button to see the picture in full size
    view_large_picture = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view_full_size"]')))
    # Click on picture VIEW LARGE button
    view_large_picture.click()

    time.sleep(1)

    # Find PREVIOUS button
    previous_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div[1]/a[1]')))
    # Click PREVIOUS button to see the next image
    previous_button.click()

    time.sleep(2)

    # Find PREVIOUS button 2
    previous_button_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[1]')))
    # Click PREVIOUS button 2 to see the next image
    previous_button_2.click()

    time.sleep(2)

    # Find PREVIOUS button 3
    previous_button_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[1]')))
    # Click PREVIOUS button 3 to see the next image
    previous_button_3.click()

    time.sleep(2)

    # Find PREVIOUS button 4
    previous_button_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[1]')))
    # Click PREVIOUS button 4 to see the next image
    previous_button_4.click()

    time.sleep(2)

    # Find CLOSE button (x) to close the large picture
    close_large = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/a')))
    # Click to close the window
    close_large.click()


faded_short_sleeve_t_shirts_more_view_larger_swipe_left()









