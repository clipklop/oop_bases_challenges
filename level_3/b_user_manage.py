"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
# noqa: E501
"""


class UserManager:
    def __init__(self) -> None:
        self.usernames: list[str] = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        print(self.usernames)
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        if username in self.usernames:
            self.usernames.remove(username)
            print(f"Пользователь {username} удален из списка.")
        else:
            print("Такого пользователя не существует.")


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()
        print("Все пользователи удалены из списка.")


if __name__ == '__main__':
    users = SuperAdminManager()
    users.add_user('Julia')
    users.add_user('Alex')
    users.get_users()
    users.ban_username('Julia')
    users.ban_username('Juliass')
    users.add_user('Vasily')
    users.get_users()
    users.ban_all_users()
    users.get_users()
