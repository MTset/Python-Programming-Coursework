#!/usr/local/bin/python3
""" Read a string and separate out words with one or more upper-case letters and lower-case letters only into two lists """
import string

inputString = input("Enter your string: ")
inputString = inputString.translate(str.maketrans("","", string.punctuation)) #remove any punctuation
upperCaseList = []
lowerCaseList = []

words = inputString.split()
for word in words:
    if word.islower():
        lowerCaseList.append(word)
    else:
        upperCaseList.append(word)

wordList = upperCaseList + lowerCaseList
for word in wordList:
    print(word, "\t")