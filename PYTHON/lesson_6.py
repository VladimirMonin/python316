"""
Lesson 6
20.01.2024
- for else
- operators
- while else
   - Итерируемые объекты
    - Строки
    - Списки
    - Кортежи
    - Словари
    - Множества
- Методы списков
- range
- append split join
- другие методы списков
- практика с count
- pop
- comprihanshions

Завтра
# Вложенные компрехеншены + вложенные списки
# Проверка пароля циклом
- вложенные списки
- random
- tabulate ?
- set
"""

# Список с паролями, один из них с пробелом
# passwords = ['qwerty', '12345', 'password', 'пароль', 'пароль123']
# bad_passwords = []
# # Проверка наличия пробела в пароле
# good_passwords = []
# for password in passwords:
#     if ' ' in password:
#         # print(f'Пароль "{password}" содержит пробелы')
#         bad_passwords.append(password)
#         continue
#     good_passwords.append(password)
#     # print(f'Пароль "{password}" корректный')
#
# if bad_passwords:
#     bad_passwords_string = ', '.join(bad_passwords)
#     print(f'Плохие пароли: {bad_passwords_string}')
# else:
#     good_passwords_string = ', '.join(good_passwords)
#     print(f'Все пароли корректные: {good_passwords_string}')
#
# # Методы списков
# # .append - добавляет элемент в конец списка
# # .insert - добавляет элемент в список по индексу
# # .join - объединяет список в строку по разделителю
# # .split - разделяет строку в список по разделителю
# # .count - возвращает количество элементов в списке
# # .extend - расширяет список другим списком
# # .pop - возвращает и удаляет элемент из списка по индексу
# # .remove - удаляет элемент из списка по значению
# # .insert - добавляет элемент в список по индексу
# # .index - возвращает индекс элемента
# # .sort - сортирует список
# # .reverse - разворачивает список
# # .clear - очищает список
# # .copy - возвращает копию списка
#
# # append - добавляет элемент в конец списка
# # range - генератор последовательности (start, stop, step)
# some_list = list(range(10))
# some_sym_list = list('Привет, Python!')
# print(f'{some_list=}')
# print(f'{some_sym_list=}')
#
# some_list.append(10)
# print(f'{some_list=}')
#
# result_list = []
# for i in range(len(some_sym_list)):
#     element = some_sym_list[i]
#     string = f'{i}:{element}'
#     result_list.append(string)
#
# # print(f'{result_list=}')
# print(f'{"\n".join(result_list)}')
#
# # count - возвращает количество элементов в списке
# shop_list = ["молоко", "бананы", "чай", "конфеты", "мороженое",
#              "мОлОко", "бАнаны", "чАй", "кОнфеты", "мОрОженОе"
#              ]
# print(f'В списке всего молока: {shop_list.count("молоко")}')
#
# # Как правильно посчитать количество молока?
# # 1. Цикл. + lower потом count (или сразу считаем через счетчик)
# # 2. Собрать в строку, привести к нижнему регистру, посчитать через count
# # 3. Comprehension + lower потом count (или сразу считаем через счетчик)
#
# # 1. Цикл. + lower потом count (или сразу считаем через счетчик)
# new_lower_shop_list = []
# for product in shop_list:
#     new_lower_shop_list.append(product.lower())
#
# print(f'В списке всего молока: {new_lower_shop_list.count("молоко")}')
#
# # 2. Собрать в строку, привести к нижнему регистру, посчитать через count
# new_lower_shop_str = ', '.join(shop_list).lower()
# new_lower_shop_list = new_lower_shop_str.split(', ')
# print(new_lower_shop_list)
# milk_count = new_lower_shop_list.count('молоко')
# print(f'В списке всего молока: {milk_count}')
#
# print(f'В списке всего молока: {", ".join(shop_list).lower().count("молоко")}')

new_lower_shop_list = ['молоко', 'бананы', 'чай', 'конфеты', 'мороженое', 'молоко', 'бананы', 'чай', 'конфеты',
                       'мороженое']

# pop - возвращает и удаляет элемент из списка по индексу (по умолчанию последний)
# insert - добавляет элемент в список по индексу
# extend - расширяет список другим списком
# sort - сортирует список
#
# print(f'{new_lower_shop_list=}')
# pop_default_result = new_lower_shop_list.pop(-2)
# print(f'{pop_default_result=}')
# print(f'{new_lower_shop_list=}')
#
# # insert - добавляет элемент в список по индексу
# new_lower_shop_list.insert(0, 'печенье')
# new_lower_shop_list.insert(0, 'меренговый рулет')
# new_lower_shop_list.insert(3, 'ананас')  # индекс третьего элемента +1
# print(f'{new_lower_shop_list=}')
#
# add_shop_list = ['хлеб', 'мясо', 'масло']
# # new_lower_shop_list.append(add_shop_list)
# new_lower_shop_list.extend(add_shop_list)
# print(f'{new_lower_shop_list=}')

# sort - сортирует список
# (по умолчанию по возрастанию)
# (reverse=True - по убыванию)
# (key=функция - по результату функции)
# (key=len - по длине элемента)

# new_lower_shop_list.sort()
# print(f'{new_lower_shop_list=}')
#
# new_lower_shop_list.sort(reverse=True)
# print(new_lower_shop_list)
#
# new_lower_shop_list.sort(key=len, reverse=True)
# print(new_lower_shop_list)

"""
Получите от пользователя строку текста.
Вам необходимо пройти по строке циклом и собрать новый список
В котором будет буква и количество ее вхождений в строку

Пример: мама
Результат: ['м:2', 'а:2', 'м:2', 'а:2']

*Усложняем
Пример: мама
Результат: [['м', 2], ['а', 2], ['м', 2], ['а', 2]]

** Еще усложняем
Пример: мама
Результат: [['м', 2], ['а', 2]] или ['м:2', 'а:2']
# Для адекватного счета нужно будет привести строку к одному регистру

# Как сделать уникальным список?
# создать список посчитанных букв, и перед подсчетом проверять наличие буквы в списке
"""

# user_input = input('Введите строку: ').lower()
# result_1 = []
# for letter in user_input:
#     # result_string = ''
#     # result_string += letter + ':'
#     # letter_count = user_input.count(letter)
#     # result_string += str(letter_count)
#     result_string = f"{letter}:{user_input.count(letter)}"
#     result_1.append(result_string)
#
# print(result_1)

# result_2 = []
# counted_letters = []
#
# for letter in user_input:
#     if letter in counted_letters:
#         continue
#     counted_letters.append(letter)
#     new_list = [letter, user_input.count(letter)]
#     # new_str = f'{letter}:{user_input.count(letter)}'
#     result_2.append(new_list)
#
# print(result_2)

# Comprehensions - списковые включения (списковые выражения)

shop_list = ['молОко', 'бананы', 'Чай', 'конфетЫ', 'мороженое']
comprehension_list = [product for product in shop_list]

list_ = []
for product in shop_list:
    list_.append(product)

comprehension_list_2 = [product.lower() for product in shop_list]

list_ = []
for product in shop_list:
    list_.append(product.lower())

comprehension_list_2 = [product.lower() for product in shop_list if "о" not in product.lower()]
comprehension_list_3 = [product for product in shop_list if "о" not in product.lower()]

list_ = []
for product in shop_list:
    if "о" not in product.lower():
        list_.append(product.lower())

print(comprehension_list_2)
print(comprehension_list_3)

# Если продукт начинается на б то None
comprehension_list_4 = [product if not product.lower().startswith('б') else None for product in shop_list]
print(comprehension_list_4)
