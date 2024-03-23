"""
Lesson 20
23.03.2024
ООП
Нейминг
ключевое слово class
Создание экземпляра класса
Проверка типа объекта
Атрибуты класса
"""


# атрибуты класса

class Person:
    name = 'Дмитрий'


Person.name = 'Александр'

# Создание экземпляра класса
person = Person()
person2 = Person()
person2.name = 'Алексей'
Person.name = 'Иван'
print(person.name)
print(person2.name)
