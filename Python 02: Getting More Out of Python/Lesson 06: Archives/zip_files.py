"""
Input: Path to directory whose files are to be archived as a zip archive. Files
only, no sub-directories or archives.

Output: Zipped archive of files created in parent directory of Path.  Returns a
list of files in the zip archive.
"""

import os
import zipfile
import glob

def zip_files(path):
    os.chdir(os.path.dirname(path))
    archive = '.\\' + os.path.basename(path) + '.zip'
    open_archive = zipfile.ZipFile(archive, 'w')
    files_to_zip = glob.glob(os.path.join('.\\' + os.path.basename(path), '*'))
    for file in files_to_zip:
        """ Make sure to only pick up files and not directories or archives """
        if os.path.isfile(file) and not zipfile.is_zipfile(file):
            open_archive.write(file)
    open_archive.close()
    open_archive = zipfile.ZipFile(archive) 
    return open_archive.namelist()