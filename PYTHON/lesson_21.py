"""
Lesson 21
ООП - инкапсуляция
Понятие инкапсуляции
- Функция `hasattr()`
- Функция `delattr()`
- Функция `setattr()`
- Функция `getattr()`
- Атрибут `__dict__` - словарь атрибутов объекта
- Функция `dir()`
- __repr__ - представление объекта ("техническое")
- __str__ - строковое представление объекта
"""


# Функция `hasattr()` - проверяет наличие атрибута у объекта


# Создадим класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        Мы видем это при прямом print(person)
        :return:
        """
        return f'Персона: {self.name}, {self.age} годиков'

    def __repr__(self):
        """
        Мы видим это при выводе объекта в списке
        :return:
        """
        return f'Person({self.name}, {self.age})'


# Создадим объект класса Person
person = Person('John', 30)

# __dict__ - словарь атрибутов объекта
print(person.__dict__)

# Установим атрибут объекту
person.__dict__['city'] = 'New York'

# Проверим наличие атрибута
print(person.__dict__)
print(hasattr(person, 'city'))  # True

# Словарь для создания экземпляра класса
data = {'name': 'John', 'age': 30}

# Создадим объект класса Person
person = Person(**data)
# Равносильно
person1 = Person(data['name'], data['age'])
person2 = Person(name="John", age=30)

# Список словарей в список экземпляров класса

data = [
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 25},
    {'name': 'Bob', 'age': 35},
]
# Создадим список экземпляров класса Person
persons = [Person(**item) for item in data]

# Выведем список экземпляров класса Person
# (увидим результат работы метода __repr__)
print(persons)
# Увидим результат работы метода __str__
print(persons[0])

# Увидим результат работы метода __str__
[print(person) for person in persons]
