**Question #1:**
If you had a file object f open for writing, how would you write the string "my text" to that file?

If the same file object was open for reading, how would you print all of its contents in a single statement?

**Answer #1:**
1. f.write('my text')

2. Using the print() function and the readlines(function). e.g.
print(open('english_piglatin.txt', 'r').readlines())

**Comments:**
Either print(f.readlines()) or print(f.read()) work here.

**Overall Comments:**
 Perfect, Mark.

-Pat

**GRADE: Great**s
 You have passed this quiz.
