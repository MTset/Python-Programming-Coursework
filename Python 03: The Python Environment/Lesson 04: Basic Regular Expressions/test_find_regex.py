"""
test_find_regex.py: Test that module find_regex determines the start and end
positions of a search string correctly, by cross checking the reported positions
with those determined by the str find() method.
"""

import unittest
from find_regex import locate_search_string

class TestFindRegex(unittest.TestCase):
    
    def setUp(self):
        self.textfile = open("text_to_search.txt", 'r')
        self.text = self.textfile.read()
        
    def tearDown(self):
        self.textfile.close()
    
    def test_1_string_exists_location(self):
        """
        Test 1: Test that a string's start and end positions of a string that
        exists in the text is correctly detected
        """
        search_string = "Regular Expressions"
        expected = (self.text.find(search_string),
                    self.text.find(search_string) + len(search_string))
        observed = locate_search_string(self.textfile.name, search_string)
        self.assertEqual(expected, observed, "String not located correctly")
        
    def test_2_string_doesnt_exist(self):
        """
        Test 2: Test that a string which does not exist in the text is not
        reported as found, including None and zero length string.
        """
        search_string_list = ["Irregular Expressions", None, ""]
        for search_string in search_string_list:
            observed = locate_search_string(self.textfile.name, search_string)
            self.assertIsNone(observed, "Missing string incorrectly identified")
            
    def test_3_bad_textfile(self):
        """
        Test 3: Test that notification is received if the file could not be
        located or opened.
        """
        text_file_list = ["nosuchfile.txt", None, "python-logo.gif"]
        expected = "Missing or unreadable file"
        for textfile_name in text_file_list:
            observed = locate_search_string(textfile_name, "E")
            self.assertEqual(expected, observed, "Check file used")        
        
if __name__ == "__main__":
    unittest.main()