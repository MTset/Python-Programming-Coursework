"""
Test_sstr.py: test the sstr module.
"""
import unittest
from sstr import *

class TestCyclicStringShift(unittest.TestCase):
        def setUp(self):
            self.s1 = sstr("abcde")
        
        def test_no_shift_left(self):
            expected = "abcde"
            observed = self.s1 << 0
            self.assertEqual(expected, observed)
            
        def test_no_shift_right(self):
            expected = "abcde"
            observed = self.s1 >> 0
            self.assertEqual(expected, observed)
            
        def test_part_shift_left(self):
            expected = "cdeab"
            observed = self.s1 << 2
            self.assertEqual(expected, observed)
            
        def test_part_shift_right(self):
            expected = "deabc"
            observed = self.s1 >> 2
            self.assertEqual(expected, observed)
            
        def test_full_shift_left(self):
            expected = "abcde"
            observed = self.s1 << 5
            self.assertEqual(expected, observed)
            
        def test_full_shift_right(self):
            expected = "abcde"
            observed = self.s1 >> 5
            self.assertEqual(expected, observed)
            
        def test_part_double_shift_leftt_right(self):
            expected = "eabcd"
            observed = (self.s1 << 2) >> 3
            self.assertEqual(expected, observed)
            
        def test_full_double_shift_right_left(self):
            expected = "abcde"
            observed = (self.s1 >> 5) << 5
            self.assertEqual(expected, observed)
            
        def test_str_builtin(self):
            self.assertEqual("ABCDE", self.s1.upper())
            self.assertEqual("cd", self.s1[2:4])
            self.assertTrue(self.s1.islower())
            self.assertTrue(self.s1.endswith("e"))
            self.assertEqual(["abcde"], self.s1.split())
            
        def test_issubclass(self):
            self.assertTrue(isinstance(self.s1, sstr))
            self.assertTrue(issubclass(sstr, str))
            
if __name__ == "__main__":
    unittest.main()