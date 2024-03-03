"""
Lesson 17
03.03.2024
- Анонимные функции
- lambda
- generators?
"""
from pprint import pprint
from typing import Tuple

from PYTHON.data.marvel import simple_set, small_dict, full_dict

full_list2 = [{'id': key, **value} for key, value in full_dict.items()]


# sorted + lambda
# sorted(iterable, key=lambda x: x['key'], reverse=True)

# Сортировка по ключу title

def sort_by_title(item):
    return item['title']


# sorted_list = sorted(full_list2, key=sort_by_title)
# pprint(sorted_list, sort_dicts=False)

# Это же + lambda
sorted_list = sorted(full_list2, key=lambda x: x['title'][-1], reverse=True)
# pprint(sorted_list, sort_dicts=False)

# Сортировка по ключу year
sorted_list = sorted(full_list2, key=lambda x: x['year'] if isinstance(x['year'], int) else 3000, reverse=True)


# pprint(sorted_list, sort_dicts=False)


# Сортировка по 2м признакам - нам надо вернуть кортеж

def sort_by_year_and_title(item: dict) -> Tuple[int, str]:
    if isinstance(item['year'], int):
        year = item['year']
    else:
        year = 3000

    title = item['title']

    return year, title
    # return item['year'] if isinstance(item['year'], int) else 3000, item['title']


sorted_list = sorted(full_list2, key=sort_by_year_and_title)
pprint(sorted_list, sort_dicts=False)
