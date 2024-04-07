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


class Printer:
    def __init__(self, config: PrintConfig):
        self.config = config

    def print_message(self):
        print(self.config.message)

    def __call__(self, *args, **kwargs):
        self.print_message()


config = PrintConfig(message="Hello, World!", method="print_message")
printer = Printer(config)
printer()
