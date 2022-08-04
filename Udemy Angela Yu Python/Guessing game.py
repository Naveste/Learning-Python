from random import *

#randomly choose a number between 1 and 100
rand_num = randint(1, 100)

difficulty = ['easy', 'hard']
guess_attempts = 0
#let user choose difficulty level
user_level = input("Choose difficulty, 'easy' or 'hard': ").lower()

#if user level doesnt enter either 'easy' or 'hard' then keep repeating input until valid input is entered.
while user_level not in difficulty:
    user_level = input("Error, please write only 'easy' or 'hard': ").lower()
else:
    if user_level == 'easy':
        guess_attempts = 10
    elif user_level == 'hard':
        guess_attempts = 5

print(f"You have {guess_attempts} attempts to guess the number.")

#cheat:
print(f"The random number is {rand_num}")

active = True

while active:
    try:
        user_guess = int(input("Guess the number: "))
    #thrown an error if user doesnt enter a number.
    except ValueError:
        print("Please enter only a number.")
        continue
    
    guess_attempts -= 1
    attempts_remaining = f"You have {guess_attempts} attempts remaining to guess the number."

    if user_guess == rand_num:
        print(f"Correct. The number was {rand_num}.")
        active = False
    elif guess_attempts == 0:
        print(attempts_remaining)
        print("You ran out of guesses!")
        active = False
    
    elif user_guess > rand_num:
        print("Too high.")
        print(attempts_remaining)
    else:
        print("Too low.")
        print(attempts_remaining)