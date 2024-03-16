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

# Мы можем использовать переменные для того, чтобы ссылаться на функции

ppp = print
ppp('Hello')


def sum_a_b(a, b):
    return a + b


new_name: Callable[[int, int], int] = sum_a_b

print(new_name(1, 2))

"""
Пока sn ссылается на функцию say_name2, то она не будет удалена из памяти.
Соответственно и Олег останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к sn

sn -> say_name2 -> say_goodbye -> name = "Олег" 
"""


# Делаем счетчик хранящий состояние

def counter(start: int = 0) -> Callable[[], int]:
    # Счетчик start
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1: Callable = counter(10)
c2: Callable = counter()

print(c1())
print(c1())
print(c1())

print(c2())
print(c2())
print(c2())

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "lemon", "orange", "grape"]

"""
аннотация List[str] указывает, что fruits должен быть списком строк, 
и аннотация Callable[[], List[str]] указывает, что возвращаемое значение является функцией, 
которая не принимает аргументы (пустые скобки) и возвращает список строк.
"""


# Функция с кешем
def sort_fruits(fruits: List[str]) -> Callable[[], List[str]]:
    """
    Сортируем список и сохраняем результат в кеш
    :param fruits:
    :return:
    """
    # fruits - local
    cache: list = []

    def sort() -> List[str]:
        nonlocal cache
        if not cache or len(cache) != len(fruits):
            cache = sorted(fruits)
        return cache

    return sort


# Тестируем функцию с кешем

sorter: Callable = sort_fruits(fruits)
print(sorter())

# Вызываем повторно с этими же данными (сортировка не будет произведена - вернется кеш)
print(sorter())

# # Добавляем новый фрукт
fruits.append("apples")

# # Пересортируем
print(sorter())

print(fruits)


# Первая декорация

def print_decorator(func: Callable[[], None]) -> Callable[[], None]:
    # func - будет ссылаться на функцию, которую мы обернем, и лежать внутри wrapper
    def wrapper() -> None:
        print("Start")
        func()
        print("End")

    return wrapper


def some_func() -> None:
    print("Вызов функции some_func")


f: Callable = print_decorator(some_func)
f()


@print_decorator
def some_func2() -> None:
    print("Вызов функции some_func2")


some_func2()
