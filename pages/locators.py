from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div .col-sm-6 h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div .col-sm-6 p.price_color")
    CART_NAME = (By.CSS_SELECTOR, "div .alert-success strong")
    CART_PRICE = (By.CSS_SELECTOR, "div .alert-info strong")


