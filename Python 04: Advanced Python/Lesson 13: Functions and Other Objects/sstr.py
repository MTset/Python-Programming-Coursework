"""
sstr.py: Implement a subclass of str, adding '<<' and '>>' methods to allow
cyclic shifting of characters in a string.
"""
class sstr(str):
    def __lshift__(self, value=0):
        return sstr(self[value:]+self[:value])
    
    def __rshift__(self, value=0):
        return self.__lshift__(-value)