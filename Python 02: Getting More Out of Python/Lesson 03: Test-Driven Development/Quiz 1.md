**Question 1:**
What method would you normally use to perform work that was needed before each test?

**Your Answer:**
The setUp() method.

**Mentor Comments:**
none

**Question 2:**
What happens if the setUp() method raises an exception?

**Your Answer:**
The test framework will declare that this test has errors and will not run it.

**Mentor Comments:**
It's completely possible to have some tests fail in other tests run. You might have a look at this:

import unittest
import random

class TestFoo(unittest.TestCase):

    def setUp(self):
        if random.randint(0, 1) == 1:
            raise Exception

    def test_1(self):
        self.assertTrue(True)

    def test_2(self):
        self.assertTrue(True)

    def test_3(self):
        self.assertTrue(True)

    def test_4(self):
        self.assertTrue(True)

    def test_5(self):
        self.assertTrue(True)

    def test_6(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

This produces the following output:

..EE.E
======================================================================
ERROR: test_3 (__main__.TestFoo)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "V:\workspace\UnitTesting\src\flaky_setup.py", line 11, in setUp
    raise Exception
Exception

======================================================================
ERROR: test_4 (__main__.TestFoo)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "V:\workspace\UnitTesting\src\flaky_setup.py", line 11, in setUp
    raise Exception
Exception

======================================================================
ERROR: test_6 (__main__.TestFoo)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "V:\workspace\UnitTesting\src\flaky_setup.py", line 11, in setUp
    raise Exception
Exception

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (errors=3)

**Question 3:**
Which method do you call to clear up after an individual test?

**Your Answer:**
The tearDown() method.

**Mentor Comments:**
none

**Question 4:**
Why do TestCase methods not normally produce any output?

Your Answer:
For the sake of brevity and clarity, because you only need details in the case of an unsuccessful run.  Normally TestCase methods should run successfully.
Mentor Comments:
Right.  Verbosity means trouble, is the unittest design.  That's not to be over-generalized
as other processes reassure us when verbose e.g. the noisy version of the Linux 
bootstrapping process

Besides, since projects may have thousands (or even more) verbose results would be totally untenable.

**Overall Comments:**
This is perfect, Mark. Please check out the comments.

-Pat

**Grade:**
Great
