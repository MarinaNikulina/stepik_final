import pytest
from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
import time


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
    
   

@pytest.mark.guest_add_to_basket                               
class TestGuestAddToBasketFromProductPage():
    @pytest.mark.xfail    
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser,link1):
        page = ProductPage(browser, link1)   
        page.open()
        page.press_basket_button()
        page.should_not_be_success_message()
        
    def test_guest_can_add_product_to_basket(self, browser,link1):
        page = ProductPage(browser, link1)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         
        page.add_to_basket()                 # добавляем товар в корзину   


    
@pytest.mark.user_add_to_basket                               
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(autouse=True)
    def setup(request, browser, link_main):
        page = MainPage(browser, link_main)     # инициализация Page Object, передача в конструктор экземпляра драйвера и url адреса 
        page.open()                             # открываем страницу
        #time.sleep(5)
        page.go_to_login_page()                 # выполняем метод страницы — переходим на страницу логина
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
        
    def test_user_can_add_product_to_basket(self, browser, link1):
        page = ProductPage(browser, link1)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         
        page.add_to_basket()                # добавляем товар в корзину           
  
#--- test_user_can_add_product_to_basket
#--- test_guest_can_add_product_to_basket
# test_guest_cant_see_product_in_basket_opened_from_product_page
# test_guest_can_go_to_login_page_from_product_page
# Отмаркируйте эти тесты меткой:
# @pytest.mark.need_review
# Не забудьте зарегистрировать метку, чтобы избежать предупреждений: Как же регистрировать метки?
# Убедитесь, что при запуске с помощью следующей команды тесты запускаются и успешно проходят: 

    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


