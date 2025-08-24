from tdd_in_python import Product


def test_product_price():
    product = Product(10_000)
    assert product.total() == 11_900
