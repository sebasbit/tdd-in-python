class Product:
    def __init__(self, price):
        self.price = price

    def total(self):
        return self.price + (self.price * 0.19)
