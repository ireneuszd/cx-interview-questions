## Documentation

Assumptions that have been made:
1) I assume that catalogue is stored as a dictionary with product name as a key, and product price as a value. That can be easily changed in future.
   Example of catalogue:
   catalogue = {
    'Baked Beans': 0.99,
    'Biscuits': 1.20
   }
2) I assume that offers are stored in dictionary of lists, where:
    - keys are product names
    - lists are containing dictionaries which corresponds to a particular offer
    - particular offer dictionary has 2 items:
      - 'amount' - describes how many product are needed for the discount
      - 'discount' - describes the offer as a lambda function 
           discount should be described related to price of 1 product. Examples:
              "buy 2, get 1 free" -- lambda price: price
              "buy 2, get second for half price" -- lambda price: Decimal(0.5) * price
              "buy 2, get discount -30 pennies for each" -- lambda price: 2 * Decimal(0.30)          
    Example of offers:
    offers = {
        'Baked Beans': [{'amount': 2, 'discount': lambda price: price / Decimal(3)},
                        {'amount': 1, 'discount': lambda price: price * Decimal(0.2)}],
        'Sardines': [{'amount': 1, 'discount': lambda price: Decimal(0.3)}]
    }
3) I assume that two or more offers can not be combined on the same product 
