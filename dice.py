import random as rd

# setting a random variable
a = True

# loop for a digit in dice
while a:
    print(rd.randint(1,6))
    roll_again = input('Wanna roll again ? (y/n) = ')
    if roll_again.lower() == 'y' :
        continue
    else :
        break
    