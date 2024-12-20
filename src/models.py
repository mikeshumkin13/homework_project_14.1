class Product:
    """Класс продукта магазина."""
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для атрибута 'price'."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для атрибута 'price'."""
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс категории товаров."""
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products else []  # Приватный атрибут

    @property
    def products(self):
        """Геттер для приватного атрибута 'products'."""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self._products
        )

    def add_product(self, product):
        """Добавление продукта в категорию."""
        if isinstance(product, Product):
            self._products.append(product)
            Category.product_count += 1

    @classmethod
    def new_product(cls, product_dict):
        """Создание нового продукта из словаря."""
        return Product(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"]
        )
