"""
email_create - This module creates JOTW (Joke Of The Week) e-mails for a list of
RECIPIENTS, to be sent starting on STARTTIME for a DAYCOUNT of days.  The e-mails
are pre-dated with the date they are to be sent and an e-mail message id.
One email per recipient per work day.  This can be changed to bulk sending later.

The e-mails are to be stored in a MySQL DB as separate fields prior to sending.
A separate module (TBA) is to actually assemble the e-mails and send them.
A new DB is used for each run.

This module is just a proof of concept, using a single test 'joke' and a test 
list of 'recipients'.  The purpose is to establish timings required to create the
e-mails using ever increasing volumes of e-mails by increasing the DAYCOUNT.

Basic timing statistics are printed out and a graph of DAYCOUNT (which is
directly proportional to e-mail volumes, given the fixed recipient list) Vs.
time in seconds required to produce the e-mails.
"""
import settings
import datetime
import time
import random
from database import login_info
from email.utils import make_msgid
import mysql.connector as msc
conn = msc.Connect(**login_info)
curs = conn.cursor()
messagect = 0
start_real_time = 0
end_real_time = 0
run_real_time = 0
start_cpu_time = 0
end_cpu_time = 0
run_cpu_time = 0
run_real_times = []
messagects = []

def email_create(starttime=None, daycount=None):
    settings.business_week(starttime, daycount)
    send_date = settings.STARTTIME # initial send date
    sender = '<a href="mailto:{0}">{1}</a>'.format(settings.SENDER[1],
                                                    settings.SENDER[0])
    
    curs.execute("DROP TABLE IF EXISTS jotd")
    conn.commit()
    curs.execute(settings.TBLDEF)
    conn.commit()
    
    for d in range(settings.DAYCOUNT):
        for r in settings.RECIPIENTS:
            subject = settings.SUBJECT + str(send_date.strftime("%a %b %d %Y"))
            idstring = random.SystemRandom()
            curs.execute("""INSERT INTO jotd (msgDate, msgSender,
                msgReceiver, msgSubject, msgEmailID, msgText)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (send_date, sender, r[1], subject, 
                 make_msgid(str(idstring.random())), settings.TEST_JOKE))
            conn.commit()
        # increase date by one day
        send_date = send_date + datetime.timedelta(days=1)
        # date messages to only send on work days
        while send_date.weekday() not in settings.WEEKDAYS:
            send_date = send_date + datetime.timedelta(days=1)
        
    curs.execute("SELECT COUNT(*) FROM jotd")
    global messagect, messagects
    messagect = curs.fetchone()[0]
    conn.commit()
    messagects.append(messagect)
    if __name__ == "__main__":
        print("Messages:", messagect)
    
if __name__ == "__main__":
    for n in settings.DAYCOUNT_RANGE:
        daycount = 2**n
        start_cpu_time = time.clock()
        start_real_time = time.time()
        email_create(None, daycount)
        end_cpu_time = time.clock()
        end_real_time = time.time()
        run_cpu_time = end_cpu_time - start_cpu_time
        run_real_time = end_real_time - start_real_time
        run_real_times.append(int(round(run_real_time, 1) * 10))
        print("Run real time: {0} - per record: {1}\nRun CPU time: {2} - per record: {3}"
        .format(run_real_time, run_real_time/messagect, run_cpu_time, run_cpu_time/messagect))
        print(70 * "-")

    # Graph Results
    max_run_real_times = max(run_real_times)

    for i in range(max_run_real_times + 1, 0, -1):
        output_line = "  {0:>4}-|  ".format(str(i/10))
        for n, j in enumerate(run_real_times):
            if i == j:
                spacing = n * 5 * " "
                output_line = output_line + spacing + "X ({0} msgs)".format(messagects[n])
        print(output_line)

    output_line = "     0-|"
    for i in range (1, max(settings.DAYCOUNT_RANGE) + 1, 1):
        output_line = output_line + "--+--"
    print(output_line)

    output_line = 7 * " "
    for i in range (1, max(settings.DAYCOUNT_RANGE) + 1, 1):
        output_line = output_line + "{0:^5}".format(i)
    print(output_line)
    output_line = "{0:^50}".format("LEGEND: X axis - Log Base 2 of DAYCOUNT")
    print(output_line)
    output_line = "{0:^46}".format("LEGEND: Y axis - Run time in seconds")
    print(output_line)
