from random import randrange

number = randrange(0, 38)
if number == 37:
    print(f'Выпавшие номер: 00')
else:
    print(f'Выпавший номер : {number}')
if number == 37:
    print(f'Выграла ставка: 00')
else:
    print(f'Выграла ставка: {number}')
if number % 2 == 1 and number >= 1 and number <= 9 or number % 2 == 0 and number >= 12 and number <= 18 \
        or number % 2 == 1 and number >= 19 and number <= 27 \
        or number % 2 == 0 and number >= 30 and number <= 36:
    print(f'выигранная ставка: Красное')
elif number == 0 or number == 37:
    pass
else:
    print(f'выигранная ставка: Черное')
if number >= 1 and number <= 36:
    if number % 2 == 1:
        print(f'Выигранная ставка : Нечетное')
    else:
        print(f'Выигранная ставка : Четное')

if number >= 1 and number <= 18:
    print('Выиграла ставка: от 1 до 18')
else:
    print('Выиграла ставка: от 19 до 36')
