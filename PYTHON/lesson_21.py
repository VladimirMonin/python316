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

    def get_is_checked(self):
        return self.__is_checked

    def __set_passport_number(self, passport_number):
        if isinstance(passport_number, int):
            self._passport_number = passport_number
        else:
            raise ValueError('Номер паспорта должен быть числом')

    def set_is_checked(self, new_passport_number: int):
        """
        Метод иницирует проверку паспорта
        Для проверки паспорта, вам необходимо установить номер паспорта повторно
        :param new_passport_number:
        :return:
        """
        self.__set_passport_number(new_passport_number)
        self.__is_checked = self.__validate_person_passport(self._passport_number)


# Создадим объект
person = Person('Вася', 21, "1234567890")

# Проверим прошел ли Василий проверку
print(person.get_is_checked())

# Устанавливаем новый номер паспорта
person.set_is_checked(123456789)

# Проверим прошел ли Василий проверку
print(person.get_is_checked())
