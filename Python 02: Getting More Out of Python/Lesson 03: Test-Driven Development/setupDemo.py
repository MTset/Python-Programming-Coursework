"""
Demonstrates the setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""

import unittest
import tempfile
import shutil
import glob
import os
import sys

class FileTest(unittest.TestCase):

#    file_list_in = {"this.txt", "that.txt", "../the_other.txt"} # Testing
    file_list_in = {"this.txt", "that.txt", "the_other.txt"}
    
    # Table of error messages - keyed by method name
    error_string = {
    'test_1': '''\nList of files to create does not match list of files created:
    Not created: {0}\n    Extra created: {1}''',
    
    'test_2': '\nDirectory not empty',
    
    'test_3': '\nBytes written ({0}) should equal filesize on disk ({1})'
                    }
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of files is possible, all get created with no extras"
        for filename in FileTest.file_list_in:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
#        f = open("extra_file.txt", "w") # Testing
#        f.close()
        file_list_out = set(os.listdir(path='.'))
        self.assertEqual(len(FileTest.file_list_in ^ file_list_out), 0,
        FileTest.error_string[sys._getframe().f_code.co_name].format(
        str(FileTest.file_list_in - file_list_out, ),
        str(file_list_out - FileTest.file_list_in)))
        
    def test_2(self):
        "Verify that the current directory is empty"
#        f = open("extra_file.txt", "w") # Testing
#        f.close()
        self.assertEqual(glob.glob("*"), [],
        FileTest.error_string[sys._getframe().f_code.co_name])
        
    def test_3(self):
        "Verify bytes written Vs file length on disk"
        bytestream_fill = 1000000 * "0".encode(encoding='utf_8',errors='strict')
        f = open("binary_file.bin", "bw")
        f.write(bytestream_fill)
        f.close()
        statinfo = os.stat("binary_file.bin")
        self.assertEqual(len(bytestream_fill), statinfo.st_size,
        FileTest.error_string[sys._getframe().f_code.co_name].format
        (len(bytestream_fill), statinfo.st_size, ))
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == "__main__":
    unittest.main()