**Question 1:**
What is another way to set the level of a logger besides the basicConfig() function?

**Your Answer:**
Using the setLevel() method, e.g.

# create logger with "spam_application"
logger = logging.getLogger("spam_application")
logger.setLevel(logging.DEBUG)

**Mentor Comments:**
Perfect.

**Question 2:**
What is a common way to display the time of a log message?

**Your Answer:**
Using the %(asctime)s key in the format parameter.

**Mentor Comments:**
none

**Question 3:**
What does '%(lineno)d %(levelname)s' display in a log message?

**Your Answer:**
%(lineno)d displays the source line number where the logging call was issued (if available) 
%(levelname)s displays the text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL') 

**Mentor Comments:**
none

**Overall Comments:**
Thanks for taking another go at this, Mark. You have it totally dialed in now.

-Pat

**Grade:**
Great
