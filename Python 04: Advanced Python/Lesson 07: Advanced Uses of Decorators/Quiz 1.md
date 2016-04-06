**Question 1:**
What does the @functools.wraps decorator do?

**Your Answer:**
It is used to ensure that decorated functions continue to "look like themselves, i.e. they report their own name and their own docstrings not those of the wrapper function.

**Mentor Comments:**
none

**Question 2:**
When using a class as a decorator, which method performs the wrapping?

**Your Answer:**
The __init__ method.

**Mentor Comments:**
That's right. It's really good to keep these two straight.

**Question 3:**
What decorator would you use to create a method that does not receive the instance as the first argument?

**Your Answer:**
@staticmethod

**Mentor Comments:**
This also works:

@ classmethod.
Overall Comments:
Thanks for taking another look, Mark. This is perfect now.

-Pat

**Grade:**
Great
