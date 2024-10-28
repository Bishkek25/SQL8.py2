import sqlite3

with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    ) ''')
    cursor.execute('''INSERT INTO employees(FirstName,LastName,BirthYear,Hobby,HomeworkScores)
    VALUES
    ('beka'),('akeb'),('milana')
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS (students_id)
       id INTEGER PRIMARY KEY AUTOINCREMENT,FirstName VARCHAR(50) NOT NULL,
       LastName VARCHAR(50) NOT NULL,BirthYear INT,Hobby VARCHAR(100),HomworkScores INT''')
    cursor.execute('''INSERT INTO Students(FirstName,LastName,BirthYear,Hobby,HomeworkScores)
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
       ('Кожокеев', 'Даир', 1999, 'Танцы', 91)''')



    cursor.execute('''CREATE TABLE IF NOT EXISTS departments(
    departments_id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER NOT NULL,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES employees(id)
    ) ''')
    cursor.execute('''SELECT * FROM employees''')
    for row in cursor:
        print(row)

    cursor.execute('''INSERT INTO departments (score, user_id)
    VALUES (101 :HR),(102:IT),(103:Sales),
    ''')
    cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM departments''')
    for row in cursor:
        print(row)
    print()
    cursor.execute('''SELECT COUNT(user_id) FROM departments WHERE user_id=1''')
    for row in cursor:
        print(row)
    print()
    # min max count avr sum
    cursor.execute('''SELECT user_id,COUNT(user_id),SUM(score) FROM departments WHERE user_id=1''')
    # for i in cursor:
    #     print(i)

    cursor.execute('''SELECT .name,COUNT(departments.user_id),SUM(departments.score)
    FROM employees JOIN departments ON departments.user_id = employees.id 
    ''')

    for row in cursor:
        print(row)