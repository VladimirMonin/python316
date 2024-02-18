"""
Lesson 9
- Распаковка коллекций
- Итерация по словарям
- Методы словарей
- Импорт модулей
- If __name__ == '__main__'
- Хранение данных в словарях и в вложенных структурах
- Списки словарей
- Словари словарей
- Перепаковка данных
- Dict Comprehension
- Фильтрация данных (цикл и comprehension)
"""
from pprint import pprint

# Пример распаковки списка списков для tabulate
# students = [
#     ['Имя', 'Фамилия', 'Возраст', 'Группа'],
#     ['Иван', 'Иванов', 19, 'МЕ-111'],
#     ['Петр', 'Петров', 20, 'МЕ-111'],
#     ['Сидор', 'Сидоров', 19, 'МЕ-111'],
# ]
#
# for name, surname, age, group, *_ in students[1:]:
#     print(f'{name=}, {surname=}, {age=}, {group=}')
#
#
# student_1 = {
#     'name': 'Иван',
#     'surname': 'Иванов',
#     'age': 19,
#     'group': 'МЕ-111',
# }

# print(student_1.items())
#
# for key, value in student_1.items():
#     print(f'{key=}, {value=}')

# Методы словарей
# dict.keys() - возвращает коллекцию ключей словаря
# dict.values() - возвращает коллекцию значений словаря
# dict.items() - возвращает коллекцию пар ключ:значение словаря
# dict.update(other_dict) - обновляет словарь, добавляя пары ключ:значение из other_dict
# dict.get(key) - возвращает значение по ключу key, если ключа нет, возвращает None
# dict.get(key, default) - возвращает значение по ключу key, если ключа нет, возвращает default
# dict.copy() - возвращает копию словаря
# dict.pop(key) - удаляет пару ключ:значение по ключу key, возвращает значение
# dict.pop(key, default) - удаляет пару ключ:значение по ключу key, возвращает значение, если ключа нет, возвращает default
# dict.popitem() - удаляет последнюю пару ключ:значение, возвращает пару ключ:значение
# dict.clear() - очищает словарь
# dict.fromkeys(iterable, value) - создает словарь из iterable, где ключи - элементы iterable, а значения - value
# dict.setdefault(key, default) - возвращает значение по ключу key, если ключа нет, возвращает default, если default не указан, возвращает None
# dict.reverse() - изменяет порядок следования элементов словаря на обратный
# dict.sort() - сортирует элементы словаря

# CRUD - Create, Read, Update, Delete (прочитать, создать, обновить, удалить)
# Create
# Пустой словарь
# empty_dict = {}
# empty_dict = dict()

# Словарь с данными
# some_dict = {'ключ': 'значение', 'ключ 2': 'значение 2'}

# Создание запиcи в словаре
# 1. Присвоение значения по ключу
# some_dict['ключ 3'] = 'значение 3'

# 2. Обновление словаря
# some_dict['ключ 3'] = 'значение 3.1'
# print(some_dict)

# 3. Метод update
# some_dict.update({'ключ 3': 'значение 3.2',
#                   'ключ 4': 'значение 4',
#                   'ключ 5': 'значение 5',
#                   })

# print(some_dict)

# Delete
# 1. Удаление по ключу
# del some_dict['ключ 5']

# 2. Метод pop
# key4 = some_dict.pop('ключ 4')
# print(key4)

# 3. Метод popitem
# key = some_dict.popitem()
# print(key)
# print(some_dict)

# 4. Метод clear
# some_dict.clear()

# print(some_dict)

# Read
# 1. Получение значения по ключу
# some_dict = {'ключ': 'значение', 'ключ 2': 'значение 2'}
# print(some_dict['ключ5']) # KeyError
# Вернет значение по ключу, если ключа нет, то вернет None (или то, что указано вторым аргументом)
# print(some_dict.get('ключ5', 'Опциональный аргумент, None по-умолчанию'))  # None

# Работа с Marvel словарями из другого файла
import lesson_8
# Импортирует ВСЕ и оно доступно ниже
# Минусы
# 1. Не понятно что именно импортировалось
# 2. Возможны конфликты имен
# 3. Неудобно читать
# 4. Неудобно писать
# 5. Выполняются все команды из другого файла

# print(lesson_8.say_hello)

# from lesson_8 import *  # Импортирует ВСЕ и оно доступно ниже
# print(say_hello)

from lesson_8 import say_hello
from lesson_8 import say_hello as hello

print(say_hello)
# print(hello)

from data.marvel import (simple_set as marvel_simple_set,
                         small_dict as marvel_small_dict, full_dict as marvel_full_dict)

# print(marvel_full_dict)

# TODO - Сделайте импорт и принт
# TODO - marvel_small_dict - пересоберите этот словарь, чтобы в нем были фильмы не старше 2020 года и None
"""
1. Создать пустой словарь
2. Пройти циклом по ключам и значениям словаря marvel_small_dict.items()
3. Если год выпуска фильма от 2020 и новее (или None), то добавить в новый словарь
- new_dict[key] = value
4. Вывести новый словарь
"""
new_dict = {}

for key, value in marvel_small_dict.items():
    if value is None or value >= 2020:
        new_dict[key] = value

# print(new_dict)
# Красивый принт. sort_dicts=False - не сортировать словари по алфавиту, indent=4 - отступ 4 пробела
# pprint(new_dict, sort_dicts=False, indent=4)

# Comprihension - просто пересоберем словарь
# new_small_dict = {key: value for key, value in marvel_small_dict.items()}
# new_small_dict_2021 = {key: value for key, value in marvel_small_dict.items() if value == 2021}

# # TODO Практика Поисковик фильмов
# """
# 1. Запросите у пользователя поисковую фразу
# 2. Сделайте комприхеншн словаря, где ключ - название фильма, а значение - год выпуска
# - Он должен состоять только из тех фильмов, которые содержат поисковую фразу
# """
#
# search_phrase = input('Введите поисковую фразу: ')
# # films_result = {key: value for key, value in marvel_small_dict.items() if search_phrase in key}
#
# films_result = {key: value for key, value in marvel_small_dict.items()
#                 if search_phrase.lower().replace(' ', '').replace(':', '')
#                 .replace('-', '') in key.lower().replace(' ', '').replace(':', '').replace('-', '')}
#
# pprint(films_result, sort_dicts=False, indent=4)
#
# # Из marvel_full_dict получаем список словарей
# # 1. Вариант с методом values и функцией list
# marvel_full_list = list(marvel_full_dict.values())
# pprint(marvel_full_list, sort_dicts=False)
#
# # 2. Вариант с циклом
# marvel_full_list = []
#
# for values in marvel_full_dict.values():
#     marvel_full_list.append(values)
#
# pprint(marvel_full_list, sort_dicts=False)
#
# # 3. Вариант с comprehension
# marvel_full_list = [values for values in marvel_full_dict.values()]

# TODO - Пересобрать full_dict добавив ключ 'id' и значение из ключа 'id' из внешнего ключа словаря
result_list = []

for key, value in marvel_full_dict.items():
    value['id'] = key
    result_list.append(value)

# pprint(result_list, sort_dicts=False)

# Это же, на комприхеншн
# result_list = [value.update({'id': key}) or value for key, value in marvel_full_dict.items()]


result_list = [{**value, 'id': key} for key, value in marvel_full_dict.items()]

# То же, но распишем весь словарь ручками
result_list = [
    {
        'id': key,
        'title': value['title'],
        'year': value['year'] if value['year'] != 'TBA' else None,
        'stage': value['stage'],
    }
    for key, value in marvel_full_dict.items() if value['stage'] == 'Шестая фаза'

]

pprint(result_list, sort_dicts=False)
