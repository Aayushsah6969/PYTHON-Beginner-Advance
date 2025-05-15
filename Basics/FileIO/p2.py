# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score

import random

L=[0,1,2,3,4,5,6,7,8,9,10]

def game():
    a=random.choice(L)
    return a

new_score=game()

f= open("Hi-score.txt","r")
previous = f.read()
f.close()

if(previous):
    previous_score =int(previous)
else:
    previous_score=0

if(previous_score < new_score):
    print("Hi score detected")
    f2=open("Hi-score.txt", "w")
    new=str(new_score)
    f2.write(new)
    f2.close()
else:
    print("High Score is not crossed")




    
