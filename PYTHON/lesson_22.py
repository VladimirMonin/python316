"""
Lesson 22
30.03.2024

Концепция наследования
Наследование без init
Переопределение методов
Вызов метода родительского класса
super()
Вызов инициализатора родительского класса
"""


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}'

    def voice(self):
        print('Animal voice')


class Dog(Animal):
    def voice(self):
        # Animal.voice(self)
        super().voice()
        print('Woof woof')


class Cat(Animal):
    def voice(self):
        print('Meow meow')


dog = Dog('Bobik', 5)
print(dog)
dog.voice()
