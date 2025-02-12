class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для обновления цены с проверкой на положительное значение."""
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_dict):
        """Класс-метод для создания нового продукта из словаря."""
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"]
        )

class Category:
    product_count = 0  # Класс-атрибут для подсчета количества продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products  # Приватный атрибут для списка продуктов
        Category.product_count = len(products)  # Инициализация счетчика продуктов

    def add_product(self, product):
        """Метод для добавления нового продукта в категорию."""
        if isinstance(product, Product):  # Проверяем, что добавляем именно продукт
            self._products.append(product)  # Добавляем продукт в список
            Category.product_count += 1  # Увеличиваем счетчик продуктов
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Геттер для получения списка продуктов в категории в нужном формате."""
        return "\n".join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products])