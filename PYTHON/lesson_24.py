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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.remote.webelement import WebElement
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

books: List[WebElement] = driver.find_elements(By.CLASS_NAME, "product_pod")
# print(len(books))
# print(books)
# [print(book.text) for book in books]

books_dicts = []
time.sleep(1)

for book in books:
    new_book = {}
    # title - a внутри h3 - значение атрибута title
    title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
    # price - внутри p.price_color - текст book.find_element(By.CLASS_NAME, "price_color").text
    # in_stock - внутри p.instock - текст book.find_element(By.CLASS_NAME, "instock").text
    # ссылка на картинку внутри img атрибут src подставляем в url http://books.toscrape.com/ + src.text book.find_element(By.TAG_NAME, "img").get_attribute("src") 
    #  http://books.toscrape.com/ + src
    # rating - p.star-rating в атрибут class 1 Элемент find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
    # 
    
    
    
    new_book.update({"title": title,
                     ...})
    books_dicts.append(new_book)

print(books_dicts)

# Практика 2
# Допишите этот цикл, чтобы собрать все данные о каждой книге с одной странцы