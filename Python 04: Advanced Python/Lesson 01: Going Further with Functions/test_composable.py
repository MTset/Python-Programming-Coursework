"""
test_composble.py: performs simple tests of composble functions.
"""
import unittest
from composable import Composable

def reverse(s):
    "Reverse a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself"
    return x * x

class ComposableTestCse(unittest.TestCase):
    
    def test_inverse(self):
        reverser = Composable(reverse)
        # same function
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)
            
        # different functions
        nulltran = reverser * reverse
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)
            
    def test_square(self):
        # same function
        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)        

        # different functions
        squarer = Composable(square)
        po4 = squarer * square
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)
    
    def test_power(self):
        reverser = Composable(reverse)
        reversed = reverser ** 3
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(reversed(s), reverse(s))
            
        powerer = Composable(square)
        po8 = powerer ** 3
        for v, r in ((1, 1), (2, 256), (3, 6561)):
            self.assertEqual(po8(v), r)
        
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = square ** '1'
        with self.assertRaises(TypeError):
            fc = square ** 1.1
            
        with self.assertRaises(ValueError):
            test = fc**0
            test = fc ** -1
        " or - better "
        with self.assertRaises(ValueError):
            test= fc.__pow__(0)
            test=fc.__pow__(-1)
            
        """            
        # could not these to work with 'with'
        self.assertRaises(ValueError, fc.__pow__, 0)
        self.assertRaises(ValueError, fc.__pow__, -1)
        """    
if __name__ == "__main__":
    unittest.main()