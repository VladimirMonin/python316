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
    def __init__(self, name: str, health: int, mana: int, damage: int, *args, **kwargs):
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
        self.is_alive = True
        super().__init__(*args, **kwargs)

    def __str__(self):
        is_alive = 'Жив и здравствует.' if self.is_alive else 'Доблестно пал в бою'
        # Обойдем все атрибуты и распечатем их циклом, ключ и значение
        return ', '.join([f'{key}: {value}' for key, value in self.__dict__.items()]) + f'. {is_alive}'

    @abstractmethod
    def get_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            print(f'Доблестно пал в бою {self.name}')

    @abstractmethod
    def get_attack(self):
        return self.damage

    def test_method(self):
        print(f'Тестовый метод класса {self.__class__.__name__}')


class Thief(Character):
    def __init__(self, name: str, health: int, damage: int, stealth: int):
        super().__init__(name, health, 0, damage)
        self.stealth = stealth

    def get_attack(self):
        return self.damage + self.stealth

    def get_damage(self, damage: int):
        super().get_damage(damage)


class Mage(Character):
    def __init__(self, intelligence: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.intelligence = intelligence

    def get_attack(self):
        return self.damage + self.intelligence

    def get_damage(self, damage: int):
        super().get_damage(damage)


class FireMageMixin:
    def __init__(self, fire_damage: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fire_damage = fire_damage

    def get_attack(self):
        return super().get_attack() + self.fire_damage

    def test_method(self):
        print(f'Тестовый метод класса {self.__class__.__name__}')


class WaterMageMixin:
    def __init__(self, water_damage: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.water_damage = water_damage

    def get_attack(self):
        return super().get_attack() + self.water_damage


class ScrollsReadMixin:
    """
    В инициализаторе добавим список заклинаний
    """

    def __init__(self, spells: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spells = spells


class FireMage(Mage, FireMageMixin, ScrollsReadMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def test_method(self):
    #     print(f'Тестовый метод класса {self.__class__.__name__}')


t = Thief('Вор', 100, 10, 50)
print(t)

spells_list_fire = ['файеркусь', 'огнелап']

m = FireMage(name='Огненный маг', health=100, mana=100, damage=10, intelligence=50, fire_damage=20,
             spells=spells_list_fire)
print(m)
print(FireMage.mro())
m.test_method()
