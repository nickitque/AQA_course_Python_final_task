from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # def check_message_in_cart(self):
    #     empty_cart_message = (self.browser.find_element(*BasketPageLocators.CART_MESSAGE_EMPTY)).text
    #     assert "Ваша корзина пуста" in empty_cart_message
