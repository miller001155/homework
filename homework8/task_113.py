import csv

user_ask = int(input('Сколько записей вы хотите добавить в список?:'))
count = 0
while count < user_ask:
    user_input = input('Введите данные для добавления в файл через точку с запятой(;):')
    user_input = user_input.split(';')
    examplefile = open('Books.csv', 'a', encoding='UTF-8', newline='')
    examplewriter = csv.writer(examplefile, delimiter=';')
    examplewriter.writerow(user_input)
    examplefile.close()
    count += 1
author_name = input('Введите имя автора:')
examplefile = open('Books.csv', encoding='UTF-8')
examplereader = csv.reader(examplefile, delimiter=';')
exampledata = list(examplereader)
fa = exampledata[0].count(author_name)
if fa > 0:
    for i in exampledata:
        q = exampledata.index(author_name)
        w = exampledata[q]
        print(w)
else:
    print('Такого автора нет в списке')
