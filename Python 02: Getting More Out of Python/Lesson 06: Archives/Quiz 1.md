**Question 1:**
If t is a tarfile object, what method would you call to add file f to the archive?

**Your Answer:**
You would use the add() method.  In this case, assuming 't' is already opened, you would use t.add(f).

**Mentor Comments:**
tar comes from Tape Archive.  You have probably seen those pictures of old computers,
mainfames, that spooled huge tapes on tape drives.  This API comes from those.  Obviously
it takes a relatively long time to find and mount a tape and sequential access (vs. random)
means if what you want is towards the end....  Like VHS tape and cassette tape, the 
computer tape devices have become relatively rare as better options have become less
expensive.

**Question 2:**
What second argument to tarfile.open() specifies writing the archive to disk with Gzip compression?

**Your Answer:**
The second argument to tarfile.open() for writing an archive with Gzip compression is 'w:gz'. e.g. tarfile.open('name', 'w:gz')

**Mentor Comments:**
none

**Question 3:**
What zipfile method returns the names of all files in the archive?

**Your Answer:**
The zipfile method namelist() returns returns a list of the archive member names. e.g. zf.namelist()

**Mentor Comments:**
none

**Overall Comments:**
Hi Mark,

Congratulations on a perfect quiz. Please have a look at the comments on Q1 for little bit of history behind tar.

-Pat

**Grade:**
Great
