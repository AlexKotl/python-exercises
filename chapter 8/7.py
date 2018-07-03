import csv
import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

with open('books.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    for row in cin: 
        print(row)
        cursor.execute('INSERT INTO books (author, title) VALUES (?, ?)', (row['author'], row['book'])       )
    #books = [row for row in cin]
connection.commit()


