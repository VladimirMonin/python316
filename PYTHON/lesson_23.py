"""
Lesson 23
31.03.2024
Цепочка наследования
Множественное наследование
Конфликт имен
Метод разрешения конфликтов
Миксины
"""


class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health


class Elf(Character):
    def __init__(self, name: str, health: int, mana: int):
        super().__init__(name, health)
        self.mana = mana


class MageElf(Elf):
    def __init__(self, name: str, health: int, mana: int, damage: int):
        super().__init__(name, health, mana)
        self.damage = damage


me = MageElf('Elf', 100, 100, 100)
# MRO - Method Resolution Order - порядок разрешения методов
print(MageElf.mro())
