import random

def guessing (x):
    random_number = random.randint(1,x)
    guessing = 0
    while guessing != random_number:
        guessing= int (input (f'Guess a number between 1 and {x}: '))
        if guessing>random_number:
            print("The number is too high")
        elif guessing <random_number:
            print ("The number is too low ")
    print (f"The number {random_number} is  correctly ")

guessing(10)

