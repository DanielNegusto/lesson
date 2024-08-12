import pytest

from src.classes import Product, Category


@pytest.fixture
def setup_products():
    # Fixture для создания продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return product1, product2, product3


@pytest.fixture
def setup_categories(setup_products):
    # Fixture для создания категорий с продуктами
    product1, product2, product3 = setup_products
    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [product1, product2, product3])
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", [product4])
    return category1, category2, product4