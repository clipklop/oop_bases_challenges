"""
Нам необходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def should_be_banned(self) -> bool:
        return self.last_name in SURNAMES_TO_BAN


if __name__ == '__main__':  
    user = User('Julia', 'Church', 29)
    user2 = User('Julia', 'Porter', 55)
    print(user.should_be_banned())
    print(user2.should_be_banned())
