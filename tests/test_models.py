import pytest
from src.models import Product, Category


def test_product_initialization():
    """Проверяет корректность инициализации объекта Product."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization():
    """Проверяет корректность инициализации объекта Category."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Категория для смартфонов", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Категория для смартфонов"
    assert len(category.products) == 2


def test_category_and_product_counts():
    """Проверяет корректность подсчета количества продуктов."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Категория для смартфонов", [product1, product2])

    assert len(category.products) == 2  # Теперь проверяем длину списка


def test_add_product():
    """Проверяет добавление продукта в категорию."""
    category = Category("Телевизоры", "Категория для телевизоров")
    product = Product("Samsung QLED 55", "55\" 4K UHD", 123000.0, 7)

    category.add_product(product)

    assert product in category.products  # Проверяем, что продукт добавлен


def test_price_setter():
    """Проверяет корректность работы сеттера цены."""
    product = Product("Test Product", "Test Description", 100.0, 10)

    product.price = 200.0
    assert product.price == 200.0

    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        product.price = -50


def test_new_product():
    """Проверяет создание нового продукта через метод new_product."""
    product_dict = {
        "name": "Sony Xperia",
        "description": "Compact phone",
        "price": 70000.0,
        "quantity": 15
    }
    new_product = Product.new_product(product_dict)

    assert isinstance(new_product, Product)
    assert new_product.name == "Sony Xperia"
    assert new_product.description == "Compact phone"
    assert new_product.price == 70000.0
    assert new_product.quantity == 15


def test_product_str():
    """Тест строкового представления Product."""
    product = Product("iPhone 15", "512GB, Gray", 210000, 8)
    assert str(product) == "iPhone 15, 210000 руб. Остаток: 8 шт."


def test_category_str():
    """Тест строкового представления Category."""
    category = Category("Ноутбуки", "Категория для ноутбуков")
    assert str(category) == "Ноутбуки, количество продуктов: 0 шт."
