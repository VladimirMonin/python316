"""
Lesson 5
14.01.2024

- Итерируемые объекты
    - Строки
    - Списки
    - Кортежи
    - Словари
    - Множества

- Итерация
- For - else
- While - else
- # Списки - упорядоченные изменяемые коллекции объектов произвольных типов
- Знакомство с методами списков
"""
# Строка как итерируемый объект
#
# some_string = 'Привет, Python316!'
# some_int = 123
#
# only_alpha = ''
# only_digit = ''
#
# for symbol in some_string:
#     if symbol.isalpha():
#         only_alpha += symbol
#     elif symbol.isdigit():
#         only_digit += symbol
#
# some_string_2 = "Сказка о рыбаке и рыбке"
# # счетчик можно сделать тут
# for symbol in some_string_2:
#     if symbol.isdigit():
#         break
# else:
#     print('В этой строке нет цифр нет!')

# TODO
"""
Картавая задачка

Запросите у пользователя ввод строки.
Если в строке есть 2 буквы р или более, остановите цикл через break

Напишите что это плохое слово)

Иначе напишите что это хорошее слово
"""

# user_word = "БобР Добр!"
#
# BAD_LETTER = "р"
# THRESHOLD = 2
# counter = 0
#
# for letter in user_word:
#     if letter.lower() == BAD_LETTER.lower():
#         counter += 1
#         if counter >= THRESHOLD:
#             print(f'Слово {user_word} плохое!\n'
#                   f'В нем буква {BAD_LETTER} встречается {counter} раз')
#             break
# else:
#     print(f'Слово {user_word} хорошее!')
#
# if user_word.lower().count(BAD_LETTER.lower()) >= THRESHOLD:
#     print(f'Слово {user_word} плохое!')
# else:
#     print(f'Слово {user_word} хорошее!')

# While - else
# counter = 0
# some_str = 'Привет'
"""
Достижимые и недостижимые условия остановки цикла
"""
# while True:
#     counter += 1
#     print(f'Итерация номер {counter}')
#     if counter == 5:
#         break

# if some_str.isdigit():
#     break

# answer = ''
# while answer.lower() != 'stop':
#     answer = input('Введите команду или stop: ')
#     print(f'Вы ввели {answer}')
#
# input('Введите enter чтобы выйти')
#
# while True:
#     answer = input('Введите команду или stop: ')
#     if answer.lower() == 'stop':
#         break
#     print(f'Вы ввели {answer}')

# todo Практика
"""
Напишите переменную ответ = " "
Напишите переменную коллекция ответов = ''
Цикл пока ответ
    Если ответ
        Пока ответ существует, запрашивайте у пользователя 
        ответ - добавляйте ответ в коллекцию ответов
Выводите коллекцию ответов

"""

# answer = ' '
# answer_collection = ''
#
# while answer:
#     answer = input('Введите ответ или просто нажмите Enter: ')
#     if answer:
#         answer_collection += answer + '\n'
#         continue
#     break
#
# print(answer_collection)

# string_1 = 'Привет'
# string_2 = 'Привет'
# string_3 = 'Привет'
#
# print(string_1, string_2, string_3, sep='\n')

# Списки - упорядоченные изменяемые коллекции объектов произвольных типов
# Создание пустого списка
empty_list = []
empty_list = list()

# Создание списка с данными
some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
some_list1 = ["Привет", 316, 3.14, True, [1, 2, 3]]

# Изменяемость
print(some_list1)
print(some_list1[0])
some_list1[0] = 'Здравствуй'
print(some_list1[0])
print(some_list1)
# some_list2 = list('Привет, Python!')
# print(some_list2)

# user_input = "молоко, банан, шоколадный дед мороз, картофель"
# user_product_list = user_input.split(', ')
# print(user_product_list)
#
# for product in user_product_list:
#     print(f'А еще куплю {product}', end='! ')

user_product_list = ['молоко', 'банан',
                     'шоколадный дед мороз', 'картофель']

# for product in user_product_list:
#     print(' ', end='')
#     for symbol in product:
#         print(symbol, end='')

print(', '.join(user_product_list).capitalize())

# Todo Практика
"""
(это можно сделать через цикл for + count + f-строки)
(или через индексы списков, или через enumerate)

Напишите программу которая принимает от пользователя список
продуктов и выводит его на экран в формате:
1. Продукт 1
2. Продукт 2
3. Продукт 3
"""

user_input = "молоко, банан, шоколадный дед мороз, картофель".split(', ')
# num_count = 1
#
# for product in user_input:
#     print(f'{num_count}. {product.capitalize()}')
#     num_count += 1

# enumerate
for num, product in enumerate(user_input):
    print(f'{num + 1}. {product.capitalize()}')
