import unittest
import mysql.connector
from collections import namedtuple
from database import login_info
from classFactory_old import build_row

class DBTest(unittest.TestCase):
    
    def setUp(self):
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()
        
        self.table = "test_animal"
        self.cols = 'id name family weight'
        
        self.datarec_in = namedtuple('datarec', self.cols.split())    
        self.data = (
                (1, "Ellie", "Elephant", 2350),
                (2, "Gerald", "Gnu", 1400),
                (3, "Gerald", "Giraffe", 940),
                (4,"Leonard", "Leopard", 280),
                (5,"Sam", "Snake", 24),
                (6,"Steve", "Snake", 35),
                (7, "Zorro", "Zebra", 340)
                )
        
        self.conditions = (
                      ("WHERE name = 'Gerald'"),
                      ("WHERE family = 'Snake'"),
                      ("WHERE weight < 500"),
                      ("") # No condition
                      )
        
        #Set up test animal table
        self.cursor.execute("""DROP TABLE IF EXISTS {0}""".format(self.table))
        self.cursor.execute("""
            CREATE TABLE {0}(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50),
            family VARCHAR(50),
            weight INTEGER) ENGINE = MYISAM;
            """.format(self.table))
        
        for t in self.data:
            self.cursor.execute("""
            INSERT INTO {0} ({1})
            VALUES (%s, %s, %s, %s)""".format(self.table, ", ".join(self.cols.split())), t)
            
        self.db.commit()

        self.C = build_row(self.table, self.cols)
                
    def test_create(self):
        self.errors_encountered = False
        for i, t in enumerate(self.data):
            nt = self.datarec_in(t[0], t[1], t[2], t[3])
            self.c = self.C(list(t))
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
        for cond in self.conditions:
            # just to initialize
            self.r = self.C(('', '', '', ''))
            self.db.commit()
            expected_rows = []
            retrieved_rows = []

            # retrieve all records from DB for the given condition using
            # classFactory.retrieve method, including no condition
            for row in self.r.retrieve(self.cursor, cond):
                retrieved_rows.append(repr(row))

            # retrieve all records from DB for the given condition NOT using
            # classFactory.retrieve method, including no condition
            self.cursor.execute("""
                SELECT * FROM {0} {1} """.format(self.table, cond))
            for row in self.cursor.fetchall():
                expected_rows.append(repr(self.C(row)))
                             
            self.tests = [
                # Test that for every condition, the list of records retrieved
                # using classFactory.retrieve method is the same as directly
                # retrieving those records, including no condition.
                ("Test 3", expected_rows, retrieved_rows,
                """
                AssertionError: Test 3 for condition "{0}"
                Expected records for condition {1} 
                Observed records for condition {2}\n""".format(cond,
                                                expected_rows, retrieved_rows))
                ]
                    
            self.perform_test()
        self.assertFalse(self.errors_encountered, "AssertionErrors encountered")
        
    def perform_test(self):
        # Code below to cope with running multiple instances of the same test
        # on multiple records and not stopping after the first failure
        for test, expected, observed, msg in self.tests:
            try:
                self.assertEqual(expected, observed, msg)
            except AssertionError:
                print(msg)
                self.errors_encountered = True
                
    def tearDown(self):
        self.db.close()
     
if __name__ == "__main__":
    unittest.main()