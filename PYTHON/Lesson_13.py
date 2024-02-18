# """
# Lesson 13
# 11.02.2024
#
# - Повторение. Распаковка и *args
# - **kwargs
# - Пример функции с *args и **kwargs и tabulate
# - Type hints import Typing
# - pip install mypy
# - MyPy
# - Демонстрация - модуль проверки пароля
# - all и any
# """
# from typing import Dict
#
# # Повторение. Распаковка и *args
# products = ['bread', 'milk', 'eggs', 'butter', 'flour', 'sugar', 'salt', 'pepper', 'sausage']
# print(products)
# print(*products)
# print('привет')
# print(*'привет', sep='+')
#
#
# # Распаковка в функции
# def print_products(*args):
#     print(type(args))
#     print(*args)
#     print(args)
#
#
# print_products(*products)
#
# # **kwargs - keyword arguments, распаковка словаря
# some_dict = {
#     'name': 'Василий',
#     'age': 30,
#     'job': 'разраб'
# }
#
# # print(some_dict)
# # print(*some_dict)
# # print(**some_dict)
# # print(name='Василий', age=30, job='разраб')
#
# print_dict_param = {
#     'sep': '+',
#     'end': '!\n'
# }
#
# print('Привет', 'Василий', '!', sep='+', end='!\n')
# print('Привет', 'Василий', '!', **print_dict_param)
#
#
# # Функция с использованием **kwargs
# def print_person_info(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
#
# print_person_info(name='Василий', age=30, job='разраб')
# print_person_info(**some_dict)
# print_person_info(name='Василий', age=30, job='разраб', salary=1000.0, skills=['python', 'git', 'linux'], married=True,
#                   hobbies=None)
#
#
# # Все типы аргументов
# def all_args(a, b, *args, c=10, d=20, **kwargs):
#     print(f'{a=}')
#     print(f'{b=}')
#     print(f'{args=}')
#     print(f'{c=}')
#     print(f'{d=}')
#     print(f'{kwargs=}')
#
#
# all_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, c=30, d=40, name='Василий', age=30, job='разраб', salary=1000.0)
#
# param1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# param2 = {'c': '30c', 'd': '40d', 'name': 'Василий', 'age': 30, 'job': 'разраб', 'salary': 1000.0}
#
# all_args(*param1, **param2)
#
# """
# Напишите функцию, которая принимает **reports_dict и выводит отчет
# в красивом виде, это СЛОВО палиндром, это СЛОВО не палиндром
# """
#
# from lesson_12 import is_palindromes, BAD_SYM
#
#
# def print_palindromes(**reports_dict: Dict[str, bool]) -> None:
#     for word, result in reports_dict.items():
#         # if result:
#         #     print(f'Слово "{word}" - палиндром')
#         # else:
#         #     print(f'Слово "{word}" - не палиндром')
#         print(f'Слово "{word}" - {"палиндром" if result else "не палиндром"}')
#
#
# def print_tabulate_palindromes(**reports_dict: Dict[str, bool]) -> None:
#     from tabulate import tabulate
#     table = []
#     for word, result in reports_dict.items():
#         table.append([word, 'палиндром' if result else 'не палиндром'])
#
#     print(tabulate(table, headers=['Слово', 'Результат'], tablefmt='grid'))
#
#
# palindromes = ['А роза упала на лапу Азора', 'Аргентина манит негра', 'Топот', 'Котоп', 'Кот топот']
# result = is_palindromes(*palindromes, bad_sym=BAD_SYM)
# print_palindromes(**result)
# print_tabulate_palindromes(**result)
#
# # print_palindromes(**is_palindromes('А роза упала на лапу Азора',
# #                                    'Аргентина манит негра', 'Топот', 'Котоп', 'Кот топот'))
#
#
# """
# Фукнция которая принимает *args словарей и печатает это в tabulate таблице
# При этом ключи словарей это заголовки таблицы, которые добываются из первого словаря
# """
#
#
# def dicts_printer_tabulate(*args: dict):
#     """
#     Функция принимает *args словарей и печатает это в tabulate таблице, превращая ключи словарей в заголовки таблицы
#     А значения в строки таблицы
#     :param args: словари
#     :return: None
#     """
#     from tabulate import tabulate
#     headers = list(args[0].keys())
#     table = []
#     # for dict_ in args:
#     #     table.append([dict_[key] for key in headers])
#     # Это же, но без comprehension
#     for dict_ in args:
#         row = []
#         for key in headers:
#             row.append(dict_[key])
#         table.append(row)
#
#     print(tabulate(table, headers=headers, tablefmt='grid'))
#
#
# persons_list_dicts = [
#     {'name': 'Василий', 'age': 30, 'job': 'разраб'},
#     {'name': 'Иван', 'age': 25, 'job': 'тестировщик'},
#     {'name': 'Петр', 'age': 35, 'job': 'менеджер'},
# ]
#
# dicts_printer_tabulate(*persons_list_dicts)
#
# """
# Аннотация типов - это подсказка для IDE и других разработчиков, какие типы данных ожидаются
# в качестве аргументов и возвращаемого значения функции
#
# str - строка
# int - целое число
# float - число с плавающей точкой
# bool - булево значение
# list - список
# tuple - кортеж
# dict - словарь
# set - множество
# None - пустое значение
# callable - вызываемый объект
# list[str] - список строк
# tuple[int, str] - кортеж из целого числа и строки
# set[float] - множество чисел с плавающей точкой
# dict[str, str|list] - словарь с ключами строками и значениями строками или списками
# int | float - либо целое число, либо число с плавающей точкой
# | - или
#
# """
#
# # from typing import List, Tuple, Dict, Set, Union, Any, Callable, Optional, Iterable
#
# """
# List - список
# Tuple - кортеж
# Dict - словарь
# Set - множество
# Union - объединение типов
# Any - любой тип
# Callable - вызываемый объект
# Optional - опциональный тип (может быть None)
# Iterable - итерируемый объект
#
# List[str] - список строк
# List[Optional[str]] - список строк, которые могут быть None
# Dict[str, Union[str, List[Optional[str]]]] - словарь с ключами строками и значениями строками или списками строк, которые могут быть None
#
# Callable[[int, int], int] - функция, которая принимает два целых числа и возвращает целое число
# Iterable[Union[int, float]] - итерируемый объект, который содержит целые числа или числа с плавающей точкой
#
# """
# from typing import Dict, Any
#
#
# # Простые функции с type hints
# def simple_func(a: int, b: int, c: int = 10) -> int:
#     return a + b + c
#
#
# def simple_func2(*args: int) -> int:
#     return sum(args)
#
#
# def simple_func3(**kwargs: int) -> int:
#     return sum(kwargs.values())
#
#
# # simple_func3 **kwargs: int - мы предполагаем, что все значения в словаре будут целыми числами
#
# persons_list_dicts = [
#     {'name': 'Василий', 'age': 30, 'job': 'разраб'},
#     {'name': 'Иван', 'age': 25, 'job': 'тестировщик'},
#     {'name': 'Петр', 'age': 35, 'job': 'менеджер'},
# ]
#
#
# def dicts_printer_tabulate(*args: Dict[str, Any]) -> None:
#     """
#     Функция принимает *args словарей и печатает это в tabulate таблице, превращая ключи словарей в заголовки таблицы
#     А значения в строки таблицы
#     :param args: словари
#     :return: None
#     """
#     from tabulate import tabulate
#     headers = list(args[0].keys())
#     table = []
#     # for dict_ in args:
#     #     table.append([dict_[key] for key in headers])
#     # Это же, но без comprehension
#     for dict_ in args:
#         row = []
#         for key in headers:
#             row.append(dict_[key])
#         table.append(row)
#
#     print(tabulate(table, headers=headers, tablefmt='grid'))
#
#
# dicts_printer_tabulate(*persons_list_dicts)

# All и Any
# all - возвращает True, если все элементы истинные
# any - возвращает True, если хотя бы один элемент истинный

list_1 = [True, True, True, True]
list_2 = [True, False, True, True]

print(all(list_1))
print(all(list_2))

print(any(list_1))
print(any(list_2))

# Пример на is_alpha
list_1 = ['a', 'b', 'c', 'd']
list_2 = ['a', 'b', 'c', 'd', '1']

print(all([symbol.isalpha() for symbol in list_1]))
print(all([symbol.isalpha() for symbol in list_2]))

"""
Документация для модуля
Мы пишем модуль для проверки пароля
КОНСТАНТЫ:

- MIN_LENGTH - минимальная длина пароля
- MAX_LENGTH - максимальная длина пароля
- DIGITS_TRESHOLD - минимальное количество цифр
- UPPER_TRESHOLD - минимальное количество заглавных букв
- LOWER_TRESHOLD - минимальное количество строчных букв
- SPECIAL_TRESHOLD - минимальное количество спец символов
- LETTERS_TRESHOLD - минимальное количество букв

ФУНКЦИИ:
0. Точка входа в программу - функция main
1. Функция main - запускает программу и принимает пароли от пользователя через запятую
2. Функция is_password_valid - проверяет пароль на валидность (используя все остальные функции)
3. Функция is_length_valid - проверяет длину пароля
4. Функция is_digit_valid - проверяет наличие цифр в пароле
5. Функция is_upper_valid - проверяет наличие заглавных букв в пароле
6. Функция is_special_valid - проверяет наличие спец символов в пароле
7. Функция is_alpha_valid - проверяет наличие букв в пароле

"""
MIN_LENGTH = 8
MAX_LENGTH = 16
DIGITS_TRESHOLD = 2
UPPER_TRESHOLD = 2
SPECIAL_TRESHOLD = 2
LETTERS_TRESHOLD = 2
LOWER_TRESHOLD = 2


def is_length_valid(password: str, min_length: int = MIN_LENGTH, max_length: int = MAX_LENGTH) -> bool:
    """
    Функция проверяет длину пароля
    :param max_length: максимальная длина пароля
    :param min_length: минимальная длина пароля
    :param password: пароль
    :return: результат проверки
    """
    return min_length <= len(password) <= max_length


def is_digit_valid(password: str, treshold: int = DIGITS_TRESHOLD) -> bool:
    """
    Функция проверяет наличие цифр в пароле
    :param treshold: минимальное количество цифр
    :param password: пароль
    :return: результат проверки
    """

    # bool_list = [symbol.isdigit() for symbol in password]
    # return bool_list.count(True) >= treshold
    return sum([1 for symbol in password if symbol.isdigit()]) >= treshold


def is_upper_valid(password: str, treshold: int = UPPER_TRESHOLD) -> bool:
    """
    Функция проверяет наличие заглавных букв в пароле
    :param treshold: минимальное количество заглавных букв
    :param password: пароль
    :return: результат проверки
    """
    return sum([1 for symbol in password if symbol.isupper()]) >= treshold


def is_special_valid(password: str, treshold: int = SPECIAL_TRESHOLD) -> bool:
    """
    Функция проверяет наличие спец символов в пароле
    :param treshold: минимальное количество спец символов
    :param password: пароль
    :return: результат проверки
    """
    return sum([1 for symbol in password if not symbol.isalnum()]) >= treshold


def is_alpha_valid(password: str, treshold: int = LETTERS_TRESHOLD) -> bool:
    """
    Функция проверяет наличие букв в пароле
    :param treshold: минимальное количество букв
    :param password: пароль
    :return: результат проверки
    """
    return sum([1 for symbol in password if symbol.isalpha()]) >= treshold


def is_password_valid(password: str) -> bool:
    """
    Функция проверяет пароль на валидность
    Главная функция, которая использует все остальные функции
    :param password: пароль
    :return: результат проверки
    """
    # Красиво, но не инфомативно - человек не узнает, что с паролем не так!
    return all([
        is_length_valid(password),
        is_digit_valid(password),
        is_upper_valid(password),
        is_special_valid(password),
        is_alpha_valid(password)
    ])


def main():
    user_passwords = input('Введите пароли через пробел: ').split()
    for password in user_passwords:
        if is_password_valid(password):
            print(f'Пароль "{password}" валиден')
        else:
            print(f'Пароль "{password}" не валиден')


if __name__ == '__main__':
    main()
