#Write a program using functions to find greatest of three numbers.
def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
n3=int(input("Enter number: "))
g=great(n1,n2,n3)
print(f"The greatest is: {g}")