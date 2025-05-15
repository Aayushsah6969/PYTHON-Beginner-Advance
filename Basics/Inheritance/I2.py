class Animal:
    def speak(self):
        print("I am an Animal")

class Dog(Animal):
    def speak(self):  #Overriding the speak method of parent successfully
        super().speak()
        print("I am a Dog")

    def bark(self):
        print("I Bark")

d=Dog()
d.speak()
d.bark()
