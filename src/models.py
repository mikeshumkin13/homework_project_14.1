class Product:
    """Класс, представляющий продукт для приложения."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, представляющий категорию продуктов для приложения."""

    category_count = 0  # Атрибут класса для подсчета категорий
    product_count = 0   # Атрибут класса для подсчета продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    @classmethod
    def increment_counts(cls, products):
        """Увеличивает счетчики категорий и продуктов."""
        cls.category_count += 1
        cls.product_count += len(products)

