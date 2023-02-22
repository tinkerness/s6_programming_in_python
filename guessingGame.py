"""
a simple game to guess number generated
"""
import random

low = int(input("enter lower range : "))
high = int(input("enter higher range : "))

numberGenerated = random.randint(low, high)
# print(numberGenerated)
count = 0
while 1:
    count += 1
    guess = int(input("enter guess : "))

# if guess = numberGenerated:
#    print("you are right")
    if guess < numberGenerated:
        print("\nnumber is too small")
    elif guess > numberGenerated:
        print("\nnumber is too big")
    else:
        print("\ncongratulations! you got it in ", count, " tries!")
        break
