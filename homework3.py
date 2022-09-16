"""Упражнение 36 собачий возраст """

dog_age = float(input("введите возраст:"))
if dog_age > 0 and dog_age <= 2:  # если возраст от 0 до 2 лет
    dog_age_standards = dog_age * 10.5  # то просто умножаем на 10.5 и храним в переменной
    print(f'возраст по собачим меркам:{dog_age_standards}')  # выводим сообшение
elif dog_age > 2:  # если возраст больше 2 лет
    dog_age_standards = (dog_age * 4) + 13  # то умножаем на 4 и прибовляем 2 раза по 6,5
    print(f'возраст по собачим меркам:{dog_age_standards}')  # выводим сообшение
else:
    print("Вы ввели отрицательное число")  # выводим сообшение о том что пользователь ввел отричательное число

"""Упражнение 39 Сколько дней в месяце """

month_name = input("введите название месяца:")  # просим пользователя ввести название месяца
month = {'january': 31, 'march': 31, 'april': 30, 'may': 31, 'june': 30,  # создаем словарь и храним в нем количество д
         'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
if month_name in month:  # если название месяца есть в словаре
    print(f'количество дней: {month.get(month_name)}')  # выводим значение ключа
elif month_name == "February":  # если пользователь ввел февраль
    print("в зависимости от года может быть 28 или 29 дней")  # то выводим такое сообщение
else:  # если значения нет в словаре
    print("вы ввели не правильно название месяца")

"""Упражнение 42 частота по ноте """
note_review = input("Введите обозначение ноты:")  # просим пользователя ввести ноту
note_name = note_review[0]  # с помощью среза созраняем букву ноты в переменной
octave = int(note_review[1])  # с помощью среза созраняем цифру ноты в переменной
C4, D4, E4, F4, G4, A4, B4 = 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88  # присваеваем переменным значения
if note_name == 'C':  # сравниваем то что ввел пользователь
    note_frequency = C4
elif note_name == 'D':
    note_frequency = D4
elif note_name == 'E':
    note_frequency = E4
elif note_name == 'F':
    note_frequency = F4
elif note_name == 'G':
    note_frequency = G4
elif note_name == 'A':
    note_frequency = A4
elif note_name == 'B':
    note_frequency = B4
else:
    print("вы не правильно ввели ноту")  # в других случаях мы ноту не знаем
note_frequency = note_frequency / 2 ** (4 - octave)  # делим на 2 в степени 4 - х
print(f'Частота ноты {note_name}, равна :{note_frequency}') # выводим результат


"""Упражнение 43 узнать ноту по частоте """

C4, D4, E4, F4, G4, A4, B4 = 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88
input_error = 1
note_frequency_new = float(input("Введите частоту ноты :"))

if note_frequency_new >= C4 - input_error and note_frequency_new <= C4 + input_error:
    note_new = 'C4'
elif note_frequency_new >= D4 - input_error and note_frequency_new <= D4 + input_error:
    note_new = 'D4'
elif note_frequency_new >= E4 - input_error and note_frequency_new <= E4 + input_error:
    note_new = 'E4'
elif note_frequency_new >= G4 - input_error and note_frequency_new <= G4 + input_error:
    note_new = 'G4'
elif note_frequency_new >= A4 - input_error and note_frequency_new <= A4 + input_error:
    note_new = 'A4'
elif note_frequency_new >= B4 - input_error and note_frequency_new <= B4 + input_error:
    note_new = 'B4'
elif note_frequency_new >= F4 - input_error and note_frequency_new <= F4 + input_error:
    note_new = 'F4'
else:
    note_new = ''

if note_new:
    print(f'введенная частота соответствует ноте: {note_new}')
else:
    print("не соответствует не одной ноте")

"""Упражнение 49 """

"""Упражнение 52 """
