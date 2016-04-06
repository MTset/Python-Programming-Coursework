**Question #1:**
Look at the following code:

x = {1,2,3,4,5}
y = {4,5,6,7,8}
How can you determine the numbers shared by both?

**Answer #1:**
By using the intersection of sets: e.g.

z = x & y

**Comments:**

**Question #2:**
How do you determine the length of a dict or set?

**Answer #2:**
using len() e.g.

len(z)

**Comments:**

**Question #3:**
How do you print all of the keys and values of a dict named d? 

**Answer #3:**
By using the items() method e.g.

To PRINT all of the keys and values of a dict named d (as in the question above)

d = {'1':'a','2':'b','3':'c','4':'d'}
for k in d.items():
    print(k)

To GRAB both the keys and values immediately storing them in variables

d = {'1':'a','2':'b','3':'c','4':'d'}
for k in d.items():
    key = k[0]
    value = k[1]
    .
    . do stuff with key and value
    .

**Comments:**
A common idiom:

for key,value in d.items():
     print(key, value)

... this has the advantage of compactly providing recyclable variable names and enhancing readability.

**Overall Comments:**
 It looks like the fourth time's a charm, Mark. Good job.

-Pat

**GRADE: Great**
 You have passed this quiz.
