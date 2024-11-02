import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import math
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_presense_of_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(10)
    try:
        browser.find_element(By.CSS_SELECTOR, ".bAtn-add-to-basket")
    except (NoSuchElementException):
        assert False, "There's no such button"