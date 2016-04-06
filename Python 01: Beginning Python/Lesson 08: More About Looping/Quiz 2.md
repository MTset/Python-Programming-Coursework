**Question #1:**
The code while True: is an infinite loop. How do you terminate this loop?

**Answer #1:**
Using the 'break' statement e.g.

while True:
    if x == y: # correct condition
        break

**Comments:**
Right. The break statement immediately terminates the loop without waiting for the condition to be reevaluated.

sys.exit( ), yield and return also may work.

The 'break' statement's philotic twin is the 'continue' statement which moves execution immediately to the top of the loop.

**Question #2:**
Which dict method generates an iterable of (key, value) tuples?

**Answer #2:**
'enumerate' e.g.

list1 = ('a', 'b', 'c', 'd', 'e')
for key, value in enumerate(list1):
    print(key, value)

**Comments:**

**Question #3:**
How would you remove the dict item whose key is "Steve" from dict d?

**Answer #3:**
Using 'del' e.g.

del d['Steve']

**Comments:**

**Overall Comments:**
 Hi Mark,

This is really good. You will provided some really solid examples the demonstrate your understanding of this material.

Enjoy your weekend.

-Pat

**GRADE: Great**
 You have passed this quiz.
