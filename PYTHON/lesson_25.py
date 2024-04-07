""" 
Lesson 25
07.04.2024
Dataclasses
__bool__
__post_init__
интегрировали dataclass Book в парсер книг
dataclass как конфиг для класса
__call__
"""
from dataclasses import dataclass
import re



"""
Определим класс Worker а так же dataclass WorkerConfig
Сделаем контролер, который будет фасадом для обоих классов
Укажим в dataclass WorkerConfig параметры:
message: str
method: str

Заставим работника выполнить метод и вывести сообщение
"""

@dataclass
class PrintConfig:
    message: str
    method: str

    # Делаем post_init с валидацией методов
    def __post_init__(self):
        if self.method not in ["print_message", "return_message"]:
            raise ValueError("Недопустимый метод")


class Printer:
    def __init__(self):
        self.config = None

    def print_message(self):
        print(self.config.message)

    def return_message(self):
        return self.config.message

    def __call__(self, config: PrintConfig) -> None | str:
        self.config = config
        method = getattr(self, config.method)
        result = method()
        return result


config = PrintConfig(message="Hello, World!", method="print_message")
config2 = PrintConfig(message="Hello, World!", method="return_message")
printer = Printer()
printer(config)
result = printer(config2)
print(result)