**Question #1:**
How do you:

calculate a non-negative value for any numeric input?
calculate the highest value from the objects n1, n2, n3, and n4?
round the value 1.3234 to the nearest integer?

**Answer #1:**
1. Using the abs() function. e.g.
x = abs(int(input("type in a number: ")))

2. max(n1,n2,n3)

3. round(1.3234)

**Comments:**
Technically you are missing one of the objects from # 2, but I see you understand the learning/teachings here, so close enough.

Any type with meaning for &gt; and &lt; (__gt__, __lt__) may logically be fed to max()

class N:
    """compare strings purely on basis of relative length
    Note: no __eq__ implemented"""
    def __init__(self,s):
        self.string = s
    def __len__(self):
        """len(N)"""
        return len(self.string)
    def __lt__(self, other):
        """N1 &lt; N2"""
        return len(self) &lt; len(other)
    def __gt__(self, other):
        """N1 &gt; N2"""
        return len(self) &gt; len(other)
    def __repr__(self):
        return "N = {} of length {}".format(self.string, len(self.string))

n1 = N("jimmy")
n2 = N("chum")
n3 = N("Tylenol")
n4 = N("gypsy moth")
n5 = N("much") # same len as "chum"

thelist = [n1,n2,n3,n4,n5]
print(max(thelist))

thelist.sort()
print(thelist)

Runs to give the output:

N = gypsy moth of length 10
[N = chum of length 4, N = much of length 4, N = jimmy of length 5, N = Tylenol of length 7, N = gypsy moth of length 10]

**Overall Comments:**
 Awesome, Mark. Please take a couple minutes and read the comments.

-Pat

**GRADE: Great**
 You have passed this quiz.

