from abc import ABC, abstractmethod


class CreationLoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ", ".join(f"{arg}" for arg in args)
        print(f"{class_name} создан с параметрами: {params}")


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if not isinstance(name, str) or not isinstance(description, str):
            raise TypeError("Имя и описание должны быть строками")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

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
    @abstractmethod
    def new_product(cls, product_data: dict, existing_products: list):
        """Метод для создания или обновления продукта"""
        pass

    @abstractmethod
    def update_quantity(self, quantity: int):
        """Метод для обновления количества продукта"""
        pass

    @abstractmethod
    def delete_product(self):
        """Метод для удаления продукта"""
        pass

    def __str__(self):
        return f"{self.name}, {format(self.price, '.2f')} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Нельзя складывать товары разных типов")
        total_cost = self.price * self.quantity + other.price * other.quantity
        return total_cost


class Product(CreationLoggingMixin, BaseProduct):
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
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объекты класса Product или его наследников")
        self.__products.append(product)

    def get_products(self):
        return self.__products

    @property
    def products(self):
        product_strings = []
        for product in self.__products:
            product_string = f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт."
            product_strings.append(product_string)
        return "\n".join(product_strings)

    def middle_price(self):
        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            average = total_price / total_quantity
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            return 0
        return round(average, 2)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
