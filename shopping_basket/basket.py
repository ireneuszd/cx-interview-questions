class CatalogueException(Exception):
    """Exception raised for errors in the Catalogue"""
    def __init__(self, message):
        super().__init__(message)


class BasketException(Exception):
    """Exception raised for errors in the Basket"""
    def __init__(self, message):
        super().__init__(message)


class Basket:
    def __init__(self, name, catalogue, offers):
        self.__name = name
        self.__products = []
        self.__products_distinct = {}
        self.subtotal = 0
        self.discount = 0
        self.total = 0
        self.offers = offers
        self.catalogue = catalogue

    def get_basket_prices(self, pennies=False):
        """Returns subtotal, discount and total prices in given order

        :param pennies: True if price should be return in pennies
        :type pennies: bool
        :returns tuple of prices
        :return type: tuple
        """
        divider = 1 if pennies else 100
        return (self.subtotal / divider,
                self.discount / divider,
                self.total / divider)

    def set_products(self, products):
        """Sets products for the basket

        :param products: list of products
        :type products: list
        """
        self.__products.clear()
        self.__products_distinct.clear()

        for product in products:
            self.check_if_product_in_catalogue(product)
            self.__products.append(product)

        self.count_basket()

    def count_basket(self):
        """Counts subtotal and total prices for basket"""
        self.subtotal = self.discount = self.total = 0

        for product in self.__products:
            self.subtotal += self.get_price(product)
            if product not in self.__products_distinct:
                self.__products_distinct[product] = 1
            else:
                self.__products_distinct[product] += 1

        self.count_discount()
        self.total = self.subtotal - self.discount

    def count_discount(self):
        """Counts total discount based on basket content"""
        for product in self.__products_distinct:
            tmp_amount = self.__products_distinct[product]
            if product in self.offers:
                price = self.get_price(product)
                for offer in self.offers[product]:
                    while tmp_amount >= offer['amount']:
                        self.discount += round(offer['discount'](price))
                        tmp_amount -= offer['amount']

    def get_price(self, product):
        """Gets price for given product

        :param product: product name (must exists in product list)
        :type product: string
        :returns: product subtotal price
        """
        return self.catalogue[product]

    def check_if_product_in_catalogue(self, product):
        """Checks if given product exists in catalogue

        :param product: product name (must exists in product list)
        :type product: string
        :raises CatalogueException: if product does not exist in catalogue
        """
        if product not in self.catalogue.keys():
            raise CatalogueException(f"{product} not in Catalogue")
