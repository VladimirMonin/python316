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
"""


# Функция `hasattr()` - проверяет наличие атрибута у объекта


# Создадим класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        Мы видем это при прямом print(person)
        :return:
        """
        return f'Персона: {self.name}, {self.age} годиков'

    def __repr__(self):
        """
        Мы видим это при выводе объекта в списке
        :return:
        """
        return f'Person("{self.name}", {self.age})'


# Создадим объект класса Person
person = Person('John', 30)

# Получим строковое представление объекта, и преобразуем его в объект через eval()
string_object = repr(person)
print(string_object)

# Получим объект обратно
# Eval - это функция, которая выполняет строку как код
new_person = eval(string_object)
print(new_person)

eval_string = 'print("Hello")'
eval(eval_string)

"""
ПРАКТИКА!

Создайте класс `Car`, у которого есть атрибуты `model`, `year`, `color`, `price`.
Опишите ему методы `__str__` и `__repr__`.
Создайте 3 объекта класса `Car` и поместите их в список.
Распечатайте этот список через print comprehension.
Превратите эти классы в строки, поместите их в переменные с помощью функции `repr()`.
Произведите обратное преобразование с помощью функции `eval()`.

"""


# Создание класса

class Car:
    def __init__(self, model, year, color, price):
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def __str__(self):
        return f'Модель: {self.model}, год: {self.year}, цвет: {self.color}, цена: {self.price}'

    def __repr__(self):
        return f'Car("{self.model}", {self.year}, "{self.color}", {self.price})'


# Создание объектов класса Car
car1 = Car('BMW', 2020, 'black', 100000)
car2 = Car('Audi', 2019, 'white', 80000)
car3 = Car('Запорожец', 1980, 'yellow', 1000)

# Создание списка объектов
cars = [car1, car2, car3]

# Вывод списка объектов
[print(car) for car in cars]

# Преобразование объектов в строки
cars_str = [repr(car) for car in cars]
[print(type(car)) for car in cars_str]
print(cars_str)

# Преобразование строк в объекты
new_cars = [eval(car) for car in cars_str]
[print(type(car)) for car in new_cars]
print(new_cars)
