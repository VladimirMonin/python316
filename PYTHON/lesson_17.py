"""
Lesson 17
03.03.2024
- Анонимные функции
- lambda
- map + lambda
- filter + lambda
- sorted + lambda
- сортировка по 2м признакам
- generators?
"""
from pprint import pprint
from typing import Tuple


# Генераторы - это функции, которые возвращают итераторы
# Итератор - это объект, который возвращает свои элементы по одному за раз
# Генераторы создаются с помощью ключевого слова yield - в переводе "давать", "уступать"
# Генераторы могут быть бесконечными
# Генераторы могут быть использованы в циклах for, в списковых включениях, в функции sum, max, min и т.д.
# Генераторы могут быть переданы в функцию list, чтобы получить список из всех значений генератора
# Генераторы могут быть переданы в функцию next, чтобы получить следующее значение генератора
# Генераторы могут быть однострочными (генераторное выражение)

# Пример генератора
def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))  # StopIteration

for i in my_generator():
    print(i)


def my_generator_2(n):
    for i in range(n):
        yield i


def my_list(n):
    return [i for i in range(n)]


# print(my_list(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))

# Получаем MemoryError
# print(my_list(100 ** 100))

# for i in my_generator_2(100 ** 100):
#     print(i)

# for i in my_list(100 ** 100):
#     print(i)

# Генераторное выражение
gen = (i for i in range(10))

print(next(gen))
gen_list = list(gen)

print(gen_list)
# print(next(gen_list)) # TypeError: 'list' object is not an iterator

map_list = (map(lambda x: x ** 2, range(10)))
print(next(map_list))
print(next(map_list))
print(next(map_list))
print(next(map_list))
print(next(map_list))

for i in map(lambda x: x ** 2, range(10000000000000000000000000000000000000000000000000000)):
    if i == 778446231616:
        print(f'Found {i}')
