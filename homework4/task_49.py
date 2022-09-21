compnum = 50  # переменная с которой должно совпасть
number = int(input('введите число:'))  # запрос на ввод переменной
attempts = 1  # счетчик хранения числа попыток
while compnum != number:  # цикл
    print('введенное вами число не совпадает, ', end='')  # вывод информации, что числа не совпадают
    if number < compnum:  # условие
        print('оно меньше ')
    else:
        print('оно больше')
    attempts += 1  # прибавляем один к счетчику
    number = int(input('введите число:'))  # запрос на повторную попытку
print(f'Well done you took {attempts} attempts')  # вывод количества попыток
