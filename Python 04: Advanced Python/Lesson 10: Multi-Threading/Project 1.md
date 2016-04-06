**Here are your instructions:**
Write a program that determines whether changing the current directory using os.chdir in one thread changes the current directory for:
a thread that is created after the call to os.chdir.

State your conclusions, based on experiment, in your comments.

**Your Comment:**
Hi Pat,

According to my results, os.chdir() is not thread-safe. A change of directory in any thread affects
the process, and thus all the threads running in that process.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Your research is spot-on. The way the threading module works is that there is a single instance of the Python interpreter, shared by all the threads. Behind the scenes, the interpreter is locked while working on any specific thread. When the lock is released, the interpreter goes on to the next task.

When you use multiprocessing, you don't run into this issue because each process has its own and runs in its own sandbox. This is important to keep in mind if you value your sanity :-)

-Pat

**Grade:**
Great
