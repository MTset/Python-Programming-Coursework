**Question 1:**
How does a for loop extract values from a generator?

**Your Answer:**
By using the for loop's built in next() function, or in the case of Python 3, the for loop's __next__() method.

**Mentor Comments:**
none

**Question 2:**
Which generator can be used to concatenate multiple sequences?

**Your Answer:**
itertools.chain().

**Mentor Comments:**
none

**Question 3:**
What is the difference between a generator expression and a list comprehension?

**Your Answer:**
A generator expression does not actually create a list or immediately evaluate the expression within the parentheses.  Rather, it creates a generator object which yields values on demand via iteration.  This can mean significant savings in procssing time and memory usage.

A generator expression does not create an iterable object, so it cannot be indexed or subscripted and most of the other operations for use with lists and tuples cannot be used.

**Mentor Comments:**
Generator expressions forced to the end are not faster than list comprehensions with the same fate. Why generators speed up the code is lists tend to be used to store data before it's needed and then the program may take a turn where that data is discarded, unused.  A generator, on the other hand, is more controlled about when it produces and therefore helps programmers avoid the wastefulness of list-based computing.

**Overall Comments:**
You have perfected this, Mark. Thank you so much for your second effort.

-Pat

**Grade:**
Great
