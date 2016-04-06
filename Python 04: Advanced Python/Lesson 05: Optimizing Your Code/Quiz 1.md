**Question 1:**
Which two modules can be used to record profiling information from a Python program? Which is preferred?

**Your Answer:**
cProfile and profile. When available cProfile is preferred.

**Mentor Comments:**
none

**Question 2:**
What are the three different restrictions you can use to filter statistics output?

**Your Answer:**
An integer will limit the output to the given number of lines.
A floating-point number between 0 and 1 will restrict the output to the given proportion of entries.
A regular expression will limit the output to those entries whose filename:lineno(function) fields contain the given regular expression.

You can also limit the output to omit the details of the "structural" entries (those that relate strictly to the profiling framework) using the simple expression r"\.py", 

**Mentor Comments:**
none

**Question 3:**
What module would you use to time snippets of code?

**Your Answer:**
timeit()

**Mentor Comments:**
none

**Overall Comments:**
Completely awesome, Mark.

-Pat

**Grade:**
Great
