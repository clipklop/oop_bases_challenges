"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json
from typing import Mapping


class FileHandler:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read(self) -> str:
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()


class JSONHandler(FileHandler):
    # Here mypy is not happy, because we're violating the Liskov Substitution Principle
    def read(self) -> Mapping[str, str | int | float | bool]:
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)


class CSVHandler(FileHandler):
    # Here mypy is not happy, because we're violating the Liskov Substitution Principle
    def read(self) -> list[Mapping[str, str | int | float | bool]]:
        with open(self.filename, 'r', encoding='utf-8') as file:
            return list(csv.DictReader(file))


if __name__ == '__main__':
    fh = FileHandler('data/text.txt')
    # print(fh.read())

    jh = JSONHandler('data/recipes.json')
    # print(jh.read())

    ch = CSVHandler('data/user_info.csv')
    # print(ch.read())
