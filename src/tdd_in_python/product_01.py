class Product:
    VAT = 0.19

    def __init__(self, price):
        self.price = price

    def total(self):
        return self.price + (self.price * self.VAT)


class InvalidPriceError(ValueError):
    pass
