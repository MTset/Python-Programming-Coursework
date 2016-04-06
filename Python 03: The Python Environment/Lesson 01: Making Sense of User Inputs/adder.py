'''
Created on Aug 24, 2015
@author: mtsikano

This module accepts the input of two integers and displays their sum.  Any other
input results in a TypeError
'''

def add(x=None, y=None):
    error_msg = "Both inputs must be integers."
    try:
        if not isinstance(x, bool) and not isinstance(y, bool)\
            and isinstance(x, int) and isinstance(y, int):
            return x + y
        else:
            raise TypeError(error_msg)
    except TypeError:
        return

if __name__ == '__main__':
    result = add(1.1, 1)
    print(result)