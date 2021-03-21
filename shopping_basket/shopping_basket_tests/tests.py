from sequences import Basket

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
        subtotal_price = 12.08
        discount_price = 0.50
        total_price = 11.58

        test_basket = Basket('TC01_basket', catalogue, offers)
        test_basket.set_products(products)
        prices = test_basket.get_basket_prices()

        self.assertEqual(subtotal_price, prices[0], "subtotal_price is not proper")
        self.assertEqual(discount_price, prices[1], "discount_price is not proper")
        self.assertEqual(total_price, prices[2], "total_price is not proper")

    def TC02_empty_product(self):
        catalogue = {
            'Baked Beans': 99,
            'Biscuits': 120,
        }
        offers = {
            'Sardines': [{'amount': 1, 'discount': lambda price: 30}],
            'Shampoo (small)': []
        }
        products = [product for product in catalogue]
        test_basket = Basket('TC02_basket', catalogue, offers)
        test_basket.set_products(products)
        test_basket.set_products([])

        prices = test_basket.get_basket_prices()

        self.assertEqual(0, prices[0], "subtotal_price is not proper")
        self.assertEqual(0, prices[1], "discount_price is not proper")
        self.assertEqual(0, prices[2], "total_price is not proper")

    def TC03_six_for_a_price_of_four(self):
        catalogue = {
            'Baked Beans': 99,
            'Biscuits': 120,
        }
        offers = {
            'Baked Beans': [{'amount': 3, 'discount': lambda price: price},
                            {'amount': 1, 'discount': lambda price: round(price * 0.2)}]
        }
        products = ['Baked Beans'] * 6
        test_basket = Basket('TC03_basket', catalogue, offers)
        test_basket.set_products(products)

        prices = test_basket.get_basket_prices()

        self.assertEqual(5.94, prices[0], "subtotal_price is not proper")
        self.assertEqual(1.98, prices[1], "discount_price is not proper")
        self.assertEqual(3.96, prices[2], "total_price is not proper")
