class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def printInfo(self):
        print(f"My name is {self.name} and age is {self.age}")

m1 = Student("Aayush",21)
m2=Student("Kumar",20)

m1.printInfo()
m2.printInfo()