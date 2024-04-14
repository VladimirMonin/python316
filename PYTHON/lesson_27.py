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

# Пример 2 - Работа с курсами валюты

"""
Класс Currency:

Атрибуты:
value - сумма в валюте.
rate - курс конвертации в другую валюту.
Методы:
__init__ - инициализирует сумму и курс.
__mul__ - умножает сумму на курс (или на число).
__truediv__ - делит сумму на курс (или на число).
__str__ - возвращает строковое представление объекта.

"""

class Currency:
    """Класс для работы с курсами валюты.
    
    атрибуты:
    value - сумма в валюте.
    rate - курс конвертации в доллары
    name - название валюты

    """

    def __init__(self, value, dollar_rate, name):
        self.value = value
        self.dollar_rate = dollar_rate
        self.name = name
        self.dollar_value: None | float = None
        self.get_dollar_value()

        
    def __add__(self, other):
        """
        Если операция происходит с числом, то мы изменяем self.value
        Если операция происходит с другим объектом Currency, то создаем новый объект Currency
        """
        if isinstance(other, (int, float)):
            self.value += other
            self.get_dollar_value()
            return self.value
        
        elif isinstance(other, Currency):
            if self.name != other.name:
                raise ValueError('Разные валюты')
            
            self.get_dollar_value()
            return Currency(self.value + other.value, self.dollar_rate, self.name)
        else:
            raise ValueError('Неверный тип данных')

        
    def get_dollar_value(self):
        self.dollar_value = round(self.value / self.dollar_rate, 2)
    
    def __str__(self):
        return f'Валюта: {self.name}, Сумма: {self.value}, Курс: {self.dollar_rate}, Сумма в долларах: {self.dollar_value}'
    

# Создаем объекты Currency
rub = Currency(1000, 93.33, 'RUB')
rub2 = Currency(1000, 93.33, 'RUB')
bat = Currency(100, 36.38, 'BAT')
kzt = Currency(10000, 448.36, 'KZT')

# Тестируем математические операции
print(f'{rub + 20000 = }')
print(rub)