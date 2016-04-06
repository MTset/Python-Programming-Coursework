**Question 1:**
With a single line of code, create a memory-efficient iterator from which a for loop could obtain a million numbers. What is the technique called?

**Your Answer:**
(n for n in range(1000000)) is a generator expression

**Mentor Comments:**
none

**Question 2:**
What is the difference between list comprehension and a generator expression?

**Your Answer:**
A list comprehension processes an entire list and produces a new list.  A generator expression processes a list a value at a time and produces, on-demand, a single value at a time.  The former uses square brackets, the latter uses parantheses.  The latter uses a relatively static amount of memory and is faster (as datasets grow) than the former.

**Mentor Comments:**
Here's a generator that appears to give successive digits of pi:
def pi_digits():
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while True:
        p, q, k = k*k, 2*k+1, k+1
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        d, d1 = a/b, a1/b1
        while d == d1:
            yield int(d)
            a, a1 = 10*(a%b), 10*(a1%b1)
            d, d1 = a/b, a1/b1

[  http://mail.python.org/pipermail/edu-sig/2012-December/010728.html ]

&gt;&gt;&gt; pi = pi_digits()
&gt;&gt;&gt; "".join([str(next(pi)) for i in range(100)]))
'3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067'

**Question 3:**
What is the tool used in the correct answer to question 1 above?
1.list comprehension
2.tuple
3.generator expression
4.list generator
5.None of the above

**Your Answer:**
3. generator expression

**Mentor Comments:**
none

**Overall Comments:**
This is awesome, Mark. Please check out the comments for some fun generator code.

-Pat

**Grade:**
Great
