"""
Test Tree building module
"""
import unittest
from tree import *

class TestArray(unittest.TestCase):
    
    def setUp(self):
        self.t = Tree("D", "Don")
        for c, d in [("B", "Bob"),("J", "Jack"), ("Q", ""), ("K", "Karen"),
                      ("F", "Fred"), ("A", "Andrew"), ("C", "Cathy")]:
            self.t.insert(c, d)
            
    def test_walk(self):
        expected = ['A', 'B', 'C', 'D', 'F', 'J', 'K', 'Q']
        observed = list(self.t.walk())
        self.assertEqual(expected, observed)
        
    def test_find(self):
        self.assertEqual('Bob', self.t.find('B'))
        self.assertEqual('Karen', self.t.find('K'))
        self.assertEqual('Don', self.t.find('D'))
        self.assertEqual('', self.t.find('Q'))
        
    def test_missing_key(self):
        with self.assertRaises(KeyError):
            self.t.find('E')
        with self.assertRaises(KeyError):
            self.t.find('')
    
if __name__ == "__main__":
    unittest.main()