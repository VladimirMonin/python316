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
        self.is_alive = True

    def __str__(self):
        is_alive = 'Жив и здравствует.' if self.is_alive else 'Доблестно пал в бою'
        return f'Имя: {self.name}, Здоровье: {self.health}, Мана: {self.mana}, Урон: {self.damage}. {is_alive}'

    def get_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            print(f'Доблестно пал в бою {self.name}')

    def get_attack(self):
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

    def get_attack(self):
        final_damage = super().get_attack() * self.damage_mod
        return final_damage


class Mage(Character):
    def damage(self):
        result = super().get_damage()
        return result + 10


# Список словарей с воинами

warriors = [
    {'name': 'Лучекусь', 'health': 100, 'mana': 50, 'damage': 10, 'custom': 'Warrior1 custom', 'damage_mod': 2.1},
    {'name': 'Святомяу', 'health': 120, 'mana': 50, 'damage': 10, 'custom': 'Warrior2 custom', 'damage_mod': 2.2},
    {'name': 'Великохвост', 'health': 100, 'mana': 50, 'damage': 10, 'custom': 'Warrior3 custom', 'damage_mod': 2.1},
    {'name': 'Красноглаз', 'health': 140, 'mana': 50, 'damage': 10, 'custom': 'Warrior4 custom', 'damage_mod': 2.5},
    {'name': 'Хитрокусь', 'health': 100, 'mana': 50, 'damage': 10, 'custom': 'Warrior5 custom', 'damage_mod': 2.1},

]

# Создаем список магов

mages = [
    {'name': 'Фаеркусь', 'health': 90, 'mana': 50, 'damage': 10, 'custom': 'Mage1 custom'},
    {'name': 'Ледяной хвост', 'health': 95, 'mana': 50, 'damage': 10, 'custom': 'Mage2 custom'},
    {'name': 'Молнилап', 'health': 99, 'mana': 50, 'damage': 10, 'custom': 'Mage3 custom'},
    {'name': 'Пламявзгляд', 'health': 80, 'mana': 50, 'damage': 10, 'custom': 'Mage4 custom'},
    {'name': 'Водабрр', 'health': 75, 'mana': 50, 'damage': 10, 'custom': 'Mage5 custom'},

]

# Создаем список воинов
warriors_list = [Warrior(**warrior) for warrior in warriors]

# Создаем список магов
mages_list = [Mage(**mage) for mage in mages]

# Объединим всех персонажей в один список
characters = warriors_list + mages_list

# Выдадим им по 100 урона каждому
for char in characters:
    char.get_damage(80)
    print(char)

"""
### Задание на практику по ООП в Python: Реализация класса Mage

#### Общее описание

В этом задании вам предстоит погрузиться в мир объектно-ориентированного программирования (ООП) на языке 
Python, создав базовую структуру для класса персонажей в игровом приложении. Основной фокус будет сделан на
 реализации класса `Mage` (Маг), который будет обладать уникальными способностями и характеристиками. 
 Для этого необходимо будет также реализовать два дополнительных класса: `Character` и `ManaMixin`.

#### Часть 1: Класс Character

1. Создайте класс `Character`, который будет являться базовым классом для всех персонажей.
2. В классе `Character` определите следующие атрибуты:
   - `name` (имя): строка, имя персонажа.
   - `health` (здоровье): целое число, уровень здоровья персонажа.

#### Часть 2: Класс ManaMixin

1. Создайте класс `ManaMixin`, который будет предоставлять дополнительные характеристики и методы для персонажей, 
обладающих магическими способностями.
2. В классе `ManaMixin` определите следующие атрибуты и методы:
   - `mana` (мана): целое число, уровень маны персонажа.
   - `intelligence` (интеллект): целое число, уровень интеллекта персонажа.
   - `mage_attack()` (атака магии): метод, который возвращает урон, равный `intelligence * 2`.

#### Часть 3: Класс Mage

1. Создайте класс `Mage`, который будет наследоваться от классов `Character` и `ManaMixin`.
2. В классе `Mage` реализуйте следующие дополнительные методы:
   - `cast_spell(spell_name)`: метод, принимающий в качестве аргумента название заклинания (`spell_name`) и 
   выводящий информацию о произнесении заклинания. Например, при вызове метода с аргументом "Fireball" должна быть
    выведена строка "Casting Fireball!".
   - `restore_mana(amount)`: метод для восстановления маны, где `amount` — количество восстанавливаемой маны.
    Метод должен увеличивать уровень маны персонажа на указанное значение.

#### Цели задания

- Практика в применении принципов ООП.
- Использование наследования для создания иерархии классов.
- Реализация методов и управление состоянием объектов.

Убедитесь, что ваш код соответствует PEP8 и протестирован на различных сценариях использования созданных классов. 
Это задание поможет вам лучше понять, как организовать структуру программы и как 
использовать наследование и композицию для создания гибкой и расширяемой архитектуры.
"""
