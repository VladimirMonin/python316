"""
Lesson 26
13.04.2024
assert
магические методы в ООП
__init__ - инициализатор конструктора
__new__ - создание объекта в конструкторе
__str__ - строковое представление объекта
__repr__ - служебное строковое представление объекта
__len__ - длина объекта
__call__ - вызов объекта
__bool__ - логическое значение объекта
Сравнение
__eq__ - равенство (сокращение от equal)
__ne__ - неравенство (сокращение от not equal)
__lt__ - меньше (сокращение от less than)
__gt__ - больше (сокращение от greater than)
__le__ - меньше или равно (сокращение от less or equal)
__ge__ - больше или равно (сокращение от greater or equal)

Декоратор который сгенерерирует все магические методы сравнения
@total_ordering
Для него достаточно описать только __eq__ и __lt__ 
или __eq__ и __gt__ методы

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

from functools import total_ordering


@total_ordering
class Book:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def __eq__(self, other):
        return self.price == other.price and self.title == other.title

    def __lt__(self, other):
        return self.price < other.price


book1 = Book('Book1', 100)
book2 = Book('Book2', 200)
book3 = Book('Book1', 100)
book4 = Book('Book1', 50)

print(f'{book1 == book2=}')
print(f'{book1 == book3=}')
print(f'{book1 == book4=}')
print(f'{book1 != book2=}')
print(f'{book1 != book3=}')
print(f'{book1 != book4=}')
print(f'{book1 < book2=}')
print(f'{book1 < book3=}')
print(f'{book1 < book4=}')
print(f'{book1 <= book2=}')
print(f'{book1 <= book3=}')
print(f'{book1 <= book4=}')
"""

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


book1 == book2=False
book1 == book3=True
book1 == book4=False
book1 True
book1 False
book1 True
book1 < book2=True
book1 < book3=False
book1 < book4=False
book1 <= book2=True
book1 <= book3=True
book1 <= book4=False


return self.price == other.price and self.title == other.title

(.venv) C:\PY\ПРИМЕРЫ КОДА\python316>"c:/PY/ПРИМЕРЫ КОДА/python316/.venv/Scripts/python.exe" "c:/PY/ПРИМЕРЫ КОДА/python316/PYTHON/lesson_26.py"
book1 == book2=False
book1 == book3=True
book1 == book4=False
book1 True
book1 False
book1 True
book1 < book2=True
book1 < book3=False
book1 < book4=False
book1 <= book2=True
book1 <= book3=True
book1 <= book4=False
"""