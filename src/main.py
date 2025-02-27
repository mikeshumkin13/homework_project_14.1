from models import Product, Category, ZeroQuantityError

if __name__ == '__main__':
    # Проверка обработки исключения при создании продукта с нулевым количеством
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ZeroQuantityError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print("Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    # Создание нескольких товаров
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории и добавление в неё товаров
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    # Вычисление средней цены в категории
    print(f"Средний ценник в категории '{category1.name}': {category1.middle_price()} руб.")

    # Создание пустой категории и вычисление средней цены
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средний ценник в категории '{category_empty.name}': {category_empty.middle_price()} руб.")

    # Проверка обработки пользовательского исключения
    try:
        category1.add_product(Product("Дефектный товар", "Ошибка количества", 5000.0, 0))
    except ZeroQuantityError as e:
        print(f"Ошибка: {e}")
    else:
        print("Товар успешно добавлен")
    finally:
        print("Обработка добавления товара завершена")
