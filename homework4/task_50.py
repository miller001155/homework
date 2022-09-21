number = int(input('Введите число от 10 до 20 :'))  # запрос на ввод переменной
while number < 10 or number > 20:  # цикл, который срабатывает если число не в заданном диапазоне
    if number < 10:
        print('Too low')
    elif number > 20:
        print('Too high')
    number = int(input('Введите число от 10 до 20 : '))  # повторный запрос на ввод переменной
print('Thank you')  # вывод сообщения
