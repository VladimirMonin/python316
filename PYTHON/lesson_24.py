"""
Lesson 24
06.04.2024
Активация виртуального окружения venv в PyCharm
Команда активации для windows и linux
windows: venv\Scripts\activate
linux: source venv/bin/activate
Selenium webdriver
pip install selenium
"""

# Установка библиотеки selenium
# pip install selenium

# Импорт библиотеки
import time
from selenium import webdriver


# Создание объекта драйвера
driver = webdriver.Chrome()

# Переход на сайт
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()