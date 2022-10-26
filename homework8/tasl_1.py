import json  # импортируем модуль

data = {"key1": "value1", "key2": "value2"}  # создаем словарь который, хотим добавить в файл
with open('data.json', 'w', encoding='UTF-8') as file:  # используем оператор with, чтобы открыть файл
    string = json.dump(data, file)  # используем метод json.dump, чтобы записать наши словари в файл.
