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
"""


# Функция `hasattr()` - проверяет наличие атрибута у объекта


# Создадим класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

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


# Создадим объект класса Person
person = Person('John', 30)

# Получим строковое представление объекта, и преобразуем его в объект через eval()
string_object = repr(person)
print(string_object)

# Получим объект обратно
# Eval - это функция, которая выполняет строку как код
new_person = eval(string_object)
print(new_person)

eval_string = 'print("Hello")'
eval(eval_string)
