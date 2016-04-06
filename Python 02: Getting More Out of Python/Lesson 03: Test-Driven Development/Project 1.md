**Here are your instructions:**
Make a TestDrivenDevelopment_Homework project and assign it to the Python2_Homework working set.

Copy the setupDemo.py file from the TestDrivenDevelopment/src folder to the TestDrivenDevelopment_Homework/src folder.

Modify it so that:A test_3() method creates a binary file that contains exactly a million bytes, closes it and then uses os.stat to verify that the file on disk is of the correct length (with os.stat, statinfo.st_size returns the size in bytes).

**Your Comment:**
no comment given

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,You have done a really good job on this project. Your coding is very sophisticated.

Here are a few tips that might serve you well in the future:

-If you don't care what's in the file, you don't need to write to it.  And if you're not going to do anything with it, you don't even need a handle for it.  So for this project, you could create a file that simply as:

open('myfile', 'w').close()

-Most of the utilities that operate on the filesystem take the current working directory as the default path. In other words you typically don't need to specify:

path='.'

-Whenever you find yourself typing something more than once, you'll want to ask yourself whether or not there is an easy way to create a variable instead. The test_3() method is a case in point. You really only have to specify the filename once. If it ever needed to be changed, you would have to remember to change your code into places. A trivial matter here, but what if test_3 () span a couple of pages?

-In Python, we typically use all_lower_case words for variable names, CamelCase for classes and ALLCAPS for constants per the Python styling guidelines.

If you're interested, you can pick up your own copy of "PEP-8" at:

https://www.python.org/dev/peps/pep-0008

**Overall:**
 awesome !

-Pat

**Grade:**
Great
