import pytest
#from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

    #link_main = "http://selenium1py.pythonanywhere.com/"
    #link_basket = "http://selenium1py.pythonanywhere.com/en-gb/basket/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # гость может перейти к формам регистрации/входа
    def test_guest_can_go_to_login_page(self, browser, main_page):
        main_page.go_to_login_page()          #  переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
    # гость видит ссылку на страницу регистрации  
    def test_guest_should_see_login_link(self, browser, main_page):
        main_page.should_be_login_link() 
        
class TestBasketFromMainPage():
    # при открытии корзины из главной гость не видит в ней товары
    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, main_page):
        main_page.go_to_basket_page()          #  переходим в корзину
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.is_message_basket_empty_about()
        
    