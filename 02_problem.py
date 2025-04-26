""" The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score. """
import random
def game():
    print("Your are playing the game...")
    score = random.randint(1,100)
    # Fetch the hiscore
    with open("Hi_score.txt")as f:
        Hi_score = f.read()
        if(Hi_score!= ""):
            Hi_score = int(Hi_score)
        else:
            Hi_score = 0
    print(f"Your score : {score}")
    if(score>Hi_score):
        # write this hiscore to the file
        with open("Hi_score.txt","w")as f:
            f.write(str(score))
    return score
game()                
                
        
        