**Question 1:**
How do you set the attributes of a function?

**Your Answer:**
function.attribute= value or __setattr__(function, attribute, value)

**Mentor Comments:**
none

**Question 2:**
What statement is used to identify names in a function's surrounding scope?

**Your Answer:**
nonlocal

**Mentor Comments:**
none

**Question 3:**
Which methods might the interpreter call to evaluate the expression a // b?

**Your Answer:**
initially __floordiv__() and if that fails, __rfloordiv__() (only if the arguments are not the same type)

**Mentor Comments:**
Perfect.  This is what Python 2.X did, driving many people  insane  trying to figure out why 1/2 != 0.5  :-)

**Overall Comments:**
This is awesome, Mark.

-Pat

**Grade:**
Great
