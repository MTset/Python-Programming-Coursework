#!/usr/local/bin/python3

import clear_screen
import string

def word_length_distrib(infile):
    """ Reads an input file, and produces a word length distribution.  Case-insensitive, punctuation not included. """
    word_lengths = {}
    open_infile = open(infile,'r').read()
    open_infile = open_infile.translate(str.maketrans("","", string.punctuation)).lower().split() #remove any punctuation and case distinction
    for word in open_infile:
        if len(word) in word_lengths:
            word_lengths[len(word)] += 1
        else:
            word_lengths[len(word)] = 1
    print('Length  Count')
    for key in word_lengths:
        print("{0:>2}{1:>11}".format(key, word_lengths[key]))

if __name__ == "__main__":
    word_length_distrib('declaration.txt')