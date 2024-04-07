""" 
Lesson 25
07.04.2024
Dataclasses
__bool__
__post_init__
"""
from dataclasses import dataclass



# Определим BookValidationError
class BookValidationError(Exception):
    pass

@dataclass
class Book:
    title: str
    price: float
    in_stock: bool
    cover_url: str
    rating: int

    def is_in_stock(self) -> bool:
        return self.in_stock
    
    # post __init__ method - валидация данных
    def __post_init__(self):
        if not isinstance(self.title, str):
            raise BookValidationError('title должен быть строкой')
        if not isinstance(self.price, (int, float)):
            raise BookValidationError('price должен быть числом')
        if not isinstance(self.in_stock, bool):
            raise BookValidationError('in_stock должен быть булевым значением')
        if not isinstance(self.cover_url, str):
            raise BookValidationError('cover_url должен быть строкой')
        if not isinstance(self.rating, int):
            raise BookValidationError('rating должен быть числом')
        if not 0 <= self.rating <= 5:
            raise BookValidationError('rating должен быть от 0 до 5')
    

book = Book('Гарри Поттер и Поездка на Бали', 1000.0, False, 'https://www.google.com', 10)

if book:
    print(f'{book.title} в наличии')
else:
    print(f'{book.title} нет в наличии')