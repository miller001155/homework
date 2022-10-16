def decorator_test(func):  # функция декоратор
    def wrapper(a, b):  # доп функция в которую мы оборачиваем старую функцию
        print('выводим сообщение до старой функции :)')  # расширение функционала
        func(a, b)  # вызов функции
        print('Сообщение после функции:)')  # расширение функционала

    return wrapper  # возврат функции


def old_func(a, b):  # старая функция с устаревшим функционалом
    result = a ** b
    print(f'старый код функции, результат возведения в степень: {result}')


old_func = decorator_test(old_func)  # сохраняем декоратор как обновленную функцию
old_func(5, 9)  # вызов обновленной функции
