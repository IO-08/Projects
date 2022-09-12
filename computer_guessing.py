import random

def computer_guess ( x ) :
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high :
            guess = random.randint ( low, high )
        else :
            guess = low  # could be low as well
        feedback = input ( f'Is {guess} too High (H), too low (L), is correct (C) ??' ).lower
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1


    print (f'yah the computer {guess} is the correct number')


computer_guess (10)
