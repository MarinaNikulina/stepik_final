from selenium.webdriver.common.by import By

class BasePageLocators():
    BODY = (By.CSS_SELECTOR, "body")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTR = (By.ID, "id_registration-email")
    PASSWORD_REGISTR_1 = (By.ID, "id_registration-password1")
    PASSWORD_REGISTR_2 = (By.ID, "id_registration-password2")
    SUBMIT_BUTTON= (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_COST =  (By.CSS_SELECTOR, ".product_main > p.price_color")
    SENDBOX = (By.CSS_SELECTOR, "#messages")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div') 

