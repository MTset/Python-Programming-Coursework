**Question 1:**
What is masking?

**Your Answer:**
Masking is when an instance's method overides the class definition's method of the same name.

**Mentor Comments:**
You have the right idea. The term "masking" is more generally reserved for the case when attribute assigned to an object override the method.

**Question 2:**
What do the getattr, hasattr, and setattr functions do?

**Your Answer:**
getattr returns the value of a named attribute of an object.[name] or raises an AttributeError if no such attribute exists, unless a default value is set.
hasattr tests for the existence of a named attribute.  It returns True if the attribute exists, otherwise it returns False.
setattr creates (if it does not exist) and assigns a value to an object.[name] attribute.  Same as object.[name] = value.

**Mentor Comments:**
none

**Question 3:**
What is critical in creating an API? 

**Your Answer:**
The critical element in creating a sucessful API is the documentation as to what input in what format the API expects to recieve and what output, if any, is returned by the program.  The program itself should be able to be treated as a black box.

**Mentor Comments:**
And naturally you will need be underlying code and great tests "under the hood".

**Question 4:**
In "class Monty(Cleese, Chapman, Idle, Palin)" which inherited class has precedence?
1.Chapman
2.Idle
3.Palin 
4.None of the above.

**Your Answer:**
4.None of the above, using the left-first depth-first search.  Obviously this is not the Full Monty.

**Mentor Comments:**
none

**Overall Comments:**
This is perfect, Mark.

-Pat

**Grade:**
Great
