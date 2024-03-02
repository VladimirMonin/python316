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
- filter - фильтрация коллекции
"""
from pprint import pprint
from typing import Callable, Iterable, List, Set, Tuple, Any

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


def my_filter(func: Callable[[Any], bool], collection: List | Set | Tuple) -> List:
    """
    Функция высшего порядка, которая принимает функцию и коллекцию.
    После чего фильтрует коллекцию по функции
    :param func: функция
    :param collection: коллекция
    :return:
    """
    result = []
    for item in collection:
        if func(item):
            result.append(item)
    return result


def filter_film_by_first_letter(film: str, letter: str = 'Ч') -> bool:
    """
    Функция фильтрации фильмов по первой букве
    :param letter: буква
    :param film: название фильма
    :return: результат фильтрации
    """
    return film[0].lower() == letter.lower()


# Тестируем my_filter и filter_film_by_first_letter
# print(my_filter(filter_film_by_first_letter, simple_set))

# Это же на комприхеншн
# print([film for film in simple_set if filter_film_by_first_letter(film, 'ж')])

# Filter - фильтрация коллекции. Встроеенная функция в Python
# filter(функция, коллекция)

# Это же на filter
print(list(filter(filter_film_by_first_letter, simple_set)))
