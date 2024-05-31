from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        # проверка на корректный url адрес
        assert 'basket' in self.browser.current_url,"'Basket' is not in current url"
        
    def is_basket_empty(self):
        # проверка, что корзина  пуста
        assert self.is_not_element_present(* BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
        
    def is_message_basket_empty_about(self):
        # проверка, что есть сообщение о пустой корзине
        WebDriverWait(self.browser, 4).until(
        EC.visibility_of_element_located(BasketPageLocators.EMPTY_MESSAGE),'Timed out waiting for empty_basket')
        message = self.browser.find_element(* BasketPageLocators.EMPTY_MESSAGE).text
        print(message)
        assert "empty" in message, "Empty basket must be in alert message"
        
        