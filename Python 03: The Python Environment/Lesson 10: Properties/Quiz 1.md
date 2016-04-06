**Question 1:**
Are Properties more or less specific than the special attribute methods? Explain your answer.

**Your Answer:**
Properties are more specific than the special attribute methods, because properties basically intercept the special attribute methods, pre-processing or re-computing the values before they are stored, returned or deleted.

**Mentor Comments:**
none

**Question 2:**
What is the customary prefix character on the storage field of a property?

**Your Answer:**
A single or double underscore.

**Mentor Comments:**
A double underscore character would be most unusual, but it would work

**Question 3:**
What is the decorator for turning the time() method into a property setter? Your answer should replace the ??? below:
???
def time(self, value):
    self._time = value

**Your Answer:**
@time.setter
def time(self, value):
    self._time = value

**Mentor Comments:**
none

**Question 4:**
What is the decorator for turning the time() method into a property getter—replacing the ??? below?
???
def time(self):
    return self._time
 
**Your Answer:**
@property
def time(self):
    return self._time

**Mentor Comments:**
none

**Overall Comments:**
Nicely done, Mark.

-Pat

**Grade:**
Great
