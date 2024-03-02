"""
Lesson 16
1. Повторение
- comprehension
- условие в начале
- условие в конце
- list comprehension
- dict comprehension
- перепаковка данных

2. Функции высшего порядка
"""
from pprint import pprint

from data.marvel import simple_set, small_dict, full_dict

# 1.2. Словарные включения

# Простая копия small_dict
new_small_dict = {key: value for key, value in small_dict.items()}
# pprint(new_small_dict, sort_dicts=False)

# Условие после. Фильтрация - год не None
new_small_dict = {key: value for key, value in small_dict.items() if value is not None}
# pprint(new_small_dict, sort_dicts=False)

# Условие после. Фильмы где год выпуска не None и 2020 и новее
new_small_dict = {key: value for key, value in small_dict.items() if value is not None and value >= 2020}
# pprint(new_small_dict, sort_dicts=False)

# Условие после. Фильмы где год выпуска не None и 2020 и новее
# Замена символов в ключе
new_small_dict = {key.replace("Ч", "ЧЧ"): value for key, value in small_dict.items() if
                  value is not None and value >= 2020}
# pprint(new_small_dict, sort_dicts=False)

# Реплейс в ключе по условию, если в строке есть буква ё
new_small_dict = {key.replace("Ч", "ЧЧ") if 'ё' in key else key: value for key, value in small_dict.items() if
                  value is not None and value >= 2020}
# pprint(new_small_dict, sort_dicts=False)

# full_dict - получаем копию
new_full_dict = {key: value for key, value in full_dict.items()}
# pprint(new_full_dict, sort_dicts=False)

# Список словарей full_dict
full_list = [value for value in full_dict.values()]
# pprint(full_list, sort_dicts=False)

# Список словарей full_dict, добавляем внешний ключ как значение в каждый словарь в списке словарей
# Получаем список словарей с ключом 'id', который равен ключу словаря (key)
full_list2 = [{'id': key, **value} for key, value in full_dict.items()]
# pprint(full_list2, sort_dicts=False)

full_lst3 = [{'айди': key, 'название': value['title'], 'год': value['year'] if value['year'] != 'TBA' else 0} for
             key, value in full_dict.items()]
pprint(full_lst3, sort_dicts=False)
# Ключ id только внутри каждого словаря
