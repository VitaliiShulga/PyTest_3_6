import time
from selenium import webdriver
link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


def test_button_add_to_basket(browser):

    browser.get(link)
    time.sleep(10)
    #browser.fimd_element_by_xpath('//button [@value="Добавить в корзину"]')