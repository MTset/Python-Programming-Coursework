#!/usr/local/bin/python3
"""Print out a prime example of multiplication"""
data = [
        (2,3),
        (5,7),
        (11,13),
        (17,19),
        (23,29),
        (31,37),
        (41,43),
        (47,53),
        (59,61),
        (67,71),
        (73,79),
        (83,89)
       ]
       
for multiple1, multiple2 in data:
    result = (multiple1 * multiple2)
    print("{0:4d} = {1:2d} * {2:2d}".format(result, multiple1, multiple2))
        