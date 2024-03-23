"""
Lesson 20
23.03.2024
ООП
Нейминг
ключевое слово class
Создание экземпляра класса
Проверка типа объекта
Атрибуты класса
Магический метод __init__ (дандер метод) - double underscore
Магический метод __new__
Конструктор класса
Как происходит создание экземпляра класса
Атрибут экземпляра
Методы экземпляра
Метод класса- @classmethod
Статический метод- @staticmethod
"""

# TODO Практика!
"""
1. Опишите класс Mattr (матрешка)
2. Определите инициализатор и атрибуты экземпляра класса:
- Цвет
- Материал
3. Определите методы:
__str__ - вывод информации об объекте
change_color - изменение цвета матрешки (переопределение атрибута цвет)
4. Создайте 3 экземпляра класса Mattr
5. Выведите информацию об объектах
6. Измените цвет у 2х матрешек
7. Попробуйте получить цвет напрямую из атрибута переменная.color
"""


class Mattr:
    count = 0

    def __init__(self, color: str, material: str):
        """Инициализатор класса"""
        self.color = color
        self.material = material
        # Мы обращаемся к атрибуту класса через self.__class__ и увеличиваем его на 1
        # Mattr.count += 1
        self.__class__.count += 1
        self.id = self.__class__.count

    def __str__(self) -> str:
        """Представление объекта в виде строки"""
        return (f'Цвет: {self.color}, '
                f'Материал: {self.material} '
                f'ID: {self.id}')

    def change_color(self, new_color: str) -> None:
        """Метод изменения цвета матрешки"""
        self.color = new_color

    def get_mattr_count(self) -> int:
        """
        Тоже будет работать, но лучше использовать метод класса
        """
        return self.__class__.count

    @classmethod
    def get_mattr_count_2(cls) -> int:
        """
        Раз мы работаем с аттрибутами класса, то
        лучше использовать метод класса
        """
        return cls.count

    @staticmethod
    def get_mattr_value(heigth: int, width: int, depth: int) -> int:
        """
        Метод для получения объема матрешки
        """
        return heigth * width * depth


m1 = Mattr('красный', 'дерево')
m2 = Mattr('зеленый', 'пластик')
m3 = Mattr('синий', 'стекло')

# Вывод информации о состоянии счетчика
print(f'Количество матрешек: {Mattr.count}')
print(f'Количество матрешек: {m3.count}')
print(f'Количество матрешек: {m3.__class__.count}')

# Тестируем оба метода получения количества матрешек
print(f'Методы получения количества матрешек:')
print(f'Количество матрешек: {m1.get_mattr_count()}')
print(f'Количество матрешек: {m1.get_mattr_count_2()}')

print(m1, m2, m3, sep='\n')

# Тестируем метод измерения объема матрешки
print(f'Объем матрешки: {Mattr.get_mattr_value(10, 20, 30)}')
print(f'Объем матрешки: {m1.get_mattr_value(10, 20, 30)}')
