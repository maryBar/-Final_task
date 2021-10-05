from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_an_item_to_the_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()

    def should_be_same_cart_and_page_item(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        cart_name = self.browser.find_element(*ProductPageLocators.CART_NAME).text
        print(product_name)
        print(cart_name)
        assert product_name == cart_name, "Names in cart and on page do not match"

    def should_be_same_cart_and_page_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        print(product_price)
        print(cart_price)
        assert product_price == cart_price, "Price in cart and on page do not match"




