import pytest
from src.models import Product, Category, Smartphone, LawnGrass, BaseProduct, LoggingMixin, ZeroQuantityError


# ------------------------ ТЕСТИРОВАНИЕ PRODUCT ------------------------

def test_product_initialization():
    """Проверяет корректность инициализации объекта Product."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str():
    """Тест строкового представления Product."""
    product = Product("iPhone 15", "512GB, Gray", 210000, 8)
    assert str(product) == "iPhone 15, 210000 руб. Остаток: 8 шт."


def test_price_setter():
    """Проверяет корректность работы сеттера цены."""
    product = Product("Test Product", "Test Description", 100.0, 10)

    product.price = 200.0
    assert product.price == 200.0

    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        product.price = -50


def test_product_zero_quantity():
    """Проверяет, что нельзя создать продукт с нулевым количеством."""
    with pytest.raises(ZeroQuantityError, match="Ошибка: Нельзя добавить товар с нулевым количеством."):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


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


# ------------------------ ТЕСТИРОВАНИЕ CATEGORY ------------------------

def test_category_initialization():
    """Проверяет корректность инициализации объекта Category."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Категория для смартфонов", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Категория для смартфонов"
    assert len(category.products) == 2


def test_add_product():
    """Проверяет добавление продукта в категорию."""
    category = Category("Телевизоры", "Категория для телевизоров")
    product = Product("Samsung QLED 55", "55\" 4K UHD", 123000.0, 7)

    category.add_product(product)
    assert product in category.products


def test_middle_price():
    """Тест на подсчет средней цены в категории."""
    product1 = Product("Товар1", "Описание1", 1000.0, 5)
    product2 = Product("Товар2", "Описание2", 2000.0, 3)
    category = Category("Категория", "Тестовая", [product1, product2])

    assert category.middle_price() == 1500.0


def test_middle_price_empty_category():
    """Тест на случай, когда в категории нет товаров."""
    category = Category("Пустая категория", "Без товаров", [])
    assert category.middle_price() == 0


# ------------------------ ТЕСТИРОВАНИЕ ИСКЛЮЧЕНИЙ ------------------------

def test_add_product_only_valid_types():
    """Тест на запрет добавления объектов, не являющихся Product."""
    category = Category("Смартфоны", "Описание")
    smartphone = Smartphone("Samsung S23", "256GB", 180000, 5, 95.5, "S23 Ultra", 256, "Серый")

    category.add_product(smartphone)

    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_add_product_zero_quantity():
    """Тест на попытку добавления товара с нулевым количеством в категорию."""
    category = Category("Электроника", "Категория для электроники")
    with pytest.raises(ZeroQuantityError, match="Ошибка: Нельзя добавить товар с нулевым количеством."):
        category.add_product(Product("Товар", "Описание", 1500.0, 0))


def test_addition_of_same_type():
    """Тест сложения объектов одного типа."""
    smartphone1 = Smartphone("Samsung S23", "256GB", 180000, 5, 95.5, "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("iPhone 15", "512GB", 210000, 8, 98.2, "15", 512, "Gray space")
    assert smartphone1 + smartphone2 == (180000 * 5) + (210000 * 8)


def test_addition_of_different_types():
    """Тест невозможности сложения товаров разных типов."""
    smartphone = Smartphone("Samsung S23", "256GB", 180000, 5, 95.5, "S23 Ultra", 256, "Серый")
    grass = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        smartphone + grass


# ------------------------ ТЕСТИРОВАНИЕ МИКСИНОВ ------------------------

def test_logging_mixin(capsys):
    """Тест миксина LoggingMixin."""

    class TestClass(LoggingMixin, BaseProduct):
        def __init__(self, name, description, price, quantity):
            super().__init__(name, description, price, quantity)

        def __str__(self):
            return "Тестовый продукт"

    obj = TestClass("Товар", "Описание", 1000, 10)
    captured = capsys.readouterr()
    assert "Создан объект TestClass с параметрами" in captured.out


def test_category_counts():
    """Тест счетчиков категорий и продуктов."""
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Смартфоны", "Категория смартфонов", [
        Product("Samsung", "256GB", 1000, 2),
        Product("iPhone", "512GB", 2000, 3)
    ])
    category2 = Category("Телевизоры", "Категория телевизоров", [
        Product("LG OLED", "4K UHD", 120000, 4)
    ])

    assert Category.category_count == 2
    assert Category.product_count == 3  # В сумме 3 продукта
