class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Цена не может быть отрицательной или нулевой")

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
