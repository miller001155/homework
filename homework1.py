""" задание 1"""

a = 17 / 2 * 3 + 2  # 27.5
b = 2 + 17 / 2 * 3  # 27.5
c = 19 % 4 + 15 / 2 * 3  # 25.5
d = (15 + 6) - 10 * 4  # -19
e = 17 / 2 % 2 * 3  # 1.5
print(a, b, c, d, e, )

""" задание 2"""

a_1 = 17 / (2 * 3) + 2  # 4.83
b_1 = (2 + 17) / 2 * 3  # 28.5
c_1 = 19 % 4 + 15 / (2 * 3)  # 5.5
d_1 = 15 + (6 - 10) * 4  # -1
e_1 = 17 / 2 % (2 * 3)  # 2.5
print(a_1, b_1, c_1, d_1, e_1)

""" задание 3"""

dima = 28
sasha = 29
andrew = 30
print(dima + sasha + andrew)  # простой способ
friends = [dima, sasha, andrew]
print(sum(friends))  # вывод через функцию

""" задание 4"""

average_age_of_friends = sum(friends) / len(friends)
print((average_age_of_friends))

""" задание 5"""

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
my_list_set = set(my_list)
my_list_amount_of_non = len(my_list) - len(my_list_set)
print(my_list_amount_of_non)

""" задание 6"""

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
my_list_2 = my_list[2:5]
my_list_2.reverse()  # пробовал сразу с обратным индексок в шеге , не помогло
print(my_list_2)

""" задание 7"""

side_of_a_square = int(input("Введите сторону квадрата:"))
list_area_perimeter_diagonal = [side_of_a_square * 4, side_of_a_square ** 2, (2 * side_of_a_square ** 2) ** .5]
print(list_area_perimeter_diagonal)