"""
Lesson 10
- Разбор домашнего задания (Генератор пословиц)
- Разбор домашнего задания (Игра Города)
- Кодировка текста
- Виды кодировок
- ascii - american standard code for information interchange
- Кодировка UTF-8
- Кодировка Windows-1251
- ord - функция которая добывает номер в таблице символов
- chr - функция которая добывает символ по номеру в таблице символов
- эмоджи
- Сравнение строк
- Запись данных в файл
- open
- close
- указание пути (./, ../, ../../)
- флаги открытия файла
- read - чтение всего файла (возвращает строку)
- readline - чтение одной строки (достаем строки построчно до конца файла)
- readlines - чтение всех строк (возвращает список строк)
- read - чтение всего файла (возвращает строку - весь документ)
- with open
- writelines - запись списка строк в файл
- write - запись строки в файл
"""

# Кодировка текста
# Пробуем напечатать эмоджи
# print('😂')
# print('🤣')
# print('🤔')

# - ord - функция которая добывает номер в таблице символов
# - chr - функция которая добывает символ по номеру в таблице символов

# Получаем номер символа
# print(ord('A'))
# print(ord('🤔'))

# Получаем символ по номеру
# print(chr(65))
# print(chr(129300))

# Сравнение строк при помощи кодировки и номеров символов
# print(ord('A'))  # английская буква
# print(ord('B'))  # английская буква
# print(ord('А'))  # русская буква
# print(ord('a'))  # английская буква
# print(ord('b'))  # английская буква
# print(ord('а'))  # русская буква
#
# print('A' < 'А')  # True
# print('a' < 'а')  # Trueq

# Запись данных в файл - open
# open - функция для открытия файла
# Close - метод для закрытия файла
# Флаги открытия файла
# r - только чтение (если файла нет, то ошибка)
# w - только запись (если файла нет, то создается, если есть, то перезаписывается)
# a - только дозапись (если файла нет, то создается, если есть, то дозаписывается)

# read - чтение всего файла (возвращает строку)
# readline - чтение одной строки (достаем строки построчно до конца файла)
# readlines - чтение всех строк (возвращает список строк)

# write - запись строки в файл
# writelines - запись списка строк в файл
# ./ - от адреса текущего файла в котором код
# ../ - на уровень выше от адреса текущего файла в котором код
# ../../ - на два уровня выше от адреса текущего файла в котором код

# txt_file = open('./data/test.txt', 'a')
# txt_file.write('Еще одна строка\n')
# txt_file.close()

# Читаем файл
# txt_file = open('./data/test.txt', 'r')
# print(txt_file.read().replace('\n', '++'))
# print(txt_file.readline())
# for line in txt_file:
# print(line.strip())
#     print(line, end='')
# print(txt_file.readlines())
# result = [line.strip() for line in txt_file]
# print(result)

# Закрываем файл
# txt_file.close()

# Добавим в файл result через запись списка строк

# file = open('./data/test.txt', 'w', encoding='utf-8')
# result = [line + '\n' for line in result]
# file.writelines(result)
# file.close()

# Контекстный менеджер гарантирует закрытие файла и в случае ошибки в блоке with файл все равно закроется
with open('./data/test.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())

# todo Практика
"""
1.
Напишите программу, которая принимает от пользователя список покупок через запятую
Записывает его в файл используя контекстный менеджер и флаг 'a', а так же кодировку 'utf-8'

2. Пользователь вводит продукты которые он уже купил, разделенные запятой
Программа должна прочитать файл и удалить из списка продуктов те, которые уже куплены
Запись с флагом 'w' и кодировкой 'utf-8'
"""

# 1. Получаем список покупок от пользователя и удаляем пробелы
users_products = input('Введите список покупок через запятую: ').split(',')
users_products = [product.strip() for product in users_products]

# Запись списка покупок в файл
with open('./data/products.txt', 'a', encoding='utf-8') as file:
    for product in users_products:
        file.write(product + '\n')

# 2. Получаем список купленных продуктов от пользователя и удаляем пробелы
products_bought = input('Введите список купленных продуктов через запятую: ').split(',')
products_bought = [product.strip() for product in products_bought]

# Чтение списка покупок из файла и удаление купленных продуктов
with open('./data/products.txt', 'r', encoding='utf-8') as file:
    products = [product.strip() for product in file.readlines()]

# Отфильтровываем купленные продукты
remaining_products = [product for product in products if product not in products_bought]

# Перезапись файла с оставшимися продуктами
with open('./data/products.txt', 'w', encoding='utf-8') as file:
    for product in remaining_products:
        file.write(product + '\n')
