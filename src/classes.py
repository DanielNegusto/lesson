class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self._price:
            confirmation = input(f"Вы уверены, что хотите понизить цену с {self._price} до {value}? (y/n): ")
            if confirmation.lower() == "y":
                self._price = value  # Устанавливаем новую цену, если пользователь согласен
                print(f"Цена успешно изменена на {self._price}")
            else:
                print("Изменение цены отменено.")
        else:
            self._price = value  # Устанавливаем новую цену, если она валидна

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list):
        # Проверка на наличие товара с таким же именем
        for existing_product in existing_products:
            if existing_product.name == product_data["name"]:
                # Если товар существует, обновляем количество и цену
                existing_product.quantity += product_data["quantity"]
                existing_product.price = max(existing_product.price, product_data["price"])
                return existing_product  # Возвращаем обновленный товар

        # Если товара нет, создаем новый
        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут для хранения списка товаров

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)  # Добавляем товар в приватный список
        Category.product_count += 1

    def get_products(self):
        """Возвращает список объектов Product."""
        return self.__products

    @property
    def products(self):
        product_strings = []
        for product in self.__products:
            product_string = f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт."
            product_strings.append(product_string)
        return "\n".join(product_strings)
