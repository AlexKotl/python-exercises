content = '''author,book,id
Alex K,The Programmer,1
Katie K,"Best wife, ever,2"'''

f = open("books.csv", 'wt')
f.write(content)
f.close()
