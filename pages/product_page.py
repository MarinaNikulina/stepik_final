from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import ProductPageLocators
#import time

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
        
    def should_be_add_to_basket_button(self):
        # проверка наличия кнопки добавления в корзину
        assert self.is_element_present(* ProductPageLocators.BASKET_BUTTON), "Basket_button is not presented"
        
    def press_basket_button(self):
        basket_link = self.browser.find_element(* ProductPageLocators.BASKET_BUTTON)
        basket_link.click()
        #print("кнопка нажата")
        
    def should_be_alert_add_to_basket(self):
        # проверка  наличия сообщения, что товар добавлен в корзину
        WebDriverWait(self.browser, 4).until(
        EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE),'Timed out waiting for alert_add_to_basket')
        message = self.browser.find_element(* ProductPageLocators.SUCCESS_MESSAGE).text
        print(message)
        assert "has been added to your basket" in message, "Success_add_to_basket must be in alert message"

    def should_be_alert_add_to_basket_product_name(self, pr_name):
        # проверка, что в сообщении о добавлении есть имя продукта, и название соответствует выбранному продукту
        sendbox_product = self.browser.find_element(* ProductPageLocators.PRODUCT_MESSAGE).text
        assert pr_name == sendbox_product,"The products name must be in alert message"
        
    def should_be_alert_add_to_basket_product_cost(self, pr_cost):
        # проверка, что в сообщении о добавлении есть цена, равная цене выбранного продукта
        sendbox_cost = self.browser.find_element(* ProductPageLocators.COST_MESSAGE).text
        assert pr_cost in sendbox_cost,"The products cost must be in alert message"
        
    def should_not_be_success_message(self):
        # проверка, что нет сообщения, что товар добавлен в корзину
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
