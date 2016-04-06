#!/usr/local/bin/python3

"""English to Pig Latin Translator"""
from subprocess import call
import os
import sys
host_platform = sys.platform

options = ('add', 'delete', 'delete all')
vowels = ('a', 'e', 'i', 'o', 'u')
user_nudge = "a"
user_nudge2 = "number"
phrases_in_file = 0
eng_pig_file = 'english_piglatin.txt'

phrasebook = open(eng_pig_file, 'a')
phrasebook.close()

while True:
# To help legibility, clear input screen first
    if host_platform == "win32": # windows
        os.system('cls')
    else: # *nix and OS X
        os.system('clear')
    print("This program translates English into Pig Latin\n")

    open_phrasebook = open(eng_pig_file,'r').readlines()
    if open_phrasebook: 
        for i, phrase in enumerate(open_phrasebook):
            print(i, phrase.strip())
            phrases_in_file = i        

    option_input = "\nPick {0} option from: {1} or just <Enter> to quit: \n".format(user_nudge, options)
    option = input(option_input)
    if not option:
        break
    elif option not in options:
        user_nudge = "a VALID"
        continue
    else:
        user_nudge = "a"
        
    if option == "add":
        phrase = input("Enter phrase to translate: \n")
        translation = []        
        for word in phrase.split():
            if word[0:1] in vowels:
                translation.append(word.replace(word, word[1:] + word[0:1] + "way"))
            else:
                while True:
                    if word[0:1] not in vowels:
                        word = word.replace(word, word[1:] + word[0:1])
                    else:
                        break
                translation.append(word.replace(word, word + "ay"))
        
        phrasebook = open(eng_pig_file, 'a')
        phrasebook.write("{0:50}".format(phrase) + '     ' + "{0:50}".format(" ".join(translation)) + '\n')
        phrasebook.close()
    elif option == "delete":
        while True:   
            phrase_number = input("Enter the {0} of phrase to delete: \n".format(user_nudge2))
            if not phrase_number:
                user_nudge2 = "number"
                break
            elif phrase_number.isdigit():
                phrase_number = int(phrase_number)
                user_nudge2 = user_nudge2.lower()
                if phrase_number > phrases_in_file:
                    user_nudge2 = "number in range 0 - " + str(phrases_in_file)
                    continue
                break
            else:
                user_nudge2 = user_nudge2.upper()
                continue
        with open(eng_pig_file,'r+') as phrasebook_file:
            open_phrasebook = phrasebook_file.readlines()
            for i, phrase in enumerate(open_phrasebook):
                if phrase_number == i:
                    del open_phrasebook[i]
                    break
            phrasebook_file.seek(0)
            phrasebook_file.writelines(open_phrasebook)
            phrasebook_file.truncate(phrasebook_file.tell())
    else:
        with open(eng_pig_file,'w+') as phrasebook_file:
            continue