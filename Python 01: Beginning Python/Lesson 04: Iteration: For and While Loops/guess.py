#!/usr/local/bin/python3
"""Guess the Secret Number"""
#secretNumber = 7 # for initial testing
import random
secretNumber = random.randint(1, 20)
guess = 0
wrongGuessesToGo = 5

while guess != secretNumber and wrongGuessesToGo > 0:
    guess = int(input("Please guess a number between 1 and 20: "))
    wrongGuessesToGo -= 1
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        wrongGuessesToGo = 1
        print("Well done you - that's correct!")
        break
if wrongGuessesToGo == 0:
    print("Sorry, you are out of guesses.  The number was: ", secretNumber)