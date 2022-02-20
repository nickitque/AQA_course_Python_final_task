# import time
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#
#
# def test_find_basket_button(browser):
#     browser.get(url)
#     basket_button = browser.find_elements_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
#     """
#     !!!!!!! the examiner has himself add time.sleep !!!!!!!
#     """
#     #time.sleep(15)
#     assert basket_button, "There is no element of basket button"
