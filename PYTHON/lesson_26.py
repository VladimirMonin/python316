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
from abc import ABC, abstractmethod


class PrintedEdition(ABC):
    """
    Абстрактный класс печатного издания
    Родительский класс для книги и журнала
    """
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def _validate_other(self, other: 'PrintedEdition'):
        """
        Проверяет, является ли сравниваемый объект экземпляром класса PrintedEdition
        """
        if not isinstance(other, PrintedEdition):
            raise ValueError('Сравниваемый объект не является печатным изданием')

    def __eq__(self, other: 'PrintedEdition'):
        self._validate_other(other)
        return self.title == other.title and self.author == other.author and self.pages == other.pages
    
    def __lt__(self, other: 'PrintedEdition'):
        self._validate_other(other)
        return self.pages < other.pages
    
    def __gt__(self, other: 'PrintedEdition'):
        self._validate_other(other)
        return self.pages > other.pages
    
    def __le__(self, other: 'PrintedEdition'):
        self._validate_other(other)
        return self.pages <= other.pages
    
    def __ge__(self, other: 'PrintedEdition'):
        self._validate_other(other)
        return self.pages >= other.pages 
    

class Book(PrintedEdition):
    """
    Класс книги
    """
    def __init__(self, isbn: str, title: str, author: str, pages: int):
        super().__init__(title, author, pages)
        self.isbn = isbn

    def __str__(self):
        return f'Книга: {self.title}'



class Magazine(PrintedEdition):
    """
    Класс журнала
    """
    def __init__(self, title: str, author: str, pages: int, issue: int):
        super().__init__(title, author, pages)
        self.issue = issue

    def __str__(self):
        return f'Журнал: {self.title}'
    

book1 = Book('978-5-6040728-6-7', 'Война и мир', 'Лев Толстой', 1225)
book2 = Book('978-5-389-07428-7', 'Преступление и наказание', 'Федор Достоевский', 671)

magazine1 = Magazine('National Geographic', 'National Geographic Society', 150, 4)
magazine2 = Magazine('Forbes', 'Forbes Media', 100, 5)

# Журнал 'Преступление и наказание', 'Федор Достоевский', 671
magazine3 = Magazine('Преступление и наказание', 'Федор Достоевский', 671, 1)

print(book1 == book2)
print(book1 < book2)

print(magazine1 > magazine2)
print(magazine1 <= magazine2)

print(book1 == magazine1)

print(book2 == magazine3)

list_magazines = [magazine1, magazine2, magazine3]
