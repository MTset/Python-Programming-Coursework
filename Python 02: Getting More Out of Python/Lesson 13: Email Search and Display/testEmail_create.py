"""
testEmail_create - Tests the email_create module.
The email_create module creates JOTW (Joke Of The Week) e-mails for a list of
RECIPIENTS, to be sent starting on STARTTIME for a DAYCOUNT of days.  The e-mails
are pre-dated with the date they are to be sent and an e-mail message id.
One email per recipient per work day.

The e-mails are to be stored in a MySQL DB as separate fields prior to sending.
A new DB is used for each run.
"""
import email_create
import unittest
import settings
import datetime
import time
from database import login_info
from email.utils import make_msgid
import mysql.connector as msc
conn = msc.Connect(**login_info)
curs = conn.cursor()

class testEmail_create(unittest.TestCase):
    def test_1_default_run(self):
        """
        Tests a default run of email_create.  This tests that:
        1. The DB is set up and 
        2. It is populated with the correct number of records given
        the default DAYCOUNT as provided by the settings module.
        
        Get the defaults from settings module much as create_email would get,
        if neither STARTTIME nor DAYCOUNT are provided
        """
        settings.business_week()
        default_daycount = settings.DAYCOUNT
        number_of_recipients = len(settings.RECIPIENTS)
        expected_db_records = default_daycount * number_of_recipients
        email_create.email_create()
        curs.execute("SELECT COUNT(*) FROM jotd")
        observed_db_records = curs.fetchone()[0]
        self.assertEqual(expected_db_records, observed_db_records)
        conn.commit()
        
    def test_2_all_recipients(self):
        """
        Test that all recipients got one email each for each day of DAYCOUNT
        """
        curs.execute("SELECT msgReceiver FROM jotd")
        expected_recipients = []
        for r in settings.RECIPIENTS:
            expected_recipients.append((r[1],))
        for d in range(settings.DAYCOUNT):
            observed_recipients = curs.fetchmany(len(settings.RECIPIENTS))
            self.assertEqual(expected_recipients, observed_recipients)
        conn.commit()
        
    def test_3_sender(self):
        """
        Test that the sender of each message is the correct, same, addresss
        """
        curs.execute("SELECT msgSender FROM jotd")
        observed_db_msgSenders = curs.fetchall()
        observed_set_msgSenders = set(observed_db_msgSenders) # there can be only One
        sender = '<a href="mailto:{0}">{1}</a>'.format(settings.SENDER[1],
                                                    settings.SENDER[0])
        self.assertEqual({(sender,)}, observed_set_msgSenders)
        conn.commit()
            
    def test_4_message(self):
        """
        Test that the text of each message is the correct, same, text
        """
        curs.execute("SELECT msgText FROM jotd")
        observed_db_msgTexts = curs.fetchall()
        observed_set_msgTexts = set(observed_db_msgTexts) # there can be only One
        self.assertEqual({(settings.TEST_JOKE,)}, observed_set_msgTexts)
        conn.commit()
            
            
    def test_5_starttime_to_monday_run(self):
        """
        Test that if the STARTTIME falls on a weekend, the run defaults to the
        following Monday.  This is also true of the 'default' run when the
        STARTTIME defaults to tomorrow, unless tomorrow is a weekend.  Otherwise
        STARTTIME is unchanged.  The default run time is 07:00
        """
        settings.business_week(datetime.datetime(
                                    2099, 12, 26, 7, 0, 0)) # its a Saturday
        self.assertEqual(settings.STARTTIME, datetime.datetime(
                                    2099, 12, 28, 7, 0, 0)) # defaults to Monday
        settings.business_week(datetime.datetime(
                                    2099, 12, 27, 7, 0, 0)) # its a Sunday
        self.assertEqual(settings.STARTTIME, datetime.datetime(
                                    2099, 12, 28, 7, 0, 0)) # defaults to Monday
        # Check that this is also reflected in the initial run date on the DB
        email_create.email_create(datetime.datetime(2099, 12, 27, 7, 0, 0))
        curs.execute("SELECT msgDate FROM jotd")
        observed_db_msgDate = curs.fetchall()[0]
        self.assertEqual((datetime.datetime(
                                    2099, 12, 28, 7, 0, 0),), observed_db_msgDate)
        conn.commit()

    def test_6_run_only_on_weekdays(self):
        """
        Test that the email dates, i.e. when the emails are to be sent out is
        only on week days, not weekends, this also checks that DAYCOUNT is
        is used correctly.  Also checks that the date in the email subject line
        corresponds to the actual send send date.
        """
        # Run from Thursday 10th for 10 days - ends two weeks Wednesday 23rd
        email_create.email_create(datetime.datetime(2099, 12, 10, 7, 0, 0), 10)
        curs.execute("SELECT msgDate, msgSubject FROM jotd")
        observed_db_msgDate = curs.fetchall()
        # check send date against date in subject
        for n in observed_db_msgDate:
            self.assertEqual(settings.SUBJECT + str(n[0].strftime("%a %b %d %Y")),
                n[1])
        # check start date on first record in DB
        self.assertEqual((datetime.datetime(
                                    2099, 12, 10, 7, 0, 0)), observed_db_msgDate[0][0])
        # check end date on last record in DB
        self.assertEqual((datetime.datetime(
                                    2099, 12, 23, 7, 0, 0)), observed_db_msgDate[-1][0])
        conn.commit()
        
    def test_7_unique_email_msgid(self):
        """
        Test that the Emai-ID fields generated are unique.
        """
        curs.execute("SELECT msgEmailID FROM jotd")
        observed_db_msgEmailIDs = curs.fetchall()
        observed_set_msgEmailIDs = set(observed_db_msgEmailIDs)
        self.assertEqual(len(observed_db_msgEmailIDs), len(observed_set_msgEmailIDs))
        conn.commit()
    
if __name__  == "__main__":
    unittest.main()            