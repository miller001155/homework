'''Задача 71'''

types_of_sports = ['football', 'basketball']  #  список
user_favorite_sport = input('Введите ваш любимый вид спорта:')  #  запрос на ввод значения
types_of_sports.append(user_favorite_sport)  #  добавляем в список элемент что ввол пользователь
types_of_sports.sort()  #  сортируем список
print(types_of_sports)  #  выводим список на экран
