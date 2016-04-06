**Question 1:**
In a SELECT statement, how do you retrieve all columns?

**Your Answer:**
Using the SELECT * FROM ;

**Mentor Comments:**
none

**Question 2:**
How do you indicate that no data is available for a particular column and a given row?

**Your Answer:**
BY using the NULL value.

**Mentor Comments:**
One thing you'll want to be aware of is that NULL is treated much differently in a database than None is treated in Python. In MySQL, you need to make an explicit test using IS NULL  or IS NOT NULL or IFNULL() when looking for a null value.   

In Python, when you use Boolean logic involving None, the None is treated as False:

&gt;&gt;&gt; a=None
&gt;&gt;&gt; if not(a):
              print("sorry, no a here")

sorry, no a here

... But that won't work the same in MySQL. Here is a link to the official MySQL documentation:

https://dev.mysql.com/doc/refman/5.0/en/working-with-null.html

**Question 3:**
Write a statement that retrieves the total number of rows from a table named "user."

**Your Answer:**
SELECT COUNT(*) FROM user;

**Mentor Comments:**
none

**Overall Comments:**
 Good work here, Mark. Please take a couple minutes and look at the comments on Q2 For some more background  on NULL.

-Pat

**Grade:**
Great
