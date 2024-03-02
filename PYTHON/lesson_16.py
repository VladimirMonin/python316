"""
Lesson 16
1. Повторение
- comprehension
- условие в начале
- условие в конце
- list comprehension
- dict comprehension
- перепаковка данных

2. Функции высшего порядка
- my_map - пишем сами map
- map - применение функции к каждому элементу коллекции
"""
from pprint import pprint
from typing import Callable, Iterable, List, Set, Tuple

from data.marvel import simple_set, small_dict, full_dict

# 2. Функции высшего порядка
"""
Допустим, у нас есть коллекция, и мы хотим к каждому элементу применить функцию.
При функциональном стиле, нам нужно написать функцию, которая принимает функцию и коллекцию.
А внутри этой функции мы применяем функцию к каждому элементу коллекции в цикле.

Давайте это напишем!
"""


def my_map(func: Callable, collection: List | Set | Tuple) -> List:
    """
    Функция высшего порядка, которая принимает функцию и коллекцию.
    После чего применяет функцию к каждому элементу коллекции
    :param func: функция
    :param collection: коллекция
    :return:
    """
    result = []
    for item in collection:
        result.append(func(item))
    return result


def string_processor(string: str) -> str:
    """
    Функция принимает строку и возвращает ее в верхнем регистре
    :param string: строка
    :return: строка в верхнем регистре
    """
    return string.upper().replace(' ', '_').replace('-', '_').replace(':', '')


# Применяем функцию высшего порядка к simple_set

# pprint(my_map(string_processor, simple_set))

# Применю функцию string_processor к каждому элементу simple_set через map
# map(функция, коллекция)

# pprint(list(map(string_processor, simple_set)))

# В таком варианте мы получим map object (генератор), который нужно преобразовать в список
# Или нет. Если вам нужен генератор, то оставьте его в таком виде
pprint(map(string_processor, simple_set))
pprint(next(map(string_processor, simple_set)))