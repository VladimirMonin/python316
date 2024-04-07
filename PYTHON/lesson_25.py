""" 
Lesson 25
07.04.2024
Dataclasses
__bool__
__post_init__
интегрировали dataclass Book в парсер книг
dataclass как конфиг для класса
__call__
"""
from dataclasses import dataclass

"""
Практика!

1. Создайте dataclass Person c полями
first_name: str
last_name: str
age: int
city: str
---
2. Опишите post __init__ метод, который будет проверять, что
1. first_name и last_name - строки, длинной не менее 2 символов
2. age - число от 0 до 150
3. city - строка, длинной не менее 2 символов
---
3. Опишите __bool__ метод, который будет возвращать True, если 
возраст человека больше 18 лет, иначе False
---
4. Создайте список экземпляров класса Person
---
5. Пройдитесь по нему циклом (можно comrehension) и соберите 
через if в новый список только тех, кто старше 18 лет
---
"""