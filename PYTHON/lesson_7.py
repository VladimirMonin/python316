"""
Lesson 7
# Проверка пароля циклом
# Вложенные компрехеншены + вложенные списки
- вложенные списки
- tabulate ?
- random
- set

В следующих сериях!)
any - возвращает True если хотя бы один элемент списка True
all - возвращает True если все элементы списка True
set - множество и методы
"""

# Пример с проверкой пароля посимвольно

# password = 'tyFdgGSFsf&123'
#
# LEN_THRESHOLD = 8  # len
# NUM_THRESHOLD = 1  # isdigit
# UPPER_THRESHOLD = 1  # isupper
# SPEC_THRESHOLD = 1  # not isalnum
# LETTER_THRESHOLD = 2  # isalpha
#
# num_counter = 0
# upper_counter = 0
# spec_counter = 0
# letter_counter = 0
#
# report_list = []

# for symbol in password:
#     if symbol.isdigit():
#         num_counter += 1
#     elif symbol.isupper():
#         upper_counter += 1
#     elif not symbol.isalnum():
#         spec_counter += 1
#     elif symbol.isalpha():
#         letter_counter += 1
#
# if len(password) < LEN_THRESHOLD:
#     report_list.append(f'Длина пароля: {len(password)} меньше допустимой {LEN_THRESHOLD}')
#
# if num_counter < NUM_THRESHOLD:
#     report_list.append(f'Цифр в пароле: {num_counter} меньше допустимого {NUM_THRESHOLD}')
#
# if upper_counter < UPPER_THRESHOLD:
#     report_list.append(f'Заглавных букв в пароле: {upper_counter} меньше допустимого {UPPER_THRESHOLD}')
#
# if spec_counter < SPEC_THRESHOLD:
#     report_list.append(f'Спец символов в пароле: {spec_counter} меньше допустимого {SPEC_THRESHOLD}')
#
# if letter_counter < LETTER_THRESHOLD:
#     report_list.append(f'Букв в пароле: {letter_counter} меньше допустимого {LETTER_THRESHOLD}')
#
# if report_list:
#     print('Пароль не подходит по следующим параметрам:')
#     print('\n'.join(report_list))

# Пробуем обойти пароль в comprehension и составить список из 1 и 0 если условие выполняется
# digit_counter = sum([1 for symbol in password if symbol.isdigit()])
# digit_counter2 = len([1 for symbol in password if symbol.isdigit()])
#
# print(f'{digit_counter=}')
# print(f'{digit_counter2=}')

# sum - суммирует все элементы списка
# len - возвращает длину списка
# max - возвращает максимальный элемент списка
# min - возвращает минимальный элемент списка
# any - возвращает True если хотя бы один элемент списка True
# all - возвращает True если все элементы списка True

# TODO Практика comprehension
"""
Задача 1
1. Пользователь вводит слова через пробел
2. Программа преобразует слова в список
3. Comprehension собирает список из слов (дубликат)
4. Описываем comprehension который собирает список букв эр из слова
5. Выводим количество букв эр в списке

Регистронезависимость
"""

# user_input = input('Введите слова через пробел: ').split()
# user_input_list_double = [word for word in user_input]
# user_input_list_word_r = [word for word in user_input if 'р' in word.lower()]
# word_counter = len(user_input_list_word_r)
#
# print(f'Исходный список: {user_input}')
# print(f'Список из слов с буквой р: {user_input_list_word_r}')
# print(f'Количество слов с буквой р: {word_counter}')

# user_input = ['хлеб', 'молоко', 'яйца', 'масло',
#               'мука', 'сахар', 'соль', 'перец', 'колбаса', ]
# res = []
# for product in user_input:
#     if 'р' in product.lower():
#         for letter in product:
#             if letter.lower() == 'р':
#                 res.append(letter)
#
# print(res)
#
# # Comprihension внутри comprehension
#
# res = [letter for product in user_input if 'р' in product.lower() for letter in product if letter.lower() == 'р']
#
# print(res)

# Tabulate + список списков
# pip install tabulate

student_list = [
    ['ID', "Фамилия", "Имя", "Возраст", "Курс", "Группа"],
    ["1", "Иванов", "Иван", "22", "2", "БСТ162"],
    ["2", "Петров", "Семен", "21", "1", "БСТ161"],
    ["3", "Сидоров", "Семен", "21", "1", "БСТ161"],
    ["4", "Иванов", "Андрей", "22", "2", "БСТ162"],
    ["5", "Андреев", "Иван", "21", "1", "БСТ161"],

]

from tabulate import tabulate

# print(tabulate(student_list, tablefmt='html'))
html_table = tabulate(student_list, tablefmt='html')
html_doc = f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student list</title>

    <style>
        table {{
            border-collapse: collapse;
        }}

        td, th {{
            border: 1px solid black;
            padding: 5px;
        }}
    </style>
</head>
<body>
<h1>Student list</h1>
{html_table}
</body>
</html>
"""
# print(html_doc)
# Сохраним в html файл
# with open('student_list.html', 'w', encoding='utf-8') as f:
#     f.write(html_doc)

# user_choise_id = input('Выберите запись по id: ')
#
# result = ";".join([student for student in student_list if student[0] == user_choise_id][0])
# print(result)

# Как это было бы на циклах?
# result = None

# for student in student_list:
#     if student[0] == user_choise_id:
#         result = ";".join(student)
#         break

# random - модуль для генерации случайных чисел
# shuffle - перемешивает список
# choice - возвращает случайный элемент списка

from random import shuffle, choice, randint

# Генерируем рандомное число от 0 до 10 ВКЛЮЧИТЕЛЬНО
print(randint(0, 10))

# Список игр для розыгрыша
game_list = ['GTA3', 'Original Sin 2', 'Sims 4', 'Baldurs Gate 3',
             'Cyberpunk 2077', 'Witcher 3', 'Skyrim', 'Fallout 4', ]

# Добываем рандомную игру из списка
# index = randint(0, len(game_list) - 1)  # -1 или IndexError: list index out of range
# random_game = game_list[index]

# print(f'Победитель получает игру: {random_game}')
# удалим игру из списка по индексу
# game_list.remove(random_game)
# del game_list[index]

# Перемешаем список через shuffle
# a = shuffle(game_list) # None
# shuffle(game_list)
# random_game = game_list.pop()
# print(f'Победитель получает игру: {random_game}')
# print(game_list)

# Random.choice - возвращает случайный элемент списка
random_game = choice(game_list)
print(f'Победитель получает игру: {random_game}')

# Удаляем игру из списка
game_list.remove(random_game)

# Set - множество
# Множество - неупорядоченная коллекция уникальных элементов
# Элементы множества могут быть только неизменяемыми типами данных:
# int, float, tuple, str, frozenset, bool, NoneType
# Эти же типы данных являются хешируемыми
# Хеш - это некий уникальный идентификатор объекта

# Создание пустого множества
empty_set = set()
# empty_set = {} # Это не пустое множество, это пустой словарь!

# Создание множества с данными
some_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(some_set)
some_str = 'Тролололо лололо лололо, трололололо! Тролололо ло!'
some_list = list(some_str)
some_set = set(some_list)

print(some_list)
print(some_set)

# Получить список очищенный от дублей
clear_unique_list = list(set(some_list))

# Еще один вариант
set_comprihension = {letter.lower() for letter in some_str}
print(set_comprihension)

some_set_str = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(some_set_str)

game_set = {'GTA3', 'Original Sin 2', 'Sims 4', 'Baldurs Gate 3',
            'Cyberpunk 2077', 'Witcher 3', 'Skyrim', 'Fallout 4'}

print(game_set.pop())
print(game_set)

# Клуб знакомств - все знакомятся со всеми
# Сколько свиданий будет?

boys = {'Андрей', 'Вася', 'Миша', 'Саша', 'Петя'}
girls = {'Аня', 'Катя', 'Лена', 'Маша', 'Света'}

meetings = set()
user_input = 10

while len(meetings) != user_input or len(meetings) != len(boys) * len(girls):
    boy = boys.pop()
    girl = girls.pop()
    meet = f'{boy} and {girl}'
    meetings.add(meet)

print(meetings)
