**Question 1:**
Which function can you call to delete a single file from the filestore?

**Your Answer:**
Not sure about the reference to 'filestore' in the question.  The only reference to 'filestore' in this course is in the section 'Archives - Reading and Writing Archives Using tarfile and zipfile' which is yet to come.

To delete a single file (which is not in an archive) you can use os.remove(path) or os.unlink(path).

**Mentor Comments:**
Thanks for the feedback.  You guessed right -  we meant "filesystem"..

**Question 2:**
What is a "stub" function?

**Your Answer:**
A 'stub' function is one which provides the correct interface for the calling function, but minimal if any functionality.  Used so that the calling function at least does not get errors because the called function does not yet exist.

**Mentor Comments:**
none

**Question 3:**
What should you verify regarding the status of the tests before replacing your stub functions with real code?

**Your Answer:**
The status of the tests, with a stub function should be Failure rather than Error, indicating that at least the stub function's interface is correct and the type of returned values is what's expected. 

**Mentor Comments:**
Typical TDD scenario:

EEEFEEFF   # &lt;-- still fine tuning stubs
EFFFFEEF   # &lt;-- close to ready to develop
FFFFFFFF    # &lt;-- ready to develop!
F..F...FFF     # &lt;-- getting to the goal
........    # &lt;-- yay, all tests pass

**Question 4:**
What does the os.path.exists(f) function do?

**Your Answer:**
os.path.exists(f) will return True if the path 'f' actually exists and False if path 'f' is a broken symbolic link.

**Mentor Comments:**
This works for directories, as well.

**Overall Comments:**
Terrific job here, Mark.

-Pat

**Grade:**
Great
