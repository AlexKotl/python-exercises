import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM books ORDER BY title')
rows = cursor.fetchall()
for row in rows:
    print(row[2])
