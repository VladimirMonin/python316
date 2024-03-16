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
    # global a
    a = "шавуха"  # local
    print(f'Local: {a}')

    def inner_func():
        nonlocal a  # Выйдет на уровень выше
        a = 'бургер'
        print(f'Inner: {a}')

    inner_func()
    print(f'Local: {a}')


print(f'Global: {a}')  # global
some_func()
print(f'Global: {a}')  # global


# Мы можем использовать функции внутри функций в своих целях!

def say_name(name: str):
    # name - local in say_name
    def say_goodbye():
        print(f"Привет {name}!")

    say_goodbye()


say_name("Валера")


def say_name2(name: str) -> Callable[[], None]:
    # Олег тут
    def say_goodbye():
        print(f"Привет {name}!")

    return say_goodbye


sn: Callable = say_name2("Олег")
# sn2: Callable = say_name2("Вася")
# sn3: Callable = say_name2("Петя")
sn()
# sn2()
# sn3()

ppp = print
ppp('Hello')

"""
Пока sn ссылается на функцию say_name2, то она не будет удалена из памяти.
Соответственно и Олег останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к sn

sn -> say_name2 -> say_goodbye -> name = "Олег" 
"""
