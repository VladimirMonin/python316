"""
Lesson 21
ООП - инкапсуляция
Понятие инкапсуляции
- Функция `hasattr()`
- Функция `delattr()`
- Функция `setattr()`
- Функция `getattr()`
- Атрибут `__dict__` - словарь атрибутов объекта
- Функция `dir()`
- __repr__ - представление объекта ("техническое")
- __str__ - строковое представление объекта
- repr() - встроенная функция, которая вызывает __repr__
- eval() - встроенная функция, которая выполняет строку как код
- приватные и защищенные атрибуты и методы
- _name - защищенный атрибут. Доступ к нему есть в наследниках и извне.
- __name - приватный атрибут. Доступ к нему есть только внутри класса.
- доступ извне к приватным атрибутам через методы
- методы __set_attr() и __get_attr() - геттеры и сеттеры - позволяют управлять доступом к атрибутам
- getter и setter через декораторы @property
"""


# Пример класса с __set_attr() и __get_attr()
class PngImage:
    def __init__(self, width: int, height: int, file_path: str):
        self._width = width
        self._height = height
        self._file_path = file_path
        self.__saturation = 100

    def __str__(self):
        return (f'Формат изображения: {self.__class__.__name__}, ширина: {self._width}, '
                f'высота: {self._height}, путь к файлу: {self._file_path}, насыщенность: {self.__saturation}')

    @property  # getter - декоратор всегда первый, и называется property (одинаково для всех)
    def saturation(self):
        """
        Getter для атрибута saturation
        Методы геттера и сеттера называются одинаково
        :return:
        """
        return self.__saturation

    @saturation.setter  # setter - декоратор для установки значения (называется имя_геттера.setter)
    def saturation(self, value: int):
        """
        Setter для атрибута saturation
        Методы геттера и сеттера называются одинаково
        :param value:
        :return:
        """
        self.__validate_saturation(value)

    def __validate_saturation(self, value: int):
        if 0 <= value <= 100:
            self.__saturation = value
        else:
            raise ValueError('Насыщенность должна быть в пределах от 0 до 100')


image = PngImage(100, 100, 'image.png')

print(image)
image.saturation = 50
print(image)

"""
Практика!
Опишите класс Person c 2мя приватными атрибутами: __name и __age
Опишите в нем 2 приватных__ метода __validate_name и __validate_age
Валидаторы делают raise ValueError, если валидация не прошла
Поместите методы в инициализатор __init__, чтобы при создании объекта класса Person
происходила валидация атрибутов name и age

Опишите геттеры и сеттеры для атрибутов name и age
с использованием декораторов @property, а так же методы __validate_name и __validate_age

Проведите тестирование класса Person, и убедитесь, что валидация работает корректно
Как на инициализации, так и при изменении атрибутов
"""
