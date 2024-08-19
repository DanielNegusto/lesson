class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if not isinstance(name, str) or not isinstance(description, str):
            raise TypeError("Имя и описание должны быть строками")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif value < self.__price:
            confirmation = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): ")
            if confirmation.lower() == "y":
                self.__price = value
                print(f"Цена успешно изменена на {self.__price}")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list):
        for existing_product in existing_products:
            if existing_product.name == product_data["name"]:
                existing_product.quantity += product_data["quantity"]
                existing_product.price = min(existing_product.price, product_data["price"])
                return existing_product

        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])

    def update_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        self.quantity = quantity

    def delete_product(self):
        self.quantity = 0

    def __str__(self):
        return f"{self.name}, {format(self.price, '.2f')} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        total_cost = self.price * self.quantity + other.price * other.quantity
        return total_cost


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += product.quantity

    def get_products(self):
        return self.__products

    @property
    def products(self):
        product_strings = []
        for product in self.__products:
            product_string = f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт."
            product_strings.append(product_string)
        return "\n".join(product_strings)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.get_products()):
            product = self.category.get_products()[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
