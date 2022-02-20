from selenium.common.exceptions import NoSuchElementException


class BasePage():
    """В конструктор в качестве параметров мы передаем экземпляр драйвера и url адрес."""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    """Метод Open должен открывать нужную страницу в браузере, используя метод get()."""
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
