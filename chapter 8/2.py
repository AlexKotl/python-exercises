try:
    f = open('test.txt', 'rt')
    test2 = f.read()
    print(test2)
except:
    print("Cant open file")



