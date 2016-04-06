**Here are your instructions:**
Create a Python3_Homework01 project and assign it to your Python3_Homework working set. In the Python3_Homework01/src folder, create a program named adder.py; in it, create a function that takes two objects and adds them together only if they are both of the integer type. Raise a TypeError otherwise. Then, create a test_adder.py file that tests the correctness of this function.

When they are working to your satisfaction, submit adder.py and test_adder.py.

**Your Comment:**

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Just so you understand, I turned your first attempt back mostly because it didn't meet the project specs (it did not ensure that the inputs were integers).

The polymorphism is pretty darn handy sometimes because you can do a quick mathematical addition of a bunch of Boolean values.  Let's say you had some survey data where respondents had answer True or False. You can easily figure out the True percent  by going something like:

mydata=[True, True, False, True, True, False]

print('hit rate:  {0:.2%}'.format(sum(mydata)/len(mydata)))

Here's another interesting subtlety that you might find useful:

&gt;&gt;&gt; isinstance(True, int)
True

&gt;&gt;&gt; type(True) == int
False

-Pat

**Grade:**
Great
