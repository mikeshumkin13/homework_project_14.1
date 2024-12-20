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
    assert len(category1._products) == 3  # Прямой доступ к приватному атрибуту


def test_category_and_product_counts():
    """Проверяет корректность подсчета количества категорий и продуктов."""
    # Сброс счетчиков перед тестом
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category("Смартфоны", "Категория для смартфонов", [product1, product2])

    assert Category.product_count == 2


def test_add_product():
    """Проверяет добавление продукта в категорию и увеличение счетчика."""
    category = Category("Телевизоры", "Категория для телевизоров")
    product = Product("Samsung QLED 55", "55\" 4K UHD", 123000.0, 7)

    initial_count = Category.product_count
    category.add_product(product)

    assert product in category._products  # Проверяем добавление в список
    assert Category.product_count == initial_count + 1


def test_products_getter():
    """Проверяет работу геттера для списка продуктов."""
    category = Category("Телевизоры", "Категория для телевизоров")
    product1 = Product("Samsung QLED 55", "55\" 4K UHD", 123000.0, 7)
    product2 = Product("LG OLED 65", "65\" 4K HDR", 210000.0, 5)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = (
        "Samsung QLED 55, 123000.0 руб. Остаток: 7 шт.\n"
        "LG OLED 65, 210000.0 руб. Остаток: 5 шт."
    )
    assert category.products == expected_output


def test_price_setter():
    """Проверяет корректность работы сеттера цены."""
    product = Product("Test Product", "Test Description", 100.0, 10)

    product.price = 200.0
    assert product.price == 200.0

    product.price = -50
    assert product.price == 200.0  # Цена не должна измениться

    product.price = 0
    assert product.price == 200.0  # Цена не должна измениться


def test_new_product():
    """Проверяет создание нового продукта через метод new_product."""
    product_dict = {
        "name": "Sony Xperia",
        "description": "Compact phone",
        "price": 70000.0,
        "quantity": 15
    }
    new_product = Category.new_product(product_dict)

    assert isinstance(new_product, Product)
    assert new_product.name == "Sony Xperia"
    assert new_product.description == "Compact phone"
    assert new_product.price == 70000.0
    assert new_product.quantity == 15
