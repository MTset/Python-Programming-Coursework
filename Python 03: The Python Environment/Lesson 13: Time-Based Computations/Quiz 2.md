**Question 1:**
What is the best way to validate a string that is supposed to represent a date?

**Your Answer:**
By trying to create a valid date(time)object from the string using the strptime method, e.g.

    try:
        # create a datetime object from the date value
        formatter_string = "%m-%d-%Y" 
        birthday = datetime.strptime(date, formatter_string)
    except ValueError as e: 
        # log the format error then raise it again so it can be handled gracefully 
        logging.error(e)
        raise InvalidDateFormat(e)

**Mentor Comments:**
none

**Question 2:**
Using datetime.datetime, how do I construct a datetime object for '07-24-1985 2:00 AM'?

**Your Answer:**
datetime.datetime(1985, 7, 24, 2)

**Mentor Comments:**
none

**Question 3:**
If my_date is the name of my datetime object, how do I get its hour?

**Your Answer:**
my_date.hour, e.g.

print(my_date.hour)

**Mentor Comments:**
none

**Overall Comments:**
Perfectly done, Mark. Enjoy your weekend.

-Pat

**Grade:**
Great
