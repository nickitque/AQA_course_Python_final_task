
class BasePage():
    """В конструктор в качестве параметров мы передаем экземпляр драйвера и url адрес."""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    """Метод Open должен открывать нужную страницу в браузере, используя метод get()."""
    def open(self, browser):
        self.browser.get(self.url)
