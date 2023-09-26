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
from pathlib import Path
from typing import Union
from pprint import pprint
from typing import Mapping


class FileHandler:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.filename_path = Path('data', filename)

    def read(self) -> str:
        with open(self.filename_path, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self) -> Mapping['str', Union[list[str], int, str]]:
        with open(self.filename_path, 'r') as json_file:
            return json.load(json_file)


class CSVHandler(FileHandler):
    def read(self) -> list[dict[str, str]]:
        with open(self.filename_path, 'r') as csv_file:
            return [x for x in csv.DictReader(csv_file)]


if __name__ == '__main__':
    text = FileHandler('text.txt')
    pprint(text.read())
    
    recipes = JSONHandler('recipes.json')
    pprint(recipes.read())

    user_info = CSVHandler('user_info.csv')     
    pprint(user_info.read())
