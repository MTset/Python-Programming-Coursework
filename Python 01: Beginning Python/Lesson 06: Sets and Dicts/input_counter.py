#!/usr/local/bin/python3
"""Display words in order of discovery"""
import string

inputString = " "
inputWords = set()
prevInputWordsLength = 0
inputWordsOrder = {}

while True:
    inputString = input("Enter your text: ")
    inputString = inputString.translate(str.maketrans("","", string.punctuation)).lower().split() #remove any punctuation and case distinction
    if not inputString:
        break
    for word in inputString:
        prevInputWordsLength = len(inputWords)
        inputWords.add(word)
        if len(inputWords) > prevInputWordsLength:
            inputWordsOrder[word] = len(inputWords)
    for word in inputWords:
        print(word, inputWordsOrder[word])
print("Finished")
    