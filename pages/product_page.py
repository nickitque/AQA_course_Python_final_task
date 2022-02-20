from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        """Метод, который будет проверять наличие кнопки <Добавить в корзину>."""
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Button <add to cart> is not presented"
        button_add_to_cart.click()

    def check_messages(self):
        """Метод, который будет проверять наличие сообщений о добавлении в корзину."""
        alert_message_success = (self.browser.find_element(*ProductPageLocators.ALERT_INNER_CART)).text
        alert_message_discount = (self.browser.find_element(*ProductPageLocators.ALERT_INNER_DISCOUNT)).text
        assert "был добавлен в вашу корзину" in alert_message_success
        assert "Ваша корзина удовлетворяет условиям предложения" in alert_message_discount
