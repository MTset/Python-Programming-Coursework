"""
list_vs_generate.py: Uses timeit() to show the difference between a list
comprehension and the list() function applied to creating a million random numbers.
"""

from random import random
from timeit import timeit, Timer

y = 999999
cycles = 50

def list_comprehension_rand():
    return [random() for _ in range(y)]

def list_function_rand():
    return list(random() for _ in range(y))

time1 = (timeit("list_comprehension_rand()", "from __main__ import list_comprehension_rand", number=cycles))
time2 = (timeit("list_function_rand()", "from __main__ import list_function_rand", number=cycles))

print("list comprehension - time 1:                   ", time1)
print("list function - time 2:                        ", time2)
print("difference in time 1 vs time 2  over {0} cycles: {1}".format(cycles, time2 - time1))

"""
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
"""