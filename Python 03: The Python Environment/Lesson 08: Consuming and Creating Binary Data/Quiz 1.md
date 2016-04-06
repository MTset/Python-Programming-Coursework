**Question 1:**
Name at least two differences between ASCII and Unicode.

**Your Answer:**
ASCII uses one byte to represent a character in a character set.  Unicode uses one to four bytes to represent a character in a character set.
ASCII is based on 7-bit code (originally, with some use of an 8th bit for parity or error checking).  Unicode is based on 16-bit code (originally).
In ASCII the same control point (code) may have several uses, e.g. LF is both a control and a formating separator.  In unicode one control point has one use.

**Mentor Comments:**
Unicode is a different encoding that ASCII but it can encode all the same characters ASCII does.  The subset of unicode for so doing is called Latin-1 -- still a bigger set than just what's on a standard US keyboard.  Note that as of Python3, .py file source code is itself in Unicode, UTF-8 format.  That means Python may use Chinese characters, Hiragana, Katakana etc.  Variable, function and class names can use those character sets (Arabic, Thai, Hindi etc. etc.).

Only the keywords need to stay in Python, plus the Standard Library is supposed to stay in English to maximize accessibility. 3rd party modules are under no such restrictions.

Here's a Youtube that takes about half an hour to display the 49,571 printable characters that UTF covers.  Fun to scroll around in.  So many Chinese ideograms!

[

http://youtu.be/Z_sl99D2a18](http://youtu.be/Z_sl99D2a18)

**Question 2:**
What module does Python use to interact with binary data?

**Your Answer:**
The struct module

**Mentor Comments:**
none

**Question 3:**
What do the pack() and unpack() methods of the struct module do?

**Your Answer:**
pack() packs values into a byte string.
unpack() unpacks values from a byte string.

**Mentor Comments:**
none

**Overall Comments:**
Hi Mark,

Terrific work on this one.  Please see the comments on Q1 for some elaboration  and a link to a really cool site.

-Pat

**Grade:**
Great
