from models import Product, Category

if __name__ == "__main__":
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Вывод списка товаров с использованием геттера
    print("Товары в категории:")
    print(category1.products)

    # Добавление нового продукта
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nТовары после добавления нового:")
    print(category1.products)

    # Работа с методом new_product()
    new_product = Product.new_product(
        {"name": "Sony PlayStation 5", "description": "Игровая консоль нового поколения", "price": 50000.0,
         "quantity": 10}
    )
    print("\nСозданный продукт:")
    print(f"{new_product.name}, {new_product.price} руб. Остаток: {new_product.quantity} шт.")

    # Тестирование работы сеттера для цены
    print("\nИзменение цены продукта:")
    print(f"Старая цена: {new_product.price}")
    new_product.price = 55000
    print(f"Новая цена: {new_product.price}")
    try:
        new_product.price = -100  # Ошибка!
    except ValueError as e:
        print(f"Ошибка: {e}")


