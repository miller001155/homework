import sqlite3 as sq  # импорт нужной библиотеки

with sq.connect('PhoneBook.db') as con:
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS name (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        First_name TEXT,
        Surname TEXT,
        Phone_Number INTEGER
    )
    """
                )  # создание таблицы
    con.commit()  # сохранение изменений

    cur.execute('''
        INSERT INTO name (id, First_name, Surname, Phone_Number) VALUES (1,'Simon', 'Howeis', 01223349752);
 ''')  # добавление данных в таблицу
    cur.execute('''
        INSERT INTO name (id, First_name, Surname, Phone_Number) VALUES (2, 'Karen', 'Philips', 01954295773);
    ''')
    cur.execute('''
        INSERT INTO name (id, First_name, Surname, Phone_Number) VALUES (3,'Darren', 'Smith', 01583749012);
 ''')
    cur.execute('''
        INSERT INTO name (id, First_name, Surname, Phone_Number) VALUES (4, 'Anne', 'Jones', 01323567322);
    ''')
    cur.execute('''
        INSERT INTO name (id, First_name, Surname, Phone_Number) VALUES (5, 'Mark', 'Smith', 01223855534);
    ''')
    con.commit()  # сохранение изменений_
