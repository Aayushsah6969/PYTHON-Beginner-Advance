age=int(input("Enter your age: "))

if(age <=40):
    print("You are Young")
    if(age <= 20 & age >= 13):
        print("You are a Teenager")
        if(age <=12):
            print("You are a Kid")
elif(age >= 60):
    print("Cannot work for government")
    print("You get pension")
elif(age>100):
    print("You are too old to work")
else:
    print("Please enter a valid age")


        