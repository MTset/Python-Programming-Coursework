#!/usr/local/bin/python3

"""Encode/Decode input text"""

import os
import sys
import random
host_platform = sys.platform


options = ('encrypt', 'decrypt', 'self destruct')
user_nudge = "a"
output_string = ""
i = 0

while True:
# To help legibility, clear input screen first
    if host_platform == "win32": # windows
        os.system('cls')
    else: # *nix and OS X
        os.system('clear')
    print("Enigma Lite Cipher Engine\n")

    if output_string:
        print(option.title() + "ed string: \"" + output_string[::-1] + "\"")

    option_input = "\nPick {0} option from: {1} or just <Enter> to quit: \n".format(user_nudge, options)
    option = input(option_input)
    if not option:
        break
    elif option not in options:
        user_nudge = "a VALID"
        option = ""
        continue
    else:
        user_nudge = "a"
    
    if option == "encrypt":
        crypt_key = 1
    elif option == "decrypt":
        crypt_key = -1
    else:
        j = 10000000
        k = 0
        while True:
            while j > 100000:
                i = random.randint(10000, 100000)
                j -= i
                k += i
                print("SELF DESTRUCT SEQUENCE INITIATED... DELETING ALL FILES... FILES DELETED SO FAR - ", k, "FILES REMAINING", j)
                continue
            print("Goodbye Dave")
            break
        break

    user_input = input("Enter string to {0}: ".format(option))
    output_string = ""        
    for letter in user_input:
        output_letter = chr(ord(letter) + crypt_key)
        output_string += output_letter