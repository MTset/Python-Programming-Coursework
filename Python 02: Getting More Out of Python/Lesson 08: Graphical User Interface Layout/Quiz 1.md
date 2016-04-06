**Question 1:**
Using the pack geometry manager, how would you ensure that widget W occupies the full width and height of its containing element?

**Your Answer:**
By using, for the pack() method the 'fill' argument with a value of 'BOTH' and the 'expand' argument with a value of 'True'. e.g. W.pack(side=TOP, fill=BOTH, expand=True).  The latter necessary only if the container is to be resized in a dimension other than how the widget W is stacked.

**Mentor Comments:**
none

**Question 2:**
What are the two most commonly used geometry managers in Tkinter?

**Your Answer:**
pack() and grid().

**Mentor Comments:**
none

**Question 3:**
When using grid layout, which argument to grid can you use to cause the cell content to align with one or more sides of the cell?

**Your Answer:**
sticky() along with the values of N, S, E, W, which can be combined using '+' e.g. self.grid(sticky=W+E+N+S)

**Mentor Comments:**
From the docs:

sticky=  Defines how to expand a child widget if the resulting pane is larger than the widget itself. This can be any combination of the constants S, N, E, and W, or NW, NE, SW, and SE. 

I think of it in terms of compass points.

**Overall Comments:**
This is perfect, Mark. Please look at the comments in Q3 for a small clarification.

-Pat

**Grade:**
Great
