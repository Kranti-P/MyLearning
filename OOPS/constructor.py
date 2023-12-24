class Person:
    def __init__(self):
        print('Default constructor is called')

    def __init__(self, n, o):
        self.name = n
        self.gender = o

    def identity(self, name, gender):
        print(self.name, "is a person having gender =", self.gender)

    def identity(self, name, gender):
        print(name, "is having gender =", gender)


p = Person("Kranti", "Female")
p.identity("Kranti", "F")
p.identity("Atul", "M")