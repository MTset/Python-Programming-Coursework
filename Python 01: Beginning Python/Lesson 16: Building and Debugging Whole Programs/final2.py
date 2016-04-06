#!/usr/local/bin/python3

import clear_screen
import string

def word_length_distrib(infile):
    """ Reads an input file, and produces a word length distribution.  Case-insensitive, punctuation not included. Histogram of distribution."""
    word_lengths = {}
    open_infile = open(infile,'r').read()
    open_infile = open_infile.translate(str.maketrans("","", string.punctuation)).lower().split() #remove any punctuation and case distinction
    for word in open_infile:
        if len(word) in word_lengths:
            word_lengths[len(word)] += 1
        else:
            word_lengths[len(word)] = 1
    max_word_length = len(word_lengths)    
    max_word_length_count =  max(word_lengths.values())
    
    print('Length  Count')
    for key in word_lengths:
        print("{0:>2}{1:>11}".format(key, word_lengths[key]))
    print("\n\n")

    # Create Histogram        
    for i in range(max_word_length_count + 1, 0, -1):
        output_line = "  {0:>3}-| ".format(str(i))
        for j in word_lengths:
            if word_lengths[j] + 1 == i:
                output_line = output_line + " _   "
            elif word_lengths[j] >= i:
                output_line = output_line + "|#|  "
            else:
                output_line = output_line + "     "
        
        print(output_line)

    output_line = "    0-|"
    for i in range (1, max_word_length + 1, 1):
        output_line = output_line + "--+--"
    print(output_line)

    output_line = 7 * " "        
    for i in range (1, max_word_length + 1, 1):
        output_line = output_line + "{0:^5}".format(i)
    print(output_line)

if __name__ == "__main__":
    word_length_distrib('declaration.txt')