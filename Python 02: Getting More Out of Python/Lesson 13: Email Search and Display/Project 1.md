**Here are your instructions:**
Write a program that imports the following names from a "settings" module:
RECIPIENTS   a list of (name, email-address) tuples
STARTTIME    datetime.datetime object for first message
DAYCOUNT    number of daily message generations

The program should produce a message of the format:
Date: {{date}}
From: &lt;a href="mailto:website@example.com"&gt;website@example.com&lt;/a&gt;
To: {{recipient}}
Message-Id: &lt;NNNNNN&gt;

This is a test message.

Your program should save these messages in the messages table.

Use test-driven development, and state the purpose of each test in the suite in docstrings that will eventually document your program.

Time your program for DAYCOUNTS of 1, 10, 50, 100, and 500 and plot the results (on a sheet of paper). How reliable are the timings?

Think of it like this: You are soon to go on vacation, at STARTTIME, for DAYCOUNT days, and you want your co-workers (RECIPIENTS) to continue getting your famous Joke of the Day (JOTD).

Your strategy is to store up the emails ahead of time, predated with the date they're to be sent. So if you leave on vacation on Jan 3, 2013, the first set of emails might be dated Jan 4 (each recipient gets one), then Jan 5 and so on, for DAYCOUNT days.

A good test that you have the right number is DAYCOUNT * len(RECIPIENTS) should equal SELECT COUNT(*) FROM jotd_emails; that is, the total number of days you're on vacation times the number of receivers, should equal the total number of records in the table generated. Of course, this will only be true if your To: line is only to a single recipient, and not all of them separated by commas.

Storing the right date for each email will likely involve using a timedelta to increment a datetime by one day at a time for DAYCOUNT days.

Regarding timing, it's enough to count under your breath and give a sense in your remarks about how you think time might be a function of DAYCOUNT. If you have your email generating and storing function where you might conveniently go:
    start = time.time()
    call_function(args)
    end = time.time()
    interval = end - start
    print("Time to complete: ", end)

Then you could also give some hard numbers as to the relative times the program took as a function of changing DAYCOUNT. The purpose of this requirement is to look ahead to future projects where timing / profiling is a core focus.

**Your Comment:**
Hi Pat,

Please also run email_create directly for the actual timings output and graph.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

This is really sophisticated - you put together the most impressive implementation of this objective I have seen in my entire tenure at OST!

All I can say is "WOW".

As your analysis indicates, there is roughly a linear relationship between the number of email messages and the system resources required. The fixed cost of setting up the database connections, etc. are pretty minimal in the time required is a direct function of the number of times the database gets hit.

Your results are typical, and represent something to think about as you design your own database-enabled projects.

Congratulations on your performance in this class and on your strong finish. You rock!

I will see you in Python 3.

-Pat

**Grade:**
Great
