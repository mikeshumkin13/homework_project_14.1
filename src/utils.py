import json
from src.models import Product, Category


def load_data_from_json(filepath):
    """
    Загружает данные из JSON-файла и создает объекты категорий и продуктов.
    """
    categories = []
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for category_data in data:
            # Создаем продукты для текущей категории
            products = [
                Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
                for prod in category_data["products"]
            ]
            # Создаем категорию с продуктами
            category = Category(category_data["name"], category_data["description"], products)
            categories.append(category)

    return categories

