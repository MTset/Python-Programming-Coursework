**Here are your instructions:**
Write a program that uses timeit() to show the difference between a list comprehension and the list() function applied to:
a generator that generates a sequence of a million random numbers. 

**Your Comment:**
no comment given

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Excellent work here, dude. But I'm getting used to that :-)

Generator expressions forced to the end are not faster than list comprehensions with the same fate. Why generators speed up the code is lists tend to be used to store data before it's needed and then the program may take a turn where that data is discarded, unused.  A generator, on the other hand, is more controlled about when it produces and therefore helps programmers avoid the wastefulness of list-based computing.

In brick and mortar world we have what's called "just in time" inventory management which is the opposite of stockpiling and is instead just having what you need to get through the next  day or two -- order in small amounts and in direct response to customer demand.  In programming terms, this philosophy / strategy has become a part of Agile.

FYI, here's a solution that I think is pretty clean in terms of extricating much of the code into module-level functions:

===

from random import random
from timeit import Timer

j = 1000000

# list comprehension example

def a():
  return [random() for i in range(j)]

# list function applied to a generator

def b():
  return list(random() for i in range(j))

t = Timer("time = a()", "from __main__ import a")
 
v = Timer("time = b()", "from __main__ import b")

# printing results

print ("List comprehension example: ")
print (t.timeit(number=10))

print ("List function applied to a generator: ")
print (v.timeit(number=10))

===

-Pat

**Grade:**
Great
