'''Задача 74'''

colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white', 'turquoise']  # список цветов
initial_range = int(input('Введите начальный диапазон от 0 до 4:'))  # начальный диапазон
end_ange = int(input('Введите конечный диапазон от 5 до 9:'))  # конечный диапазон
if (initial_range <= 4 and initial_range >= 0) and (end_ange >= 5 and end_ange < 9):  # условие проверки ввода
    slice = colors_list[initial_range:end_ange]  # сохранение среза в переменную
    print(slice)  # вывод на экран среза
else:
    print('Вы ввели не правильные параметры!')  # вывод ошибки ввода
