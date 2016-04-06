**Here are your instructions:**
Create a Python3_Homework05 project and assign it to your Python3_Homework working set. In the Python3_Homework05/src folder, create a program named ccn_safety.py with a function that substitutes X for all but the last four digits of any credit card numbers in a string, returning the updated string as its result. Use the following text as a sample:

Text to use in ccn_safety.py:
Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number
that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and 
security experts.
Your project should meet the following conditions:
* For our purposes, it only needs to convert numbers of the form XXXX-XXXX-XXXX-XXXX.
* The program should return this text: "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and security experts." Note that the phone numbers should not be replaced!
* You should include a test_ccn_safety.py program in a separate file that confirms that your code functions as expected.

Submit ccn_safety.py and test_ccn_safety.py when they are working to your satisfaction.

**Your Comment:**
Hi Pat,

Once again with this project you'll notice I went slightly off track and changed the numbers in the
text.  The numbers are proper Test Credit Card Account Numbers from:
https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm

The reason is that, my ccn_safety checks for proper credit card numbers.  Better tests are available
than luhn, but they were quite a bit more complicated.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Yes, this is a little bit off track, but you demonstrated mastery of the topic so I will not whine too much. But in the future, please try to keep them on track - sometimes the specific learning goals are less than obvious (not the case here).

Good research on figuring out how to determine bogus credit card numbers. I'm not sure, but I believe a very similar algorithm is included in one of my favorite websites:

As to this project, You've done a terrific job demonstrating initial mastery of regular expressions.  Congratulations.

There's a region of overlap where ordinary string operations can do what a regex does, but then there's a wider circle where the regex expresses patterns that would take many lines of code as string ops and would run much slower.

The whole regular expression idea grew up independently of a specific language and is grafted in.  Perl is famously regex friendly.  Python's re module is very  capable but the fact that you need to import something makes regexes less a built-in feature than in Perl. A comparison:  

http://www.johndcook.com/python_regex.html

Culturally speaking, a Python programmer is less likely to use regular expressions  casually, but only out of real need, wheras a Perl programmer is more likely to sprinkle regular expressions throughout the code.

I'd say Java is closer to Python in its relationship to regular expressions, Ruby more like Perl. 

http://www.regular-expressions.info/ruby.html
http://www.regular-expressions.info/java.html

-Pat

**Grade:**
Great
