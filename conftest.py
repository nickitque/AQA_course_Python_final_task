import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Work with terminal for choosing language. The defaul lang is fr."""
    parser.addoption("--language", action="store", default="ru",
                     help="Choose language: ru or es or other")


"""Fixture for choosing lang."""


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    """Work with language in headers."""
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
