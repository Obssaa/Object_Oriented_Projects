class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        return 'Hello!'
    def get_name(self):
        return self.name

class Cat(Animal):
    def talk(self): #overode the function talk in parent class
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


# Create a list of objects
animals = [Cat('Missy'), Cat('Mr. B'), Dog('Lassie')]
for readList in animals:
    print(readList.talk()+' I am '+ readList.get_name())

