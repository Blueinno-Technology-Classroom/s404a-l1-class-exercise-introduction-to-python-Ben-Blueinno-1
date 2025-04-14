# import random

from random import randint

minimum = 1
maximum = 100

my_number = randint(minimum, maximum)

# print(my_number)

game_set = False

while not game_set:
    guess = int(input(f'Guess my number from {minimum} to {maximum}: '))

    print(f'Your guess is {guess}')

    if my_number == guess:
        print("You win! That's my number!")
        game_set = True
    elif guess > my_number:
        print('Too large')
        maximum = guess
    elif guess < my_number:
        print('Too small')
        minimum = guess
