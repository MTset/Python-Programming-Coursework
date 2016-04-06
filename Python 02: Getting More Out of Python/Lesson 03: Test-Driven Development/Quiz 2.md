**Question 1:**
What would be the best methods to use to verify the result of a floating-point computation during a test?

**Your Answer:**
Either the assertAlmostEqual() or the assertNotAlmostEqual() depending on what result is expected.

**Mentor Comments:**
none

**Question 2:**
Which function from the tempfile module would you use to create a new temporary directory?

**Your Answer:**
The tempfile.mkdtemp() module.

**Mentor Comments:**
The directories created will have very random names, so make sure you keep track of them for deletion within the program.  If on Windows, paths will use backlashes.  Paths will likewise seem random.

&gt;&gt;&gt; import tempfile
&gt;&gt;&gt; thepath = tempfile.mkdtemp()
&gt;&gt;&gt; otherpath = tempfile.mkdtemp("testdir")
&gt;&gt;&gt; thepath
'/var/folders/lf/f131hls54tv5lhx_4rn06n880000gp/T/tmp4x49to'
&gt;&gt;&gt; otherpath
'/var/folders/lf/f131hls54tv5lhx_4rn06n880000gp/T/tmpo721_5testdir'
&gt;&gt;&gt; os.rmdir(thepath)
&gt;&gt;&gt; os.rmdir(otherpath)

Using interactive Python console on Eclipse server at OST:

import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
C:\Python\python.exe 3.1.4 (default, Jun 12 2011, 14:16:16) [MSC v.1500 64 bit (AMD64)]
PyDev console: using default backend (IPython not available).
&gt;&gt;&gt; import tempfile
&gt;&gt;&gt; tempdir = tempfile.mkdtemp()
&gt;&gt;&gt; tempdir
'c:\\users\\pbarton\\appdata\\local\\temp\\3\\tmpsetizw'
&gt;&gt;&gt; import os
&gt;&gt;&gt; os.rmdir(tempdir)
&gt;&gt;&gt;

**Question 3:**
Which function from the shutil module would you use to delete a directory including all files and subdirectories in it?

**Your Answer:**
The shutil.rmtree() module.

**Mentor Comments:**
Yes.  Be careful with this one.  It does *exactly* what you ask of it - quickly and silently.  One of my students recently wiped out his entire homework directory on accident :-(

**Question 4:**
What is the first step in test-driven development?

**Your Answer:**
The first step in TDD is to identify the requirements.

Or

If the above is a given (because it's the first step in any development), the first step in TDD is to write tests.

**Mentor Comments:**
none

**Overall Comments:**
Hi Mark,

Terrific job on this quiz. Please take a minute and look at the comments, particularly on Q3. This one can really bite you if you're not careful.

-Pat

**Grade:**
Great
