"""
Задания:
    1. Создайте класс Developer, который будет наследоваться от класса ItDepartmentEmployee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self) -> str:
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float) -> None:
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float) -> None:
        employee.salary -= amount


class Developer(ItDepartmentEmployee, SuperAdminMixin):
    def __init__(self, name: str, surname: str, age: int, salary: float, language: str) -> None:
        super().__init__(name, surname, age, salary)
        self.language = language
    
    def get_info(self) -> str:
        return super().get_info() + f' and {self.language}'


if __name__ == '__main__':
    dev = Developer('John', 'Doe', 30, 1000, 'Python')
    print(dev.get_info())
    dev.increase_salary(dev, 100)
    print(dev.get_info())
    dev.decrease_salary(dev, 100)
    print(dev.get_info())
