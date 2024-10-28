import sqlite3

with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gamers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    ) ''')
    # cursor.execute('''INSERT INTO gamers(name) VALUES
    # ('beka'),('akeb'),('milana')
    # ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS games(
    games_id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER NOT NULL,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES gamers(id)
    ) ''')
    cursor.execute('''SELECT * FROM gamers''')
    for row in cursor:
        print(row)

    # cursor.execute('''INSERT INTO games (score, user_id)
    # VALUES (120,1),(120,2),(300,3),(130,1),(190,1)
    # ''')
    cursor.execute('''SELECT COUNT(DISTINCT user_id) FROM games''')
    for row in cursor:
        print(row)
    print()
    cursor.execute('''SELECT COUNT(user_id) FROM games WHERE user_id=1''')
    for row in cursor:
        print(row)
    print()
    # min max count avr sum
    cursor.execute('''SELECT user_id,COUNT(user_id),SUM(score) FROM games WHERE user_id=1''')
    # for i in cursor:
    #     print(i)

    cursor.execute('''SELECT gamers.name,COUNT(games.user_id),SUM(games.score)
    FROM gamers JOIN games ON games.user_id = gamers.id 
    ''')

    for row in cursor:
        print(row)