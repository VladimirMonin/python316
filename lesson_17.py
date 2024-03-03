"""
Lesson 17
03.03.2024
- Анонимные функции
- lambda
- generators?
"""
from pprint import pprint

from PYTHON.data.marvel import simple_set, small_dict, full_dict

# Sorted - функция высшего порядка
# Возвращает отсортированный список

simple_list = list(simple_set)

sorted_list = sorted(simple_list)


# print(sorted_list)


def sort_by_last_letter(title: str) -> str:
    return title[-1]


# Используем свю функцию sort_by_last_letter
sorted_list = sorted(simple_list, key=sort_by_last_letter)


# print(sorted_list)

def sort_dict_by_key_first_letter(key: str) -> str:
    return key[0]


# Сортировка ключей словаря по алфавиту
sorted_dict = sorted(small_dict, key=sort_dict_by_key_first_letter)
# pprint(sorted_dict, sort_dicts=False)

full_list2 = [{'id': key, **value} for key, value in full_dict.items()]

# Анонимные функции
# lambda - ключевое слово для создания анонимной функции
# lambda arguments: expression
# Особенности
# Одно выражение, нет return, нет имени, нельзя использовать вложенные блоки, можно использовать в качестве аргумента

my_lambda = lambda x: x ** 2


def my_lambda2(x):
    return x ** 2


int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(map(lambda x: x ** 2, int_list)))

# Проходим map lambda по словарю .items, работаем с ключами и значениями (small_dict)
# print(small_dict.items())
# print(list(small_dict.items()))
# print(dict(list(small_dict.items())))
# print(dict(map(lambda x: (x[0].upper(), x[1]), small_dict.items())))
# print(dict(map(lambda x: (x[0].upper(), x[1] + 1000 if isinstance(x[1], int) else x[1]), small_dict.items())))

# TODO Практика
"""
Ч1
Сделайте пользовательский ввод чисел через пробел
Разбейте это на список
Обработайте это map lambda:
- Примените int
- прибавьте 100

На выходе print(list)

Ч2 добавьте проверку на int, если строка не число, вставьте None
"""
# Ч1
user_input = input('Введите числа через пробел: ')
user_list = user_input.split()
print(list(map(lambda x: int(x) + 100, user_list)))

# Ч2
user_input = input('Введите числа через пробел: ')
user_list = user_input.split()
print(list(map(lambda x: int(x) + 100 if x.isdigit() else None, user_list)))
