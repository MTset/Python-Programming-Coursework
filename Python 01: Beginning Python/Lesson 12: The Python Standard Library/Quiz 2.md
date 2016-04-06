**Question #1:**
What is sys.path? How is it used by the Python interpreter?

**Answer #1:**
sys.path or system path, is the set of directories which the Python interpreter searches progressively to find modules requested. On this system it is:

/usr/local/lib/python34.zip
/usr/local/lib/python3.4
/usr/local/lib/python3.4/plat-linux
/usr/local/lib/python3.4/lib-dynload
/usr/local/lib/python3.4/site-packages 

**Comments:**

**Question #2:**
What value does a module's __name__ attribute receive if the module is run as a program?

**Answer #2:**
The module's __name__ attribute receives a value of __main__ if the module is run as a program.

**Comments:**

**Question #3:**
What is wrong with from module import *?

**Answer #3:**
a. There is nothing wrong with the statement itself. It is syntactically correct and legal EXCEPT in function bodies due to the way it interacts with function scoping rules. Its use, however is discouraged because of potential conflicts in symbol definitions causing overwrites.

b. Definitions which start with an underscore will not be imported.

c. The module which is imported may have restricted which definitions are exported using the __all__ list.

d. There are also potential conflicts due to the imported module's global namespace as opposed to the importing module and the use of global variables from the imported as opposed to the importing module.

**Comments:**

**Overall Comments:**
 Fabulous!

-Kelly

**GRADE: Great**
 You have passed this quiz.
