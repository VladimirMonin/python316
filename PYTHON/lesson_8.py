"""
Lesson 8

any - возвращает True если хотя бы один элемент списка True
all - возвращает True если все элементы списка True
set - множество и методы
tuple - кортеж
Распаковка коллекций

"""

# методы сетов (множеств)

# add - добавляет элемент в множество
# discard - удаляет элемент из множества (если элемента нет, то ничего не делает)
# remove - удаляет элемент из множества (если элемента нет, то выдает ошибку)
# pop - возвращает и удаляет элемент из множества
# update - обновляет множество, добавляя элементы из другого множества
# copy - копирует множество
# clear - очищает множество
# union - возвращает объединение множеств
# symmetric_difference - возвращает симметричную разность множеств
# difference - возвращает разницу множеств
# intersection - возвращает пересечение множеств
# isdisjoint - возвращает True если множества не имеют общих элементов
# issubset - возвращает True если множество является подмножеством другого множества
# issuperset - возвращает True если множество является надмножеством другого множества
# remove - удаляет элемент из множества
# symmetric_difference_update - обновляет множество симметричной разностью множеств
# difference_update - удаляет из множества все элементы, которые есть в другом множестве
# intersection_update - удаляет из множества все элементы, которых нет в другом множестве


# # TODO - примеры специальных методов для анализа данных через множества
# """
# У нас есть две коллекции фильмов.
# Фильмы которые видели вы
# Фильмы которые видел ваш друг
#
# 1. Давайте выведем на экран фильмы, которые вы оба видели
# 2. Давайте выведем на экран фильмы, которые вы видели, а друг нет
# 3. Давайте выведем на экран фильмы, которые вы не видели, но видел ваш друг
# 4. Давайте выведем на экран фильмы, которые видел кто-то один из вас (сумма 2 и 3 пункта)
# 5. Получим пункт 4. через симметричную разность
# """
#
# my_film = {'Матрица', 'Титаник', 'Джентельмены', 'Криминальное чтиво', 'Достучаться до небес'}
# friend_film = {'Матрица', 'Джентельмены', 'Достучаться до небес', 'Джокер', 'Зеленая книга'}
#
# print(f'{my_film=}')
# print(f'{friend_film=}')
#
# # 1. Давайте выведем на экран фильмы, которые вы оба видели метод intersection или &
# both_film = my_film & friend_film
# # both_film = my_film.intersection(friend_film)
# print(f'{both_film=}')
#
# # 2. Давайте выведем на экран фильмы, которые вы видели, а друг нет метод difference или -
# my_not_friend_film = my_film - friend_film
# # my_not_friend_film = my_film.difference(friend_film)
# print(f'{my_not_friend_film=}')
#
# # 3. Давайте выведем на экран фильмы, которые вы не видели, но видел ваш друг
# friend_not_my_film = friend_film - my_film
# # friend_not_my_film = friend_film.difference(my_film)
# print(f'{friend_not_my_film=}')
#
# # 4. Давайте выведем на экран фильмы, которые видел кто-то один из вас (сумма 2 и 3 пункта)
# somebody_film = my_not_friend_film | friend_not_my_film
# # somebody_film = my_not_friend_film.union(friend_not_my_film)
# print(f'{somebody_film=}')
#
# # 5. Получим пункт 4. через симметричную разность
# somebody_film = my_film ^ friend_film
# # somebody_film = my_film.symmetric_difference(friend_film)
# print(f'{somebody_film=}')
#
# # remove and discard
# my_dvd = {'Матрица', 'Титаник', 'Джентельмены', 'Криминальное чтиво', 'Достучаться до небес'}
#
# # try:
# #     give_dvd = input('Какой фильм отдаете? ')
# # except KeyError:
# #     print('Такого фильма нет в моей коллекции')
# give_dvd = input('Какой фильм отдаете? ')
# # my_dvd.remove(give_dvd)
# my_dvd.discard(give_dvd)
#
# # all - возвращает True если все элементы списка True
# # any - возвращает True если хотя бы один элемент списка True
#
# list_a = [True, True, True, True, True]
# list_b = [True, False, True, False, True]
# list_c = [False, False, False, False, False]
#
# all_res_a = all(list_a)  # True
# all_res_b = all(list_b)  # False
# all_res_c = all(list_c)  # False
# not_all_res_c = not all(list_c)  # True
#
# any_res_a = any(list_a)  # True
# any_res_b = any(list_b)  # True
# any_res_c = any(list_c)  # False
# not_any_res_c = not any(list_c)  # True
#
# letters = 'adb24'
# # isalpha - возвращает True если все символы строки являются буквами
# # isdigit - возвращает True если все символы строки являются цифрами
#
# any_letter_is_digit = any([letter.isdigit() for letter in letters])  # True
# all_letter_is_digit = all([letter.isdigit() for letter in letters])  # False
#
# names_list = ['Иван', 'Мария', 'Петр', 'Илья', 'Алексей', 'Анна', 'Александр', 'Игорь', 'Андрей', 'Антон', 'Игорь']
# # Проверяем что в списке есть хотя бы одно имя с буквой р
#
# any_name_with_r = any(['р' in name.lower() for name in names_list])  # True
# all_name_with_r = all(['р' in name.lower() for name in names_list])  # False
#
# if any_name_with_r:
#     print('В списке есть имя с буквой р')
#
# num_list = [0, 1, 0, 1]
# all_num_is_true = all(num_list)  # False
# any_num_is_true = any(num_list)  # True
#
# # TODO - практика
# """
# Проверяем что хотя бы один студент набрал проходной балл на экзамене
# Проверяем что вся группа без исключения набрала проходной балл на экзамене
# Проходной балл - 6
# Список оценок: [12, 11, 10, 8, 9, 10, 12]
# Вывести принты на экран
# """
# marks = [12, 11, 10, 8, 9, 10, 12]
# result_all_mark = all([mark >= 6 for mark in marks])  # Все студенты на экзамене набрали проходной балл
# result_any_mark = any([mark >= 6 for mark in marks])  # Хотя бы один студент на экзамене набрал проходной балл
#
# # список оценок
# scores = [12, 11, 10, 8, 9, 10, 12]
#
# # проходной балл
# passing_score = 6
#
# # Вариант от Игоря
# # проверяем, что хотя бы один студент набрал проходной балл
# # тут мы создаем генератор, который возвращает True если хотя бы один студент набрал проходной балл
# any_passing = any(score >= passing_score for score in scores)
# print(f"Хотя бы один студент набрал проходной балл: {any_passing}")
#
# # проверяем, что вся группа набрала проходной балл
# all_passing = all(score >= passing_score for score in scores)
# print(f"Вся группа набрала проходной балл: {all_passing}")
#
# # Tuple - кортеж - неизменяемый список
# # Упорядоченная неизменяемая коллекция элементов
#
# # Создание кортежа
# # 1. Пустой кортеж
# empty_tuple = ()
# empty_tuple = tuple()
#
# # 2. Кортеж с одним элементом
# one_element_tuple = (1,)
# one_element_tuple = 1,
#
# # 3. Кортеж с несколькими элементами
# tuple_with_elements = (1, 2, 3)
# tuple_with_elements = 1, 2, 3
#
# # Методы кортежей
# # count - возвращает количество элементов в кортеже
# # index - возвращает индекс элемента в кортеже
#
# salary_dollars_typle = (10000, 12000, 15000, 20000, 25000, 30000, 35000, 40000)
# # sum - возвращает сумму элементов кортежа
# sum_salary = sum(salary_dollars_typle)
# print(f'{sum_salary=}')
#
# # len - возвращает длину кортежа
# len_salary = len(salary_dollars_typle)

# index - возвращает индекс элемента в кортеже
# index_10000 = salary_dollars_typle.index(10000)
# print(salary_dollars_typle[index_10000])
#
# salary_dollars_typle[index_10000] = 20000

# delivery = ('Бургер', 'Пицца', 'Коньяк')
# delivery_l = ['Бургер', 'Пицца', 'Коньяк']
# delivery_s = {'Бургер', 'Пицца', 'Коньяк'}
#
# product_1, product_2, *_ = delivery
# print(product_1)
# print(product_2)
# print(*_)
# print(_)
# # мы можем взять элементы с конца коллекции
# *_, product_2 = delivery
# print(product_2)
# print(*_)
# print(_)

# cart = ['молоко', 'хлеб', 'яйца']
# product_1, product_2, product_3 = cart
#
# product_1 = cart[0]
# product_2 = cart[1]
# product_3 = cart[2]
#
# print(*cart, sep=', ')
# print(cart[0], cart[1], cart[2], sep=', ')
# print(product_1, product_2, product_3, sep=', ')
#
# print(f'{product_1=}')
# print(f'{product_2=}')
# print(f'{product_3=}')


# cart = ['молоко', 'хлеб', 'яйца', 'конфеты 1', 'конфеты 2', 'конфеты 3', 'конфеты 4', "булки"]
# milk, bread, eggs, *sweets = cart
#
# print(f'{milk=}')
# print(f'{bread=}')
# print(f'{eggs=}')
# print(f'{sweets=}')
#
# print(*cart)
#
# tuple_items = ('ключ', 'значение')
# key, value = tuple_items
#
# # dict - словарь. Изменяемая коллекция элементов, которая хранит элементы в виде пары ключ:значение
# # Ключ - уникальный идентификатор элемента - может быть любым неизменяемым типом данных, хешируется
# # Значение - значение элемента - может быть любым типом данных
#
# # Создание словаря
# # 1. Пустой словарь
# empty_dict = {}
# empty_dict = dict()
#
# # 2. Словарь с данными
# some_dict = {'ключ': 'значение', 'ключ 2': 'значение 2'}
#
# person_dict = {'name': 'John',
#                'age': 30,
#                'job': 'developer',
#                'salary': 1000.0,
#                'skills': ['python', 'git', 'linux'],
#                }
#
# person_dict_items = [
#     ('name', 'John'),
#     ('age', 30),
#     ('job', 'developer'),
#     ('salary', 1000.0),
#     ('skills', ['python', 'git', 'linux']),
# ]
#
# # Методы словарей
# # len - возвращает длину словаря
# # keys - возвращает ключи словаря
# # values - возвращает значения словаря
# # items - возвращает пары ключ:значение словаря
#
# print(f'{len(person_dict)=}')
# print(f'{person_dict.keys()=}')
# print(f'{type(person_dict.keys())=}')
# print(f'{person_dict.values()=}')
# print(f'{person_dict.items()=}')
#
# # for and keys, values, items
#
# for key in person_dict.keys():
#     print(key)
#
# for value in person_dict.values():
#     print(value)
#
# for key, value in person_dict.items():
#     print(key, value)

say_hello = 'Hello world!'
name = __name__
print(name)
if __name__ == '__main__':
    print(say_hello)
    print(name)
