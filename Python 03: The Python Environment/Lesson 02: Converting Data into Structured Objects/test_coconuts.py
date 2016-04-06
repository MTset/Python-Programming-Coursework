"""
Test coconuts inventory module

N.B. 
"""
from coconuts import *
import unittest

class TestCoconutsInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        
    def test_1_add_coconut(self):
        """
        Test adding of coconuts.  Add 2 South Asian
        """
        south_asian = South_Asian()
        self.inventory.add_coconut(south_asian, 2)
        expected = {'INVENTORIED COCONUTS': {'South_Asian_3': 2},
                     'TOTAL NUMBER OF NUTS': 2, 'TOTAL NUT WEIGHT': 6}
        observed = self.inventory.display_inventory()
        self.assertEqual(expected, observed, "Error: Cannot add a coconut")

    def test_2_remove_coconut(self):
        """
        Test deleting of coconuts.  Add 5 and delete 4 Middle Eastern, leaving 1
        Test that you cannot remove more coconuts of a type than there are.
        Remove 10 of 2 South Asian, leaving 0
        """
        middle_eastern = Middle_Eastern()
        self.inventory.add_coconut(middle_eastern, 5)
        self.inventory.remove_coconut(middle_eastern, 4)
        south_asian = South_Asian()
        self.inventory.remove_coconut(south_asian, 10)
        expected = {'INVENTORIED COCONUTS': {'South_Asian_3': 0, 'Middle_Eastern_2.5': 1},
                     'TOTAL NUMBER OF NUTS': 1, 'TOTAL NUT WEIGHT': 2.5}
        observed = self.inventory.display_inventory()
        self.assertEqual(expected, observed, "Error: Cannot remove a coconut")
        
    def test_3_add_not_coconut(self):
        """
        Test you cannot add a non coconut object e.g. str
        """
        self.assertIsNone(self.inventory.add_coconut('middle_eastern', 5), "Error: \
        Non-Coconut Object Added")
        
    def test_4_remove_not_coconut(self):
        """
        Test you cannot remove a non coconut object e.g. another class object
        """
        class Peanut(object):
            weight = 1
        peanut = Peanut()
        self.assertIsNone(self.inventory.add_coconut(peanut, 5), "Error: \
        Non-Coconut Object Removed")
        
    def test_5_coconut_totals(self):
        """
        Double check that returned total weight and count are correct:
        Initialize coconut_counts then add 2 South Asian, 1 Middle Eastern,
        and 3 American coconuts.  Total count = 6, Total Weight = 19
        """
        self.inventory.coconut_counts = {}
        south_asian = South_Asian()
        self.inventory.add_coconut(south_asian, 2)
        middle_eastern = Middle_Eastern()
        self.inventory.add_coconut(middle_eastern, 1)
        american = American()
        self.inventory.add_coconut(american, 3)
        observed = self.inventory.display_inventory()
        self.assertEqual(observed["TOTAL NUMBER OF NUTS"], 6, "Error: \
        Total Number of Nuts in Inventory not correct")
        self.assertEqual(observed["TOTAL NUT WEIGHT"], 19, "Error: \
        Total Nut Weight in Inventory not correct")
        
    def test_6_unique_weights(self):
        """
        Test that each coconut has a unique weight
        """
        coconut_types = Coconut.__subclasses__()
        coconut_weights = set()
        for coconut_type in coconut_types:
            coconut_weights.add(coconut_type.weight)
        self.assertEqual(len(coconut_types), len(coconut_weights), "Error: \
        Coconut weights are not unique")
        
if __name__ == "__main__":
    unittest.main()