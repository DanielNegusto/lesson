import json

from src.classes import Category, Product


def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Сброс счетчиков категорий и продуктов
    Category.category_count = 0
    Category.product_count = 0

    for category_data in data:
        # Создание продуктов
        products = []
        for product_data in category_data.get('products', []):
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            products.append(product)

        # Создание категории
        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products
        )

    # Возвращаем количество категорий и продуктов
    return Category.category_count, Category.product_count


if __name__ == "__main__":
    category_count, product_count = load_data_from_json('data/products.json')
    print(f"Number of categories: {category_count}")
    print(f"Number of products: {product_count}")