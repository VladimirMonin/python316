from PYTHON.data.cities import cities

cities_set = {city['name'] for city in cities}
print(cities_set)
computer_city = None
last_letter_index = -1

unique_symbols = set(str(cities_set).lower())
print(unique_symbols)

bad_letters_set = set()

for letter in unique_symbols:
    for city in cities_set:
        if city[0].lower() in unique_symbols:
            break
    else:
        bad_letters_set.add(letter)

#
# while True:
#    # TODO Тут может быть логика поиска города по -1 букве - если такой нет - нам надо сдвинуть индекс last_letter_index -= 1
#
#     user_city = input('Введите город: ')
#     # Проверка на СТОП
#     if user_city.lower() == 'стоп':
#         print('Человек, ты проиграл!')
#         break
#
#     # Проверка на наличие города в сете
#     if user_city in cities_set:
#         print('Человек! Город найден!')
#     else:
#         print('Человек! Город не найден!')
#         print('Человек, ты проиграл!')
#         break
#
#     # Проверить правила игры (но только не на первом ходе)
#     if computer_city and computer_city[last_letter_index].lower() != user_city[0].lower():
#         print('Человек! Ты проиграл!')
#         break
#
#     # Удаление города из сета
#     cities_set.remove(user_city)
#    # TODO Тут может быть логика сброса индекса last_letter_index = -1
#     # Ход компьютера
#    # TODO Тут может быть логика поиска города по -1 букве - если такой нет - нам надо сдвинуть индекс last_letter_index -= 1
#
#     for city in cities_set:
#         if city[0].lower() == user_city[last_letter_index]:
#             computer_city = city
#             print(f'Компьютер: {computer_city}')
#             cities_set.remove(city)
#             # TODO Тут может быть логика сброса индекса last_letter_index = -1
#             break
#     else:
#         print('Человек! Ты выиграл!')
#         break
