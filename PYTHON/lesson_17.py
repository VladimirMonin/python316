"""
Lesson 17
03.03.2024
- Анонимные функции
- lambda
- sort
- sorted
- map + lambda
- filter + lambda
- sorted + lambda
- сортировка по 2м признакам
- generators
- yield
- генераторное выражение
- ленивые вычисления
- all, any + генераторное выражение
- all, any + lambda
"""

products = ['apple', 'banana', 'orange', 'milk', 'bread', 'butter', 'cheese', 'tomato', 'cucumber', 'potato']

# Генераторное выражение с ленивыми вычислениями
gen = (x for x in products if x.startswith('b'))

for product in gen:
    print(product)

# all, any + генераторное выражение
print(all(x for x in products if x.startswith('b')))  # False

# all, any + lambda
print(all(map(lambda x: x.startswith('b'), products)))

# Проверка а все ли числа в генераторе являются четными
print(all(x % 2 == 0 for x in range(1000000000000000000000000000000000)))  # False
print(all(list((x % 2 == 0 for x in range(100000000)))))  # False
