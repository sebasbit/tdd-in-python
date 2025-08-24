import pytest

from tdd_in_python import Product


@pytest.mark.parametrize(
    "price,total", [(10_000, 11_900), (2_000, 2_380), (1_423_500, 1_693_965)]
)
def test_product_price(price, total):
    product = Product(price)
    assert product.total() == total
