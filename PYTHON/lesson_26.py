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



Декоратор @dataclass в Python, встроенный в модуль dataclasses, упрощает создание классов, 
автоматически генерируя специальные методы, такие как __init__, __repr__, __eq__ и другие. 

По умолчанию @dataclass генерирует следующие методы:

__init__ — метод инициализации, который автоматически принимает аргументы со значениями по умолчанию, 
соответствующими аннотациям типов полей класса.
__repr__ — метод представления, который возвращает строку, представляющую экземпляр класса.
__eq__ — метод сравнения на равенство, который позволяет сравнивать экземпляры на основе их полей.
Кроме того, вы можете настроить @dataclass для автоматической генерации дополнительных методов сравнения:

__lt__, __le__, __gt__, __ge__ — методы для операций меньше, меньше или равно, больше и больше или равно 
соответственно. Для их включения нужно установить параметр order=True при декларации @dataclass.


"""
from dataclasses import dataclass, field
from re import S


@dataclass()
class Singer:
    coats: int
    castles: int
    cars: int
    name: str


    def __eq__(self, other):
        return self.coats == other.coats and self.castles == other.castles and self.cars == other.cars and self.name == other.name
    
    def __gt__(self, other):
        return self.coats > other.coats and self.castles > other.castles and self.cars > other.cars
    
    def __ge__(self, other):
        return self.coats >= other.coats and self.castles >= other.castles and self.cars >= other.cars and self.name == other.name
    

    

    



actor1 = Singer(1, 2, 3, 'Распутина')
actor2 = Singer(5, 1, 2, "Агутин")
actor3 = Singer(10, 5, 25, "Киркоров")
actor4 = Singer(11, 4, 40, "Басков")
actor5 = Singer(11, 4, 40, "Басков")
actor6 = Singer(11, 4, 40, "Клон Басков")

print(f'{actor4 == actor5 = }')
print(f'{actor4 == actor6 = }')

print(f'{actor4 > actor5 = }')
print(f'{actor4 > actor6 = }')

print(f'{actor4 < actor5 = }')
print(f'{actor4 < actor6 = }')

print(f'{actor4 >= actor5 = }')
print(f'{actor4 >= actor6 = }')

print(f'{actor4 <= actor5 = }')
print(f'{actor4 <= actor6 = }')