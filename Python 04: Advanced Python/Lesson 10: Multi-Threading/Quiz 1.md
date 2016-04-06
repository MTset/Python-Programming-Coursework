**Question 1:**
What happens if you make a second call to a Thread's start() method?

**Your Answer:**
You get:

raise RuntimeError("threads can only be started once")
RuntimeError: threads can only be started once

**Mentor Comments:**
none

**Question 2:**
Which function from the threading module do you use to access the current number of threads?

**Your Answer:**
threading.active_count()

**Mentor Comments:**
none

**Question 3:**
What method would you call to wait for a thread t to terminate?

**Your Answer:**
t.join()

**Mentor Comments:**
Here's a little history on the use of the term "join", as applied to multi-processing:

"... here's the etymology and the intuition behind it, which should help you remember its meaning more easily.

The idea is that execution "forks" into multiple processes of which one is the master, the rest workers (or "slaves"). When the workers are done, they "join" the master so that serial execution may be resumed.

The join method causes the master process to wait for a worker to join it. The method might better have been called "wait", since that's the actual behavior it causes in the master (and that's what it's called in POSIX, although POSIX threads call it "join" as well). The joining only occurs as an effect of the threads cooperating properly, it's not something the master does.

The names "fork" and "join" have been used with this meaning in multiprocessing since 1963."

http://stackoverflow.com/questions/25391025/what-exactly-is-python-multiprocessing-modules-join-method-doing

**Overall Comments:**
Awesome Mark. Please check out the comments.

-Pat

**Grade:**
Great
