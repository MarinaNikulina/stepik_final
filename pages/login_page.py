from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 

class LoginPage(BasePage):
        
    def should_be_login_page(self):
        #возможен переход к формам регистрации/входа
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url,"'Login' is not in current url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(* LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(* LoginPageLocators.REGISTER_FORM), "Register form is not presented "
        
    def register_pass_log_generate(self):
        # генерация логина & пароля
        email = str(time.time()) + "@fakemail.org"
        password = 'n1n2n3n4n5n6n7'
        return email, password
        
    def register_new_user(self, email, password):
        # заполнение формы регистрации пользователя
        email_field = self.browser.find_element(* LoginPageLocators.EMAIL_REGISTR)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(* LoginPageLocators.PASSWORD_REGISTR_1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(* LoginPageLocators.PASSWORD_REGISTR_2)
        password2_field.send_keys(password)
        # ввод данных после проверки, что кнопка SUBMIT активна
        WebDriverWait(self.browser, timeout = 4).until(EC.element_to_be_clickable(LoginPageLocators.SUBMIT_BUTTON))
        button = self.browser.find_element(* LoginPageLocators.SUBMIT_BUTTON)
        button.click()
        #print("Данные в форме, кнопка активна")
       
        
        