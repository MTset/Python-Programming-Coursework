**Question 1:**
Provide a new regular expression that will find three adjacent digits, different from the one you provided in last lesson's homework. Include your previous answer.

**Your Answer:**
Previous answer was [\d]{3}
r"\d\d\d"

**Mentor Comments:**
none

**Question 2:**
What is the difference between re.match() and re.search()?

**Your Answer:**
match() checks at the start of a string and returns None if nothing is found.
search() moves up the string, looking for the first occurrence of the given pattern, and returns None only if the pattern occurs nowhere in the string. 

**Mentor Comments:**
Note that using re.search( ) with a regexp starting with "^" is equivalent to re.match( ) with the same regexp minus the "^" (it's redundant with re.match)

^ means "match from the start of the target string".

**Overall Comments:**
Awesome, Mark.

-Pat

**Grade:**
Great
