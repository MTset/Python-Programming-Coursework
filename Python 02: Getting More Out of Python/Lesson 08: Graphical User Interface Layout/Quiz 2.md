**Question 1:**
Which widget would you normally use to display a short piece of static text?

**Your Answer:**
The 'Label()' widget.

**Mentor Comments:**
none

**Question 2:**
How would you configure frame F in a grid layout to occupy three rows and two columns starting at row 3, column 2?

**Your Answer:**
F.grid(row=3, column=2, rowspan=3, columnspan=2).

**Mentor Comments:**
none

**Question 3:**
Do the row and column numbers used with the grid layout manager need to be contiguous?

**Your Answer:**
No, the 'stride' argument can be given to the 'range' function. e.g. for r in range(0, 15, 2):

**Mentor Comments:**
I think you get the idea here, but to clarify... 

You could have a 3-by-3 tic-tac-toe like grid with rows 1, 11, 111 and columns 10, 20 ,30 and all could be well in terms of no space wasted.  This design allows you to "rough in" your GUI then fill in details later without having to renumber rows and columns.

**Overall Comments:**
This looks good, Mark. Please have careful look at the comments in Q3.

-Pat

**Grade:**
Great
