**Question #1:**
What is the difference between a syntax error and an exception?

**Answer #1:**
A syntax error occurs when when the language interpreter is unable to process the code typed in.

An exception is when invalid data is attempted to be processed by syntactically correct code.

**Comments:**

**Question #2:**
How can you deal with exceptions in your code?

How can you re-raise an exception?

**Answer #2:**
1. You can deal with exceptions by:
a. Prevention - screening the data before trying to process it, e.g.
.isdigit() before trying to convert it to an integer OR
b. allowing the exception to occur, capturing it using try/except and providing 'handler' code.

2. By using the try/except error handler to deal with the exception to a certain degree, but then re-raising the exception to a higher handler by using the 'raise' statement, e.g.

try:
    &lt;some processing&gt;
except &lt;some exception&gt;
    print(&lt;some error message&gt;)
    raise

**Comments:**

**Overall Comments:**
 Beautiful!

-Kelly

**GRADE: Great**
 You have passed this quiz.
