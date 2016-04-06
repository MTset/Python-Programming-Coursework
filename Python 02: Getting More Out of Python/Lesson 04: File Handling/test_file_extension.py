"""
Create a temporary file directory and populate with known different counts of
temp files with various file extensions.  Check that the file counts, by
extension, returned by module 'file_extension' match the number of those files
generated.
"""

import unittest
import tempfile
import shutil
import os
import file_extension

class TestFileExtension(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.tempdir = tempfile.mkdtemp("testdir")
        os.chdir(self.tempdir)
        
        for file in ["test1.doc", "test2.doc", "long.file.ext.tz", "no_ext",
                     "joe.zip"]:
            open(file, 'w').close()
        # dict of expected extensions
        self.expected = {"doc":2, "tz":1, "":1, "zip":1}
            
    def test_file_extension_counts(self):
        """
        Ensure that calling the function returns correct counts for each
        extension type.
        """
 
        # dict returned by function
        extension_count = file_extension.counts(path=self.tempdir)
        self.assertEqual(extension_count, self.expected)
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.tempdir)
        
if __name__ == "__main__":
    unittest.main()