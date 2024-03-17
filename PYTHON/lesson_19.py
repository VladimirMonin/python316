"""
Lesson 19
17.03.2024
Декораторы
- Повторение материала
- Области видимости
- Практика с простым декоратором
- Декораторы с параметрами
- Практика с декоратором с параметрами
"""
import time
from typing import Callable, List, Dict, Any
from data.cities import cities

# def say_name2(name: str) -> Callable[[], None]:
#     # Олег тут
#     def say_goodbye():
#         print(f"Привет {name}!")
#
#     return say_goodbye
#
#
# sn: Callable = say_name2("Олег")
#
# sn()
# sn()
# sn()
# sn()
# # sn -> say_name2 -> say_goodbye -> name = "Олег"
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "lemon", "orange", "grape"]
#
# """
# аннотация List[str] указывает, что fruits должен быть списком строк,
# и аннотация Callable[[], List[str]] указывает, что возвращаемое значение является функцией,
# которая не принимает аргументы (пустые скобки) и возвращает список строк.
# """
#
#
# # Функция с кешем
# def sort_fruits(fruits: List[str]) -> Callable[[], List[str]]:
#     """
#     Сортируем список и сохраняем результат в кеш
#     :param fruits:
#     :return:
#     """
#     print(id(fruits))
#     cache: list = []
#     print(id(cache))
#
#     def sort() -> List[str]:
#         nonlocal cache
#         print(f'Внутри sort: {id(fruits)}')
#         if not cache or len(cache) != len(fruits):
#             cache = sorted(fruits)
#         return cache
#
#     return sort
#
#
# # Тестируем функцию с кешем
# print(id(fruits))
# sorter: Callable = sort_fruits(fruits)
# print(sorter())
#
# # Вызываем повторно с этими же данными (сортировка не будет произведена - вернется кеш)
# print(sorter())
#
# # # Добавляем новый фрукт
# fruits.append("apples")
#
# # # Пересортируем
# print(sorter())
#
# print(fruits)

"""
time.perf_counter() — это функция из модуля time в стандартной библиотеке Python, которая предоставляет доступ к 
монотонному счётчику времени с наивысшим доступным разрешением для измерения коротких промежутков времени. 
Вот несколько ключевых моментов об time.perf_counter():

Монотонность: Этот счетчик является монотонным, что означает, что его значения никогда не уменьшаются. 
Это важно для измерения временных интервалов, так как это гарантирует, что разница между концом и началом 
интервала всегда будет положительной или нулевой, даже если системные часы изменяются.

Высокое разрешение: Функция предоставляет время с высокой точностью, что делает ее идеальной для замера 
времени выполнения операций, особенно когда требуется измерить очень короткие промежутки времени.

Независимость от системного времени: Значение, возвращаемое time.perf_counter(), не зависит от системного 
времени и не подвержено изменениям из-за корректировки часов или перехода на летнее/зимнее время.

Использование: Эта функция часто используется для бенчмаркинга и профилирования кода, поскольку 
она предоставляет более точные измерения времени, чем time.time() или time.clock().

Платформонезависимость: time.perf_counter() работает на различных платформах, 
предоставляя стабильный интерфейс для замера времени.

Возвращаемое значение: Функция возвращает время в секундах как число с 
плавающей точкой. С момента запуска Python (или от момента первого вызова time.perf_counter(), 
точное определение зависит от реализации) до момента вызова функции.


start_time = time.perf_counter()
finish_time = time.perf_counter()
"""

# start_time = time.perf_counter()
# finish_time = time.perf_counter()
# result_time = finish_time - start_time
# print(f'Прошло {result_time:.10f} секунд')

"""
Практика!
1. Импортируйте time
2. Напишите декоратор check_time_decorator, который принимает функцию и возвращает функцию-обертку.
3. Внутри обертки замерьте время выполнения функции и выведите результат на экран.
4. Не забудьте передать аргументы в обертку, и вернуть результат выполнения функции.
"""


def check_time_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        # Засекаем время старта
        start_time = time.perf_counter()

        # Выполняем функцию
        result = func(*args, **kwargs)

        # Засекаем время окончания
        finish_time = time.perf_counter()

        # Считаем разницу
        result_time = finish_time - start_time
        print(f'Прошло {result_time:.10f} секунд')
        return result

    return wrapper


def log_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        # Готовим данные для логирования
        func_name = func.__name__  # Имя функции в виде строки
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join([f'{key}={value}' for key, value in kwargs.items()])
        time_now = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

        # Получаем результат выполнения функции
        result = func(*args, **kwargs)
        result_str = str(result)[:50]

        # Пишем в лог файл
        with open('log.txt', 'a') as file:
            file.write(f'[{time_now}] Вызвана функция {func_name} с аргументами {args_str[:50]}... и {kwargs_str}.'
                       f' Результат: {result_str}\n')

        print(f'[{time_now}] Вызвана функция {func_name} с аргументами {args_str[:50]}... и {kwargs_str}.')
        return result

    return wrapper


"""
Напишем 3 функции. Каждая будет принимать города и ключ для фильтрации
и возвращать фильтрованные данные.
1. Использует цикл for
2. Использует списковое включение
3. Использует встроенную функцию filter
"""


@check_time_decorator
def get_city_by_letter_in_for(cities: List[Dict[str, Any]], letter: str) -> List[str]:
    result_list: List[str] = []
    for city in cities:
        if letter in city['name']:
            result_list.append(city['name'])
    return result_list


@check_time_decorator
def get_city_by_letter_in_comprehension(cities: List[Dict[str, Any]], letter: str) -> List[str]:
    return [city['name'] for city in cities if letter in city['name']]


@check_time_decorator
def get_city_by_letter_in_filter(cities: List[Dict[str, Any]], letter: str) -> List[str]:
    return list(filter(lambda city: letter in city['name'], cities))


# Тестируем функции
letter = "Усть"
# print(cities)
# print(get_city_by_letter_in_for(cities, letter))
# print(get_city_by_letter_in_filter(cities, letter))
# print(get_city_by_letter_in_comprehension(cities, letter))

"""
Напишем 3 функции, которые будут принимать города и метод строки
который они будут применять к каждому городу, и возвращать список с названиями городов
преобразованными методом строки.
1. Использует цикл for
2. Использует списковое включение
3. Использует встроенную функцию map
"""


@check_time_decorator
def get_city_by_method_in_for(cities: List[Dict[str, Any]], method: Callable) -> List[str]:
    result_list: List[str] = []
    for city in cities:
        result_list.append(method(city['name']))
    return result_list


@check_time_decorator
def get_city_by_method_in_comprehension(cities: List[Dict[str, Any]], method: Callable) -> List[str]:
    return [method(city['name']) for city in cities]


@check_time_decorator
def get_city_by_method_in_map(cities: List[Dict[str, Any]], method: Callable) -> List[str]:
    return list(map(method, [city['name'] for city in cities]))


# Тестируем функции
method = str.upper


# print(get_city_by_method_in_map(cities, method))
# print(get_city_by_method_in_comprehension(cities, method))
# print(get_city_by_method_in_for(cities, method))

# print(len.__name__) # Имя функции в виде строки

@log_decorator  # Вторым зашел, первым вышел
@check_time_decorator  # Первым зашел, последним вышел
def get_city_by_method_in_map(cities: List[Dict[str, Any]], method: Callable) -> List[str]:
    return list(map(method, [city['name'] for city in cities]))


result = get_city_by_method_in_map(cities, method)

# Декораторы с параметрами
# Декораторы с параметрами - это функции, которые принимают параметры и возвращают декоратор.
"""
Внешняя функция - принимает параметры декоратора
Средняя функция - это декоратор, которая принимает функцию и возвращает обертку
Внутренняя функция - это обертка, которая параметры декоратора передает в обертку
"""


def print_decorator(func: Callable[[], None]) -> Callable[[], None]:
    # func - будет ссылаться на функцию, которую мы обернем, и лежать внутри wrapper
    def wrapper() -> None:
        print("Start")
        result = func()
        print("End")
        return result

    return wrapper


def print_decorator2(prefix: str = 'Привет', postfix: str = 'Пока') -> Callable:
    # Вторая функция передает обворачиваемую функцию в обвертку
    def decorator(func: Callable) -> Callable:
        # Третья функция - сама обвертка
        def wrapper(name: str) -> str:
            print(prefix)
            result = func(name)
            print(postfix)
            return result

        return wrapper

    return decorator


@print_decorator2('Hello', 'Goodbye')
def print_name(name: str) -> str:
    return f"Вызов функции print_name с параметром {name}"


result = print_name('Oleg')
print(result)


def check_time_decorator2(is_detail_log=False):
    def check_time_decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            # Засекаем время старта
            start_time = time.perf_counter()

            # Выполняем функцию
            result = func(*args, **kwargs)

            # Засекаем время окончания
            finish_time = time.perf_counter()

            # Считаем разницу
            result_time = finish_time - start_time

            if is_detail_log:
                print(f'Функция {func.__name__} выполнилась за {result_time:.10f} секунд')

            else:
                print(f'{result_time:.10f} секунд')

            return result

        return wrapper

    return check_time_decorator


@log_decorator  # Вторым зашел, первым вышел
@check_time_decorator2(is_detail_log=True)  # Первым зашел, последним вышел
def get_city_by_method_in_map(cities: List[Dict[str, Any]], method: Callable) -> List[str]:
    return list(map(method, [city['name'] for city in cities]))


result = get_city_by_method_in_map(cities, method)
