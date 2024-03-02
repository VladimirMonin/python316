"""
Lesson 16
1. Повторение
- comprehension

"""
from pprint import pprint

from data.marvel import simple_set, small_dict, full_dict

# 1. Повторение
# - comprehension

# 1.1. Списковые включения
simple_list = [film for film in simple_set]

# Условие в конце - фильтрация
simple_list1 = [film for film in simple_set if film.startswith('Ч')]

# Условие в начале - альтернативное значение
simple_list2 = [film.replace('-', '@') if '-' in film else film for film in simple_set]

# Комбо условий
simple_list3 = [film.replace('-', '@') if '-' in film else film for film in simple_set if film.startswith('Ч')]

pprint(f'{simple_list=}')
pprint(f'{simple_list1=}')
pprint(f'{simple_list2=}')
pprint(f'{simple_list3=}')
