# Add a static method in problem 2, to greet the user with hello.

import math

class Calculator:
    @staticmethod
    def greet():
        print("Hello! Welcome to Calculator")
    
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"Square of {self.n} is {self.n * self.n}")
    
    def cube(self):
        print(f"Cube of {self.n} is {self.n * self.n * self.n}")
    
    def sqrt(self):
        print(f"Square root of {self.n} is {math.sqrt(self.n)}")

# Using the static method and other methods
Calculator.greet()  # Can be called without creating an object
a = Calculator(5)
a.square()
a.cube()
a.sqrt()

