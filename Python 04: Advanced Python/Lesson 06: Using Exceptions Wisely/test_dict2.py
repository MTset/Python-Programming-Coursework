"""
Test dict2 module
"""
import unittest
from dict2 import *

class TestDict2(unittest.TestCase):
    
    def setUp(self):
        self.d = Dict("default")
        self.d["a"] = 1
        self.d["b"] = 2
        self.d["c"] = 3
        self.d["e"] = 5
        
    def test_existing_key(self):
        self.assertEqual(self.d["a"], 1)
        self.assertEqual(self.d["b"], 2)
        self.assertEqual(self.d["c"], 3)
        self.assertEqual(self.d["e"], 5)
        
    def test_non_existent_key(self):
        self.assertEqual(self.d["d"], "default")
        # Show previously non_existent key now inserted with default value
        self.assertEqual(self.d, {"a": 1, "b": 2, "c": 3, "d": "default", "e": 5})
        
if __name__ == "__main__":
    unittest.main()