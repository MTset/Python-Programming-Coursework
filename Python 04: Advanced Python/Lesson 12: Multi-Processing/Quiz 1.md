**Question 1:**
Which class in the multiprocessing library is used to model processes?

**Your Answer:**
multiprocessing.Process

**Mentor Comments:**
none

**Question 2:**
Why is it important to write multiprocessing control programs as a module with if __name__ == "__main__":?

**Your Answer:**
Because the code must now be guarded so that it isn't executed when the module is imported by the multiprocessing module.  if __name__ == "__main__": will evaluate to False.

**Mentor Comments:**
none

**Question 3:**
What two types of Queue does the multiprocessing module provide, and what is the difference between them?

**Your Answer:**
Queue and JoinableQueue. A JoinableQueue is much like Queue except it allows the consumer of items to notify the producer of those items that the items have been successfully processed using a shared semaphore and condition variable. A JoinableQue has all the methods of Queue plus a number of additional ones.

**Mentor Comments:**
none

**Overall Comments:**
Nicely done, Mark.  You've totally nailed this one :-)

-Pat

**Grade:**
Great
