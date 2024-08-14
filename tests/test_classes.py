from src.classes import Category, Product


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


def test_update_price_negative(capsys):
    product = Product("Smartphone", "Latest model", 599.99, 10)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


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


def test_new_product_existing():
    product1 = Product("Smartphone", "Latest model", 599.99, 10)
    product2 = Product("Laptop", "High-performance laptop", 1199.99, 5)
    new_product_data = {
        'name': 'Smartphone',
        'description': 'Latest model',
        'price': 649.99,
        'quantity': 5
    }
    updated_product = Product.new_product(new_product_data, [product1, product2])
    assert updated_product.price == 649.99
    assert updated_product.quantity == 15


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
