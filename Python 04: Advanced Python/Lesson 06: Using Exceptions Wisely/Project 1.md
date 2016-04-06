**Here are your instructions:**
Write a subclass of the standard dict class. Its __init__() method should take one argument, which will be used as a default value when a non-existent key is accessed (it should also call the standard dict's __init__() with no arguments). Its __getitem__() method should attempt to use the standard dict.__getitem__(), but any KeyError exceptions should be handled by returning the default value passed to __init__() on creation. Write a small test program for your object.

**Your Comment:**
Hi Pat,

On the previous project I tried using map and operator.truediv(), but it ran slower than what
I ended up submitting.  Couldn't quite get it to be a third of the original code's time.  I've had
a look at your comments and will improve the testing.  As for checking that the answers are the same
there is an "assert groffle_slow(mass, density) == groffle_fast(mass, density)" in the code...

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,
You've done an awesome job putting together this objective. It is actually pretty slick.

FYI, here is another way you might have composed it:

class SubDct(dict):
    def __init__(self, default):
        self.default = default
        super().__init__()
        
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except:
            return self.default

The advantages of using super() are non-obvious in these simple "cave paintings" but in complex hierarchies super() makes the MRO Python's headache and not
yours.

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

Also, check out the relatively new magic method __missing__ 

http://pythonquirks.blogspot.com/2010/02/missing.html
http://stackoverflow.com/questions/17956927/python-defaultdict-that-does-not-insert-missing-values

-Pat

**Grade:**
Great
