from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Login import site_login, wait
import time

# ADD FUNCTIONALITY TO PRINT ORDER CONFIRMATION ITD ITD.....
# ADD click() AT THE END OF EVERY LINE
# ADD FILE UPLOAD AUTOMATIZATION


def change_color():
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

    # Find MORE button in Printed Summer Dress and wait for it to be clickable
    more_summer_dress = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[5]/div/div/div[3]/div/div[2]/a[2]')))
    # Click on dress
    more_summer_dress.click()

    time.sleep(1)

    # Find BLACK color and wait for it to be clickable
    black_color = wait.until(EC.element_to_be_clickable((By.NAME, 'Black')))
    # Click on BLACK color
    black_color.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart_black = wait.until(EC.element_to_be_clickable((By.NAME, 'Submit')))
    # Click on ADD TO CART button
    add_to_cart_black.click()

    time.sleep(1)

    # Find CONTINUE SHOPPING button and wait for it to be clickable
    continue_shopping_black = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span')))
    # Click on ADD TO CART button
    continue_shopping_black.click()

    time.sleep(1)

    # Find ORANGE color and wait for it to be clickable
    orange_color = wait.until(EC.element_to_be_clickable((By.NAME, 'Orange')))
    # Click on BLACK color
    orange_color.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart_orange = wait.until(EC.element_to_be_clickable((By.NAME, 'Submit')))
    # Click on ADD TO CART button
    add_to_cart_orange.click()

    time.sleep(1)

    # Find CONTINUE SHOPPING button and wait for it to be clickable
    continue_shopping_orange = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span')))
    # Click on ADD TO CART button
    continue_shopping_orange.click()

    time.sleep(1)

    # Find SIZE dropdown and wait for it to be clickable
    size_dress_medium = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="group_1"]/option[2]')))
    # Select the size M and click it
    size_dress_medium.click()

    time.sleep(1)

    # Find BLUE color and wait for it to be clickable
    blue_color = wait.until(EC.element_to_be_clickable((By.NAME, 'Blue')))
    # Click on BLACK color
    blue_color.click()

    time.sleep(1)

    # Find QUANTITY and wait for it to be clickable
    dress_quantity_blue = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]')))
    # Click on + sign to increase quantity to 2
    dress_quantity_blue.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart_blue = wait.until(EC.element_to_be_clickable((By.NAME, 'Submit')))
    # Click on ADD TO CART button
    add_to_cart_blue.click()

    time.sleep(1)

    # Find CONTINUE SHOPPING button and wait for it to be clickable
    continue_shopping_blue = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span')))
    # Click on ADD TO CART button
    continue_shopping_blue.click()

    time.sleep(1)

    # Find YELLOW color and wait for it to be clickable
    yellow_color = wait.until(EC.element_to_be_clickable((By.NAME, 'Yellow')))
    # Click on BLACK color
    yellow_color.click()

    time.sleep(1)

    # Find QUANTITY and wait for it to be clickable
    dress_quantity_yellow = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quantity_wanted_p"]/a[1]')))
    # Click on - sign to decrease quantity to 1
    dress_quantity_yellow.click()
    time.sleep(1)
    dress_quantity_yellow.click()

    time.sleep(1)

    # Find SIZE dropdown and wait for it to be clickable
    size_dress_large = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="group_1"]/option[3]')))
    # Select the size L and click it
    size_dress_large.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart_yellow = wait.until(EC.element_to_be_clickable((By.NAME, 'Submit')))
    # Click on ADD TO CART button
    add_to_cart_yellow.click()

    time.sleep(1)

    # Find CONTINUE SHOPPING button and wait for it to be clickable
    continue_shopping_yellow = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span')))
    # Click on ADD TO CART button
    continue_shopping_yellow.click()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women.click()

    time.sleep(1)

    # Find ADD TO WISHLIST button and wait for it to be clickable
    add_to_wishlist = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[3]/div[1]/a')))
    # Click ADD TO WISHLIST button
    add_to_wishlist.click()
    # Now the popup will appear and say "Added to your wishlist", close it on "X" button
    popup_x = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="category"]/div[2]/div/div/a')))
    popup_x.click()

    time.sleep(1)

    # Find MORE button in Printed Summer Dress and wait for it to be clickable
    more_blouse_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div/div[3]/div/div[2]/a[2]')))
    # Click on dress
    more_blouse_button.click()

    time.sleep(1)

    # Find WRITE A REVIEW textbox and wait for it to be clickable
    write_a_review_blouse = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product_comments_block_extra"]/ul/li/a')))
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
    ok_button_review = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product"]/div[2]/div/div/div/p[2]/button')))
    # Click OK button
    ok_button_review.click()

    time.sleep(1)

    # Find WOMEN link in navbar and wait for it to be clickable
    women_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women_2.click()

    time.sleep(1)

    # Find MORE button on PRINTED CHIFFON DRESS and wait for it to be clickable
    chiffon_dress_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[7]/div/div/div[3]/div/div[2]/a[2]')))
    # Click on the image of the chiffon dress
    chiffon_dress_more.click()

    time.sleep(1)

    # Find QUANTITY and wait for it to be clickable
    chiffon_quantity = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]')))
    # Click on + sign two times to increase quantity to 3
    chiffon_quantity.click()
    time.sleep(1)
    chiffon_quantity.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart_chiffon = wait.until(EC.element_to_be_clickable((By.NAME, 'Submit')))
    # Click on ADD TO CART button
    add_to_cart_chiffon.click()

    time.sleep(1)

    # Find CONTINUE SHOPPING button and wait for it to be clickable
    continue_shopping_chiffon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span')))
    # Click on ADD TO CART button
    continue_shopping_chiffon.click()

    time.sleep(1)

    # Find green color and wait for it to be clickable
    green_color_chiffon = wait.until(EC.element_to_be_clickable((By.NAME, 'Green')))
    # Click on green color
    green_color_chiffon.click()

    time.sleep(1)

    # Find QUANTITY and wait for it to be clickable
    chiffon_quantity_green = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quantity_wanted_p"]/a[1]')))
    # Click on + sign two times to increase quantity to 3
    chiffon_quantity_green.click()
    time.sleep(1)
    chiffon_quantity_green.click()

    time.sleep(1)

    # Find SIZE dropdown and wait for it to be clickable
    size_dress_medium_chiffon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="group_1"]/option[2]')))
    # Select the size M and click it
    size_dress_medium_chiffon.click()

    time.sleep(1)

    # Find ADD TO CART button and wait for it to be clickable
    add_to_cart_chiffon_2 = wait.until(EC.element_to_be_clickable((By.NAME, 'Submit')))
    # Click on ADD TO CART button
    add_to_cart_chiffon_2.click()

    time.sleep(1)

    # Find CONTINUE SHOPPING button and wait for it to be clickable
    continue_shopping_chiffon_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span')))
    # Click on ADD TO CART button
    continue_shopping_chiffon_2.click()

    # Find WOMEN link in navbar and wait for it to be clickable
    women_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
    # Click on WOMEN in navbar
    women_3.click()


change_color()
