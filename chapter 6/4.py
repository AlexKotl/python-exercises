class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def __str__(self):
        return "" + self.__name + " " + self.__symbol + " " + str(self.__number)

obj = Element("Hydrogen", "H", 1)

data = {
    "name": "Hydrogen",
    "symbol": "H",
    "number": 1
}

obj2 = Element(**data)

print(obj2)
