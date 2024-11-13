import pytest
from src.models import Product, Category

@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

@pytest.fixture
def category1(product1, product2, product3):
    return Category("Смартфоны", "Категория для смартфонов", [product1, product2, product3])