"""
Lesson 17
03.03.2024
- Анонимные функции
- lambda
- generators?
"""
from pprint import pprint

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
pprint(sorted_list, sort_dicts=False)
