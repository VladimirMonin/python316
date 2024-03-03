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

# filter + lambda
# filter(func, iterable)

# Отберем ID меньше 10
# result = list(filter(lambda x: x['id'] < 10, full_list2))
# pprint(result)

# TODO: ищем фильмы с Тор в названии - печатаем
result = list(filter(lambda x: x['title'].startswith('Тор'), full_list2))

query = 'Железный'
result2 = list(filter(lambda x: query in x['title'], full_list2))
pprint(result2)
