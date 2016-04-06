**Question 1:**
What are some advantages of compiled regular expression methods over re module functions?

**Your Answer:**
Improvement in efficiency (speed).
Additional features that the basic search functions lack.
Code that is more compact, more readable, and more usable. 

**Mentor Comments:**
Terrific, thoughtful response. Building on your answer:

Advantages of regular expression methods over re module functions:
 - compiled regular expression have pos and endpos arguments which act as string slicing
 - compiled regular expression more efficient than re module
 - if we need a greater performance(i.e gigantic strings) it is a good practice to compile the regular expressions before use
 - in compiled regular expression the code is more compact, more readable, and more usable. 
 - complex regular expression can be broken up (and commented) and still useable using the FLAG 're.VERBOSE'

**Question 2:**
How would you compile the regular expression "\d{3}"?

**Your Answer:**
re.compile(r"\d{3}") - assuming '?' is not part of the regex.

**Mentor Comments:**
You are correct in the assumption. The  "?" is out side of the quoted expression, so cannot be part of it.

**Overall Comments:**
This is excellent, Mark.

-Pat

**Grade:**
Great
