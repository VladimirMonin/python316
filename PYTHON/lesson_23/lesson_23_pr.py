from abc import ABC, abstractmethod


class Product(ABC):
    """
    Абстрактный класс продукта
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self):
        pass


class FragileMixin:
    """
    Миксин для хрупких товаров
    """

    def packaging_instructions(self):
        """
        Инструкции по упаковке
        :return:
        """
        return "Используйте упаковочный материал с воздушными подушками."


class BulkyItemMixin:
    """
    Миксин для крупногабаритных товаров
    """

    def shipping_instructions(self):
        """
        Инструкции по доставке
        :return:
        """
        return "Крупногабаритный товар. Необходим подъемник."


# Класс Smartphone, наследуется от Product и использует FragileMixin
class Smartphone(Product, FragileMixin):
    """
    Класс смартфона
    """

    def __init__(self, name, price, battery_life):
        super().__init__(name, price)
        self.battery_life = battery_life

    def get_description(self):
        return f"{self.name}: {self.price}$, работа акб: {self.battery_life} часов. {self.packaging_instructions()}"


# Класс Laptop, наследуется от Product и использует BulkyItemMixin
class Laptop(Product, BulkyItemMixin):
    """
    Класс ноутбука
    """

    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def get_description(self):
        return f"{self.name}: {self.price}$, weight: {self.weight}kg. {self.shipping_instructions()}"


# Создаем объекты и тестируем
smartphone = Smartphone("BananaPhone", 999, 24)
print(len(smartphone))
laptop = Laptop("MacPro", 3499, 2.5)

# Выводим описания товаров
print(smartphone.get_description())
print(laptop.get_description())
