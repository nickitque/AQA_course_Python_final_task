import time

from pages.main_page import MainPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_open_product_page(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_messages()
