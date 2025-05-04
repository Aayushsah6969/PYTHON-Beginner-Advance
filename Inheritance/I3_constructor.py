class Animal:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent __init__
        self.breed = breed

    def show_breed(self):
        print("Breed:", self.breed)

d = Dog("Buddy", "Labrador")
d.show_name()   # Name: Buddy
d.show_breed()  # Breed: Labrador
