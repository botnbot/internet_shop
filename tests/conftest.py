import pytest

from src.category import Category
from src.product import Product

@pytest.fixture
def first_category():
    return Category(
        name='Mobile Phones',
        description='cool',
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name='TV',
        description='very cool',
        products=[
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7),
        ]
    )

@pytest.fixture
def product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)