while True:  # создаем бесконечный цикл
    print('деления двух чисел :')
    arg = input("если ходите остановить то введите (y) иначе нажмите Enter: ")  # для выхода из цикла создаем переменную
    if arg == "y":
        break
    else:
        try:  # две переменные должны быть числами
            num_1 = int(input('Введите число:'))
            num_2 = int(input('Введите 2 число:'))
            print( num_1 / num_2)
        except ValueError:  # введена буква
            print('Введите только цифры и попробуйте снова')
        except TypeError:  # введена строка
            print('Введите правильный тип данных')
        except ZeroDivisionError:  # если второе число 0
            try:
                print('Деление на ноль не возможно')
                num_2 = int(input('Введите 2 число:'))  # запрос на повторный ввод
                print(num_1 / num_2)
            except ValueError:
                print('Введите только цифры')  # если ввел букву, то повтор ввода
                num_2 = int(input('Введите 2 число:'))
                print(num_1 / num_2)

        finally:
            print('будут еще действия на ', end='')