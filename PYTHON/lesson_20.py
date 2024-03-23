"""
Lesson 20
23.03.2024
ООП
Нейминг
ключевое слово class
Создание экземпляра класса
Проверка типа объекта
Атрибуты класса
Магический метод __init__ (дандер метод) - double underscore
Магический метод __new__
Конструктор класса
Как происходит создание экземпляра класса
Атрибут экземпляра
Методы экземпляра
Метод класса- @classmethod
Статический метод- @staticmethod
Полиморфизм - преемственность методов
"""


class PngImage:
    def __init__(self, width: int, height: int, file_path: str):
        self.width = width
        self.height = height
        self.file_path = file_path
        self.saturation = 100

    def __str__(self):
        return (f'Формат изображения: {self.__class__.__name__}, ширина: {self.width}, '
                f'высота: {self.height}, путь к файлу: {self.file_path}, насыщенность: {self.saturation}')

    def open(self):
        print(f'Открытие файла {self.file_path}')

    def save(self):
        print(f'Сохранение файла {self.file_path}')

    def change_saturation(self, value: int):
        print(f'Изменение насыщенности на {value}')
        self.saturation += value


class WebPImage:
    def __init__(self, width: int, height: int, file_path: str):
        self.width = width
        self.height = height
        self.file_path = file_path
        self.saturation = 100

    def __str__(self):
        return (f'Формат изображения: {self.__class__.__name__}, ширина: {self.width}, '
                f'высота: {self.height}, путь к файлу: {self.file_path}, насыщенность: {self.saturation}')

    def open(self):
        print(f'Открытие файла {self.file_path}')

    def save(self):
        print(f'Сохранение файла {self.file_path}')

    def change_saturation(self, value: int):
        print(f'Изменение насыщенности на {value}')
        self.saturation += value


class JpegImage:
    def __init__(self, width: int, height: int, file_path: str):
        self.width = width
        self.height = height
        self.file_path = file_path
        self.saturation = 100

    def __str__(self):
        return (f'Формат изображения: {self.__class__.__name__}, ширина: {self.width}, '
                f'высота: {self.height}, путь к файлу: {self.file_path}, насыщенность: {self.saturation}')

    def open(self):
        print(f'Открытие файла {self.file_path}')

    def save(self):
        print(f'Сохранение файла {self.file_path}')

    def change_saturation(self, value: int):
        print(f'Изменение насыщенности на {value}')
        self.saturation += value


# Создаем по 1 экземпляру каждого класса
png = PngImage(1920, 1080, 'image.png')
webp = WebPImage(1920, 1080, 'image.webp')
jpeg = JpegImage(1920, 1080, 'image.jpeg')

# Помещаем их в список
images = [png, webp, jpeg]

# Перебираем список и вызываем методы
for image in images:
    image.open()
    image.change_saturation(50)
    image.save()
    print(image)
