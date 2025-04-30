#  snake, water gun game
import random
'''
snake= 1
water = -1 
gun =0
'''
print("Enter\n s for snake \n w for water \n g for gun")

userInput =input("Enter you choice: ")

all = {"s":1,"w":-1, "g":0}

userChoice=all[userInput]
print("User choice: ",userChoice)

compChoice=random.choice(list(all.values()))
print("Computer Choice: ",compChoice)

if(compChoice == userChoice):
    print("Draw")
else:
    if(userChoice==1 and compChoice==-1):
        print("User wins")
    elif(userChoice==-1 and compChoice==0):
        print("User wins")
    elif(userChoice==1 and compChoice==0):
        print("Computer wins")
    elif(userChoice==-1 and compChoice==1):
        print("Computer wins")
    elif(userChoice==0 and compChoice==-1):
        print("Computer wins")
    elif(userChoice==0 and compChoice==1):
        print("User wins")
    else:
        print("Something went wrong")
