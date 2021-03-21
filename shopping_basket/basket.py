

class CatalogueException(Exception):
    """Exception raised for errors in the catalogue"""
    def __init__(self, product):
        self.message = f"Product: '{product}' does not exist in catalogue"
        super().__init__(self.message)


class Basket:
    def __init__(self, name, catalogue, offers):
        self.__name = name
        self.__products = []
        self.subtotal = 0
        self.discount = 0
        self.total = 0
        self.products_distinct = {}
        self.offers = offers
        self.catalogue = catalogue

    def get_basket_prices(self):
        """Returns subtotal, discount and total prices in given order

        :returns tuple of prices
        :return type: tuple
        """
        return self.subtotal, self.discount, self.total

    def set_products(self, products):
        """Sets products for the basket

        :param products: list of products
        :type products: list
        """
        self.__products.clear()
        for product in products:
            self.check_if_product_in_catalogue(product)
            self.__products.append(product)

        self.count_basket()

    def count_basket(self):
        """Counts subtotal and total prices for basket"""
        self.subtotal = self.discount = self.total = 0

        for product in self.__products:
            self.subtotal += self.get_price(product)
            if product not in self.products_distinct:
                self.products_distinct[product] = 1
            else:
                self.products_distinct[product] += 1

        self.count_discount()
        self.total = self.subtotal - self.discount

    def count_discount(self):
        """Counts total discount based on basket content"""
        for product in self.products_distinct:
            tmp_amount = self.products_distinct[product]
            if product in self.offers:
                price = self.get_price(product)
                for offer in self.offers[product]:
                    while tmp_amount >= offer['amount']:
                        self.discount += round(offer['discount'](price))
                        print(self.discount)
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
            raise CatalogueException(product)


