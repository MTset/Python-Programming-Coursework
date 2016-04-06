**Here are your instructions:**
Create a Pydev project named Python3_Homework09 and assign it to your Python3_Homework working set. In Python3_Homework09/src, create a program named centipede.py, including a class named "Centipede." This class has the following requirements:

1. Once instantiated if called with a value, it appends that argument to an internal list:
&gt;&gt;&gt; from centipede import Centipede
&gt;&gt;&gt; ralph = Centipede()
&gt;&gt;&gt; ralph('pretzel')
&gt;&gt;&gt; ralph.stomach
['pretzel']
2. If you print() the class, it returns a comma-delimited string of the internal list:
&gt;&gt;&gt; ralph('pickles')
&gt;&gt;&gt; print(ralph)
pretzel,pickles
3. Each time an attribute is set on the centipede object, it appends the name of the attribute to another internal list:
&gt;&gt;&gt; ralph.shoes = 100 
&gt;&gt;&gt; ralph.hat = 1
&gt;&gt;&gt; ralph.legs
['shoes', 'hat']
4. The representation of the centipede object must be a comma-delimited string of this second internal list.
&gt;&gt;&gt; repr(ralph)
'shoes,hat'
5. The legs and stomach attributes should be protected against having their values reset from outside. They're "internal use only" when it comes to changing them, and an AttributeError should be raised if attempts are made to set them.
&gt;&gt;&gt; ralph.legs = 3
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "V:\workspace\Python3_Homework09\src\centipede.py", line 15, in __setattr__
    raise AttributeError("{0} is for internal use only".format(key))
AttributeError: legs is for internal use only

Copy and include this test_centipede.py unittest file, which your centipede program should pass:
    
import unittest
    
from centipede import Centipede

class TestBug(unittest.TestCase):
    def test_stomach(self):
        ralph = Centipede()
        ralph('chocolate')
        ralph('bbq')
        ralph('cookies')
        ralph('salad')
        self.assertEqual(ralph.__str__(), 'chocolate,bbq,cookies,salad')
        
    def test_legs(self):
        ralph = Centipede()
        ralph.friends = ['Steve', 'Daniel', 'Guido']
        ralph.favorite_show = "Monty Python's Flying Circus"
        ralph.age = '31'
        self.assertEqual(ralph.age, '31', "ralph doesn't know how old he is")
        self.assertEqual(ralph.__repr__(), 'friends,favorite_show,age')
        
        
    def test_protected(self):
        ralph = Centipede()
        self.assertRaises(AttributeError, setattr, ralph, "legs", [])
        self.assertRaises(AttributeError, setattr, ralph, "stomach", [])

if __name__ == "__main__":
    unittest.main()

**Your Comment:**

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

You've done a terrific job not only putting together your Centipede, but ensuring its biological integrity - as demonstrated by its ability to pass this additional test:

    def test_individuality(self):
        ralph = Centipede()
        self.assertEqual(ralph.__str__(), '')  #new 'pede with empty stomach
        ralph('chocolate')
        ralph('bbq')
        mary = Centipede()                     #another 'pede with empty stomach
        self.assertEqual(mary.__str__(), '')

Best,

-Pat

**Grade:**
Great
