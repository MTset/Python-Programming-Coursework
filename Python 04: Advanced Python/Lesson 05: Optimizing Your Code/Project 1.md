**Here are your instructions:**
Take the following function and using timings (and profiling if necessary to determine where the program is spending its time), reduce its execution time as much as you can.

You should be able to get it down to less than one third of what it is now.

Test both functions in the same file (the original and your faster version) to compare their respective execution times.

Also confirm that they give the same answer.

groffle.py:
""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log 
from timeit import Timer 

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

mass = 2.5 
density = 12.0 

timer = Timer("total = groffle_slow(mass, density)", 
 "from __main__ import groffle_slow, mass, density") 
print("time:", timer.timeit(number=1000)) 

**Your Comment:**
Hi Pat,

Thank you for giving me the opportunity to resubmit, with improvements.

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark --

Kirby here.

Your code here is stellar.  I see the Euler-Mascheroni solution very infrequently and maybe never as 
succinctly as in your groffle_fastest.  I'm impressed!

-Kirby

**Grade:**
Great
