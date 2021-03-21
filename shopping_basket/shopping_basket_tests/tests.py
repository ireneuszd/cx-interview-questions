from sequences import Basket

from decimal import Decimal
import unittest


class TestBasket(unittest.TestCase):
    def TC01_add_each_product_and_check_price(self):
        catalogue = {
            'Baked Beans': 99,
            'Biscuits': 120,
            'Sardines': 189,
            'Shampoo(small)': 200,
            'Shampoo(medium)': 250,
            'Shampoo(large)': 350
        }
        offers = {
            'Baked Beans': [{'amount': 2, 'discount': lambda price: round(price / 3)},
                            {'amount': 1, 'discount': lambda price: round(price * 0.2)}],
            'Sardines': [{'amount': 1, 'discount': lambda price: 30}],
            'Shampoo (small)': []
        }
        products = [product for product in catalogue]
        subtotal_price = 1208
        discount_price = 50
        total_price = 1158

        test_basket = Basket('TC01_basket', catalogue, offers)
        test_basket.set_products(products)
        self.assertEqual(subtotal_price, test_basket.subtotal, "subtotal_price is not proper")
        self.assertEqual(discount_price, test_basket.discount, "discount_price is not proper")
        self.assertEqual(total_price, test_basket.total, "total_price is not proper")


a = TestBasket()
a.TC01_add_each_product_and_check_price()
