**Question 1:**
Write an expression that takes two lists of equal length, k and v, and produces a dict where the keys are the elements of k and the corresponding values are the elements of v.

**Your Answer:**
result = dict(zip(k,v))

**Mentor Comments:**
Showing how zip() may take multiple (more than two) iterables:

&gt;&gt;&gt; starters = ["soup", "salad", "bread", "bread sticks"]
&gt;&gt;&gt; entres = ['spaghetti', 'pizza', 'hamburger']
&gt;&gt;&gt; desserts = ['ice cream', 'pie','cake']
&gt;&gt;&gt; tuple(zip(starters, entres, desserts))
(('soup', 'spaghetti', 'ice cream'), ('salad', 'pizza', 'pie'), ('bread', 'hamburger', 'cake'))

**Question 2:**
What function of the mysql.connector module must you call to establish a connection with a database?

**Your Answer:**
.Connect()

**Mentor Comments:**
none

**Question 3:**
If the built-in zip() function is given two lists of unequal length as arguments, what is the result?

**Your Answer:**
The result is a list of tuples combining the two arguments, stopping with the shortest of the two arguments.

**Mentor Comments:**
That's right.  The technical term for this is 'truncate'.

**Overall Comments:**
Perfect, Mark. Please have a look at the comments on Q1 for a little amplification.

-Pat

**Grade:**
Great
