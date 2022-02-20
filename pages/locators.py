
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ALERT_INNER_CART = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")
    ALERT_INNER_DISCOUNT = (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div")