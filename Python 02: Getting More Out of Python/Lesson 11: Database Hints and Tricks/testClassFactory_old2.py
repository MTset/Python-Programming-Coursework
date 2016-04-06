import unittest
import mysql.connector
from collections import namedtuple
from database import login_info
from classFactory_old2 import build_row

class DBTest(unittest.TestCase):
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    
    table = "test_animal"
    
    #Set up test animal table
    cursor.execute("""DROP TABLE IF EXISTS {0}""".format(table))
    cursor.execute("""
        CREATE TABLE {0}(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50),
        family VARCHAR(50),
        weight INTEGER) ENGINE = MYISAM;
        """.format(table))

    datarec_in = namedtuple('datarec', ['name', 'family', 'weight'])    
    data = (
            ("Ellie", "Elephant", 2350),
            ("Gerald", "Gnu", 1400),
            ("Gerald", "Giraffe", 940),
            ("Leonard", "Leopard", 280),
            ("Sam", "Snake", 24),
            ("Steve", "Snake", 35),
            ("Zorro", "Zebra", 340)
            )
    
    conditions = (
                  ("WHERE", "name", "= 'Gerald'"),
                  ("WHERE", "family", "= 'Snake'"),
                  ("WHERE", "weight", " <500")
                  )

    def setUp(self):
        self.C = build_row(self.cursor, self.table)
        self.db.commit()
                
    def test_create(self):
        self.errors_encountered = False
        for i, t in enumerate(self.data):
            nt = self.datarec_in(t[0], t[1], t[2])
            self.c = self.C(list(t))
            self.db.commit()
            self.tests = [
                # Test individual instance attributes are correctly set when
                # adding a record to the DB table.  Successful addition of the
                # record indicated by the return of the id which is an auto-increment
                # field.
                ("Test 1", [i+1, nt.name, nt.family, nt.weight],
                [self.c.id, self.c.name, self.c.family, self.c.weight],
                """
                AssertionError: Test 1
                Expected id: {0}, name: {1}, family: {2}, weight: {3}
                Observed id: {4}, name: {5}, family: {6}, weight: {7}\n
                """.format(i+1, nt.name, nt.family, nt.weight, self.c.id, self.c.name,
                           self.c.family, self.c.weight)),

                # Test that the representation of the instance before writing
                # to the DB table is as expected.
                ("Test 2", "test_animal_record({0}, '{1}', '{2}', {3})".
                 format(i+1, nt.name, nt.family, nt.weight), repr(self.c),
                """
                AssertionError: Test 2
                Expected record representation: test_animal_record({0}, '{1}', '{2}', {3})
                Observed record representation: {4}\n""".format(i+1, nt.name,
                                                        nt.family, nt.weight, repr(self.c)))
                ]
            
            self.perform_test()
        self.assertFalse(self.errors_encountered, "AssertionErrors encountered")
        
    def test_retrieve(self):
        self.errors_encountered = False
        for i, c in enumerate(self.conditions):
            self.c = self.C()
            datarec_out = self.c.retrieve(' '.join(c))
            self.db.commit()
            in_data = []
            in_retrieved = []
                 
            for j, d in enumerate(self.data):
                nt = self.datarec_in(d[0], d[1], d[2])
                if eval("nt." + c[1] + c[2].replace('=', '==')):
                    in_data.append((nt.name, nt.family, nt.weight))  
                             
            while True:
                try:
                    next(datarec_out)
                except StopIteration:
                    break
                in_retrieved.append((self.c.name, self.c.family, self.c.weight))
            
            self.tests = [
                # Test that for every condition, the list of records retrieved
                # from the DB is the same as the list of records in initial
                # 'data' when subject to the same condition
                ("Test 3", in_data, in_retrieved,
                """
                AssertionError: Test 3 for condition {0}
                Expected added data records for condition {1} 
                Observed retrieved  records for condition {2}'\n""".format(' '.join(c),
                                                        in_data, in_retrieved))
                ]
                    
            self.perform_test()
        self.assertFalse(self.errors_encountered, "AssertionErrors encountered")
        
    def perform_test(self):
        # Code below to cope with running multiple instances of the same test
        # and not stopping after the first failure
        for test, expected, observed, msg in self.tests:
            try:
                self.assertEqual(expected, observed, msg)
            except AssertionError:
                print(msg)
                self.errors_encountered = True
     
if __name__ == "__main__":
    unittest.main()