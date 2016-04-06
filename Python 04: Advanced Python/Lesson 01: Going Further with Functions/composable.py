"""
composable.py: defines a composable function class
"""
import types
class Composable:
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
        
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    
    def __mul__(self, other):
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    
    def __pow__(self, power):
        "Return a function x to the power of y"
        error_msg = "Power must be a positive, non-zero integer"
        if not isinstance(power, int):
            raise TypeError(error_msg)
        elif power <= 0:
            raise ValueError(error_msg)
        
        result = self.func
        for p in range(power - 1):
            result = self.__mul__(result)
        return result 

    """ Pat's suggestion - a recursive approach
     def __pow__(self, power):
            if type(power) != int:
                raise TypeError('%s is not an integer' % power)
            if not power > 0:
                raise ValueError('%s is not greater than zero' % power)
            
            if power == 1:
                return self
            else:
                return self ** (power - 1) * self
    
    """
    
    def __repr__(self):
        return "<Composable function {0} at 0x{1:x}>".format(
                            self.func.__name__.id(self))