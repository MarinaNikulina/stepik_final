from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # добавление в корзину
    def add_to_basket(self):
        # название выбранного продукта и цена
        product_name = self.browser.find_element(* ProductPageLocators.PRODUCT).text
        product_cost = self.browser.find_element(* ProductPageLocators.PRODUCT_COST).text
        
        self.should_not_be_success_message()
        self.should_be_add_to_basket_button()
        self.press_basket_button()
        #self.solve_quiz_and_get_code()  # считаем секретное число при применении промокода
        self.should_be_alert_add_to_basket()
        self.should_be_alert_add_to_basket_product_name(product_name)
        self.should_be_alert_add_to_basket_product_cost(product_cost)
        print("basket_button test passed")
    # проверка наличия кнопки добавления в корзину    
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(* ProductPageLocators.TO_BASKET_BUTTON), "Basket_button is not presented"
    # нажатие кнопки добавления в корзину    
    def press_basket_button(self):
        basket_link = self.browser.find_element(* ProductPageLocators.TO_BASKET_BUTTON)
        basket_link.click()
        #print("кнопка нажата")
        
    # проверка  наличия сообщения, что товар добавлен в корзину    
    def should_be_alert_add_to_basket(self):
        WebDriverWait(self.browser, 4).until(
        EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE),'Timed out waiting for alert_add_to_basket')
        message = self.browser.find_element(* ProductPageLocators.SUCCESS_MESSAGE).text
        print(message)
        assert "has been added to your basket" in message, "Success_add_to_basket must be in alert message"
    
    # проверка, что в сообщении о добавлении есть имя продукта, и название соответствует выбранному продукту
    def should_be_alert_add_to_basket_product_name(self, pr_name):
        sendbox_product = self.browser.find_element(* ProductPageLocators.PRODUCT_MESSAGE).text
        assert pr_name == sendbox_product,"The products name must be in alert message"
     
    # проверка, что в сообщении о добавлении есть цена, равная цене выбранного продукта 
    def should_be_alert_add_to_basket_product_cost(self, pr_cost):
        sendbox_cost = self.browser.find_element(* ProductPageLocators.COST_MESSAGE).text
        assert pr_cost in sendbox_cost,"The products cost must be in alert message "
    
    # проверка, что нет сообщения, что товар добавлен в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
