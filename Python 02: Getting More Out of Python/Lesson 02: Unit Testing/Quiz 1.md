**Question 1:**
What determines whether a TestCase method will be run as a test?

**Your Answer:**
This is determined by TestRunner finding class methods, inherited from the unittest.TestCase class, beginning with the word 'test'.

**Mentor Comments:**
none

**Question 2:**
Which TestCase method would you use to verify that calling a function with particular arguments raises a specific type of exception?

**Your Answer:**
TestCase method assertRaises()

**Mentor Comments:**
The syntax on this one is a bit different than that for other tests:

assertRaises(, function, *args, **kwargs)

The star in front of args means "split this tuple of args into individual positional arguments" whereas the ** in front of kwargs 
means "explode this dict into separate keyword arguments".  That tells the reader an arbitrary number of positional and
keyword arguments are possible.  It doesn't mean that a *tuple and **dict must be used.

For example, a given assertRaises might look like:

assertRaises(AttributeError, callme, "503-444-1212", "10:00 PM", status = "Not urgent")  # two positional and one keyword argument, all fed to callme.

**Question 3:**
What does the unittest framework print to indicate a successful test?

**Your Answer:**
unittest framework prints a dot per successful test at the top and 'OK' at the bottom of the console.

**Mentor Comments:**
none

**Question 4:**
What is the name of the testing framework we used in this lesson?

**Your Answer:**
The testing framework used in this lesson is called 'unittest'

**Mentor Comments:**
none

**Overall Comments:**
Hi Mark,

Terrific job on this one. Please take a look at the comments on Q2. The syntax on assertRaises is a little bit weird.

-Pat

**Grade:**
Great
