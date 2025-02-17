# Homework Project 14.1

## Описание проекта

Этот проект представляет собой базовую модель e-commerce приложения, реализованную на языке Python с использованием объектно-ориентированного подхода. В рамках проекта созданы классы для моделирования продуктов и категорий товаров, а также функция для загрузки данных из JSON-файла. Программа поддерживает подсчет количества категорий и продуктов и может быть легко расширена для более сложной логики.

### Основные компоненты

- **Класс `Product`**: Определяет товар с атрибутами:
  - `name` (название продукта)
  - `description` (описание продукта)
  - `price` (цена продукта)
  - `quantity` (количество продукта на складе)

- **Класс `Category`**: Определяет категорию товаров и включает:
  - `name` (название категории)
  - `description` (описание категории)
  - `products` (список товаров, относящихся к категории)
  - Методы для ручного подсчета количества категорий и продуктов

- **Функция `load_data_from_json`**: Загружает данные из JSON-файла и создает объекты `Category` и `Product` на основе загруженных данных.

## Установка и запуск

1. **Клонирование репозитория**:

   ```bash
   git clone git@github.com:mikeshumkin13/homework_project_14.1.git
   cd homework_Project_14_1

2. **Установка зависимостей**:
Используйте Poetry для установки зависимостей:

poetry install

3. **Запуск программы**:
Для запуска программы, выполните:

poetry run python src/main.py
Эта команда загружает данные из JSON-файла products.json и выводит информацию о категориях и продуктах.
Тестирование

Для тестирования проекта используются pytest и pytest-cov.

4. **Запуск тестов**:
poetry run pytest tests/
Создание отчета о покрытии тестами:
Для создания отчета о покрытии выполните:

poetry run pytest --cov=src --cov-report=term-missing
Этот отчет отобразит в терминале покрытие кода тестами и выделит строки, которые не были покрыты.
Покрытие тестами

Проект включает тесты для следующих компонентов:

Инициализация объектов Product и Category: проверка корректности атрибутов.
Подсчет категорий и продуктов: проверка логики подсчета в Category.
Загрузка данных из JSON: проверка корректного создания объектов на основе данных из JSON-файла.
Отчет о покрытии кода можно найти в файле coverage.txt, который включает информацию обо всех протестированных и непокрытых строках кода.

**Cтруктура проекта**
.
├── README.md
├── coverage.txt
├── htmlcov
│   ├── class_index.html
│   ├── coverage_html_cb_6fb7b396.js
│   ├── favicon_32_cb_58284776.png
│   ├── function_index.html
│   ├── index.html
│   ├── keybd_closed_cb_ce680311.png
│   ├── status.json
│   ├── style_cb_8e611ae1.css
│   ├── z_145eef247bfb46b6___init___py.html
│   ├── z_145eef247bfb46b6_main_py.html
│   ├── z_145eef247bfb46b6_models_py.html
│   └── z_145eef247bfb46b6_utils_py.html
├── poetry.lock
├── products.json
├── pyproject.toml
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   └── utils.cpython-312.pyc
│   ├── main.py
│   ├── models.py
│   └── utils.py
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── conftest.cpython-312-pytest-8.3.3.pyc
    │   ├── test_main.cpython-312-pytest-8.3.3.pyc
    │   ├── test_models.cpython-312-pytest-8.3.3.pyc
    │   └── test_utils.cpython-312-pytest-8.3.3.pyc
    ├── conftest.py
    ├── test_models.py
    └── test_utils.py

6 directories, 33 files

