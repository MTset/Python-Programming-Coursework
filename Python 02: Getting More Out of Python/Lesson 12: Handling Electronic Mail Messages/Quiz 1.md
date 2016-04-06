**Question 1:**
What function can you use to create an email.message.Message object from its string representation?

**Your Answer:**
The message_from_string() function.

**Mentor Comments:**
none

**Question 2:**
Which library would you use to send emails?

**Your Answer:**
The smtplib library.

**Mentor Comments:**
none

**Question 3:**
What is the structure of an email header?

**Your Answer:**
Field Name     Example 
orig-date      Date: 24 Apr 2010 10:00:00 -0700 
from           From: someone@domain.bar 
to             To: foo@example.bar 
subject        Subject: Hello 

**Mentor Comments:**
Right, and another good answer would be:

One or more instances of individual headers, which consist of field name, followed by a :, followed by a field body.  The field name must be comprised of printable US-ASCII characters (excluding :), while the body can contain any US-ASCII characters except CR and LF.  Headers are separated from each other by CRLF characters.

**Overall Comments:**
Awesome, Mark.

-Pat

**Grade:**
Great
