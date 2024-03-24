"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельный
        класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def decrease_balance(self, amount: float) -> float:
        self.balance -= amount
        return self.balance


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    bank_account = BankAccount('Dusky', 99.9)
    bank_account.increase_balance(900)
    bank_account.decrease_balance(900)
    print(bank_account.balance)

    credit_account = CreditAccount('Musky', 99.9)
    credit_account.increase_balance(600)
    credit_account.decrease_balance(500)
    print(credit_account.balance)
