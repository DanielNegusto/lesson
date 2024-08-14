class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"Product(name='{self.name}', description='{self.description}', price={self.price}, "
                f"quantity={self.quantity})")


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем количество категорий на 1
        Category.category_count += 1

        # Увеличиваем общее количество товаров на количество товаров в данной категории
        Category.product_count += len(products)

    def __repr__(self):
        return f"Category(name='{self.name}', description='{self.description}', products={self.products})"
