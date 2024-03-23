"""
Lesson 20
23.03.2024
ООП
Нейминг
ключевое слово class
Создание экземпляра класса
Проверка типа объекта
"""
# Нейминг
"""
Классы в Python называются с большой буквы
Классы в Python называются в единственном числе
Классы в Python называются существительными
Классы в Python называются CamelCase
"""


# ключевое слово class

class Person:
    pass


# Создание экземпляра класса
person = Person()
person2 = Person()
print(person)
print(person2)
# <__main__.Person object at 0x000001C1A8FC3170>
# main - имя модуля
# Person - имя класса
# 0x000001C1A8FC3170 - адрес в памяти
print(type(person))
