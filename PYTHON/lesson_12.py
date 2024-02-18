"""
Lessson 12
10.02.2024
Функции
- Правила именования
- Определение функции
- Вызов функции
- Параметры функции
- Возвращаемое значение
- Позиционные аргументы
- Именованные аргументы
- Параметры функции по умолчанию
- Документация функции
- Простые type hints (без Typing)
- args
- Практика палиндром + args




"""
from typing import List, Dict

"""
Правила именования функций
- Имя функции должно быть осмысленным
- Имя функции должно содержать глагол
- Имя функции должно быть в нижнем регистре
- Имя функции может содержать буквы, цифры и символ _
- Имя функции не должно начинаться с цифры
- Имя функции не должно быть зарезервированным словом
- Имя функции не должно быть встроенной функцией
"""


# Определение функции
def greet_user():
    print('Hello!')


# Вызов функции
# greet_user()

print_greet = print('hey!')
greet = greet_user()

print(f'{print_greet=}')
print(f'{greet=}')


def greet_user2():
    return 'Hello!'


greet = greet_user2()
print(f'{greet=}')


# Параметры функции
def greet_by_name(name):
    return f'Hello, {name}!'


greet = greet_by_name('John')
# greet2 = greet_by_name()  # TypeError: greet_by_name() missing 1 required positional argument: 'name'
# greet3 = greet_by_name('John', 'Doe')  # TypeError: greet_by_name() takes 1 positional argument but 2 were given
print(f'{greet=}')


# Параметры функции по умолчанию
def message_by_name(name, message='Hello!'):
    return f'{message}, {name}!'


# Позиционные аргументы
msg = message_by_name('John')
msg2 = message_by_name('John', 'Hi!')
msg3 = message_by_name('Goodbye!', 'John')
print(f'{msg=}')
print(f'{msg2=}')
print(f'{msg3=}')

# Именованные аргументы
msg = message_by_name(message='Hi!', name='John')
msg2 = message_by_name(name='John', message='Hi!')
print(f'{msg=}')
print(f'{msg2=}')

# Порядок аргументов
# 1. Позиционные аргументы
# 2. *args
# 3. Именованные аргументы
# 4. **kwargs
# 5. Параметры функции по умолчанию

# TODO Практика
"""
Напишите функцию, которая принимает один параметр - строку
И проверяет является ли строка палиндромом, возвращает True или False
Многослоный палиндром тоже должен быть обработан
def is_palindrome
"""

# Docstring - строка документации
"""
Строка
"""


def is_palindrome(string):
    """
    Функция проверяет является ли строка палиндромом.
    Работает с многословными палиндромами
    :param string: строка для проверки
    :return: True если строка палиндром, иначе False
    """
    bad_sym = [' ', ',', '.', '!', '?', ':', ';', '-', '(', ')', '"', "'"]

    # for sym in bad_sym:
    #     string = string.replace(sym, '')
    # string = string.lower()

    # Аналог на map
    # string = ''.join(map(lambda sym: sym if sym not in bad_sym else '', string)).lower()
    # Комприхеншн
    string = ''.join([sym for sym in string if sym not in bad_sym]).lower()

    # string = string.replace(' ', '').replace(',', '').replace('.', '').replace('.', '').lower()
    return string == string[::-1]


# while True:
#     user_words = input('Введите строку для проверки на палиндром:')
#     if not user_words:
#         break
#
#     if is_palindrome(user_words):
#         print(f'Строка {user_words} является палиндромом')
#     else:
#         print(f'Строка {user_words} не является палиндромом')

# Простые type hints (без Typing) (аннонотация типов)
"""
Аннотация типов - это подсказка для IDE и других разработчиков, какие типы данных ожидаются
в качестве аргументов и возвращаемого значения функции

str - строка
int - целое число
float - число с плавающей точкой
bool - булево значение
list - список
tuple - кортеж
dict - словарь
set - множество
None - пустое значение
callable - вызываемый объект
list[str] - список строк
tuple[int, str] - кортеж из целого числа и строки
set[float] - множество чисел с плавающей точкой
dict[str, str|list] - словарь с ключами строками и значениями строками или списками
int | float - либо целое число, либо число с плавающей точкой
| - или

"""
BAD_SYM = [' ', ',', '.', '!', '?', ':', ';', '-', '(', ')', '"', "'"]


def is_palindrome(string: str, bad_sym: list[str] = BAD_SYM) -> bool:
    """
    Функция проверяет является ли строка палиндромом.
    Работает с многословными палиндромами
    :param bad_sym:
    :param string: строка для проверки
    :return: True если строка палиндром, иначе False
    """

    string = ''.join([sym for sym in string if sym not in bad_sym]).lower()
    return string == string[::-1]


# while True:
#     user_words = input('Введите строку для проверки на палиндром:')
#     if not user_words:
#         break
#
#     if is_palindrome(user_words):
#         print(f'Строка {user_words} является палиндромом')
#     else:
#         print(f'Строка {user_words} не является палиндромом')

# args - множественные позиционные аргументы
# * - распаковывает список или кортеж

# some_integers = [1, 2, 3, 4, 5]
# one, two, three, four, five = some_integers
# one, two, *other = some_integers
# *other, five = some_integers
# print(f'{other=}')
# print(f'{five=}')

# print(*some_integers, sep=';')
# print(some_integers[0], some_integers[1], some_integers[2], some_integers[3], some_integers[4], sep=';')
# print(some_integers)

def get_sum_two_numbers(a, b):
    return a + b


def get_sum_three_numbers(a, b, c):
    return a + b + c


def get_sum(*nums: int | float) -> int | float:
    """
    Функция возвращает сумму всех аргументов
    :param nums: список чисел
    :return: сумма всех чисел
    """
    print(f'{type(nums)=}')
    print(f'{nums=}')
    return sum(nums)


result = get_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'{result=}')

# TODO Практика
"""
Обновите функцию is_palindrome так, чтобы она принимала неограниченное количество строк
а на выходе возвращала словарь, где ключ - это исходная строка, а значение - результат проверки на палиндром (true/false)
"""


def is_palindromes(*strings: str, bad_sym: list[str] = BAD_SYM) -> dict[str, bool]:
    """
    Функция проверяет является ли строка палиндромом.
    :param strings: строки на проверку
    :return: словарь, где ключ - это исходная строка, а значение - результат проверки на палиндром (true/false)
    """
    result = {}
    for string in strings:
        pripare_string = ''.join([sym for sym in string if sym not in bad_sym]).lower()
        result[string] = pripare_string == pripare_string[::-1]

    return result


palindromes = ['А роза упала на лапу Азора', 'Аргентина манит негра', 'Sum summus mus', 'дед', "репа"]
result = is_palindromes(*palindromes)
print(f'{result=}')

result2 = [is_palindromes(palindrome) for palindrome in palindromes]
print(f'{result2=}')


def get_prepared_string(string: str, bad_sym: list[str] = BAD_SYM) -> str:
    """
    Функция возвращает строку, где удалены все символы из bad_sym и приведена к нижнему регистру
    :param string: строка для обработки
    :param bad_sym: список символов для удаления
    :return: обработанная строка
    """
    return ''.join([sym for sym in string if sym not in bad_sym]).lower()


def is_palindromes(*strings: str, bad_sym: List[str] = BAD_SYM) -> Dict[str, bool]:
    """
    Функция проверяет является ли строка палиндромом.
    :param bad_sym: список символов для удаления (запятые, пробелы и т.д.)
    :param strings: строки на проверку
    :return: словарь, где ключ - это исходная строка, а значение - результат проверки на палиндром (true/false)
    """
    # return {string: get_prepared_string(string, bad_sym) == get_prepared_string(string, bad_sym)[::-1] for string in strings}

    result = {}
    for string in strings:
        prepared_string = get_prepared_string(string, bad_sym)
        result[string] = prepared_string == prepared_string[::-1]

    return result
