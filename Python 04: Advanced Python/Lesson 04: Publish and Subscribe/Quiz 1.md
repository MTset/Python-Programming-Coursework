**Question 1:**
What is the primary purpose of the publish-and-subscribe mechanism?

**Your Answer:**
To "loosen the coupling" between the producers and consumers of data, allowing each to be written in a general way, pretty much independent of each other. 

**Mentor Comments:**
none

**Question 2:**
What does the Publisher object do if an already-registered object tries to register a new subscription?

**Your Answer:**
Raises a ValueError, indicating that multiple subscriptions are not allowed.

**Mentor Comments:**
none

**Question 3:**
Why is it better to allow the registration of arbitrary methods?

**Your Answer:**
In order to allow for fewer constraints on the nature of subscribers.   Publishers acn then call the subscribers directly rather than calling a method of the subscriber. This makes it possible to subscribe functions to the Publisher.

**Mentor Comments:**
none

**Overall Comments:**
Perfect, Mark.

-Pat

**Grade:**
Great
