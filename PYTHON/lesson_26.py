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
    
    @abstractmethod
    def _bool_validate(self):
        """
        Серия проверок для __bool__
        Проверяет типы данных атрибутов класса
        """
        return self._validate_pages() and self._validate_author() and self._validate_title()

    def _validate_pages(self):
        """
        Проверяет количество страниц
        """
        return isinstance(self.pages, int) and self.pages > 0
    

    def _validate_author(self):
        """
        Проверяет автора
        """
        return isinstance(self.author, str) and len(self.author) > 0
    
    def _validate_title(self):
        """
        Проверяет название
        """
        return isinstance(self.title, str) and len(self.title) > 0

    
    @abstractmethod
    def __bool__(self):
        """
        Проверяет, что все атрибуты класса соответствуют условиям
        """
        return self._bool_validate()

class Book(PrintedEdition):
    """
    Класс книги
    """
    def __init__(self, isbn: str, title: str, author: str, pages: int):
        super().__init__(title, author, pages)
        self.isbn = isbn

    def __str__(self):
        return f'Книга: {self.title}'
    
    def _validate_isbn(self):
        """
        Проверяет ISBN
        """
        return isinstance(self.isbn, str) and len(self.isbn) > 5
    
    def _bool_validate(self):
        """
        Проверяет ISBN
        """
        return self._validate_isbn() and super()._bool_validate()
    
    def __bool__(self):
        return self._bool_validate()



class Magazine(PrintedEdition):
    """
    Класс журнала
    """
    def __init__(self, title: str, author: str, pages: int, issue: int):
        super().__init__(title, author, pages)
        self.issue = issue

    def __str__(self):
        return f'Журнал: {self.title}'
    
    def _validate_issue(self):
        """
        Проверяет номер выпуска
        """
        return isinstance(self.issue, int) and self.issue > 0
    

    def _bool_validate(self):
        """
        Проверяет номер выпуска
        """
        return self._validate_issue() and super()._bool_validate()
    
    def __bool__(self):
        return self._bool_validate()
    

book1 = Book('978-5-6040728-6-4', 'Война и мир', 'Лев Толстой', 1225)
book2 = Book('978', 'Война и мир', ' ', -1225)

if book1:
    print('Книга валидна')
else:
    print('Библиотекоря на мыло!')


magazine1 = Magazine('National Geographic', 'National Geographic Society', 150, 2345)
magazine2 = Magazine('Playboy', 'Playboy Enterprises', 98, 1234)
magazine3 = Magazine('Игромания', 'Игромания', 123, 1223)

# Список журналов
magazines = [magazine1, magazine2, magazine3]

# Сортировка по количеству страниц
magazines.sort()
print(magazines)

# Сортировка по номеру выпуска
magazines.sort(reverse=True, key=lambda x: x.issue)
