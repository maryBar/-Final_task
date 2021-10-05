import time

import pytest

from .product_page import ProductPage
# from base_page import BasePage
import time


@pytest.mark.parametrize('links', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, links):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    page = ProductPage(browser, link)
    page.open()
    page.adding_an_item_to_the_cart()
    page.solve_quiz_and_get_code()
    page.should_be_same_cart_and_page_item()
    page.should_be_same_cart_and_page_price()




