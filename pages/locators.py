
from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")
    ALERT_INNER_DISCOUNT = (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div")

class BasketPageLocators():
    CART_MESSAGE_EMPTY = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")