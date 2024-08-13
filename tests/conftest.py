import pytest

from src.classes import Product, Category


@pytest.fixture
def reset_category_count():
    # Перед каждым тестом сбрасываем счетчики категорий и продуктов
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture
def sample_categories(sample_products, reset_category_count):
    category1 = Category("Смартфоны", "Описание категории смартфонов", sample_products)
    category2 = Category("Телевизоры", "Описание категории телевизоров", [])
    return category1, category2
