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
__lt__ - меньше (сокращение от less than)
__gt__ - больше (сокращение от greater than)
__le__ - меньше или равно (сокращение от less or equal)
__ge__ - больше или равно (сокращение от greater or equal)

Декоратор который сгенерерирует все магические методы сравнения
@total_ordering

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


class Book:
    """
    Класс книги
    """
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __eq__(self, other: 'Book'):
        return self.title == other.title and self.author == other.author and self.pages == other.pages

b1 = Book('Python', 'Guido', 600)
b2 = Book('HTML', 'Bill', 400)
b3 = Book('CSS', 'Bill', 200)
b4 = Book('Python', 'Guido', 600)

# Сравнение происходит по адресу в памяти (is)
print(b1==b2)
print(b1==b4)
