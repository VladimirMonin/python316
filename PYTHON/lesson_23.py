"""
Lesson 23
31.03.2024
Цепочка наследования
Множественное наследование
Абстрактные классы
ABC
@abstractmethod
Конфликт имен
Метод разрешения конфликтов
Миксины
"""
from abc import ABC, abstractmethod


# Abstract Base Class

class Character(ABC):
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    @abstractmethod
    def say(self, text: str):
        print(f'{self.name} говорит: {text}')


class Thief(Character):
    def __init__(self, name: str, health: int, agility: int):
        super().__init__(name, health)
        self.agility = agility

    def say(self, text: str):
        super().say(text)


t = Thief('Вор', 100,
          50)  # TypeError: Can't instantiate abstract class Thief without an implementation for abstract method 'say'

c = Character('Персонаж', 100)  # TypeError: Can't instantiate abstract class Character with abstract methods say
t.say('Привет!')
