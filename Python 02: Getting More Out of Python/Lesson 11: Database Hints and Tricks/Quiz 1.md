**Question 1:**
What methods are available to retrieve data from a database cursor after it has been used to execute a SQL SELECT statement?

**Your Answer:**
cursor.fetchone()
cursor.fetchmany()
cursor.fetchall()

**Mentor Comments:**
Note that fetchmany() requires an integer argument.

**Question 2:**
What method do you need to implement to control an object's printable representation?

**Your Answer:**
format() to create a formatted representation
repr() to create a string representation which can be evaluated to re-create the object
str() to create a simple string representation

**Mentor Comments:**
Right, if __str__ is present then print(n) will go for __str__.   format() works for strings only.

class Foo:

    def __init__(self, n):
        self.name = n

    def __repr__(self):
        return "".format(id(self))

    def __str__(self):
        return "".format(self.name)

obj = Foo("Hercules")
print(obj.__repr__())
print(obj)
print([obj])

OUTPUT:

[]

**Question 3:**
Write an expression that produces a comma-separated representation of the elements in a list named lst.

If lst = ["monkey","parrot","penguin","tiger","bear"], the result of the expression would be 'monkey, parrot, penguin, tiger, bear'.

The number of elements is not fixed, however.

**Your Answer:**
print(repr(', '.join(lst)))

**Mentor Comments:**
none

**Overall Comments:**
Good work here, Mark.  Please see the comments on Q2 for a couple clarifications.

-Pat

**Grade:**
Great
