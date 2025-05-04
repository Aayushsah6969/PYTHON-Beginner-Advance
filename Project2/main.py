from random import randint

target= randint(40,190)
print("Target is: ",target)

print("Guess the number between 0 to 200")
print("You get only 6 chances")
chances=6
while(chances >= 1):
    guess=int(input("Enter your guess: "))
    chances = chances-1
    if(guess == target):
        print("YOU WIN")
        break
    elif(guess > target):
        print("Guess is higher")
        print("Remaining chances: ",chances)
    else:
        print("Guess is Lower")
        print("Remaining chances: ",chances)



    


