**Question 1:**
What is the difference between an iterator and an iterable?

**Your Answer:**
An iterable is an object, such as a list, tuple or string whose values can be iterated over.
An iterator is the mechanism the interpreter uses, such as the __iter__() method or the __getitem__() method to iterate over an iterable object.

**Mentor Comments:**
none

**Question 2:**
What is a generator function and what is its advantage?

**Your Answer:**
A generator function is a function which iterates over a list, applying that function to each member of that list and gives the result of that function on demand, internally using yeild and externally using next().
The main advantage is that, as the dataset to be processed grows, the memory requirement does not as the results are produced and consumed on-demand.  With less need for memory management, speed too is not compromised.

**Mentor Comments:**
FYI, generators also have the ability to *receive* new data when paused at the yield 
statement; you can push them onward with send( ) versus next( ) -- a feature we 
do not explore in the Lessons.

Here's an example of a generator that does Fibonacci numbers, but which allows 
it's two inputs to be reset in any cycle:

import unittest

def fibs(a, b):
    while True:
        d = yield a  # send to a, b
        if d:
            a, b = d[0], d[1]
            continue
        b, a = a + b, b

class Test_Fib(unittest.TestCase):

    def test_basics(self):
        thegen = fibs(0, 1)
        self.assertEqual(next(thegen), 0)
        self.assertEqual(next(thegen), 1)
        self.assertEqual(next(thegen), 1)
        self.assertEqual(next(thegen), 2)
        self.assertEqual(next(thegen), 3)
        self.assertEqual(next(thegen), 5)
        self.assertEqual(next(thegen), 8)
        self.assertEqual(next(thegen), 13)
        self.assertEqual(next(thegen), 21)

    def test_updating(self):
        thegen = fibs(0, 1)
        self.assertEqual(next(thegen), 0)
        self.assertEqual(next(thegen), 1)
        self.assertEqual(thegen.send((20, 21)), 20)  # update pairing
        self.assertEqual(next(thegen), 21)
        self.assertEqual(next(thegen), 41)
        self.assertEqual(next(thegen), 62)
        self.assertEqual(next(thegen), 103)

if __name__ == "__main__":
    unittest.main()

**Question 3:**
Internally, what type of exception does old-style Iteration throw?
1.AttributeError
2.IndexError
3.StopIteration
4.None of the above

**Your Answer:**
2. IndexError

**Mentor Comments:**
none

**Question 4:**
Internally, what type of exception does new-style Iteration throw?
1.AttributeError
2.IndexError
3.StopIteration
4.None of the above

**Your Answer:**
3. StopIteration

**Mentor Comments:**
none

**Overall Comments:**
Good work here, Mark.  Please check out the comments.

-Pat

**Grade:**
Great
