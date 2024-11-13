import pytest
from src.utils import load_data_from_json
from src.models import Category

def test_load_data_from_json():
    """Проверяет загрузку данных из JSON и создание объектов категорий и продуктов."""
    # Сброс глобальных счетчиков перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем данные из тестового JSON файла
    categories = load_data_from_json('products.json')

    # Увеличиваем счетчики вручную после загрузки
    for category in categories:
        Category.increment_counts(category.products)

    # Проверяем количество загруженных категорий и продуктов
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1

    # Проверяем глобальные счетчики
    assert Category.category_count == 2
    assert Category.product_count == 4


