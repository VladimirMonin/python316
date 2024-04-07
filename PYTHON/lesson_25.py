""" 
Lesson 25
07.04.2024
Dataclasses
"""
from dataclasses import dataclass
from tkinter import N


@dataclass
class Person:
    name: str
    age: int
    city: str = "Moscow"

p = Person("Ivan", 30)
print(p)