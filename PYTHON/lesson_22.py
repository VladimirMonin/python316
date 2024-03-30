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


class Character:
    def __init__(self, name: str, health: int, mana: int, damage: int, custom: str):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage
        self.custom = custom

    def __str__(self):
        return (f'Имя: {self.name}, Здоровье: {self.health}, Мана: {self.mana}, Урон: {self.damage}')

    def get_custom(self):
        return self.custom

    def damage(self):
        return self.damage()


class Warrior(Character):
    # Сделаем инициализатор без super
    def __init__(self, name: str, health: int, mana: int, damage: int, damage_mod: int):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage
        self.damage_mod = damage_mod

    def damage(self):
        return self.damage * self.damage_mod


class Mage(Character):
    def damage(self):
        result = super().damage()
        return result + 10


warrior = Warrior('Warrior', 100, 50, 20, 2)
print(warrior)
# warrior.custom = 'Warrior custom'
warrior.get_custom()  # AttributeError: 'Warrior' object has no attribute 'custom'
