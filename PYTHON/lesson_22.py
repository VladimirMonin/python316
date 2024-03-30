"""
Lesson 22
30.03.2024

Концепция наследования
Наследование без init
Переопределение методов
Вызов метода родительского класса
super()
__init__ в дочернем классе без super
зачем нужен super в __init__ наследника
"""


class Character:
    def __init__(self, name: str, health: int, mana: int, damage: int, custom: str):
        """

        :param name:
        :param health:
        :param mana:
        :param damage:
        :param custom:
        """
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage
        self.custom = custom

    def __str__(self):
        return (f'Имя: {self.name}, Здоровье: {self.health}, Мана: {self.mana}, Урон: {self.damage}')

    def get_custom(self):
        return self.custom

    def get_damage(self):
        return self.damage


class Warrior(Character):
    """
    Класс воин, наследуется от класса Character
    """

    # Сделаем инициализатор без super
    def __init__(self, damage_mod: int, *args, **kwargs):
        """
        :param damage_mod: Модификатор урона
        :param
        
        """
        super().__init__(*args, **kwargs)
        self.damage_mod = damage_mod

    def damage(self):
        final_damage = super().get_damage() * self.damage_mod
        return final_damage


class Mage(Character):
    def damage(self):
        result = super().get_damage()
        return result + 10


warrior = Warrior(2, name='Warrior', health=100, mana=50, damage=10, custom='Warrior custom')
print(warrior)
# warrior.custom = 'Warrior custom'
warrior.get_custom()  # AttributeError: 'Warrior' object has no attribute 'custom'

# Список словарей с воинами

warriors = [
    {'name': 'Лучекусь', 'health': 100, 'mana': 50, 'damage': 10, 'custom': 'Warrior1 custom', 'damage_mod': 2},
    {'name': 'Святомяу', 'health': 100, 'mana': 50, 'damage': 10, 'custom': 'Warrior2 custom', 'damage_mod': 3},
    {'name': 'Великохвост', 'health': 100, 'mana': 50, 'damage': 10, 'custom': 'Warrior3 custom', 'damage_mod': 4},
]

# Создаем список воинов
# warriors_list = []
#
# for warrior in warriors:
#     warriors_list.append(Warrior(**warrior))


# comprehension
warriors_list = [Warrior(**warrior) for warrior in warriors]
