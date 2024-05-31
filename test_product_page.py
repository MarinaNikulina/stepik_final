import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   # # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   # # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   # # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   # # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   # # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   # # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                   # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.fixture(scope = "class")
def link1(request):
    return  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    # "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    
@pytest.fixture()
def prod_page(request, browser, link1):
    page = ProductPage(browser, link1)   
    page.open()
    return page    

@pytest.mark.guest_add_to_basket                               
class TestGuestAddToBasketFromProductPage():
    @pytest.mark.xfail    
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, prod_page):
        prod_page.press_basket_button()
        prod_page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, prod_page):
        prod_page.add_to_basket()                 # добавляем товар в корзину
        
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, prod_page):
        prod_page.press_basket_button()
        assert prod_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is disappeared, but should not be"        

@pytest.mark.user_add_to_basket                               
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(autouse=True)
    def setup(request, browser, link_main):
        page = MainPage(browser, link_main)     # инициализация Page Object, передача в конструктор экземпляра драйвера и url адреса 
        page.open()                             # открываем страницу
        page.go_to_login_page()                 # переход на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        users_data = login_page.register_pass_log_generate()    # генерация логина и пароля
        login_page.register_new_user(* users_data)    # регистрация нового пользователя
        login_page.should_be_authorized_user()        # проверка, что пользователь залогинен 
        
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser, link1):
        page = ProductPage(browser, link1)   
        page.open()
        page.press_basket_button()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser, link1):
        page = ProductPage(browser, link1)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         
        page.add_to_basket()                # добавляем товар в корзину
        
@pytest.mark.from_product_page        
class TestSeeAndDoFromProductPage():
    # гость видит ссылку на страницу регистрации
    def test_guest_should_see_login_link_on_product_page(self, prod_page):
        prod_page.should_be_login_link()
    
    # гость может перейти на страницу регистрации
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, prod_page):
        prod_page.go_to_login_page()
        
    # гость видит ссылку на корзину
    def test_guest_should_see_basket_link_on_product_page(self, prod_page ):
        prod_page.should_be_basket_link()
        
    # гость может перейти в корзину
    def test_guest_can_go_to_basket_page_from_product_page(self, prod_page ):
        prod_page.go_to_basket_page()
     
    # при открытии корзины из продукта гость не видит в ней товары
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, prod_page ):
        prod_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.is_message_basket_empty_about()
    
