class Product:
    VAT = 0.19

    def __init__(self, price):
        self.price = price

    def total(self):
        return self.price.value + (self.price.value * self.VAT)


class ProductPrice:
    def __init__(self, value):
        self.value = value
        if self.value < 0:
            raise InvalidPriceError()


class InvalidPriceError(ValueError):
    pass
