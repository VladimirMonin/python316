"""
Lesson 18
16.03.2024
Области видимости переменных
Переменные внутри функций
Функции внутри функций
Замыкания
Декораторы
Декораторы с параметрами
"""

from typing import Callable, List, Any

# Области видимости переменных

# 0. Built-in scope- встроенная область видимости
# Описаны все встроенные функции и переменные
print2 = 'Чебурек'
# Сломал принт!!!
print('Hello world')

# 1. Global scope - глобальная область видимости
print3 = 'Чебурек'  # global

# 2. Local scope - локальная область видимости
a = 'чебурек'  # global


def some_func():
    global a
    a = "шавуха"  # local
    print(f'Local: {a}')


some_func()
print(f'Global: {a}')  # global

# 4. Nonlocal scope - область видимости внутри вложенных функций
a = 'чебурек'  # global


def some_func():
    a = "шавуха"  # local
    print(f'Local: {a}')

    def inner_func():
        a = 'бургер'
        print(f'Inner: {a}')

    inner_func()


some_func()
print(f'Global: {a}')  # global
