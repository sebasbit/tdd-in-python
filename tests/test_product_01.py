import pytest

from tdd_in_python import InvalidPriceError
from tdd_in_python import Product
from tdd_in_python import ProductPrice


@pytest.mark.parametrize(
    "price,total", [(0, 0), (10_000, 11_900), (1_423_500, 1_693_965)]
)
def test_product_price(price, total):
    product = Product(ProductPrice(price))
    assert product.total() == total


def test_product_price_cannot_be_negative():
    with pytest.raises(InvalidPriceError):
        Product(ProductPrice(-1))
