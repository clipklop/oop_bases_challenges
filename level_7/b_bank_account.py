"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float) -> None:
        if self.balance - amount < self.min_balance:
            raise ValueError
        self.balance -= amount


if __name__ == '__main__':
    ba = BankAccount('Dusky', 99.9)
    ba.decrease_balance(900)
    print(ba.balance)
    ba1 = BankAccount('Musky', 99.9)
    ba1.decrease_balance(199.9)
    print(ba1.balance)
