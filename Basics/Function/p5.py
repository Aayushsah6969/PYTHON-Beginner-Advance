'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*

'''

a=int(input("Enter number: "))

def pattern(n):
    if(n<=0):
        return
    else:
        print("*"*n)
        print("")
        pattern(n-1)
pattern(a)
