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

"""
Практика!
Опишите класс игрового персоонажа
class Character
С атрибутами name: str, health: int, mana: int, damage: int
С методами:
- __init__
- __str__
- damage - нанесение урона возвращает 1 (int)
Опишите классы наследники
class Warrior(Character)
Переопределите метод damage, чтобы воин наносил урона *2

class Mage(Character)
Расширение метода.
Вызовите метод damage родительского класса, поместите результат в переменную
Добавьте к результату 10 и верните

"""
