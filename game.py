print('----------STARTING NEW RUN----------')

import pandas as pd
import random

lowest_num = 0
highest_num = 100

print('GENERATING RANDOM NUMBER BETWEEN: ' , lowest_num , ' AND ' , highest_num)
random_number = random.randint(lowest_num, highest_num)
print(random_number)

user_guess = -1


user_guess = input('Guess the random number:')
user_guess = int(user_guess)

print('User guess: ', user_guess)

while user_guess != 'quit':
    user_guess = input('Type a random number:')

    try:
        user_guess = int(user_guess)
    except:
        if user_guess == 'quit':
            break
        else:
            print('Please type a number or quit\n')
    print('User guess: ', user_guess, '\n')
    if user_guess == random_number:
        break

if user_guess == 'quit':
    print('Sorry try again later :(')
else:
    print('CONGRATS you guessed the mystery number!\n')

print('----------FINISHED RUN----------')
# TODO: Cannot win game on first guess for some reason?