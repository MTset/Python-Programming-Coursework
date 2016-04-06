import unittest
import mysql.connector
from database import login_info
from classFactory import build_row

class DBTest(unittest.TestCase):
    
    def setUp(self):
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()
        
        self.table = "test_animal"
        self.cols = 'id name family weight'

        self.data = (
                ("Ellie", "Elephant", 2350),
                ("Gerald", "Gnu", 1400),
                ("Gerald", "Giraffe", 940),
                ("Leonard", "Leopard", 280),
                ("Sam", "Snake", 24),
                ("Steve", "Snake", 35),
                ("Zorro", "Zebra", 340)
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
            VALUES (%s, %s, %s)""".format(self.table, ", ".join(self.cols.split()[1:])), t)

        # check that the table is created and with all the right columns            
        self.cursor.execute("""
        SELECT column_name FROM information_schema.columns 
        WHERE table_name='{0}'""".format(self.table))
        fetched_cols = self.cursor.fetchall()
        cols = [(col,) for col in self.cols.split()]
        assert(fetched_cols == cols)
            
        self.db.commit()

        self.C = build_row(self.table, self.cols)
                       
    def test_retrieve(self):
        self.errors_encountered = False
        for cond in self.conditions:
            # just to initialize
            self.r = self.C(('999', 'Moby', 'Whale', '1000000'))
            self.db.commit()
            expected_rows = set()
            retrieved_rows = set()

            # retrieve all records from DB for the given condition using
            # classFactory.retrieve method, including no condition
            for row in self.r.retrieve(self.cursor, cond):
                retrieved_rows.add(repr(row))

            # retrieve all records from DB for the given condition NOT using
            # classFactory.retrieve method, including no condition
            self.cursor.execute("""
                SELECT * FROM {0} {1} """.format(self.table, cond))
            for row in self.cursor.fetchall():
                expected_rows.add(repr(self.C(row)))
                             
            self.tests = [
                # Test that for every condition, the list of records retrieved
                # using classFactory.retrieve method is the same as directly
                # retrieving those records, including no condition.
                ("Test 1", expected_rows, retrieved_rows,
                """
                AssertionError: Test 1 for condition "{0}"
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