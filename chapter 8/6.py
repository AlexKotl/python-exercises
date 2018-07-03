import sqlite3
db = sqlite3.connect('books.db')
cursor = db.cursor()
cursor.execute(''' CREATE TABLE books (
    id INT PRIMARY KEY,
    author VARCHAR(255),
    title VARCHAR(255))''')
