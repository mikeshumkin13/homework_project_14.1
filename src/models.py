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
            raise ValueError("Количество не может быть отрицательным")

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение стоимости товаров"""
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Складывать можно только объекты класса Product")

    @classmethod
    def new_product(cls, product_dict):
        """Создает новый продукт на основе данных из словаря."""
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"]
        )


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products or []

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.products.append(product)

    @property
    def products(self):
        return self._products


    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self._products = value
        else:
            raise ValueError("Products must be a list")

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
