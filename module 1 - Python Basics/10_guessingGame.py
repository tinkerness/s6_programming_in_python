'''At start-up, the user enters the smallest number and the largest number in the range. The computer then selects a number from this range. On each pass through the loop, the user enters a number to attempt to guess the number selected by the computer. The program responds by saying “You’ve got it,” “Too large, try again,” or “Too small, try again.” When the user finally guesses the correct number, the program congratulates him and tells him the total number of guesses.'''

import random

low = int(input("enter lower range : "))
high = int(input("enter higher range : "))

numberGenerated = random.randint(low,high)
#print(numberGenerated)
count=0
while(1):
    count+=1
    guess = int(input("enter guess : "))

    if guess < numberGenerated:
        print("Too small, try again.")
    elif guess > numberGenerated:
        print("Too large, try again")         
    else:
        print("congratulations! You’ve got it in ",count," tries!")
        break