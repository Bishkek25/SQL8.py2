import sqlite3 as sq

# Создаем или открываем базу данных
with sq.connect('test.db') as connection:
    cursor = connection.cursor()

    # Создаем таблицу, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName VARCHAR(50) NOT NULL,
            LastName VARCHAR(50) NOT NULL,
            BirthYear INT,
            Hobby VARCHAR(100),
            HomeworkScores INT
        )
    ''')

    # Вставляем данные о студентах
    cursor.execute('''
        INSERT INTO Students (FirstName, LastName, BirthYear, Hobby, HomeworkScores)
        VALUES
        ('Абдырахманова', 'Кундуз', 2000, 'Чтение', 85),
        ('Ажибекова', 'Камила', 1999, 'Спорт', 90),
        ('Анарабекова', 'Сайкал', 2001, 'Музыка', 78),
        ('Арзыматов', 'Марат', 2000, 'Рисование', 92),
        ('Асанов', 'Абдель', 1998, 'Туризм', 88),
        ('Аширматкулов', 'Нурислам', 1999, 'Фотография', 95),
        ('Баштовенко', 'Дарья', 2002, 'Кулинария', 80),
        ('Дуйшеев', 'Атай', 2001, 'Путешествия', 87),
        ('Клычев', 'Темирлан', 2000, 'Игры', 82),
        ('Кожокеев', 'Даир', 1999, 'Танцы', 91)
    ''')

    # Сохраняем изменения
    connection.commit()

    # Выбираем данные о студентах
    cursor.execute('SELECT FirstName, LastName, BirthYear, Hobby, HomeworkScores FROM Students')

    # Выводим результаты
    for row in cursor.fetchall():
        print(row)
