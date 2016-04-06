**Question 1:**
Provide a regular expression pattern that will find three adjacent digits.

**Your Answer:**
[\d]{3}

**Mentor Comments:**
none

**Question 2:**
If a re.match() or re.search() fails to find anything, what kind of object does it return?

**Your Answer:**
None

**Mentor Comments:**
none

**Question 3:**
What method returns the found pattern string in a match object?

Your Answer:
group()

**Mentor Comments:**
m.group(0) returns the entire matched pattern.  If there are parenthesized subgroups in the regex, then those are found in group(1) and beyond.

m.groups() returns all the subgroups.

[

http://docs.python.org/3.4/library/re.html#match-objects](http://docs.python.org/3.4/library/re.html#match-objects)

**Overall Comments:**
Perfect Mark. Thank you for taking a second look.

-Pat

**Grade:**
Great
