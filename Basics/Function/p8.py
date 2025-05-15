# Write a python function to print multiplication table of a given number

a=int(input("Enter number: "))

def table(n=5,i=10):
    if(i<=0):
        return
    else:
        print(f"{n} * {i} = {n*i}")
        table(5,i-1)
table(a)