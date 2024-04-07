""" 
Lesson 25
07.04.2024
Dataclasses
__bool__
__post_init__
интегрировали dataclass Book в парсер книг
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
class WorkerConfig:
    message: str
    method: str


class Worker:
    def __init__(self, config: WorkerConfig):
        self.config = config

    def say_hello(self):
        print(self.config.message)

    def say_goodbye(self):
        print("Goodbye")


class WorkFacade:
    def __init__(self, config: WorkerConfig):
        self.worker = Worker(config)

    def work(self):
        method = getattr(self.worker, self.worker.config.method, None)
        if method:
            method()
        else:
            print("Unknown method")


config = WorkerConfig("Hello", "say_hello")
config2 = WorkerConfig("Goodbye", "say_goodbye")
facade = WorkFacade(config2)
facade.work()
