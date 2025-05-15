# def get():
#     print("Hello from function 1")
# get()

# def helo(name):
#     print("Hello Mr. ",name)
# helo("Aayush")

# a=int(input("Enter a number: "))
# def square(num):
#     num=num*num
#     print("Square of given number is: ",num)
# square(a)

# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# def agv(a,b):
#     c=(a+b)/2
#     return c
# d=agv(4,5)
# print("Average of two numbers is: ",d)
# print("Average of two numbers is: ",c) c is only in the scope of function


# def gret(name, end="Thank You"):
#     print("Good day, "+name)
#     print(end)
#     print(f"Have a nice day {name}")
# gret("Aayush","Nice day")

#factorial
def fact(n):
    i=1
    f=1
    for i in range(n,1,-1):
        f=f*i
    print(f"Factorial = {f}")
a=int(input("Enter a number: "))
fact(a)



