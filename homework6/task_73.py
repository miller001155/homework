'''Задача 73'''

favorite_dishes = input('введите ваши любимые блюда:').split()  # запрашиваем у пользователя любимые блюда
favorite = {}  # создаем пустой словарь
for key in range(len(favorite_dishes)):  # через цикл добавляем значения в словарь
    favorite[(key + 1)] = favorite_dishes[key]  # добавление в словарь значений
print(favorite)  # вывод словаря на экран

removing_a_dish = int(input('какой элемент вы хотите исключить:'))  # запрос на удаления блюда из списка
favorite_dishes.pop((removing_a_dish - 1))
for key in range(len(favorite_dishes)):  # через цикл добавляем значения в словарь
    favorite[(key + 1)] = favorite_dishes[key]  # добавление в словарь значений
print(favorite)

# торт пиво чай кофе
