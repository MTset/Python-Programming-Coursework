"""
test_furnishings.py: tests the furnishings.py module
"""

import unittest
import gc
from furnishings import *

class TestFurnishings(unittest.TestCase):
    # create the Home object
    def setUp(self):
        self.home = Home()
        self.home.add_furnishing(Bed('Bedroom'))
        self.home.add_furnishing(Table('Bedroom'))
        self.home.add_furnishing(Chair('Bedroom'))
        self.home.add_furnishing(Chair('Bedroom'))
        self.home.add_furnishing(Bookshelf('Bedroom'))
        self.home.add_furnishing(Table('Dining Room'))
        self.home.add_furnishing(Chair('Dining Room'))
        self.home.add_furnishing(Chair('Dining Room'))
        self.home.add_furnishing(Chair('Dining Room'))
        self.home.add_furnishing(Chair('Dining Room'))
        self.home.add_furnishing(Chair('Dining Room'))
        self.home.add_furnishing(Chair('Dining Room'))
        self.home.add_furnishing(Sofa('Living Room'))
        self.home.add_furnishing(Sofa('Living Room'))
        self.home.add_furnishing(Bookshelf('Living Room'))
        self.home.add_furnishing(Bookshelf('Living Room'))

    def test_1_furnishing_with_no_room(self):
        """
        Test that if no room or an empty string is given, a TypeError is raised
        with the appropriate message.
        """
        with self.assertRaises(TypeError) as cm:
            self.home.add_furnishing(Bed())
        self.assertEqual(repr(cm.exception), "TypeError('Invalid or no room given',)")
        
        with self.assertRaises(TypeError) as cm:
            self.home.add_furnishing(Bed(""))
        self.assertEqual(repr(cm.exception), "TypeError('Invalid or no room given',)")
        
    def test_2_add_furnishings(self):
        """
        Test that the various furnishings added at setUp to various rooms
        have actually been created as instances of Furnishings, with the correct
        (room) attribute.
        """
        expected = [
        ('Bed', 'Bedroom'),
        ('Table', 'Bedroom'),
        ('Chair', 'Bedroom'),
        ('Chair', 'Bedroom'),
        ('Bookshelf', 'Bedroom'),
        ('Table', 'Dining Room'),
        ('Chair', 'Dining Room'),
        ('Chair', 'Dining Room'),
        ('Chair', 'Dining Room'),
        ('Chair', 'Dining Room'),
        ('Chair', 'Dining Room'),
        ('Chair', 'Dining Room'),
        ('Sofa', 'Living Room'),
        ('Sofa', 'Living Room'),
        ('Bookshelf', 'Living Room'),
        ('Bookshelf', 'Living Room')
        ]
        observed = []
        for instance in gc.get_objects():
            if isinstance(instance, Furnishings):
                observed.append((instance.__class__.__name__, instance.room))
        self.assertEqual(expected, observed, "home_add_furnishings failed")
        
    def test_3_map_the_home(self):
        """
        Test that the list of added furnishings been converted to a dict,
        where rooms are the keys of the main dict and the values are sub-dicts
        where the furnishing is key and the value is the number of that type
        of furnishing in that room - so you can have two sofas in the Living Room.
        """
        expected = {'Living Room': {'Bookshelf': 2, 'Sofa': 2},
                    'Bedroom': {'Bookshelf': 1, 'Table': 1, 'Chair': 2, 'Bed': 1},
                    'Dining Room': {'Table': 1, 'Chair': 6}}
        observed = self.home.map_the_home()
        self.assertEqual(expected, observed, "map_the_home failed")
    
    def test_4_furnishings_count(self):
        """
        Test that the total number of furnishings in the home is correct.
        Double check that map_the_home counts match the totals from furnishings_count
        """
        expected1 = {'Bed': 1, 'Table': 2, 'Chair': 8, 'Sofa': 2, 'Bookshelf': 3}
        observed = self.home.furnishings_count()
        self.assertEqual(expected1, observed, "furnishings_count failed")
        
        furnishings_by_room = self.home.map_the_home()
        expected2 = {}
        for room in furnishings_by_room:
            for furnishing in furnishings_by_room[room]:
                if furnishing in expected2:
                    expected2[furnishing] += furnishings_by_room[room][furnishing]
                else:
                    expected2[furnishing] = furnishings_by_room[room][furnishing]
        self.assertEqual(expected2, observed, "map_the_home counts do not match\
        furnishings_count")
    
if __name__ == "__main__":
    unittest.main()