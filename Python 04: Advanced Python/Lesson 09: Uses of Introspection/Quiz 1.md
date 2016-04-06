**Question 1:**
Given an object o, how would you determine whether or not the object has a method m? The result should be True or False.

**Your Answer:**
class O():
    def m(self):
        pass
    
    n = 2
    
if __name__ == "__main__":
    o = O()
    
    def hasmethod():
        try:
            o.m()
            return True
        except (AttributeError, TypeError):
            return False
    
    print(hasmethod())

o.m() returns True  - o has an m callable method
o.n() returns False - o has an n attribute, but it's not a callable method
o.p() returns False - o has no such attribute

**Mentor Comments:**
This works, but  takes the long way around the block. It's worth poking around with some of Python's built-in methods.  Here you could use something as simple as:

hasattr(o, 'm') and inspect.ismethod(getattr(o, 'm'))

**Question 2:**
Given a module m, how would you produce a list object containing just the names of the classes defined in the module?

**Your Answer:**
import inspect
import m

classnames = [name for name, obj in inspect.getmembers(m) if inspect.isclass(obj)]

**Mentor Comments:**
none

**Question 3:**
Given a function f, how would you get a string of the names of its positional and keyword arguments? Example: if the function is def f(a,b,c,d=3,*,e): print(a,b,c,d,e), how would you get output '(a, b, c, d=3, *, e)' from input f?

**Your Answer:**
import inspect

def f(a,b,c,d=3,*,e): 
    print(a,b,c,d,e)
     
print(inspect.formatargspec(*inspect.getfullargspec(f)))

**Mentor Comments:**
none

**Overall Comments:**
Hi Mark,

I admire you for your effort and diligence. But then again, there's much to be said for insightful sloth :-)  Please see the comments.

-Pat

**Grade:**
Great
