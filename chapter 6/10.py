class Bear:
    def eats(self):
        return "berries"

class Rabbit:
    def eats(self):
        return "clover"

class Octothorpe:
    def eats(self):
        return "campers"

class Superanimal:
    def __init__(self):
        self.rabbit = Rabbit()
        self.bear = Bear()

    def eating(self):
        return '''
            Eating many food:
            %s and %s
            ''' % (self.rabbit.eats(), self.bear.eats())

animal = Superanimal()
print(animal.eating())
