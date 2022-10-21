import sqlite3 as sq  # импорт нужной библиотеки

with sq.connect('PhoneBook.db') as con:
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS names (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First name TEXT,
    Surname TEXT,
    Phone Number INTEGER
    )
    """
                )  # создание таблицы
    con.commit()  # сохранение изменений

    cur.execute('''
    INSERT INTO names (id, First, Surname, Phone) VALUES (1,'Simon', 'Howeis', 01223349752);
    INSERT INTO names (id, First, Surname, Phone) VALUES (2, 'Karen', 'Philips', 01954295773);
    INSERT INTO names (id, First, Surname, Phone) VALUES (3,'Darren', 'Smith', 01583749012);
    INSERT INTO names (id, First, Surname, Phone) VALUES (4, 'Anne', 'Jones', 01323567322);
    INSERT INTO names (id, First, Surname, Phone) VALUES (5, 'Mark', 'Smith', 01223855534);
    ''')  # добавление данных в таблицу
    con.commit()  # сохранение изменений
