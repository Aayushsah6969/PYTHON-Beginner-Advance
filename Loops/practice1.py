'''for i in range(1,11,1):
    print("5 X ", i, "=", 5*i)'''

"""l = ["Harry", "Soham", "Sachin", "Rahul"]
for item in l:
    print("Good morning Mr.", item)"""

# i=1
# while(i<=10):
#     print("5 X ", i, "=", 5*i)
#     i+=1

a = int(input("Enter a number: "))

if a < 2:
    print("Not a prime number")
else:
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")