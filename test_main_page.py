import pytest

from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com"


@pytest.mark.xfail
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Гость открывает главную страницу. Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров. Ожидаем, что есть текст о том что корзина пуста """
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    page.check_message_in_cart()
