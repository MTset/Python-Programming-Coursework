'''
Created on Aug 24, 2015
@author: mtsikano

Tests the adder module which accepts the input of two integers and displays
their sum.  Any input other than two integers results in a TypeError in the
module or returns 'None' to the calling module - e.g. test module.
'''
import unittest
import adder

class Test(unittest.TestCase):
    def test_1_alpha_input_error(self):
        self.assertIsNone(adder.add("a",2), "Error: Accepted alpha character")
        
    def test_2_float_input_error(self):
        self.assertIsNone(adder.add(1.2,2), "Error: Accepted floating point")
        
    def test_3_complex_input_error(self):
        self.assertIsNone(adder.add(7, 1.2J), "Error: Accepted complex number")

    def test_4_null_input_error(self):
        self.assertIsNone(adder.add(7), "Error: Accepted null input")
        
    def test_5_none_input_error(self):
        self.assertIsNone(adder.add(7, None), "Error: Accepted 'None' type")
        
    def test_6_sequence_input_error(self):
        self.assertIsNone(adder.add(7, [1]), "Error: Accepted 'sequence' type")

    def test_7_set_input_error(self):
        self.assertIsNone(adder.add(7, {2}), "Error: Accepted 'set' type")

    def test_8_dict_input_error(self):
        self.assertIsNone(adder.add(7, {1:2}), "Error: Accepted 'dict' type")
        
    def test_9_range_input_error(self):
        self.assertIsNone(adder.add(1, range(1)), "Error: Accepted 'range' type")
        
    def test_10_bool_input_error(self):
        self.assertIsNone(adder.add(True, 3), "Error: Accepted Mapped boolean")        
        
    def test_11_integer_input_success(self):
        self.assertEqual(adder.add(1, 3), 4, "Error: Integer Not accepted")
        
    def test_12_neg_integer_input_success(self):
        self.assertEqual(adder.add(1, -3), -2, "Error: Negative integer Not accepted")

if __name__ == "__main__":
    unittest.main()