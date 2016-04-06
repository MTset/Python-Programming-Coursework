**Objective:**
This project further tests your ability to write and use custom functions.

Create a new Python source file named caser.py.
Create these functions:
capitalize accepts a string parameter and applies the capitalize() method.
title accepts a string parameter and applies the title() method.
upper accepts a string parameter and applies the upper() method.
lower accepts a string parameter and applies the lower() method.
exit ends the program.
Store these functions in a dict with the keys matching the function names.
Create a while loop that requests two inputs from the user: one of the above function names, and any string.
Use function dispatch to get the correct function based on the first input, and then apply that function to the second input.
Below is an example of possible output from running the program (note the difference between upper case, capitalization, and title case).

Enter a function name (capitalize, title, upper, lower, or exit): lower
Enter a string: python is a Dynamic language
python is a dynamic language
Enter a function name (capitalize, title, upper, lower, or exit): upper
Enter a string: python is a Dynamic language
PYTHON IS A DYNAMIC LANGUAGE
Enter a function name (capitalize, title, upper, lower, or exit): capitalize
Enter a string: Python Is A Dynamic language
Python is a dynamic language
Enter a function name (capitalize, title, upper, lower, or exit): title
Enter a string: python is a Dynamic language
Python Is A Dynamic Language
Enter a function name (capitalize, title, upper, lower, or exit): exit
Enter a string: seeya
Goodbye for now!
Can you think of a way you could simplify the creation of the function dispatch table? (Hint: you can use methods of the string type, str, directly as functions that take a single string argument.)

**Here are the files you handed in:**
python1Homework/clear_screen.py

**Overall Comments:**
 Excellent!

-Kelly

**GRADE: Great**
 You have passed this objective.
