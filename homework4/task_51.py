score = int(input('Введите количество бутылок: '))  # вводим количество бутылок
print(f'There are {score} green bottles hanging on the wall, {score} '
      f'green bottles hanging on the wall, and if 1 green bottle should accidentally fall.')  # выводим на экран условие
print('how many green bottles will be hanging on the wall?')
answer = int(input('Введите ответ:'))  # просим ввести пользователя ответ на заданное условие
while answer != score - 1:  # задаем цикл при котором ответ не верный
    if answer == 0:
        print('there are no more green hanging on the wall')
        break
    print('no, try again')  # выводим на экран, что ответ неверный
    answer = int(input('Введите ответ:'))
if answer == score - 1:
    print(f'There will be {answer} green bottles hanging on the wall')

