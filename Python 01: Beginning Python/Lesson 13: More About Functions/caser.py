#!/usr/local/bin/python3
""" Change the case of a string """

import sys
import clear_screen

def capitalize(text):
    return text.capitalize()
    
def title(text):
    return text.title()
    
def upper(text):
    return text.upper()
    
def lower(text):
    return text.lower()
    
def exit(text):
    print('Program Exiting')
    sys.exit()

if __name__ == "__main__":
    user_nudge = 'an'
    switch = {'capitalize': capitalize,
              'title': title,
              'upper': upper,
              'lower': lower,
              'exit': exit
    }
    
    options = switch.keys()
    while True:
        prompt = 'Pick {0} option from the list ({1}) followed by your text: \n'. format(user_nudge,', '.join(options))    
        user_nudge = 'an'
        user_input = input(prompt).split()
        option = switch.get(user_input[0], None)
        if option:
            print(option(' '.join(user_input[1:])) + '\n')
        else:
            user_nudge = 'a VALID'
            continue
