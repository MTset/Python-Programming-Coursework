""" 
groffle.py: Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input.

Results rounded to 12 decimal places allows a significant optimization of the
calculating algorithms for groffle_faster.
""" 

from math import log 
from timeit import Timer

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return round(total, 12)

def groffle_fast(mass, density): 
    M_D = log(mass * density)
    return round(sum([M_D/i for i in range(1, 10001)]), 12)

def groffle_faster(mass, density): 
    M_D = log(mass * density)
    SUM = sum(map(int(1).__truediv__, range(1,10001)))
    return round(M_D * SUM, 12)
    
def groffle_fastest(mass, density):
    # based on https://math.stackexchange.com/questions/496116/is-there-a-partial-sum-formula-for-the-harmonic-series
    M_D = log(mass * density)
    EULER_MASCHERONI = 0.57721566490153286060651209008240243104215933593992
    SUM = log(10000) + EULER_MASCHERONI + 1/(2 * 10000) - 1/(12 * (10000**2))
    return round(M_D * SUM, 12)

mass = 2.5
density = 12.0
passes = 5
timeit_number = 1000

if __name__ == "__main__":
    for i in range(passes):
        # make sure results stay the same
        groffle_speed1 = groffle_slow(mass, density)
        groffle_speed2 = groffle_fast(mass, density)
        groffle_speed3 = groffle_faster(mass, density)
        groffle_speed4 = groffle_fastest(mass, density)
        
        timer1 = Timer("total1 = groffle_slow(mass, density)", 
         "from __main__ import groffle_slow, mass, density")
        time1 = timer1.timeit(number=timeit_number)
        
        timer2 = Timer("total2 = groffle_fast(mass, density)", 
         "from __main__ import groffle_fast, mass, density")
        time2 = timer2.timeit(number=timeit_number)
        
        timer3 = Timer("total3 = groffle_faster(mass, density)", 
         "from __main__ import groffle_faster, mass, density")
        time3 = timer3.timeit(number=timeit_number)
        
        timer4 = Timer("total4 = groffle_fastest(mass, density)", 
         "from __main__ import groffle_fastest, mass, density")
        time4 = timer4.timeit(number=timeit_number)
        
        print("\n{0} Run {1} {2}". format(25 * "-", i + 1, 25 * "-"))
        
        if groffle_speed1 == groffle_speed2 == groffle_speed3 == groffle_speed4:
            print("All groffle speed results agree to 12 decimal places.\nIt is: ",
                  groffle_speed1, "\n")
            
            print("groffle_slow time:   ", time1, "Speed Factor: 1.00")
            print("groffle_fast time:   ", time2, "Speed Factor:", round(time1/time2, 2))
            print("groffle_faster  time:", time3, "Speed Factor:", round(time1/time3, 2))
            print("groffle_fastest time:", time4, "Speed Factor:", round(time1/time4, 2))
    
        else:
            print("groffle speed results do not agree.  They are:\n"
                  "\ngroffle_slow result:   ", groffle_speed1,
                  "\ngroffle_faster result: ", groffle_speed2,
                  "\ngroffle_fastest result:", groffle_speed3,
                  "\ngroffle_fastest result:", groffle_speed4)