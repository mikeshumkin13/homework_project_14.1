class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены"""
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.__price = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self._quantity = value
        else:
            print("Количество не может быть отрицательным")

    def __str__(self):
        return self.name


class Category:
    product_count = 0  # Переменная для отслеживания общего количества продуктов

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products or []
        Category.product_count += len(self.products)  # Увеличиваем счетчик продуктов

    def add_product(self, product):
        if not isinstance(product, Product):  # Проверяем, что product - это экземпляр Product или его наследника
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик при добавлении продукта

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self._products = value
        else:
            raise ValueError("Products must be a list")

    @staticmethod
    def new_product(product_dict):
        """Создает новый продукт на основе данных из словаря."""
        return Product(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"]
        )
