"""
Lesson 24
06.04.2024
Активация виртуального окружения venv в PyCharm
Команда активации для windows и linux
windows: venv\Scripts\activate
linux: source venv/bin/activate
Selenium webdriver
pip install selenium
webdriver.Chrome()
options = webdriver.ChromeOptions()
основные опции
устаревшие методы и новые
"""

# Установка библиотеки selenium
# pip install selenium

# Импорт библиотеки
from pprint import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from dataclasses import dataclass

list_options = [
    "--incognito",
    "--window-size=1920,1080",
    # "--headless=new",
]

URL = "http://books.toscrape.com/"






# Определим BookValidationError
class BookValidationError(Exception):
    pass

@dataclass
class Book:
    title: str
    price: float
    in_stock: bool
    cover_url: str
    rating: int

    def is_in_stock(self) -> bool:
        return self.in_stock
    
    # post __init__ method - валидация данных
    def __post_init__(self):
        if not isinstance(self.title, str):
            raise BookValidationError('title должен быть строкой')
        if not isinstance(self.price, (int, float)):
            raise BookValidationError('price должен быть числом')
        if not isinstance(self.in_stock, bool):
            raise BookValidationError('in_stock должен быть булевым значением')
        if not isinstance(self.cover_url, str):
            raise BookValidationError('cover_url должен быть строкой')
        if not isinstance(self.rating, int):
            raise BookValidationError('rating должен быть числом')
        if not 0 <= self.rating <= 5:
            raise BookValidationError('rating должен быть от 0 до 5')
    

    
class Browser:
    def __init__(self, options_list: list = []):
        self.options = webdriver.ChromeOptions()
        for option in options_list:
            self.options.add_argument(option)
        self.driver = webdriver.Chrome(options=self.options)


# Создаем класс для парсинга книг
class BooksParser:
    def __init__(self, browser: Browser):
        self.browser = browser.driver
        self.mark_dict = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        self.books_objects = []

    def parse_books(self, url: str):
        self.browser.get(url)
        while True:
            time.sleep(1)
            books: List[WebElement] = self.browser.find_elements(By.CLASS_NAME, "product_pod")
            for book in books:
                title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
                price = book.find_element(By.CLASS_NAME, "price_color").text
                in_stock = book.find_element(By.CLASS_NAME, "instock").text
                row_url = book.find_element(By.TAG_NAME, "img").get_attribute("src")
                final_url =  row_url
                rating_row = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
                rating = self.mark_dict[rating_row.split()[1]]
                
                
                new_book_obj = Book(
                    title=title,
                    price=float(price.split("£")[1]),
                    in_stock= True if in_stock == "In stock" else False,
                    cover_url=final_url,
                    rating=rating
                )
                
                self.books_objects.append(new_book_obj)

            try:
                #TODO: незабыть снять ограничение на количество страниц
                next_button = self.browser.find_element(By.LINK_TEXT, "next")
                # next_button.click()
                break
            except NoSuchElementException:
                break


class Controller:
    def __init__(self):
        self.browser = Browser(list_options)
        self.parser = BooksParser(self.browser)
        self.json_writter = None

    def run(self):
        self.parser.parse_books(URL)
        self.browser.driver.quit()
        return self.parser.books_objects





controller = Controller()
result = controller.run()
print(len(result))
pprint(result, sort_dicts=False)
print(result[0].__dict__)