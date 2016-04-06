**Question 1:**
Write a pattern that matches a sequence of one or more lower-case letters between a and h, all lowercase.

**Your Answer:**
[a-h]+

**Mentor Comments:**
none

**Question 2:**
If the pattern "((?P&lt;letters&gt;[A-Za-z]+)\d+ +)+" is matched against the string "ABC123 DEF234 GHI345" to give a match object m, how would you retrieve the string matched by the "letters" group, and what would it contain?

**Your Answer:**
return search.group("letters") which returns DEF

**Mentor Comments:**
Right. Here's how it works:

re.match("((?P[A-Za-z]+)\d+ +)+","ABC123 DEF234 GHI345").group('letters') returns the second alpha group of 'DEF'

'(?P[A-Za-z]+)' matches any consecutive string of alpha characters and is the second group of the re. The same as .group(2)
The first group is consecutive strings of alphas followed by digits separated by any number of ' '.
For this example that is "ABC123 DEF234". The remainder isn't matched because it is not followed by a space.

**Overall Comments:**
This is perfect, Mark.

-Pat

**Grade:**
Great
