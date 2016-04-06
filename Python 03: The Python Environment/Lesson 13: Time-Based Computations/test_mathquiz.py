"""
test_mathquiz.py: tests the mathquiz.py module.
"""
import unittest
import math
from mathquiz import *

class TestMathquiz(unittest.TestCase):
    def test_1_user_input(self):
        """
        Test input as it would come in from the user terminal, as str
        Accept natural numbers and nothing else.
        """
        self.assertTrue(validate_input(str(123)))
        self.assertIsNone(validate_input(str(0)))
        self.assertIsNone(validate_input(str(-123)))
        self.assertIsNone(validate_input(str(10.0)))
        self.assertIsNone(validate_input("abc"))
        
    def test_2_answer_calculation(self):
        """
        Test that the answer (first number) is indeed the
        sum of the squares of the other two numbers.
        """
        self.assertTrue(validate_answer(149, 10, 7), "right")
        self.assertTrue(validate_answer(117, 6, 9), "right")
        self.assertTrue(validate_answer(73, 8, 3), "right")
        self.assertTrue(validate_answer(149, 10, 8), "wrong")
        self.assertTrue(validate_answer(150, 10, 7), "wrong")
        self.assertTrue(validate_answer(25, 4, 4), "wrong")
        
    def test_3_randint_generation(self):
        expected = [100000]*10
        observed = [0]*10
        for i in range(1000000):
            randint = get_randint()
            # check random numbers lie within a range of 1 - 10
            self.assertTrue(randint in range(1,11))
            observed[randint - 1] += 1
        """
        Calculates the chi-square value for N (1000000 in our case) positive 
        integers up to r (10 in our case) and checks for an acceptable degree
        of randomness, acceptable being where the statistic should be within
        2(r)^1/2 of r. Source: "Algorithms in C" - Robert Sedgewick - pp 517
        """
        chi_square = 0
        for i in range(10):
            chi_square += ((observed[i] - expected[i])**2)/expected[i]
        self.assertTrue(abs(chi_square - 10) <= 2 * math.sqrt(10))
        
if __name__ == "__main__":
    unittest.main()
        