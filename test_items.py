import time

def test_button_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector('.bt-add-to-basket')
    assert button, 'button "add to basket" not found on page'
