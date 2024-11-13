import pytest
from src.models import Product, Category

def test_product_initialization(product1):
    """Проверяет корректность инициализации объекта Product."""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

def test_category_initialization(category1):
    """Проверяет корректность инициализации объекта Category."""
    assert category1.name == "Смартфоны"
    assert category1.description == "Категория для смартфонов"
    assert len(category1.products) == 3

def test_category_and_product_counts():
    """Проверяет корректность подсчета количества категорий и продуктов."""
    # Сброс счетчиков перед тестом
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category("Смартфоны", "Категория для смартфонов", [product1, product2])

    # Увеличиваем счетчики вручную
    Category.increment_counts(category1.products)

    assert Category.category_count == 1
    assert Category.product_count == 2

