"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f'Product {self.title} with price {self.price}'


class PrintLoggerMixin:
    def log(self, message: str) -> None:
        print(message)


class PremiumProduct(Product, PrintLoggerMixin):
    def increase_price(self) -> None:
        self.price *= 1.2
        self.log(f'Price increased to {self.price}')

    def get_info(self) -> str:
        message = super().get_info() + ' (Premium)'
        # return f'{base_info} (Premium)'
        self.log(message)
        return message


class DiscountedProduct(Product, PrintLoggerMixin):
    def decrease_price(self) -> None:
        self.price /= 1.2
        self.log(f'Price decreased to {self.price}')

    def get_info(self) -> str:
        message = super().get_info() + ' (Discounted)'
        self.log(message)
        return message
        # return f'{base_info} (Discounted)'


if __name__ == '__main__':
    pr = PremiumProduct('Картошечка', 33)
    pr.get_info()
    pr.increase_price()
    pr.get_info()

    dp = DiscountedProduct('Огуречек', 312)
    dp.get_info()
    dp.decrease_price()
    dp.get_info()
