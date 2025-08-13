print('----------STARTING NEW RUN----------\n\n\n')

import pandas as pd
import random

print('Welcome to the Random Number Guessing Game!!!')
print('A mystery number is going to be generated, you have as many guesses as you want!')
print('Type in a number and press enter to guess')
print('If you want to quit, just type \'quit\' and press enter\n\n')


lowest_num = 0
highest_num = 100

print('GENERATING RANDOM NUMBER BETWEEN: ' , lowest_num , ' AND ' , highest_num)
print()
random_number = random.randint(lowest_num, highest_num)
# print(random_number)

user_guess = -1


while user_guess != 'quit':
    user_guess = input('Guess the random number:')

    try:
        user_guess = int(user_guess)
    except:
        if user_guess == 'quit':
            print('-----------------------')
            break
        else:
            if user_guess == 'Claire':
                 print('I LOVE YOU CLAIRE, YOU ARE THE LOVE OF MY LIFE,')
                 print('LOVE CHARLIE <3333\n\n')
                 print('-----------------------')
                 continue
            print('Please type a number or quit\n\n')
            print('-----------------------')
            continue
    
    if user_guess > highest_num:
         print('Guess is higher than maximum number\n')
         print('-----------------------')
         continue
    if user_guess < lowest_num:
         print('Guess is lower than lowest number\n')
         print('-----------------------')
         continue

    print('User guess: ', user_guess, '\n')
    
    if user_guess == random_number:
        break
    if user_guess > random_number:
            print('Mystery number is lower than that\n')
    if user_guess < random_number:
            print('Mystery number is higher than that\n')
    print('-----------------------')

if user_guess == 'quit':
    print('Sorry try again later :(\n')
else:
    print('CONGRATS you guessed the mystery number!\n')

print('----------FINISHED RUN----------')