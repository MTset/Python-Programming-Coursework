**Question 1:**
Which class's instances can be used to ensure that only one thread can be executing a particular piece of code at any one time?

**Your Answer:**
The Lock class's instances can be used.  e.g. lock = threading.Lock(). 

**Mentor Comments:**
none

**Question 2:**
Which queue.Queue method should you call to decrement the Queue's task counter?

**Your Answer:**
To decrement the counter, the removing thread should wait until processing is complete and then call the queue's task_done() method.

**Mentor Comments:**
none

**Question 3:**
How do you remove an item from a queue.Queue object named q?

**Your Answer:**
q.get()

**Mentor Comments:**
none

**Overall Comments:**
This is completely perfect, Mark.

-Pat

**Grade:**
Great
