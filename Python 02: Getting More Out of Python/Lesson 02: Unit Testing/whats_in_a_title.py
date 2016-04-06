#!/usr/bin/python3
""" Demonstrates the unittest module in action. """
import unittest
import sys

def title(s):
    " How close is this function to str.title()? "
    return s[0].upper()+s[1:]

def title2(s):
    " A str.title() replacement"
#    return ' '.join(w[0].upper()+w[1:] for w in s.split()) # OR, further re-factored, below
    return ' '.join(w.capitalize() for w in s.split())

class TestTitleCase(unittest.TestCase):
    test_cases = {"what are we to do",
                  "What are we to do",
                  "WHAT ARE WE TO DO"
                  }
    
# Table of error messages - keyed by method name
    error_string = {
    '''test_title_case_not_equal''': '''These should not be the same:\n
    Replacement Function 1: {0}\n    Built-In Function:      {1}\n''',
           
    '''test_title_case_equal''': '''These should be the same:\n
    Replacement Function 2: {0}\n    Built-In Function:      {1}\n'''
                    }    
    
    def test_title_case_not_equal(self):
        for case in TestTitleCase.test_cases:
            self.assertNotEqual(title(case), case.title(),
                TestTitleCase.error_string[sys._getframe().f_code.co_name]
                .format(title(case), case.title()))

    def test_title_case_equal(self):
        for case in TestTitleCase.test_cases:
            self.assertEqual(title2(case), case.title(),
                TestTitleCase.error_string[sys._getframe().f_code.co_name]
                .format(title2(case), case.title()))
        
if __name__ == "__main__":
    unittest.main()