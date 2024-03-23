"""
У нас есть класс Product, который содержит в себе информацию о продукте.
Еще у нас есть класс AlcoholProduct, но метод is_available для него не подходит, так как
алкоголь нельзя продавать с 5 утра до 11 вечера

Задания:
    1. Переопределите метод is_available в классе AlcoholProduct с использованием super()
    2. is_available у AlcoholProduct должен возвращать False если сейчас часы между 5 утра и 11 вечера.
       Для определения текущего часа можно использовать datetime.now().hour
    3. Создайте экземпляр класса AlcoholProduct и проверьте, можно ли сейчас продавать алкоголь.
"""
from datetime import datetime, timedelta
from math import prod


class Product:
    def __init__(self, title: str, price: float, stock_quantity: int) -> None:
        self.title = title
        self.price = price
        self.stock_quantity = stock_quantity

    def get_discounted_price(self, discount_percentage: int) -> float:
        return self.price * (1 - discount_percentage / 100)

    def is_available(self) -> bool:
        return self.stock_quantity > 0


class AlcoholProduct(Product):
    def is_available(self, hour: int) -> bool:
        # datetime.now().hour >= 23 or datetime.now().hour <= 5
        return super().is_available() and hour >= 23 or hour <= 5


if __name__ == '__main__':
    not_allowed_hour = datetime.now().hour
    allowed_hour = (datetime.now() + timedelta(hours=9)).hour

    product = Product(title='Хлебушек', price=9.99, stock_quantity=1) # True
    print(product.is_available())

    alco_product = AlcoholProduct(title='Отвертка', price=90.99, stock_quantity=69) # True
    alco_product = AlcoholProduct(title='Отвертка', price=90.99, stock_quantity=0) # False
    print(alco_product.is_available(24))

