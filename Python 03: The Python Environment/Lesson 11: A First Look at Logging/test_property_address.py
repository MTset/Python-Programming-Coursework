import re
"""
test_property_address.py: tests the property_address.py module.
"""
import unittest
from property_address import *
 
class TestAddresses(unittest.TestCase):
   
    def setUp(self): 
        self.home = Address( name='Steve Holden', street_address='5114 Ritchie Rd',
                              city='Bealeton', state='VA', zip_code='22712' )

    def test_1_name_regex(self):
        """
        Check that the regex used to check names copes with a variety of 
        unicode character sets and excludes basics like numbers and underscores.
        """
        names = [("Björn", True),
                 ("Anne-Charlotte", True),
                 ("توماس", True),
                 ("毛", True),
                 ("מיק", True),
                 ("-Björn", False),
                 ("Anne--Charlotte", False),
                 ("Tom_", False),
                 ("THX-1138", False),
                 ("O(+>", False)]
        regex = re.compile(r"^[^\W\d_]+([ \-'‧][^\W\d_]+)*?\Z")
        for name in names:
            expected = name[1]
            observed = regex.match(name[0]) is not None
            self.assertEqual(expected, observed)

    def test_2_city_name_regex(self):
        """
        Check that the regex used to check city names copes with a variety of 
        unicode character sets.
        """
        names = [("Toronto", True),
                 ("San Fransisco", True),
                 ("Val-d'Or", True),
                 ("Val_d'Or", False),
                 ("Presqu'ile", True),
                 ("Niagara on the Lake", True),
                 ("Niagara-on-the-Lake", True),
                 ("München", True),
                 ("toronto", True),
                 ("toRonTo", True),
                 ("villes du Québec", True),
                 ("Provence-Alpes-Côte d'Azur", True),
                 ("Île-de-France", True),
                 ("Kópavogur", True),
                 ("Garðabær", True),
                 ("Sauðárkrókur", True),
                 ("Þorlákshöfn", True),
                 ("Néewiller-près-lauterbourg", True),
                 ("Wellington_", False),
                 ("San-", False),
                 ("New Y@rk", False),
                 ("De11hi", False)]
        regex = re.compile(r"^([a-zA-Z\u0080-\u024F]{1}[a-zA-Z\u0080-\u024F\. |\-| |']*[a-zA-Z\u0080-\u024F\.']{1})$")
        for name in names:
            expected = name[1]
            observed = regex.match(name[0]) is not None
            self.assertEqual(expected, observed)

    def test_3_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden')
        # check that the name cannot be reset
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')

    def test_4_street_address(self): 
        self.assertEqual(self.home.street_address, '5114 Ritchie Rd')
        # check that it must be a real world address
        self.assertRaises(ValidationError, setattr, self.home, 'street_address', '5115 Ritchie Rd')
        self.home.street_address = '5114 Ritchie Rd'

    def test_5_city(self): 
        self.assertEqual(self.home.city, 'Bealeton') 
        self.assertRaises(ValidationError, setattr, self.home, 'city', 'Washing_Ton')  
        self.home.city = 'Arlington' 

    def test_6_state(self): 
        self.assertEqual(self.home.state, 'VA') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')
        # check that it is a real state code
        self.assertRaises(StateError, setattr, self.home, 'state', 'XY')  
        self.home.state = 'CO' 

    def test_7_zip_code(self): 
        self.assertEqual(self.home.zip_code, '22712') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '123456')   
        self.home.zip_code = '54321' 
        self.assertEqual(self.home.zip_code, '54321')
        # check zipcode + 4 format
        self.home.zip_code = '54321-6789' 
        self.assertEqual(self.home.zip_code, '54321-6789')
        
        stop_logging()

if __name__ == "__main__": 
    start_logging(level="info")
    unittest.main()