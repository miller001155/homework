import csv  # импортируем модуль

examplefile = open('Books.csv', 'w', encoding='UTF-8', newline='')  # используем оператор with, чтобы открыть файл
examplewriter = csv.writer(examplefile, delimiter=';')  # конвертируем пользовательские данные в CSV-файл
exampledata = [['0', 'To Kill a Mockingbird', 'Harper Lee', '1960'],
               ['1', 'A Brief History of Time', 'Stephen Hawking', '1988'],
               ['2', 'The Great Gatsby', 'F. Scott Fitzgerald', '1922'],
               ['3', 'The Man Who Mistook His Wife for a Hat', 'Oliver Sacks', '1985'],
               ['4', 'Pride and Prejudice', 'Jane Austen', '1813']]  # список данных для записи
for row in exampledata:  # с помощью цикла добавляем каждый элемент в файл
    examplewriter.writerow(row)  # метод для записи строки
examplefile.close()  # закрываем файл
