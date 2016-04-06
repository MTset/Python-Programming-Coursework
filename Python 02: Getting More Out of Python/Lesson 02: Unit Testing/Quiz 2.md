**Question 1:**
What is the basic rule of test-driven development?

**Your Answer:**
Only write code to make a failing test pass.

**Mentor Comments:**
none

**Question 2:**
What is a test fixture?

**Your Answer:**
A test fixture is what you need to setup/create to run your test, e.g. a test server or temporary database.

**Mentor Comments:**
Examples of fixtures:
Loading a database with a specific, known set of data
Erasing a hard disk and installing a known clean operating system installation
Copying a specific known set of files
Preparation of input data and set-up/creation of fake or mock objects

[source:  wikipedia]

**Question 3:**
Why would you normally prefer to put tests in a separate module from the code they are testing?

**Your Answer:**
Putting tests in a separate module allows the tests to be used generically for testing the same basic requirements in different programs.  It makes the tests and programs easier to maintain and allows for a more standardized testing environment.

**Mentor Comments:**
Actually as the project involving def title(s) vs. s.title() showed, you *may* combine
tests and code, it just rapidly becomes iffy to do so, because you're weighing down
the module with code that is unnecessary to getting the job done.  As a professional
math teacher (off and on), I've been known to squirrel away tests, with a function, in
one module, as here;

https://mail.python.org/pipermail/edu-sig/2013-August/010872.html

(there's actually a mistake in that two of the tests have the same name,
do you see it?  A student grabbing my code would probably find that
flagged in Eclipse or whatever IDE with "intellisense" [tm] about Python).

**Question 4:**
What does "YAGNI" stand for?

**Your Answer:**
You Ain't Gonna Need It.

**Mentor Comments:**
none

**Overall Comments:**
Awesome, Mark.

-Pat

**Grade:**
Great
