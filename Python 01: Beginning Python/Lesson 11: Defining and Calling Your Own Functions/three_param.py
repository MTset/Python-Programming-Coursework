#!/usr/local/bin/python3

def my_func(a, b="b was not entered", c="c was not entered" ):
    """ right triangle check """

    result = "Values entered: a - {0}, b - {1}, c - {2}\n".format(a, b, c)
    if type(c) is int:
        d = sorted([a, b, c])
        if abs(complex(d[0], d[1])) == d[2]:
            result += "You have a right triangle!\n"
    elif type(b) is int:
        d = abs(complex(a, b))
        result += "With c = {0} you could have a right triangle.\n".format(d)
    else:
        result += "Don't abuse the hypotenuse.\n"
    return result
    
print(my_func(3))
print(my_func(3,4))
print(my_func(3,4,5))
print(my_func)