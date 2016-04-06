**Here are your instructions:**
Create a Python3_Homework04 project and assign it to your Python3_Homework working set. In the Python3_Homework04/src folder, create a program named find_regex.py that takes the following text and finds the start and end positions of the phrase, "Regular Expressions."

Text to use in find_regex.py:
In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer. 
Your project should meet the following conditions:
You must include a separate test_find_regex.py program that confirms that your code functions as instructed.

Submit find_regex.py and test_find_regex.py when they are working to your satisfaction.

**Your Comment:**
Hi Pat,

There is a minor error in the assignment.  There is no phrase "Regular Expressions." in the text.
The period should be outside the quotes (or it's a trick question) or it should be a comma, but that
would return (231, 251).

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Nice catch  on the typo. I'll pass it along - it's not there to intentionally trip you up (really ! ! !).

You done a good job on this project and your tests are epic in their thoroughness. One thing I would pass along - and this might be as much personal bias as anything else . .. 

test_1_string_exists_location() takes a fairly complicated route to determine that begins it 231 and ends at 250.  Personally I would find this much more clear:

       self.assertEqual((231, 250), 
                        locate_search_string(self.textfile.name, search_string), 
                        "String not located correctly")

For me, transparency and simplicity are really important for tests. This good chance that you, or your colleagues, will be looking at tests in the process of fixing something that's broken. So anything you can data minimize the cognitive load will be appreciated.

Efficiency is always a virtue, but not such a big concern for tests - after all they're not part of the production code and will run much less frequently. Besides, here you already know what it is you're looking for, and an expression like this:

       expected = (self.text.find(search_string),
                   self.text.find(search_string) + len(search_string))

... has to be recalculated every time so there are not even efficiency gains.

Overall, you have an awesome project on your hands. Great work.

-Pat

**Grade:**
Great
