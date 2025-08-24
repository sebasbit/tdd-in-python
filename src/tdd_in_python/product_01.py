class Product:
    VAT = 0.19

    def __init__(self, price):
        self.price = price
        if self.price < 0:
            raise InvalidPriceError()

    def total(self):
        return self.price + (self.price * self.VAT)


class InvalidPriceError(ValueError):
    pass
