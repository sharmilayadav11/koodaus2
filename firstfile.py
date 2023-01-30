class Car:
    def __init__(self, registrationnumber, color, model):
        self.registrationnumber = registrationnumber
        self.color = color
        self.model = model

    def printname(self):
        print(self.registrationnumber, self.color, self.model)

# Use the Person class to create an object, and then execute the printname method:


x = Car("1212", "Red", "Tyota")
x.printname()
