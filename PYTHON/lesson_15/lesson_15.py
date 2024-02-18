"""
Lesson 15
18.02.2024
- функции высшего порядка
"""
from typing import Callable, Iterable, List

# map
# filter
# sorted

# Давайте напишем функцию, которая принимает *args
# и функцию, применяет эту функцию к каждому элементу *args, и возвращает список результатов

some_list = ['хлеб', 'молоко', 'яйца', 'сахар', 'мука']


def some_func(item: str) -> str:
    return item.upper()


def apply_func_to_list(func: Callable, *args: Iterable[str]) -> List[str]:
    result = []
    for item in args:
        result.append(func(item))

    return result


super_print = print
super_print('Hello, world!')

test_result = apply_func_to_list(some_func, *some_list)
print(f'{test_result=}')

# map - это встроенная функция, которая делает то же самое
# map(функция, итерируемый объект) -> map object (генератор)
# Это легко можно превратить в список

result = list(map(some_func, some_list))
result_comprihension = [some_func(item) for item in some_list]


# Filter - это встроенная функция, которая фильтрует элементы итерируемого объекта
# filter(функция, итерируемый объект) -> filter object (генератор)
# Функция для фильтрации должна возвращать True или False

def is_letter_in_string(item: str) -> bool:
    """
    Функция возвращает True если в строке есть буква а
    :param item:
    :return:
    """
    return 'а' in item


result = list(filter(is_letter_in_string, some_list))
result = [item for item in some_list if is_letter_in_string(item)]

print(f'{result=}')
