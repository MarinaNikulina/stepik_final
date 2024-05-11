from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):

# метод перехода на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(* MainPageLocators.LOGIN_LINK)
        login_link.click()
# метод  проверяет наличие ссылки логина      
    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(* MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
