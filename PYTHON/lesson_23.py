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


class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health


class Elf(Character):
    def __init__(self, name: str, health: int, mana: int):
        super().__init__(name, health)
        self.mana = mana


class Dwarf(Character):
    def __init__(self, name: str, health: int, stamina: int):
        super().__init__(name, health)
        self.stamina = stamina


# Этот класс вызовет проблему, потому что Elf и Dwarf имеют общего предка (Character),
# но Python не сможет однозначно определить, в каком порядке следует вызывать методы конструктора __init__
class ElfDwarf(Elf, Dwarf):
    def __init__(self, name: str, health: int, mana: int, stamina: int):
        super().__init__(name, health, mana, stamina)


ed = ElfDwarf('Эльф', 100, 100, 100)

"""
Чтобы вызвать конфликт в порядке разрешения методов (MRO) в Python, 
можно использовать множественное наследование с диамантовой проблемой. 

Диамантовая проблема возникает, когда два класса наследуют от одного 
базового класса, а затем еще один класс наследует от обоих этих классов. 

В Python это может привести к неоднозначности порядка вызова методов.
"""
