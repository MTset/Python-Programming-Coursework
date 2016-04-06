**Question 1:**
What configuration item should you set on a button to establish the function to run when the button is clicked?

**Your Answer:**
You would set the button's 'command' item

**Mentor Comments:**
none

**Question 2:**
How would you configure a button B so it does not respond to clicks? B already exists, and has a handler function that should be left as is.

**Your Answer:**
You would set the 'state' configuration parameter of the button to 'disabled'. e.g. self.B['state'] = disabled

**Mentor Comments:**
none

**Question 3:**
How would you specify that button B should appear immediately below the last object created with the same parent?

**Your Answer:**
You could use 'grid'.
You can use nested frames.
If the previous objects are already stacked vertically use pack() with no parameters.

**Mentor Comments:**
Terrific answer. If you use pack () with no parameters, you are invoking the default side = TOP.

**Overall Comments:**
Hi Mark,

Thanks for taking a second pass at this.

-Pat

**Grade:**
Great
