#!/usr/local/bin/python3
"""Guess the Secret Number"""
#secret_number = 7 # for initial testing
import random
import clear_screen
import validate_input

secret_number = random.randint(1, 99)
guess = 0
wrong_guesses_to_go = 20

while guess != secret_number and wrong_guesses_to_go > 0:
    guess = input("Please guess a number between 1 and 99 - you have {0} guesses to go: ".format(wrong_guesses_to_go))
    checked_input = validate_input.is_numeric(guess)
    if checked_input != guess:
        print(checked_input)
        continue
#    if not guess.isdigit():
#        print("Invalid input - please try again.")
#        continue
    guess = int(guess)
    wrong_guesses_to_go -= 1
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        wrong_guesses_to_go = 1
        print("Well done you - that's correct!")
        break
if wrong_guesses_to_go == 0:
    print("Sorry, you are out of guesses.  The number was: ", secret_number)