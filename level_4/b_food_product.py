
"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""
import datetime


class Product:
    def __init__(self, title: str, quantity: int) -> None:
        self.title = title
        self.quantity = quantity

    def get_full_info(self) -> str:
        return f'Product {self.title}, {self.quantity} in stock.'

    def is_available(self) -> bool:
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title: str, quantity: int, expiration_date: datetime) -> None:
        super().__init__(title, quantity)
        self.expiration_date = expiration_date

    def get_full_info(self) -> str:
        return super().get_full_info() + f' Expiration date: {self.expiration_date}'

    def is_available(self) -> bool:
        return super().is_available() and self.expiration_date > datetime.datetime.now()


if __name__ == '__main__':
    fp = FoodProduct('Milk', 10, datetime.datetime.now() + datetime.timedelta(days=5))
    print(fp.get_full_info())
    print(fp.is_available())
