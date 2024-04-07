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


# Это же на обычном классе
class Book:
    def __init__(self, title: str, price: float, in_stock: bool, cover_url: str, rating: int):
        self.title = title
        self.price = price
        self.in_stock = in_stock
        self.cover_url = cover_url
        self.rating = rating

    def __str__(self):
        return f"Book({self.title}, {self.price}, {self.in_stock}, {self.cover_url}, {self.rating})"