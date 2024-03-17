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
from typing import Callable, List


def say_name2(name: str) -> Callable[[], None]:
    # Олег тут
    def say_goodbye():
        print(f"Привет {name}!")

    return say_goodbye


sn: Callable = say_name2("Олег")

sn()
sn()
sn()
sn()
# sn -> say_name2 -> say_goodbye -> name = "Олег"

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
    print(id(fruits))
    cache: list = []
    print(id(cache))

    def sort() -> List[str]:
        nonlocal cache
        print(f'Внутри sort: {id(fruits)}')
        if not cache or len(cache) != len(fruits):
            cache = sorted(fruits)
        return cache

    return sort


# Тестируем функцию с кешем
print(id(fruits))
sorter: Callable = sort_fruits(fruits)
print(sorter())

# Вызываем повторно с этими же данными (сортировка не будет произведена - вернется кеш)
print(sorter())

# # Добавляем новый фрукт
fruits.append("apples")

# # Пересортируем
print(sorter())

print(fruits)
