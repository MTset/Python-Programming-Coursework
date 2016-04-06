**Question 1:**
What does the statement pickle.dump(o, f) do?

**Your Answer:**
pickle.dump(o, f) will serialize object 'o' and write it to file 'f'.

**Mentor Comments:**
none

**Question 2:**
Should pickle files be opened in text or binary mode?

**Your Answer:**
pickle files should be opened in binary mode so that the interpreter does not modify the contents.

**Mentor Comments:**
From the Python documentation:

Be sure to always open pickle files created with protocols &gt;= 1 in binary mode. For the old ASCII-based pickle protocol 0 you can use either text mode or binary mode as long as you stay consistent.

A pickle file written with protocol 0 in binary mode will contain lone linefeeds as line terminators and therefore will look â??funnyâ?? when viewed in Notepad or other editors which do not support this format.

**Question 3:**
What type of key values does the shelve module require you to use?

**Your Answer:**
shelve module requires you to use keys which are encodable as strings.

**Mentor Comments:**
none

**Overall Comments:**
This is perfect, Mark.

-Pat

**Grade:**
Great
