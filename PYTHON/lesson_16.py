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
- sort - метод сортировки коллекции
- sorted - функция сортировки коллекции
"""
from pprint import pprint
from typing import Callable, Iterable, List, Set, Tuple, Any

from data.marvel import simple_set, small_dict, full_dict

simple_list = list(simple_set)
simple_list.sort()
print(simple_list)

# Передаем ключ len в качестве аргумента
simple_list.sort(key=len)
print(simple_list)


def sort_by_last_letter(title: str) -> str:
    return title[-1]


simple_list.sort(key=sort_by_last_letter)
print(simple_list)


def sort_by_words_count(title: str) -> int:
    return len(title.split())


# Сортировка по количеству слов в названии
simple_list.sort(key=sort_by_words_count, reverse=True)
print(simple_list)
