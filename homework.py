"""Программа 1"""

my_list = ['красный', 'зеленый', 'белый', 'черный', 'розовый', 'желтый']
my_list.remove("красный")  # удаление по знаению
my_list.pop()  # удаление по индексу
del my_list[-1]  # удаление по индексу с помощью del
print(my_list)

"""Программа 2"""

my_list = ['красный', 'зеленый', 'белый', 'черный', 'розовый', 'желтый']
my_list_2 = ['фиолетовый', 'синий']
my_list_new = my_list + my_list_2  # с помощью оператора + добавляем новый списzок к существующему
print(my_list_new)

"""Программа 3"""

my_dict = {1: 'main', 'volue': 2, 'master': 'api'}
my_list = list(my_dict.items())
print(my_list)

"""задача 1"""

name_user = input("введите ваше имя:")  # с помощью input запрашиваем имя пользователя
print(f'Hello {name_user}')  # с помощью F строк выводим сообщение

"""задача 2"""

name_user = input("введите ваше имя:")  # с помощью input запрашиваем имя пользователя
surname_user = input("введите вашу фамилию:")  # с помощью input запрашиваем фамилию пользователя
print(f'Hello {name_user} {surname_user}')  # с помощью F строк выводим сообщение

"""задача 3"""

print("What do you call a bear with no teeth?\nA gummy bear!")  # с помощью \n осуществляется перенос строки

"""задача 4"""

number_1 = float(input("введите число:"))  # с помощью input запрашиваем число
number_2 = float(input("введите число:"))  # с помощью input запрашиваем число
sum_of_numbers = number_1 + number_2  # создаем переменную и храним в ней сумму чисел
print(f'The total is {sum_of_numbers}')  # с помощью F строк выводим сообщение

"""задача 5"""

number_1_1 = float(input("введите число:"))  # с помощью input запрашиваем число
number_2_1 = float(input("введите число:"))  # с помощью input запрашиваем число
number_3_1 = float(input("введите число:"))  # с помощью input запрашиваем число
result = (number_1_1 + number_2_1) * number_3_1
print(f'The answer is {result}')

"""задача 5"""

number_of_pizza = int(input("Сколько кусков пиццы было ?:"))  # с помощью input запрашиваем количество кусков пиццы
amount_of_pizza_eaten = int(
    input("Сколько кусков пицццы сьеденно ?:"))  # с помощью input запрашиваем количество съеденного
resulting_of_pizza = number_of_pizza - amount_of_pizza_eaten  # подсчитываем остаток
print(f'leftover pizza: {resulting_of_pizza}')  # выводим результат

"""задача 7"""

user_name = input("введите ваше имя:")  # с помощью input запрашиваем имя пользователя
user_age = int(input("введите ваш возраст:"))  # с помощью input запрашиваем возраст
user_age_new = user_age + 1  # создаем переменную и добавляем к возрасту один год
print(f'{user_name} next birthday you will be {user_age_new}')  # с помощью F строк выводим сообщение

"""задача 8"""

invoice_amount = int(input("введите сумму счета:"))  # с помощью input запрашиваем сумму счета
number_of_participants = int(input("введите количество учасников:"))  # с помощью input запрашиваем количество гостей
amount_per_participant = invoice_amount / number_of_participants  # создаем переменную и делим сумму на количество
print(f'сумма которую должен заплатить участник: {amount_per_participant}')  # с помощью F строк выводим сумму

"""задача 9"""

time_interval_in_days = int(input("введите промежуток времени в днях:"))  # с помощью input запрашиваем промежуток
number_of_hours = time_interval_in_days * 24  # создаем переменную для хранения часов
number_of_minutes = time_interval_in_days * 1440  # создаем переменную для хранения минут
number_of_seconds = time_interval_in_days * 86400  # создаем переменную для хранения сукунд
print(f'количество часов: {number_of_hours},\n минут: {number_of_minutes},\n секунд: {number_of_seconds}')  # вывод
# результата

"""задача 10"""

weight_user = float(input("введите ваш вес:"))  # с помощью input запрашиваем вес пользователе
weight_in_pounds = weight_user * 2.204  # добовляем переменную которая переводит в фунты
print("ваш вес в фунтах:" + str(weight_in_pounds))  # вывод веса в фунтах и преобразование числа в строку

"""задача 11"""

number_greater_than_100 = int(input("введите число больше ста:"))  # с помощью input запрашиваем число
number_less_than_10 = int(input("введите число меньше 10:"))  # с помощью input запрашиваем число
number_of_occurrences = number_greater_than_100 // number_less_than_10  # переменная с целочислунным делением
print(f'меньшее число помещается в большее {number_of_occurrences} раз!')  # с помощью F строк выводим результат
