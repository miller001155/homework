import sqlite3 as sq  # импорт нужной библиотеки

more_users = [('1', 'Simon', 'Howeis', '01223349752'),
              ('2', 'Karen', 'Philips', '01954295773'), ('3', 'Darren', 'Smith', '01583749012'),
              ('4', 'Anne', 'Jones', '01323567322'), ('5', 'Mark', 'Smith', '01223855534')]  # создаем список пользоват.

with sq.connect('PhoneBook_1.db') as con:
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS name (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First name TEXT,
    Surname TEXT,
    Phone Number INTEGER
    )
    """
                )  # создание таблицы
    con.commit()  # сохранение изменений

    cur.executemany("INSERT INTO name VALUES(?, ?, ?, ?);", more_users)  # добавление данных в таблицу
    con.commit()  # сохранение изменений
