import csv

user_input = input('Введите данные для добавления в файл через точку с запятой(;):')
user_input = user_input.split(';')

examplefile = open('Books.csv', 'a', encoding='UTF-8', newline='')  # используем оператор with, чтобы открыть файл
examplewriter = csv.writer(examplefile, delimiter=';')  # конвертируем пользовательские данные в CSV-файл
exampledata = user_input  # список данных для записи
examplewriter.writerow(exampledata)  # метод для записи строки
examplefile.close()

examplefile = open('Books.csv', encoding='UTF-8')
examplereader = csv.reader(examplefile, delimiter=';')
exampledata = list(examplereader)
print(exampledata)
for i in exampledata:
    print(i)
examplefile.close()
