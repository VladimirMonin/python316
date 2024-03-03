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

print(small_dict)

# Сортировка словаря по ключам на выходе словарь
# print((sorted(small_dict.items(), key=lambda x: x[0])))

# Сортировка словаря по значениям на выходе словарь
print((sorted(small_dict.items(), key=lambda x: x[1] if isinstance(x[1], int) else 3000, reverse=True)))
