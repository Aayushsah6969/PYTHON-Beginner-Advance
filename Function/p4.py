# Write a recursive function to calculate the sum of first n natural numbers
a = int(input("Enter a number: "))

def add(n):
    if (n<=0):
        return n
    else:
        return n+add(n-1)
print("Value = ",add(a))