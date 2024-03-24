"""
Lesson 21
ООП - инкапсуляция
Понятие инкапсуляции
- Функция `hasattr()`
- Функция `delattr()`
- Функция `setattr()`
- Функция `getattr()`
- Атрибут `__dict__` - словарь атрибутов объекта
- Функция `dir()`
- __repr__ - представление объекта ("техническое")
- __str__ - строковое представление объекта
- repr() - встроенная функция, которая вызывает __repr__
- eval() - встроенная функция, которая выполняет строку как код
- приватные и защищенные атрибуты и методы
- _name - защищенный атрибут. Доступ к нему есть в наследниках и извне.
- __name - приватный атрибут. Доступ к нему есть только внутри класса.
"""


# Функция `hasattr()` - проверяет наличие атрибута у объекта


# Создадим класс
class Person:
    def __init__(self, name, age, passport_number):
        self.name = name
        self.age = age
        self._passport_number = passport_number
        self.__is_checked = self.__validate_person_passport(self._passport_number)

    def __str__(self):
        """
        Мы видем это при прямом print(person)
        :return:
        """
        return f'Персона: {self.name}, {self.age} годиков'

    def __repr__(self):
        """
        Мы видим это при выводе объекта в списке
        :return:
        """
        return f'Person("{self.name}", {self.age})'

    @staticmethod
    def __validate_person_passport(passport_number: int):
        """
        Проверка паспорта
        :return:
        """
        if isinstance(passport_number, int):
            return True
        return False


# Создадим объект
person = Person('Вася', 21, '1234567890')

# Проверим наличие атрибута passport_number и __is_checked
# print(hasattr(person, 'passport_number'))  # False
# print(hasattr(person, '_passport_number'))  # True
# print(hasattr(person, 'is_checked'))  # False
# print(hasattr(person, '__is_checked'))  # False
# print(hasattr(person, '_Person__is_checked'))  # True

# Попробуем переназначить атрибуты через экземпляр класса
# person.passport_number = '0000000000'
# print(person._passport_number)  # 1234567890
# person._passport_number = '1111111111'
# print(person._passport_number)  # 1111111111

# Пробуем private атрибут
# print(person.__is_checked)  # AttributeError: 'Person' object has no attribute '__is_checked'
# print(person._Person__is_checked)  # False

# person.__is_checked = True
# person._Person__is_checked = True
# print(person._Person__is_checked)

person.__is_checked = True
# person.__validate_person_passport(1234567890)
person._Person__validate_person_passport(1234567890)
print(person._Person__is_checked)
