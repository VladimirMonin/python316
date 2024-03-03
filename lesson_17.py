"""
Lesson 17
03.03.2024
- Анонимные функции
- lambda
- generators?
"""
from PYTHON.data.marvel import simple_set, small_dict, full_dict

# Sorted - функция высшего порядка
# Возвращает отсортированный список

simple_list = list(simple_set)

sorted_list = sorted(simple_list)
print(sorted_list)


def sort_by_last_letter(title: str) -> str:
    return title[-1]


# Используем свю функцию sort_by_last_letter
sorted_list = sorted(simple_list, key=sort_by_last_letter)
print(sorted_list)

full_list2 = [{'id': key, **value} for key, value in full_dict.items()]
