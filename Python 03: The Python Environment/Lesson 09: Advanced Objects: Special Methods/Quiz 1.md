**Question 1:**
What is the alternative name for special methods?

**Your Answer:**
magic methods

**Mentor Comments:**
none

**Question 2:**
Which special method is called by the print() built-in?

**Your Answer:**
__str__(), if available, __repr_()_ if __str__() is not available.

**Mentor Comments:**
none

**Question 3:**
Trick question! If __setattr__ sets attributes and __delattr__ deletes attributes, what method gets attributes?

**Your Answer:**
__dict__() is the default method for retrieving an attribute.  __getattr__() is used as a fallback if all other lookup methods fail to find the named atttribute, or raises an AttributeError.

**Mentor Comments:**
As a point of clarification __dict__() is an attribute, not a method. True, it contains the namespace of the object,  but will not automatically provide the attribute.

**Overall Comments:**
Good work here, Mark. Please see the comments on Q3 for an important clarification.

-Pat

**Grade:**
Great
