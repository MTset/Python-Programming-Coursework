"""
Test function zip_files()

Input: Path to directory whose files are to be archived as a zip archive. Files
only, no sub-directories or archives.

Output: Zipped archive of files created in parent directory of Path.  Returns a
list of files in the zip archive.
"""

import unittest
import zip_files
import os
import tempfile
import shutil

class TestZipFiles(unittest.TestCase):
    def setUp(self):
        """
        Set up a temporary directory and populate with files and set up a sub-
        directory within it and populate that with files.
        """
        self.tempdir = tempfile.mkdtemp("testdir")
        self.tempsubdir = tempfile.mkdtemp("testsubdir", dir=self.tempdir)
        self.tempfiles1 = ['up', 'down', 'strange']
        self.tempfiles2 = ['charm', 'bottom', 'top']
        
        for file in self.tempfiles1:
            open(os.path.join(self.tempdir, file), 'w').close()
            
        for file in self.tempfiles2:
            open(os.path.join(self.tempsubdir, file), 'w').close()

    def test_archive_file_list(self):
        expected = []
        for file in self.tempfiles1:
            expected.append(os.path.basename(self.tempdir) + '/' + file)
        observed = zip_files.zip_files(self.tempdir)
        self.assertEqual(sorted(expected), sorted(observed))
        
    def tearDown(self):
        os.remove(self.tempdir + '.zip')
        shutil.rmtree(self.tempdir)
        
if  __name__ == "__main__":
    unittest.main()