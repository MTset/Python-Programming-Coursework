"""
Test addarg module
"""
import unittest
from addarg import *

@addarg("The Day")
def movies(*args, **kwargs):
    if kwargs:
        return args, kwargs
    return args

class TestAddargs(unittest.TestCase):
        
        def test_multiple_args(self):
            self.assertEqual(movies("After Tomorrow", 2004),
                              ('The Day', 'After Tomorrow', 2004))
            self.assertEqual(movies("of the Jackal", 1973),
                              ('The Day', 'of the Jackal', 1973))
            self.assertEqual(movies("After", 1983),
                              ('The Day', 'After', 1983))
            
        def test_single_arg(self):
            self.assertEqual(movies(2011), ('The Day', 2011))
            
        def test_no_args(self):
            self.assertEqual(movies(), ('The Day', ))
            
        def test_kwargs(self):
            self.assertEqual(movies("the Earth Stood Still", 1951, Remake=2008),
                (('The Day', 'the Earth Stood Still', 1951), {'Remake': 2008}))

if __name__ == "__main__":
    unittest.main()            