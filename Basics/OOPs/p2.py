# Write a class “Calculator” capable of finding square, cube and square root of a
# number.
import math
class Calculator:
    def __init__(self,n):
        self.n=n 
    def square(self):
        print(f"Square of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"Cube of {self.n} is {self.n*self.n*self.n}")
    def sqrt(self):
        print(f"Square root of {self.n} is {math.sqrt(self.n)}")
a=Calculator(5)
a.square()
a.cube()
a.sqrt()

        