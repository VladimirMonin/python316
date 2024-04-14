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

# Пример 1 - Гиря class Kettlebell
# % - остаток от деления

class SportWeight:
    def __init__(self, weight: int | float):
        self.weight = weight
        self.min_weight = 5
        self.max_weight = 50
        self.multiplicity = 2.5

    def __validate_weight(self, weight):
        if weight < self.min_weight:
            raise ValueError(f"Вес груза не может быть меньше {self.min_weight}")
        elif weight > self.max_weight:
            raise ValueError(f"Вес груза не может быть больше {self.max_weight}")
        elif weight % self.multiplicity != 0:
            raise ValueError(f"Вес груза должен быть кратен {self.multiplicity}")
        return weight
    
    def __add__(self, other):
        other_weight = self.__validate_weight(other.weight)
        return SportWeight(self.weight + other_weight)

    def __sub__(self, other):
        other_weight = self.__validate_weight(other.weight)
        if self.weight - other_weight < 0:
            raise ValueError(f"Вес груза не может быть 0 и меньше")


# Тестирование
weight1 = SportWeight(10)
weight2 = SportWeight(15)
weight3 = SportWeight(12.5)

weight4 = weight1 + weight2
weight5 = weight1 + weight3
weight6 = weight1 - weight2