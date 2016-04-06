"""
Verify that every animal in the 'animal' table eats at least one food in the
'food' table.
"""

import mysql.connector
from database import login_info
import unittest

class FileTest(unittest.TestCase):
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    
    def setUp(self):
        #Set up test animal table
        self.cursor.execute("""DROP TABLE IF EXISTS test_animal""")
        self.cursor.execute("""
            CREATE TABLE test_animal(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50),
            family VARCHAR(50),
            weight INTEGER) ENGINE = MYISAM;
            """)
            
        data = (
                ("Ellie", "Elephant", 2350),
                ("Gerald", "Gnu", 1400),
                ("Gerald", "Giraffe", 940),
                ("Leonard", "Leopard", 280),
                ("Sam", "Snake", 24),
                ("Steve", "Snake", 35),
                ("Zorro", "Zebra", 340),
#                ('Hagar', 'Hippo', 2001),
#                ('Henry', 'Hyena', 189),
#                ('Ethel', 'Aardvaark', 50)
                )

        for t in data:
            self.cursor.execute("""
            INSERT INTO test_animal (name, family, weight)
            VALUES (%s, %s, %s)""", t)

        #Set up test food table
        self.cursor.execute("""DROP TABLE IF EXISTS test_food""")
        self.cursor.execute("""
            CREATE TABLE test_food (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                anid INTEGER,
                feed VARCHAR(20),
                FOREIGN KEY (anid) REFERENCES test_animal(id)) ENGINE = MYISAM
            """)
        
        data = [('Ellie', 'Elephant', ['hay', 'peanuts']),
                ('Gerald', 'Gnu', ['leaves', 'shoots']),
                ('Gerald', 'Giraffe', ['hay', 'grass']),
                ('Leonard', 'Leopard', ['meat']),
                ('Sam', 'Snake', ['mice', 'meat']),
                ('Steve', 'Snake', ['mice', 'meat']),
                ('Zorro', 'Zebra', ['grass', 'leaves']),
#                ('Peaches', 'Pig', ['human remains', 'slop'])
                ]
        
        for name, family, foods in data:
            self.cursor.execute("SELECT id FROM test_animal WHERE name=%s and family=%s",
                           (name, family))
            try:
                id = self.cursor.fetchone()[0]
                for food in foods:
                    self.cursor.execute("""INSERT INTO test_food (anid, feed)
                                VALUES (%s, %s)""", (id, food))
            except TypeError:
                print("Trying to add food for {0} the {1}, but it has escaped!".format(name, family))
            
        self.db.commit()        
        
    def test1_not_hungry(self):
        "Verify that no animal goes hungry"
        self.cursor.execute("""SELECT family FROM test_animal
                            WHERE id NOT IN (SELECT anid FROM test_food)""")
        hungry_animals = [id[0] for id in self.cursor.fetchall()]
        self.db.commit()
        self.assertEqual(hungry_animals, [],
                        "Animal(s) with no food for them found: {0}".format(
                        hungry_animals))
    """        
    def test2_hungry(self):
        "Verify that if we add an animal but not it's food, it's reported"
        # Add an animal
        added_animals = [('Hagar', 'Hippo', 2001),
                         ('Henry', 'Hyena', 189),
                         ('Ethel', 'Aardvaark', 50)]
        added_animal_ids = []
        for t in added_animals:
            self.cursor.execute('''
            INSERT INTO test_animal (name, family, weight)
            VALUES (%s, %s, %s)''', t)
            # Get id of just added animal
            self.cursor.execute('''SELECT LAST_INSERT_ID()''')
            added_animal_ids.append(self.cursor.fetchone()[0])
        
        self.cursor.execute('''SELECT id, family FROM test_animal
                            WHERE id NOT IN (SELECT anid FROM test_food)''')
        hungry_animals_ids = []
        hungry_animals =[]
        for id in self.cursor.fetchall():
            hungry_animals_ids.append(id[0])
            hungry_animals.append(id[1])
             
        self.db.commit()
        self.assertEqual(hungry_animals_ids, added_animal_ids,
                        "Animal(s) with no food for them found: {0}".format(
                        hungry_animals))
    """
        
    def tearDown(self):
        # Delete test tables
        self.cursor.execute("""DROP TABLE IF EXISTS test_animal, test_food""")
        self.db.commit()
        
if __name__ == "__main__":
    unittest.main()


