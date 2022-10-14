'''Задача 69'''
countries = ('Belarus', 'Russia', 'Poland', 'Lithuania', 'Ukraine')  # создаем кортеж с 5-ю странами
print(countries)  # выводим список на экран
user_country = str(input('Введите название страны:')).title()  # пользователь вводит название страны
if user_country in countries:  # если страна есть в списке
    print(countries.index(user_country))  # то выводим индекс в списке
else:
    print('Такой страны нет в списке')
