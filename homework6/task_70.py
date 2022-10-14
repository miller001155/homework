'''Задача 70'''
countries = ('Belarus', 'Russia', 'Poland', 'Lithuania', 'Ukraine')  # создаем кортеж с 5-ю странами
print(countries)  # выводим список на экран
user_country = int(input('Введите число:'))  # пользователь вводит индекс
if user_country <= (len(countries) - 1):  # проверяем что бы число не превышало длину списка стран
    print(countries[user_country])  # выводим название страны по индексу
else:
    print('Такого числа нет в списке')  # выводим что такого индекса нет в списке
