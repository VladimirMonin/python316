"""
Lesson 17
03.03.2024
- Анонимные функции
- lambda
- map + lambda
- filter + lambda
- sorted + lambda
- сортировка по 2м признакам
- generators
- yield
- генераторное выражение
- ленивые вычисления
"""
import csv
from pprint import pprint
from typing import Tuple


# Ленивое чтение построчно txt файла
def read_file(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


# Создание генератора "файлов"
file_gen = read_file('data.txt')


# Ленивое чтение построчно csv файла
def read_csv(file_name: str, delimiter: str = ';') -> Tuple:
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter, lineterminator='\n')
        for row in reader:
            yield row
