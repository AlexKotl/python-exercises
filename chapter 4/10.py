def test(func):
    print("start")
    func()
    print("end")

test(lambda : print("Hey"))
