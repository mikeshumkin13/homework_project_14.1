from models import Product, Category

if __name__ == "__main__":
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1)
    print(product2)
    print(product3)

    # Создание категории
    category1 = Category("Смартфоны", "Описание", [product1, product2, product3])
    print(category1)

    # Сложение продуктов
    print(f"Суммарная стоимость товаров 1 и 2: {product1 + product2} руб.")
    print(f"Суммарная стоимость товаров 2 и 3: {product2 + product3} руб.")

    # Добавление нового продукта
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nПосле добавления нового товара:")
    print(category1)

    # Создание нового продукта через класс-метод
    new_product = Product.new_product(
        {"name": "Sony PlayStation 5", "description": "Игровая консоль нового поколения", "price": 50000.0, "quantity": 10}
    )
    print("\nСозданный продукт:", new_product)

    # Тест сеттера цены
    print(f"\nИзменение цены: Старая: {new_product.price}")
    new_product.price = 55000
    print(f"Новая: {new_product.price}")

    try:
        new_product.price = -100  # Ошибка!
    except ValueError as e:
        print(f"Ошибка: {e}")
