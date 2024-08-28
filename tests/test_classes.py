from unittest.mock import patch

import pytest

from src.classes import Category, Product, CategoryIterator, LawnGrass, Smartphone


def test_product_init():
    product = Product("Товар", "Описание товара", 100, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100
    assert product.quantity == 10


def test_init_type_error():
    with pytest.raises(TypeError):
        Product(123, "Описание", 100.0, 10)


def test_init_value_error():
    with pytest.raises(ValueError):
        Product("Тестовый продукт", "Описание", -100.0, 10)


def test_create_product():
    product = Product("Smartphone", "Latest model", 599.99, 10)
    assert product.name == "Smartphone"
    assert product.description == "Latest model"
    assert product.price == 599.99
    assert product.quantity == 10


def test_update_price():
    product = Product("Smartphone", "Latest model", 599.99, 10)
    product.price = 649.99
    assert product.price == 649.99


def test_price_decrease_confirmed():
    product = Product("Тестовый продукт", "Описание", 100.0, 10)
    with patch('builtins.input', return_value='y'):
        product.price = 50.0
        assert product.price == 50.0


def test_update_price_negative(capsys):
    product = Product("Smartphone", "Latest model", 599.99, 10)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_decrease_declined():
    product = Product("Тестовый продукт", "Описание", 100.0, 10)
    with patch('builtins.input', return_value='n'):
        initial_price = product.price
        product.price = 50.0
        assert product.price == initial_price


def test_create_category():
    product1 = Product("Smartphone", "Latest model", 599.99, 10)
    product2 = Product("Laptop", "High-performance laptop", 1199.99, 5)
    category = Category("Electronics", "Electronic devices and accessories", [product1, product2])
    assert category.name == "Electronics"
    assert category.description == "Electronic devices and accessories"
    assert len(category.get_products()) == 2


def test_add_product_to_category():
    product1 = Product("Smartphone", "Latest model", 599.99, 10)
    product2 = Product("Laptop", "High-performance laptop", 1199.99, 5)
    category = Category("Electronics", "Electronic devices and accessories", [product1])
    category.add_product(product2)
    assert len(category.get_products()) == 2


def test_product_new_product():
    product_data = {"name": "Товар", "description": "Описание товара", "price": 100, "quantity": 10}
    existing_products = []
    new_product = Product.new_product(product_data, existing_products)
    assert new_product.name == "Товар"
    assert new_product.description == "Описание товара"
    assert new_product.price == 100
    assert new_product.quantity == 10


def test_new_product_not_existing():
    product1 = Product("Smartphone", "Latest model", 599.99, 10)
    product2 = Product("Laptop", "High-performance laptop", 1199.99, 5)
    new_product_data = {
        'name': 'Tablet',
        'description': 'Latest model tablet',
        'price': 300.00,
        'quantity': 8
    }
    new_product = Product.new_product(new_product_data, [product1, product2])
    assert new_product.name == "Tablet"
    assert new_product.price == 300.00
    assert new_product.quantity == 8


def test_category_products_property():
    product1 = Product("Smartphone", "Latest model", 599.99, 10)
    product2 = Product("Laptop", "High-performance laptop", 1199.99, 5)
    category = Category("Electronics", "Electronic devices and accessories", [product1, product2])
    products_string = category.products
    assert "Smartphone, 599.99 руб. Остаток: 10 шт." in products_string
    assert "Laptop, 1199.99 руб. Остаток: 5 шт." in products_string


def test_product_add():
    product1 = Product("Товар 1", "Описание товара 1", 100, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200, 2)
    total_cost = product1 + product2
    assert total_cost == 1400


def test_str():
    product = Product("Тестовый продукт", "Описание", 100.0, 10)
    expected_str = "Тестовый продукт, 100.00 руб. Остаток: 10 шт."
    assert str(product) == expected_str


def test_category_str():
    category = Category("Категория", "Описание категории")
    product1 = Product("Товар 1", "Описание товара 1", 100, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200, 2)
    category.add_product(product1)
    category.add_product(product2)
    category_str = str(category)
    assert "Категория" in category_str
    assert "количество продуктов" in category_str


def test_category_iterator_init():
    category = Category("Test Category", "Test Description")
    iterator = CategoryIterator(category)
    assert iterator.category == category
    assert iterator.index == 0


def test_category_iterator_iter():
    category = Category("Test Category", "Test Description")
    iterator = CategoryIterator(category)
    assert iterator.__iter__() == iterator


def test_category_iterator_next_products():
    category = Category("Test Category", "Test Description")
    product1 = Product("Test Product 1", "Test Description", 10.0, 1)
    product2 = Product("Test Product 2", "Test Description", 20.0, 2)
    category.add_product(product1)
    category.add_product(product2)
    iterator = CategoryIterator(category)
    assert next(iterator) == product1
    assert next(iterator) == product2
    with pytest.raises(StopIteration):
        next(iterator)


def test_smartphone_initialization():
    smartphone = Smartphone(
        name="iPhone 14",
        description="Смартфон от Apple",
        price=99999.99,
        quantity=5,
        efficiency=90.0,
        model="iPhone 14",
        memory=128,
        color="черный"
    )

    assert smartphone.name == "iPhone 14"
    assert smartphone.description == "Смартфон от Apple"
    assert smartphone.price == 99999.99
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 90.0
    assert smartphone.model == "iPhone 14"
    assert smartphone.memory == 128
    assert smartphone.color == "черный"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(
        name="Садовая трава",
        description="Трава для сада",
        price=499.99,
        quantity=10,
        country="Россия",
        germination_period="10 дней",
        color="зеленый"
    )

    assert lawn_grass.name == "Садовая трава"
    assert lawn_grass.description == "Трава для сада"
    assert lawn_grass.price == 499.99
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "10 дней"
    assert lawn_grass.color == "зеленый"