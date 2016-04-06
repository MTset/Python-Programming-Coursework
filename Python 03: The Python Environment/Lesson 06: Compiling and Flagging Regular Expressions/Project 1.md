﻿**Here are your instructions:**
Create a Python3_Homework06 project and assign it to your Python3_Homework working set. In the Python3_Homework06/src folder, create a program named ccn_safety2.py that duplicates the ccn_safety.py program's functionality, but uses a compiled regular expression to replace the credit card numbers in the paragraph with "CCN REMOVED FOR YOUR SAFETY". Use the following text as a sample:

Text to use in ccn_safety2.py:
Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a 
number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of 
privacy and security experts.
Your project should meet the following conditions:
* The program should return this text: "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts." Note that phone numbers should not be replaced!
* You should include a test_ccn_safety2.py program in a separate file that confirms that your code functions as expected.
* You must use the re.VERBOSE flag to properly document each element of the pattern used to identify credit card numbers.

Submit ccn_safety2.py and test_ccn_safety2.py when they are working to your satisfaction.

**Your Comment:**
Hi Pat,

Same checks for valid credit card numbers used and thus the same test credit card numbers used
as in the project.  re.compile with VERBOSE flag used everywhere it made sense.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

You have done a terrific job on this project, but you already knew that. Keep up the awesomeness.

-Pat

**Grade:**
Great