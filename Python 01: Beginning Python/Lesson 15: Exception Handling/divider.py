#!/usr/local/bin/python3
""" Divides 10 by an integer and provides basic exception handling """

import clear_screen
user_input_text = "Please input an integer: "
error_response = {'ValueError':('Invalid type of input','a valid'), 'ZeroDivisionError':('Cannot divide by zero','a non-zero')}

def validate_user_input(x):
    """ Check if user input is a non-zero integer. """

    try:
        return 10/int(x)
    except Exception as error_code:
        print(error_response[error_code.__class__.__name__][0])
        raise
        
user_input = input(user_input_text)        
while True:
    clear_screen.clear()
    if user_input:
        try:
            print(validate_user_input(user_input))
            user_input = input(user_input_text)
        except Exception as error_code:
            user_input = input("Please input {0} integer: ".format(error_response[error_code.__class__.__name__][1]))
    else:
        break