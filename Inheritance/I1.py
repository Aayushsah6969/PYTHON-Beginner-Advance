class Animal:
    def speak(self):
        print("I am an Animal")

class Dog(Animal):
    def bark(self):
        print("I Bark")

d=Dog()
d.speak()
d.bark()
