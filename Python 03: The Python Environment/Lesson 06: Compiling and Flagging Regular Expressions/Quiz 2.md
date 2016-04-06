**Question 1:**
How would you write a compiled regular expression to find the name "John Smith" in case-insensitive format?

**Your Answer:**
re.compile(r"John Smith", re.IGNORECASE)

**Mentor Comments:**
none

**Question 2:**
How would you rewrite the compiled regular expression above to include verbose comments?

**Your Answer:**
re.compile(r"John\sSmith", re.IGNORECASE | re.VERBOSE)

**Mentor Comments:**
Ye\s !!!

**Overall Comments:**
Thanks for taking a second look at this, Mark.  Perfect now.

-Pat

**Grade:**
Great
