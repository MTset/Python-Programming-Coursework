**Here are your instructions:**
Write a decorator function addarg() that takes an argument and adds that argument as the first argument to all calls to decorated functions. So if you wrote:
@addarg(1)
def prargs(*args):
 return args
prargs(2, 3)
prargs("child") 

the output would be: 
(1, 2, 3)
(1, 'child')

Write a test program to verify the decorator's operation.

Note: it's possible the wrapped function will have keyword arguments and these should be respected.

**Your Comment:**
no comment given

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

You've done an excellent job on this project, as usual. There is one trick that you may have missed, however... 

It's typically a good idea to use wraps () to make sure that you are wrapped function does not suffer from an "identity crisis". Here's how you might have applied it to this project:

from functools import wraps

def addarg(first_arg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(first_arg, *args, **kwargs)
        return wrapper
    return decorator

if __name__ == '__main__':
    @addarg(1)
    def prargs(*args):
        """just print, thank you"""
        return print(args)

    prargs(2, 3)
    prargs("child")

    print(prargs.__doc__)
    print(prargs.__name__)

-Pat

**Grade:**
Great
