"""
Test groffle module
"""
import unittest
from groffle import *

class TestAddargs(unittest.TestCase):
        
        def test_result_equality(self):
            groffle_speed1 = groffle_slow(mass, density)
            groffle_speed2 = groffle_fast(mass, density)
            groffle_speed3 = groffle_faster(mass, density)
            groffle_speed4 = groffle_fastest(mass, density)
            
            # Speeds returned accurate to 12 decimal places
            self.assertEqual(groffle_speed1, groffle_speed2)
            self.assertEqual(groffle_speed2, groffle_speed3)
            self.assertEqual(groffle_speed3, groffle_speed4)
            
        def test_optimization(self):
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
            
            # Assert time2 at least x2 faster than time 1
            self.assertNotAlmostEqual(time1 * 2, time1/time2, 2)
            # Assert time3 at least x4 faster than time 1
            self.assertNotAlmostEqual(time1 * 4, time1/time3, 2)
            # Assert time4 at least x2000 faster than time 1
            self.assertNotAlmostEqual(time1 * 2000, time1/time4, 2)
            
            
if __name__ == "__main__":
    unittest.main()            