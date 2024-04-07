""" 
Lesson 25
07.04.2024
Dataclasses
"""
from dataclasses import dataclass

"""
title
price
in_stock
url
rating
"""
@dataclass
class Book:
    title: str
    price: float
    in_stock: bool
    cover_url: str
    rating: int

    def is_in_stock(self) -> bool:
        return self.in_stock
    
    # def __bool__(self):
    #     return self.in_stock
    

book = Book('Гарри Поттер и Белое и Красное', 1000.0, True, 'https://www.google.com', 5)

if book:
    print(f'{book.title} в наличии')
else:
    print(f'{book.title} нет в наличии')