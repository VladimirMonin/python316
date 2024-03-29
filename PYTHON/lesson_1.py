"""
Lesson 1
23.12.2023

Привет из 15 урока!

- Как создать проект в PyCharm
- Зачем нам нужны проекты?
- Концепция виртуального окружения
- Как создать вирутальное окружение?
    - Создавая проект
    - Вручную в "старой" папке
- Как активировать виртуальное окружение через графический интерфейс?
- Как активировать виртуальное окружение через консоль?
- В терминале нам надо быть на уровне папки с виртуальным окружением
(в нашем случае это папка .venv)
- pwd - показывает текущую директорию
- ls - показывает содержимое текущей директории
- cd - переход в директорию
- cd - переход на уровень выше
- Переход в корень - cd /
- Работа с пакетами

    pip freeze - показывает список установленных пакетов
    pip freeze > requirements.txt - сохраняет список установленных пакетов в файл
    pip install -r requirements.txt - устанавливает пакеты из файла
    pip install name_package==1.0.0 - устанавливает конкретную версию пакета
    pip install name_package - устанавливает последнюю версию пакета
    pip install name_package --upgrade - обновляет пакет
    pip install name_package name_package2 - устанавливает несколько пакетов

- Комментарии в Python
- Присваивание переменных
- Правила названия переменных
- Ключевые слова
- Основные типы данных в Python
- Строки
- Управляющие последовательности
- Type() - функция, которая показывает тип данных
- Len() - функция, которая показывает длину объекта
- F-строки
- input() - функция, которая позволяет вводить данные с клавиатуры
"""
print('Привет, python316!')  # Выводит текст в консоль

# Комментарий в одну строку

"""
Многострочный комментарий
"""

# Присваивание переменных
a = 5
b = 0
# print(id(a))
# print(id(b))

print(a + b)
print(a - b)
print(a * b)
# print(a / b)
print(a + b)

# Правила названия переменных
"""
- Имя переменной должно быть осмысленным
- Имя переменной должно быть на английском языке
- Существительное
- Имя переменной не должно быть транслитом (imya_peremennoy, familya, nazvanie_producta)
- Имя переменной не может начинаться с цифры
- Имя переменной должно начинаться с буквы или символа подчеркивания
- Имя переменной может содержать только буквы, цифры и символ подчеркивания
- Имя переменной не может содержать пробелов
- Имя переменной не может быть ключевым словом
- Имя переменной чувствительно к регистру
- Имя переменной не может содержать специальные символы

Ключевые слова:
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for,
from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

snake_lower_case - Используем для имен переменных и функций. 
CamelUpperCase - Используем для имен классов.
"""

# Ключевые слова
# for = 45
last_name = 5

# Основные типы данных в Пайтон
"""
- Строки (str) - функция str() - преобразование в строку (string)

- Числа
    - Целые числа (int) - функция int() - преобразование в целое число (integer)
    - Вещественные числа (float) - функция float() - преобразование в вещественное число (float)


- Булевые значения (bool) - функция bool() - преобразование в булево значение (boolean)
    - True
    - False

- None (NoneType) - функция NoneType() - преобразование в None (NoneType)

- Списки (list) - функция list() - преобразование в список (list)
- Кортежи (tuple) - функция tuple() - преобразование в кортеж (tuple)
- Множества (set) - функция set() - преобразование в множество (set)
- Словари (dict) - функция dict() - преобразование в словарь (dict)

"""

# Строки. Упорядоченная, неизменяемая последовательность символов
# Мы можем записать строку с помощью одинарных, двойных и тройных кавычек ("" '' """ ''')

string_1 = 'Я строка'
string_2 = "Я строка"
string_3 = """Я строка"""

poem = """
Скажи ка дядя ведь не даром
Москва спаленная пожаром
Французу отдана?

Ведь были ж схватки боевые
Да говорят еще какие
Недаром помнит вся Россия
Про день Бородина

                Лермонтов М.Ю.
"""
print(string_1)
print(string_2)
print(string_3)
print(poem)

# Управляющие последовательности
# \n - перенос строки
# \t - табуляция
# \ - экранирование

print('\\n')
print('\\t')

poem_2 = ("Скажи ка дядя ведь не даром\n"
          "Москва спаленная пожаром\n"
          "Французу отдана?\n\n"
          "Ведь были ж схватки боевые\n"
          "Да говорят еще какие\n"
          "Недаром помнит вся Россия\n"
          "Про день Бородина"
          "\n\n\t\t\tЛермонтов М.Ю.")

print(poem_2)

# Type() - функция, которая показывает тип данных
print(type('Я строка'))
print(type(poem_2))

# Len() - функция, которая показывает длину объекта
print(len(poem_2))
print(len('Я строка'))

# Форматирование строк
name = 'Сергей'
age = 30

# Способ 1 - конкатенация
hello_str = 'Привет, ' + name + '! Тебе ' + str(age) + ' лет.'
print(hello_str)

# Способ 2 - передать аргументы в принт
print('Привет, ', name, '! Тебе ', age, ' лет.', sep='++')  # sep='' - убирает пробелы между аргументами

# Способ 3 - метод format (просто для примера)
print('Привет, {}! Тебе {} лет.'.format(name, age))

# Способ 4 - f-строки (пользуйтесь этим)
print(f'Привет, {name}! Тебе {age} лет.')

# Способ 5 - метод format_map (просто для примера)
print('Привет, {name}! Тебе {age} лет.'.format_map({'name': name, 'age': age}))

# f-строки могут содержать выражения
result = (f'\n\nЭто стихотворение:\n{poem_2}\n\n'
          f'Его длина: {len(poem_2)} символов\n'
          f'Его тип данных: {type(poem_2)}\n')

print(type(result))

# input() - пустой ввод, позволяет оставить открытой консоль, после работы программы
# input(prompt) - функция, которая позволяет вводить данные с клавиатуры

input('Нажмите Enter, чтобы продолжить...')

message = input('Введите сообщение: ')
print(message)
# todo Практика
"""
Попросите пользователя ввести имя
Попросите пользователя ввести фамилию
Попросите пользователя ввести возраст
Создайте переменную под f-строку:

Вас зовут <имя> <фамилия>. Вам <возраст> лет. 
Через год вам будет <возраст + 1> лет.

Выведите результат на экран
"""
# input всегда возвращает строку
first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
age = input('Введите возраст: ')

result = (f'Вас зовут {first_name} {last_name}.\n'
          f'Вам {age} лет.\n'
          f'Через год вам будет {int(age) + 1} лет.\n')

print(result)
