"""
Lesson 27
14.04.2024

Математические операции
__add__ - сложение (сокращение от addition)
__sub__ - вычитание (сокращение от subtraction)
__mul__ - умножение (сокращение от multiplication)
__truediv__ - деление (сокращение от true division)
__floordiv__ - целочисленное деление (сокращение от floor division)
__mod__ - остаток от деления (сокращение от modulo)
__pow__ - возведение в степень (сокращение от power)
__round__ - округление
__abs__ - модуль числа

Инплейс операции
__iadd__ - сложение с присваиванием (сокращение от in-place addition)
__isub__ - вычитание с присваиванием (сокращение от in-place subtraction)
__imul__ - умножение с присваиванием (сокращение от in-place multiplication)
__itruediv__ - деление с присваиванием (сокращение от in-place true division)
__ifloordiv__ - целочисленное деление с присваиванием (сокращение от in-place floor division)
__imod__ - остаток от деления с присваиванием (сокращение от in-place modulo)
__ipow__ - возведение в степень с присваиванием (сокращение от in-place power)
"""

# Пример 2 - Работа с курсами валюты

"""
Класс Currency:

Атрибуты:
value - сумма в валюте.
rate - курс конвертации в другую валюту.
Методы:
__init__ - инициализирует сумму и курс.
__mul__ - умножает сумму на курс (или на число).
__truediv__ - делит сумму на курс (или на число).
__str__ - возвращает строковое представление объекта.

"""
import random

# Решение практики 

class Number(int):
    
    def __new__(cls, value):
        return super(Number, cls).__new__(cls, value)

    def __add__(self, other):
        result = super().__add__(other)
        return Number(random.randint(result, result + 5))

    def __sub__(self, other):
        result = super().__sub__(other)
        return Number(random.randint(result, result + 5))

    def __mul__(self, other):
        result = super().__mul__(other)
        return Number(random.randint(result, result + 5))

    def __truediv__(self, other):
        result = int(super().__truediv__(other))
        return Number(random.randint(result, result + 5))

    def __floordiv__(self, other):
        result = super().__floordiv__(other)
        return Number(random.randint(result, result + 5))

    def __mod__(self, other):
        result = super().__mod__(other)
        return Number(random.randint(result, result + 5))

    def __pow__(self, other):
        result = super().__pow__(other)
        return Number(random.randint(result, result + 5))

    def __neg__(self):
        result = super().__neg__()
        return Number(random.randint(result, result + 5))

    def __pos__(self):
        result = super().__pos__()
        return Number(random.randint(result, result + 5))

    def __iadd__(self, other):
        result = super().__add__(other)
        return Number(random.randint(result, result + 5))

    def __isub__(self, other):
        result = super().__sub__(other)
        return Number(random.randint(result, result + 5))

    def __imul__(self, other):
        result = super().__mul__(other)
        return Number(random.randint(result, result + 5))

    def __itruediv__(self, other):
        result = int(super().__truediv__(other))
        return Number(random.randint(result, result + 5))

    def __ifloordiv__(self, other):
        result = super().__floordiv__(other)
        return Number(random.randint(result, result + 5))

    def __imod__(self, other):
        result = super().__mod__(other)
        return Number(random.randint(result, result + 5))

    def __ipow__(self, other):
        result = super().__pow__(other)
        return Number(random.randint(result, result + 5))

# Тесты
    
n1 = Number(5)
n2 = Number(3)
print(f"Сложение: {n1 + n2}")  # __add__
print(f"Вычитание: {n1 - n2}")  # __sub__
print(f"Умножение: {n1 * n2}")  # __mul__
print(f"Деление: {n1 / n2}")  # __truediv__
print(f"Целочисленное деление: {n1 // n2}")  # __floordiv__ 
print(f"Остаток от деления: {n1 % n2}")  # __mod__ 
print(f"Возведение в степень: {n1 ** n2}")  # __pow__
print(f"Отрицательное число: {-n1}")  # __neg__ 

