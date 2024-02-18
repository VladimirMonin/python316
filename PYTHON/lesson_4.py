"""
Lesson 4: Ветвления
13.01.2024
- if - elif - else
- методы строк
- вложенные условия (плоская структура и "ёлочка" и одна длинная строка)
- пример с проверкой url адреса
- пример с проверкой email адреса
- дебаггер в PyCharm
    - точки останова
    - шаги выполнения
    - condition - условие остановки

- Методы строк - нюансы проверок методами _is
"""

# Методы строк
# .lower() - приводит строку к нижнему регистру
# .replace('что меняем', 'на что меняем') - заменяет подстроку в строке
# .split("разделитель") - разделяет строку на список строк по разделителю
# " + ".join() - объединяет список строк в одну строку с разделителем [1, 2, 3] -> "1 + 2 + 3"
# .upper() - приводит строку к верхнему регистру
# .capitalize() - приводит первый символ строки к верхнему регистру
# .title() - приводит первый символ каждого слова к верхнему регистру
# .strip() - удаляет пробельные символы, а также символы \n \t \r в начале и конце строки
# .lstrip() - удаляет пробельные символы, а также символы \n \t \r в начале строки
# .rstrip() - удаляет пробельные символы, а также символы \n \t \r в конце строки
# .count() - считает количество вхождений подстроки в строку
# .startswith() - проверяет, начинается ли строка с подстроки
# .endswith() - проверяет, заканчивается ли строка подстрокой
# .find() - возвращает индекс первого вхождения подстроки в строку (если не находит, то возвращает -1)
# .index() - возвращает индекс первого вхождения подстроки в строку (если не находит, то ValueError: substring not found
# .isalpha() - проверяет, состоит ли строка из букв
# .isdigit() - проверяет, состоит ли строка из цифр
# .isalnum() - проверяет, состоит ли строка из цифр или букв
# .isspace() - проверяет, состоит ли строка из пробельных символов
# .istitle() - проверяет, начинаются ли слова в строке с заглавной буквы
# .islower() - проверяет, состоит ли строка из символов в нижнем регистре
# .isupper() - проверяет, состоит ли строка из символов в верхнем регистре
# .istitle() - проверяет, начинаются ли слова в строке с заглавной буквы
# .rfind() - возвращает индекс последнего вхождения подстроки в строку
# .rindex() - возвращает индекс последнего вхождения подстроки в строку
# .format() - форматирует строку
# .isascii() - проверяет, состоит ли строка из символов ASCII
# .swapcase() - меняет регистр всех символов строки на противоположный

# Методы строк могут применяться цепочкой

city = "москва"
print(city.replace("А", "ОЙ").upper().count("ОЙ"))
print(city.upper().replace("А", "ОЙ").count("ОЙ"))

# Find и index
print(city.upper().replace("А", "ОЙ").find("ОЙ"))
print(city.upper().replace("А", "ОЙ").index("ОЙ"))

print(city.replace("А", "ОЙ").upper().find("ОЙ"))
# print(city.replace("А", "ОЙ").upper().index("ОЙ"))

# Strip, startswith, endswith
"""
Напишем анализатор url адресов.
Нам надо проверить что адрес начинается с http:// или https://
И что это доменная зона .com или .ru

После этого отрезать https:// и http://
"""

# url = "https://www.yandex.ru"
# url2 = "http://www.google.com"
# url3 = "hppts://www.google.club"
#
# URL = url3

# Не очень хороший вариант.
"""
1. Слишком длинная проверка
2. Слишком сложная проверка
3. Нет возможности пояснить что именно пошло не так
"""
# if (URL.startswith("https://") or URL.startswith("http://")) and (URL.endswith(".com") or URL.endswith(".ru")):
#     print("Адрес сайта корректный")
#     result_url = URL.lstrip("https://").lstrip("http://")
#     print(result_url)
#
# else:
#     print("Адрес сайта не корректный")

# Вариант "ёлочка" - немного лучше

# if (URL.startswith("https://") or URL.startswith("http://")):
#     if (URL.endswith(".com") or URL.endswith(".ru")):
#         print("Адрес сайта корректный")
#         result_url = URL.lstrip("https://").lstrip("http://")
#         print(result_url)
#
#     else:
#         print(f"Адрес сайта не корректный. Доменная зона .{URL.split('.')[-1]} не .com и не .ru")
#
# else:
#     print("Адрес сайта не корректный. Фиг знает почему")

# Плоский вариант проверки - наиболее оптимальный
# bad_log_string = ''
#
# if not (URL.startswith("https://") or URL.startswith("http://")):
#     bad_log_string += "Не указан протокол передачи данных\n"
#
# if not (URL.endswith(".com") or URL.endswith(".ru")):
#     bad_log_string += f"Доменная зона .{URL.split('.')[-1]} не .com и не .ru\n"
#
# if bad_log_string:
#     print(f'Адрес сайта не корректный.\nПричины:\n{bad_log_string}')

# TODO Практика - проверка email адреса
"""
Напишите программу, которая проверяет email адрес на корректность.
Правила корректности:
- email содержит символ @ ( + содержит всего один символ @)
- email не содержит пробелов

Пользователь вводит емейл, программа его проверяет
И выдает строку с отчетом или сообщение что все хорошо
"""
# SYMBOL_SNAIL_DOT_THRESHOLD = 2
#
# # email = input("Введите email: ")
# email = "v.m@@!aru"
# report = ''
#
# # Проверка что в email есть символы @
# if '@' not in email:
#     report += "Email не содержит символ @\n"
#
# # Проверка что в email есть только один символ @
# if email.count('@') > 1:
#     report += "Email содержит больше одного символа @\n"
#
# # Проверка что в email нет пробелов
# if ' ' in email:
#     report += "Email содержит пробелы\n"
#
# # Проверка через rfind что после @ есть точка и между ними есть символы (хотя бы один)
# last_dot_index = email.rfind('.')
# snail_index = email.rfind('@')
#
# # Проверка, что в целом, есть точка в email
# if last_dot_index == -1:
#     report += "Email не содержит точку\n"
#
# # Проверка, что после @ есть точка
# if snail_index > last_dot_index:
#     report += "Email не содержит точку после символа @\n"
#
# # Проверка, что между @ и точкой есть символы
# if last_dot_index - snail_index >= SYMBOL_SNAIL_DOT_THRESHOLD:
#     report += f"Email не содержит {SYMBOL_SNAIL_DOT_THRESHOLD} символов между @ и точкой\n"
#
# # Вывод отчета
# if report:
#     print(f'Email {email} не корректный\nПричины:\n{report}')
#
# else:
#     print(f'Email {email} корректный')
#

# Методы isalpha, isdigit, isalnum, islower, isupper,

password_1 = "1234567890"
password_2 = "asdfsf"
password_3 = "ASDFSF"
password_4 = "Asdfsf"
password_5 = "Asdfsf123"
password_6 = "Asdfs134&(sf"
password_7 = "&(&*^*&^*^&&^"

print('Isalpha')
print(f'{password_1.isalpha()=}')
print(f'{password_2.isalpha()=}')
print(f'{password_3.isalpha()=}')
print(f'{password_4.isalpha()=}')
print(f'{password_5.isalpha()=}')
print(f'{password_6.isalpha()=}')
print(f'{password_7.isalpha()=}')
print("\nIsdigit")
print(f'{password_1.isdigit()=}')
print(f'{password_2.isdigit()=}')
print(f'{password_3.isdigit()=}')
print(f'{password_4.isdigit()=}')
print(f'{password_5.isdigit()=}')
print(f'{password_6.isdigit()=}')
print(f'{password_7.isdigit()=}')
print("\nIsalnum")
print(f'{password_1.isalnum()=}')
print(f'{password_2.isalnum()=}')
print(f'{password_3.isalnum()=}')
print(f'{password_4.isalnum()=}')
print(f'{password_5.isalnum()=}')
print(f'{password_6.isalnum()=}')
print(f'{password_7.isalnum()=}')
print("\nIsupper")
print(f'{password_1.isupper()=}')
print(f'{password_2.isupper()=}')
print(f'{password_3.isupper()=}')
print(f'{password_4.isupper()=}')
print(f'{password_5.isupper()=}')
print(f'{password_6.isupper()=}')
print(f'{password_7.isupper()=}')
print("\nIslower")
print(f'{password_1.islower()=}')
print(f'{password_2.islower()=}')
print(f'{password_3.islower()=}')
print(f'{password_4.islower()=}')
print(f'{password_5.islower()=}')
print(f'{password_6.islower()=}')
print(f'{password_7.islower()=}')
