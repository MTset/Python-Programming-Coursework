**Here are your instructions:**
Make a UnitTesting_Homework project and assign it to the Python2_Homework working set. In this project, write a unittest test program for the following function. (The test program makes unittest.TestCase assertions about the results of calling the function with known arguments.)
def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]
Test your results for a given string s by comparing them with s.title(). Because this is purely an exercise, it's OK to put your test code in the same file as the function and just hand in a single file. Your file should be an importable module. You should be able to find an example that shows title(s) and s.title() diverge (have different output). Bonus marks for fixing the error in the function above (making it behave more like the native method).

**Your Comment:**
Hi Pat,

I did contemplate whether to include output for the one 'successful' test where the output was different and decided to see what you thought.
The setUp() and tearDown() placeholders with just 'pass' I put in after coming across them in an example of unittest in the 'Essential Reference' and thought it might be good form.

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

No worries on any of this stuff. You're doing great in this class.

You now have a completely awesome project. My last piece of advice would be to try to keep all the stuff getting tested down in the test methods. It doesn't matter if you got redundant code, really. Tests are much more about transparency in human readability than they are about efficiency.

Besides, you want to maintain the maximum amount of isolation among the different test methods as possible. If you have a variable like test_cases defined as a global level, it is possible to have one test method make changes to it, causing another test method to fail. Working alone, and working on a project this small it is nearly material. But in a bigger project, where the people writing the tests might never have met the people developing the app, or each other, it could become an issue.

Overall: great work !

-Pat

**Grade:**
Great
