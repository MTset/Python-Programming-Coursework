"""
decoder.py: When passed a list, simply returns objects as-is unless they are
integers between 1 and 26, in which case it converts that number to the
corresponding letter. The integer-to-letter correspondence is 1=A, 2=B, 3=C...
"""

from string import ascii_uppercase
def alphabator(s=None):
    for o in s:
        if o in range(1, 27):
            yield ascii_uppercase[o-1]
#            yield chr(o+64) # another solution
        else:
            yield o
            
#def alphabator(generator):
#    for i in generator:
#        yield ascii_uppercase[i - 1] if isinstance(i, int) and 0 < i <= 26 else i


if __name__ == "__main__":
    a = alphabator(['python', object, ascii_uppercase, 10, alphabator, 15])
    for i in a:
        print(i)