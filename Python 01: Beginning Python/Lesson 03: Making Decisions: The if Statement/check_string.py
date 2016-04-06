#!/usr/local/bin/python3
"""Check input string is all upper case and ends with a period"""

answer = ""
while answer != "Correct!":
    inputString = input("\nEnter an upper-case string ending with a period: ")
    if inputString.isupper() and inputString.endswith("."):
        answer =  "Correct!"
        print(answer)
    elif inputString.isupper():
        print("Input does not end with a period")
    elif inputString.endswith("."):
        print("Input string not upper-case")
    else:
        print("Input string not upper-case and has no period")
