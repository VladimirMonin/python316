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


list_options = [
    "--incognito",
    "--window-size=1920,1080",
    # "--headless=new",
]

# Сделаем функцию для создания драйвера

def get_chrome_driver(options_list: list = []):
    options = webdriver.ChromeOptions()
    for option in options_list:
        options.add_argument(option)
    return webdriver.Chrome(options=options)


driver = get_chrome_driver(list_options)


# Устаревшие методы:
# driver.find_element_by_id()
# driver.find_element_by_name()
# driver.find_element_by_xpath()
# driver.find_elements_by_tag_name()
# Новые методы:
# driver.find_element(By.ID, "id")
# driver.find_elements(By.TAG_NAME, "tag_name")

# Объект By - это класс, который содержит методы для поиска элементов
# By.ID
# By.NAME
# By.TAG_NAME
# By.CLASS_NAME
# By.LINK_TEXT
# By.PARTIAL_LINK_TEXT
# By.CSS_SELECTOR
# By.XPATH

# импорт By
# from selenium.webdriver.common.by import By


# Начинаем работу с http://books.toscrape.com/

URL = "http://books.toscrape.com/"

driver.get(URL)

# Ищем карточки книг на странице  article class="product_pod"
# Метод find_elements возвращает список элементов
# Используем By.CLASS_NAME find_elements(By.CLASS_NAME, "product_pod")
# Используем By.CSS_SELECTOR find_elements(By.CSS_SELECTOR, ".product_pod") или  "article.product_pod"

mark_dict = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
books_dicts = []
while True:
    time.sleep(1)
    books: List[WebElement] = driver.find_elements(By.CLASS_NAME, "product_pod")
    # print(len(books))
    # print(books)
    # [print(book.text) for book in books]


    for book in books:
        new_book = {}
        # title - a внутри h3 - значение атрибута title
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        # price - внутри p.price_color - текст book.find_element(By.CLASS_NAME, "price_color").text
        price = book.find_element(By.CLASS_NAME, "price_color").text
        # in_stock - внутри p.instock - текст book.find_element(By.CLASS_NAME, "instock").text
        in_stock = book.find_element(By.CLASS_NAME, "instock").text
        # ссылка на картинку внутри img атрибут src подставляем в url http://books.toscrape.com/ + src.text book.find_element(By.TAG_NAME, "img").get_attribute("src") 
        row_url = book.find_element(By.TAG_NAME, "img").get_attribute("src")
        #  http://books.toscrape.com/ + src
        final_url =  row_url
        # rating - p.star-rating в атрибут class 1 Элемент find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
        rating_row = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
        rating = mark_dict[rating_row.split()[1]]

        
        
        
        new_book.update({"title": title,
                        "price": price,
                        "in_stock": in_stock,
                        "url": final_url,
                        "rating": rating})
        books_dicts.append(new_book)

        print('.', end='')
    # Переход на следующую страницу li с текстом Next
    try:
        next_button = driver.find_element(By.LINK_TEXT, "next")
    
    except NoSuchElementException:
        break

    else:
        next_button.click()


print(len(books_dicts))

# Запись в JSON в utf-8 ensure_ascii=False indent=4
import json
with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books_dicts, file, ensure_ascii=False, indent=4)


# Рефакторинг на ООП
    
class Browser:
    def __init__(self, options_list: list = []):
        self.options = webdriver.ChromeOptions()
        for option in options_list:
            self.options.add_argument(option)
        self.driver = webdriver.Chrome(options=self.options)


# Создаем класс для парсинга книг
class BooksParser:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.mark_dict = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        self.books_dicts = []

    def parse_books(self, url: str):
        self.browser.get(url)
        while True:
            time.sleep(1)
            books: List[WebElement] = self.browser.find_elements(By.CLASS_NAME, "product_pod")
            for book in books:
                new_book = {}
                title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
                price = book.find_element(By.CLASS_NAME, "price_color").text
                in_stock = book.find_element(By.CLASS_NAME, "instock").text
                row_url = book.find_element(By.TAG_NAME, "img").get_attribute("src")
                final_url =  row_url
                rating_row = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
                rating = self.mark_dict[rating_row.split()[1]]
                new_book.update({"title": title,
                                "price": price,
                                "in_stock": in_stock,
                                "url": final_url,
                                "rating": rating})
                
                self.books_dicts.append(new_book)

                print('.', end='')

            try:
                next_button = self.browser.find_element(By.LINK_TEXT, "next")
            except NoSuchElementException:
                break


class Controller:
    def __init__(self):
        self.browser = Browser(list_options)
        self.parser = BooksParser(self.browser)

    def run(self):
        self.parser.parse_books(URL)
        self.browser.driver.quit()


controller = Controller()
controller.run()