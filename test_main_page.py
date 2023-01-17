from .Pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    browser.get(link)
    page.open()
    page.go_to_login_page()