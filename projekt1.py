'''
projekt1.py: This is a python code that runs a guess the number game in the terminal with seven tries and a restart or exit option.

__author__  = "Benjamin Wall Freyne"
__version__ = "1.0.0"
__email__   = "benjamin.wallfreyne@elev.ga.ntig.se"
'''



import os
os.system('cls')


import random


while True:
    print("Welcome to the ultimate guess the number game!")
    print("You have 7 attempts to find my hidden number! Will you be able to do this?")


    tries = 7
    number = random.randint(1,100)


    while tries >= 0:
        print(tries, "tries left!")
        try:
            guess = int(input("Guess a number between 1-100: "))
        except:
            print("That doesn't look like a number in my eyes")
            continue


        if guess == number:
            print ("You found the number! ")
            break  


        elif tries == 0:
                print ("Sorry you lost! ")
        elif guess < number:
                print("Too Low! ")
        elif guess > number:
                print("Too High! ")
        tries -= 1


    if tries == 0:
        replay = str(input("You failed! Do you want to try again?(Y/N)")).upper()
    else:
        replay = str(input("You smashed it! Do you want to try again?(Y/N)")).upper()
    

    if replay in ["N"]:
        print("Have an absolutely awesome day!")
        break
    else:
        continue
