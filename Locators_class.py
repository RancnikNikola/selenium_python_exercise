from selenium.webdriver.common.by import By

class Locators:
    """Home page Locators"""
    # Sing in page button
    SIGN_IN_BUTTON = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    # Contact us page button
    CONTACT_US_BUTTON = (By.XPATH, '//*[@id="contact-link"]/a')

    """Sign in page Locators"""
    # Find Email address field
    EMAIL_FIELD = (By.NAME, 'email')
    # Find Password field
    PASSWORD_FIELD = (By.NAME, 'passwd')
    # Sign in button (Login)
    LOGIN_BUTTON = (By.NAME, 'SubmitLogin')
    # Forgot your password link
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="login_form"]/div/p[1]/a')
    # Create an account Email address field
    EMAIL_CREATE = (By.NAME, 'email_create')
    # Create an account button
    CREATE_BUTTON = (By.NAME, 'SubmitCreate')


Locators()




