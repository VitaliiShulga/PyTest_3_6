import time

def test_button_add_to_basket_on_screan(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert button, 'button "add to basket" not found on page'
