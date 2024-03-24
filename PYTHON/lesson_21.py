"""
Lesson 21
ООП - инкапсуляция
Понятие инкапсуляции
- Функция `hasattr()`
- Функция `delattr()`
- Функция `setattr()`
- Функция `getattr()`
- Атрибут `__dict__`
- Функция `dir()`
"""


# Функция `hasattr()` - проверяет наличие атрибута у объекта


# Создадим класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Создадим объект класса Person
person = Person('John', 30)

# hasattr() - проверяет наличие атрибута у объекта, это можно сделать через переменную
attr_for_check = 'name'
if hasattr(person, attr_for_check):
    print(f'Атрибут {attr_for_check} есть у объекта person')

# Функция setattr() - устанавливает значение атрибута у объекта
new_attr = 'surname'
new_attr_value = 'Doe'
setattr(person, new_attr, new_attr_value)

# Проверим, что атрибут установился
print(person.surname)

# Функция getattr() - получает значение атрибута у объекта
print(getattr(person, new_attr))

# Функция delattr() - удаляет атрибут у объекта
delattr(person, new_attr)
print(hasattr(person, new_attr))
