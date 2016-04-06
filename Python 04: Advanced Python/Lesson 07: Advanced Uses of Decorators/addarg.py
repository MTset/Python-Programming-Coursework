"""
addarg.py: A decorator function that accepts an argument and adds that argument
as the first argument to all calls to decorated functions.
"""
from functools import wraps

def addarg(arg):
    " Returns a decorator that prefixes a function's args with a passed arg"
    def decorator(func):
        "Wrap and decorate a function"
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(arg, *args, **kwargs)
        return wrapper
    return decorator