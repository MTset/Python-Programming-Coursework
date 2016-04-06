**Here are your instructions:**

Create a Python3_Homework10 project and assign it to your Python3_Homework working set. In the Python3_Homework10/src folder, create a program named property_address.py, including the following:
* The custom exceptions StateError and ZipCodeError.
* Class Address that takes name, street_address, city, state, and zip_code as string arguments, which must then be set as attributes. You turn any or all of these attributes into properties in order to solve this assignment so long as they also meet these requirements:
* After being set in __init__, the name attribute is read-only. Further attempts to modify it will trigger an AttributeError.
* Zip code must follow the simple US pattern (nnnnn) or it throws a ZipCodeError.
* State only allows two capital letters or it throws a StateError.
* State and Zip code validation must be done by regular expressions.
* Your project must include (and your program must pass!) the unittest test_property_address.py (listed below).

import unittest
from property_address import *
 
class TestAddresses(unittest.TestCase): 
   
    def setUp(self): 
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VA', zip_code='12345' )
       
    def test_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')  
           
    def test_state(self): 
        self.assertEqual(self.home.state, 'VA') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')  
        self.home.state = 'CO' 
        self.assertEqual(self.home.state, 'CO')  
        
    def test_zip_code(self): 
        self.assertEqual(self.home.zip_code, '12345') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '123456')   
        self.home.zip_code = '54321' 
        self.assertEqual(self.home.zip_code, '54321') 
       
if __name__ == "__main__": 
    unittest.main() 
Submit property_address.py and test_property_address.py when they are working to your satisfaction.

**Your Comment:**
Hi Pat,

Test address changed to a real one (but in keeping with the theme, it is that of
The Flying Circus AirShow) as 'real world' checking is done', though very basic.

Some of the regex's are from the net, what I felt were best of breed, I make no claim to having
created them.  The zip code and state testing are obviously very US centric, but the rest of the
validation I kept as 'world' applicable as I could.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

This is a real tour de force! You have done an awesome job tapping into Python's ability to grok Unicode and its ability to internationalize. In two years at this job, I have never seen a better implementation of this objective. Awesome !

In case you're interested, you can actually write Python code in any language (including Japanese, Arabic, etc.) the only rule is that the keywords have to be in English - but that's not a really big deal because there are only 33 of them.

Anyway, this is really outstanding. Nicely done.

-Pat

**Grade:**
Great
