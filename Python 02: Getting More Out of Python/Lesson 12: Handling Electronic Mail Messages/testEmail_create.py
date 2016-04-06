"""
Test the creation of MIME standard email with and without attachments.
"""

import unittest
import tempfile
import os
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email_create

class TestEmailCreate(unittest.TestCase):
    sender = 'tsikanovski@actrix.co.nz'
    receiver = 'tsikanovski@actrix.co.nz'
    subject = 'email creation test'
    bodytext = 'A Higgs boson walks into a bar and asks for a drinks menu.'
    attachmentext = '''
        <p>The barman says <i>"We don't see many of your type around here"</i></p>
        <p>The Higgs replies <i>"At <b>THESE</b> prices I am not surprised"</i></p>
        '''
    
    def setUp(self):
        self.tempdir = tempfile.mkdtemp("testdir")
        self.curdir = os.getcwd()
        os.chdir(self.tempdir)
        #set up msg body file
        f = open('body.txt', 'w')
        f.write(self.bodytext)
        f.close()
        # set up msg attachment file        
        f = open('attachment.html', 'w')
        f.write(self.attachmentext)
        f.close()
        
        self.msg = MIMEMultipart()
        self.msg['To'] = self.receiver
        self.msg['From'] = self.sender
        self.msg['Subject'] = self.subject
        self.body = open('body.txt', 'r').read()
        self.msg.attach(MIMEText(self.body))
        
    def test_without_attachment(self):
        expected = self.msg.as_string().splitlines()
        clean_expected = self.clean(expected)
        observed = email_create.e_create(self.sender, self.receiver,
                                          self.subject, 'return').splitlines()
        clean_observed = self.clean(observed)
        self.assertEqual(clean_expected, clean_observed)
        print(clean_expected)
        
    def test_with_attachment(self):
        attachment = MIMEText(open('attachment.html', 'r').read(),'text')
        attachment.add_header('Content-Disposition', 'attachment', 
                                  filename='attachment.html')
        self.msg.attach(attachment)

        expected = self.msg.as_string().splitlines()
        clean_expected = self.clean(expected)
        observed = email_create.e_create(self.sender, self.receiver,
                                          self.subject, 'return',
                                           ['attachment.html']).splitlines()
        clean_observed = self.clean(observed)
        self.assertEqual(clean_expected, clean_observed)
                
    def tearDown(self):
        os.chdir(self.curdir)
        shutil.rmtree(self.tempdir)
        
    def clean(self, string):
        #strip out boundary lines
        clean_string = ''
        for line in string:
            if '===============' not in line:
                clean_string += (line)
        return(clean_string)
            
if __name__ == "__main__":
    unittest.main()