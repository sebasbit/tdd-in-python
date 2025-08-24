class Product:
    VAT = 0.19

    def __init__(self, price: "ProductPrice") -> None:
        self.price = price

    def total(self) -> float:
        return self.price.value + (self.price.value * self.VAT)


class ProductPrice:
    def __init__(self, value: float) -> None:
        self.value = value
        if self.value < 0:
            raise InvalidPriceError()


class InvalidPriceError(ValueError):
    pass
