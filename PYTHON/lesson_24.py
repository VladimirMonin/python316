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
# driver = webdriver.Chrome()

# Переход на сайт
# driver.get("https://www.google.com")
# time.sleep(5)
# driver.quit()

# Попробуйте запустить код и убедитесь, что браузер открылся и перешел на сайт google.com

# Настройки драйвера
# За них отвечает отдельный объект - options
# Он позволяет настроить различные параметры драйвера

# Создание объекта опций
# options = webdriver.ChromeOptions()

# Популярные опции: 
#--headless=new, - режим без графического интерфейса
# --incognito, - режим инкогнито
# --start-maximized, - максимальный размер окна (не работает в headless режиме)
# --window-size=800,600 - размер окна (работает в headless режиме)

list_options = [
    "--incognito",
    "--window-size=1920,1080",
    # "--headless=new",
]

# for option in list_options:
#     options.add_argument(option)


# driver = webdriver.Chrome(options=options)
# driver.get("https://www.google.com")
# driver.save_screenshot("google.png")
# time.sleep(1)
# driver.quit() 

# Сделаем функцию для создания драйвера

def get_chrome_driver(options_list: list = []):
    options = webdriver.ChromeOptions()
    for option in options_list:
        options.add_argument(option)
    return webdriver.Chrome(options=options)


driver = get_chrome_driver(list_options)
driver.get("https://www.google.com")