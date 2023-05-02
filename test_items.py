import time
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_order_button_existence(browser):
    browser.get(link)
    result = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert EC.visibility_of(result), "Button isn't visible or missing"
    print('Result is ', result.text)
    time.sleep(30)
