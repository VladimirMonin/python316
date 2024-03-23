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

    def __str__(self) -> str:
        """
        Магический метод __str__ - приведение объекта к строке.
        Работает на уровне print
        """
        return f'Модель: {self.model}, Год выпуска: {self.year}, Цвет: {self.color}, Класс: {self.__class__.__name__}'

    def get_car(self) -> str:
        """
        Метод эклемпляра класса, который возвращает информацию об объекте
        :return:
        """
        return f'Автомобиль {self.model} {self.year} года выпуска сошел с конвейера'

    def change_color(self, new_color: str) -> None:
        """
        Метод экземпляра класса, который меняет цвет автомобиля
        :param new_color:
        :return:
        """
        self.color = new_color


m1 = MoscvichCar('412', 1980, 'red')
print(f'Модель: {m1.model}, Год выпуска: {m1.year}, Цвет: {m1.color}, Класс: {m1.__class__.__name__}')

# Мы добавили магический метод __str__ и можем использовать print
# Для вывода информации об объекте
print(m1)
print(m1.get_car())
m1.change_color('красный')
m1.color = 'зеленый'
print(m1)
