from src.classes import Category


def test_product_initialization(sample_products):
    product = sample_products[0]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(sample_categories):
    category1, _ = sample_categories
    assert category1.name == "Смартфоны"
    assert category1.description == "Описание категории смартфонов"
    assert len(category1.products) == 3


def test_product_count(sample_categories):
    assert Category.product_count == 3


def test_category_count(sample_categories):
    assert Category.category_count == 2
