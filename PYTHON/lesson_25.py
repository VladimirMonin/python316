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

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    growth: int
    city: str

    def __post_init__(self):
        assert self.validate_str_length(self.first_name, 3), 'Имя должно быть строкой длинной не менее 3 символов'
        assert self.validate_str_length(self.last_name), 'Фамилия должна быть строкой длинной не менее 3 символов'
        assert self.validate_integer(self.age, 0, 150), 'Возраст должен быть числом от 0 до 150'
        assert self.validate_str_length(self.city, 3), 'Город должен быть строкой длинной не менее 3 символов'
        assert self.validate_integer(self.growth, 50, 250), 'Рост должен быть числом от 50 до 250'

    def __bool__(self):
        return self.age > 18
    
    def validate_str_length(self, value, length=2):
        return isinstance(value, str) and len(value) >= length
    
    def validate_integer(self, value, min, max):
        return isinstance(value, int) and min <= value <= max
    




persons = [
    Person('Иван', 'Степененко', 25, 180, 'Москва'),
    Person('Лариса', 'Гузеева', 30, 200, 'Москва'),
]

adults = [person for person in persons if person]

# print(len(persons[0])) # TypeError: object of type 'Person' has no len()