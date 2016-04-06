"""
test_ctx_mgr.py: test the ctx_mgr module.
"""
import unittest
from ctx_mgr import *

class TestContextMnager(unittest.TestCase):
    def test_valueerror_suppressed(self):
        # check that the following operation SHOULD raise a ValueError
        with self.assertRaises(ValueError):
            _ = int("a")
        # check that in this context manager class the ValueError is suppressed
        with self.assertRaises(AssertionError):
            with self.assertRaises(ValueError):
                with ctx_mgr():
                    _ = int("a")
                
    def test_othererrors_raised(self):
        # test a selection of other errors, that they are raised
        with self.assertRaises(ZeroDivisionError):
            with ctx_mgr():
                _ = 2/0
        with self.assertRaises(TypeError):
            with ctx_mgr():
                _ = "abc"/2
        with self.assertRaises(AttributeError):
            with ctx_mgr():
                _ = [].split()
        
if __name__ == "__main__":
    unittest.main()