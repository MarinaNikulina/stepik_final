from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators

import math
import time

class BasePage():
    def __init__(self, browser, url, ):
        self.browser = browser
        self.url = url
  
    def open(self, timeout=4):
        self.browser.get(self.url)
        WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(BasePageLocators.BODY))
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
        
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
        
    def is_in(self,subStr,fullStr):
        if subStr in fullStr:
            return True
        else:
            return False
            
    #обработка капчи        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            
    # пользователь дб авторизован 
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
    # переход на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(* BasePageLocators.LOGIN_LINK)
        login_link.click()
        
    # проверка наличия ссылки на логин      
    def should_be_login_link(self):
        assert self.is_element_present(* BasePageLocators.LOGIN_LINK), "Login link is not presented"                                                             
                                                                 
    # переход в корзину        
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(* BasePageLocators.BASKET_LINK)
        basket_link.click()
        
    # проверка наличия ссылки на корзину      
    def should_be_basket_link(self):
        assert self.is_element_present(* BasePageLocators.BASKET_LINK), "Basket link is not presented"        

        
                                                           