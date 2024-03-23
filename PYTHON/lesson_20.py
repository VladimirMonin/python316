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
"""


# __init__ - конструктор класса
# Объявление класса
class MoscvichCar:
    # Используем дандер метод __init__ - инициализатор класса
    def __init__(self, model: str, year: int, color: str = 'orange'):
        # Наделяем конкретный экземпляр класса атрибутами
        self.model = model
        self.year = year
        self.color = color
        print(f'Экземпляр класса {self.__class__.__name__} создан!')

    def __new__(cls, *args, **kwargs):
        print(f'Создание экземпляра класса {cls.__name__} c аргументами {args}')
        return super().__new__(cls)


m1 = MoscvichCar('412', 1980, 'red')
print(f'Модель: {m1.model}, Год выпуска: {m1.year}, Цвет: {m1.color}')
m2 = MoscvichCar('412', 1980, 'black')
print(f'Модель: {m2.model}, Год выпуска: {m2.year}, Цвет: {m2.color}')
m3 = MoscvichCar('412', 1980)
print(f'Модель: {m3.model}, Год выпуска: {m3.year}, Цвет: {m3.color}')
