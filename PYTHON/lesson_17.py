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

from PYTHON.data.marvel import simple_set, small_dict, full_dict

full_list2 = [{'id': key, **value} for key, value in full_dict.items()]

# Фильтр (фильмы 2021 + сортировка по title в одну строку
result = sorted(filter(lambda x: x['year'] == 2021, full_list2), key=lambda x: x['title'])
pprint(result, sort_dicts=False)
