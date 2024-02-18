"""
Lesson 11
04.02.2024
- CSV - формат данных
- Модуль csv
- Reader
- Writer
- Запись в файл
- Чтение из файла
- Reader
- Writer
    - writerows - пишет список списков в файл
    - writerow - пишет список в файл
- DictReader
- DictWriter
- writeheader - запись заголовков столбцов
- Адаптация CSV для Excel
- JSON
- Модуль json
- dumps
- loads
- dump
- load
- Indent
- ASCII false

# Исклчения (продолжим от сюда)
- try
- except
- else
- finally
"""
from tabulate import tabulate

# CSV - comma separated values (значения, разделенные запятыми)

student_list = [
    ['Имя', 'Фамилия', 'Возраст'],
    ['Иван', 'Иванов', 23],
    ['Петр', 'Петров', 25],
    ['Мария', 'Сидорова', 22],
]

# Модуль csv
import csv

# Запись в файл через writerows - пишет список списков в файл
# with open('students.csv', 'w', encoding='windows-1251') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerows(student_list)

# Дозапись в файл через writerow - пишет список в файл
# with open('students.csv', 'a', encoding='windows-1251') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerow(['Ярослав', 'Кунин', 23])

# Чтение из файла через reader - возвращает список списков
# with open('students.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.reader(file, delimiter=';')
#     print(reader)
#     print(list(reader))

# DictReader - возвращает список словарей
# with open('students.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     print(list(reader))

# DictWriter - пишет список словарей в файл, заголовки столбцов НЕ пишем
# with open('students.csv', 'a', encoding='windows-1251') as file:
#     fieldnames = ['Имя', 'Фамилия', 'Возраст']
#     writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
#     # writer.writeheader() # Запись заголовков столбцов
#     writer.writerow({'Фамилия': 'Николаева', 'Возраст': 33, 'Имя': 'Никола'})

# # todo Практика
# """
# 1. Прочитать и вывести на экран (список словарей) данные из файла
# 2. Сделать отображение данных в виде таблицы в терминале (tabulate)
# 3. Введите данные о студенте через input и программа скажет, был ли такой студент на занятии
#
# """
#
# #  2. Печатаем на tabulate список словарей
# data = [{'Имя': 'Иван', 'Фамилия': 'Иванов', 'Возраст': '23'},
#         {'Имя': 'Петр', 'Фамилия': 'Петров', 'Возраст': '25'},
#         {'Имя': 'Анна', 'Фамилия': 'Сидорова', 'Возраст': '22'},
#         {'Имя': '33', 'Фамилия': 'Никола', 'Возраст': 'Николаева'},
#         {'Имя': 'Никола', 'Фамилия': 'Николаева', 'Возраст': '33'}
#         ]
#
# # pip install tabulate
# from tabulate import tabulate
#
# # print(tabulate(data, headers='keys', tablefmt='grid'))
#
# # Читаем данные список словарей из group - студенты
# with open('group.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     students = list(reader)
#     # print(students)
#
# # Выводим данные в виде таблицы
# # print(tabulate(students, headers='keys', tablefmt='grid'))
# print(students)
#
# # Вводим данные о студенте через input
# name = input('Введите имя студента: ')
# """
# Первое присоединение': '2/03/24, 1:01:25 PM', 'Последний уход
# """
#
# # Проверяем был ли такой студент на занятии
# row_name = name.replace(' ', '').lower()
#
# for student in students:
#     row_student = student.get('Имя', '').replace(' ', '').lower()
#     if row_name in row_student:
#         print(f'{student.get('Имя', '')}был на занятии\n'
#               f'Дата первого присоединения: {student["Первое присоединение"]}\n'
#               f'Дата последнего ухода: {student["Последний уход"]}')
#         break
# else:
#     print(f'{name} не был на занятии')

"""
JSON - JavaScript Object Notation (объектная нотация JavaScript)
Одного объекта. 
Поэтому в JSON можно хранить только один объект. Мы не можем использовать флаг a
Он сломает файл.

Если нам надо дописать в JSON, читаем, добавляем данные, и ПЕРЕЗАПИСЫВАЕМ файл.
"""

# JSON
import json

# dumps - преобразует объект в строку
# loads - преобразует строку в объект
# dump - записывает объект в файл
# load - читает объект из файла


# json_waether_string = """{"coord":{"lon":30.2642,"lat":59.8944},"weather":[{"id":802,"main":"Clouds",
# "description":"переменная облачность","icon":"03d"}],"base":"stations","main":{"temp":0.15,"feels_like":-4.73,
# "temp_min":-1.4,"temp_max":0.71,"pressure":980,"humidity":86},"visibility":10000,"wind":{"speed":5,"deg":240},
# "clouds":{"all":40},"dt":1707037048,"sys":{"type":2,"id":197864,"country":"RU","sunrise":1707026819,
# "sunset":1707056313},"timezone":10800,"id":498817,"name":"Санкт-Петербург","cod":200}"""
#
# # Преобразуем строку в объект
# print(type(json_waether_string))
# python_weather_dict = json.loads(json_waether_string)
# print(type(python_weather_dict))
# print(python_weather_dict)
# # Переводим обратно в строку
# json_weather_string = json.dumps(python_weather_dict)
# print(type(json_weather_string))
# print(json_weather_string)

# person_dict = {'name': 'Женя',
#                'age': 30,
#                'job': 'разраб',
#                'salary': 1000.0,
#                'skills': ['python', 'git', 'linux'],
#                'married': True,
#                'hobbies': None,
#                }
#
# print(json.dumps(person_dict, indent=4, ensure_ascii=False))
#
# # Запись в файл
# with open('person.json', 'a', encoding='utf-8') as file:
#     json.dump(person_dict, file, indent=4, ensure_ascii=False)
#
# Чтение из файла
with open('person.json', 'r', encoding='utf-8') as file:
    person = json.load(file)
    print(person['name'])

# # TODO Практика
# """
# 1. Сохранить данные о присутствии студентов на занятии в JSON файл
# 2. Открыть этот JSON файл и вывести данные в терминале в виде таблицы tabulate
# """
#
# with open('group.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     students = list(reader)
#
# # Пишем это в JSON файл
# with open('students.json', 'w', encoding='utf-8') as file:
#     json.dump(students, file, indent=4, ensure_ascii=False)
#
# # Читаем из JSON файла
# with open('students.json', 'r', encoding='utf-8') as file:
#     students = json.load(file)
#     print(students)
#     print(tabulate(students, headers='keys', tablefmt='grid'))


# print(0 / 1)
# print('s' * 5)
# print('s' / 5)
# print('Lesson 11 done')

while True:
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))

        print(a / b)
    # Любое исклчение и мы даем псевдоним e
    # except Exception as e:
    #     print(f'Ошибка: {e}')
    #     continue
    except ZeroDivisionError as e:
        print(f'Ошибка: {e}')
        continue
    except ValueError as e:
        print(f'Ошибка: {e}')
        continue
    else:
        print('Все хорошо')
        break
    finally:
        print('Это будет выполнено в любом случае')
