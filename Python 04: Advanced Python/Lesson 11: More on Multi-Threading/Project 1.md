**Here are your instructions:**
Modify the control module from the final example of the lesson so that, instead of asking the user for input, it generates a random string of alphabetic characters of length one thousand. Similarly modify the output routine to print only the length of the final string. Test the time it takes the program to run. Make sure the workers report when done by printing to console.

**Your Comment:**

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Great work on this one.

This is a design pattern, similar to pub & sub.  Queues are being used inter-thread  in that each worker is getting a next object from the input queue and putting it to the output queue, with the output thread waiting for the worker count to reach 0 before ending its run.

The main takeaway from this and the next project is that multi-thread and mutli-process programming have a lot in common, API-wise (deliberately).  Then I invite you to pick up both in self study, perhaps using Python Cookbook 3rd Edition.

-Pat

**Grade:**
Great
