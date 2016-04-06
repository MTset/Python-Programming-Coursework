**Question 1:**
What abbreviation is used for the specification of how a particular function should be called?

**Your Answer:**
API

**Mentor Comments:**
none

**Question 2:**
Write a SQL statement to determine how many rows exist in table message with a msgMessageId column value of "1234567890."

**Your Answer:**
SELECT COUNT(*) FROM message WHERE msgMessageId = "1234567890"

**Mentor Comments:**
none

**Question 3:**
How do you establish a relationship between two tables in a relational database?

**Your Answer:**
By associating indexes in in one table with the indexes in another table throught the use of FOREIGN KEY statement.  For instance consider the following two tables being created:

        self.cursor.execute("""
            CREATE TABLE test_animal(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50),
            family VARCHAR(50),
            weight INTEGER) ENGINE = MYISAM;
            """)

        self.cursor.execute("""
            CREATE TABLE test_food (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                anid INTEGER,
                feed VARCHAR(20),
                FOREIGN KEY (anid) REFERENCES test_animal(id)) ENGINE = MYISAM
            """)

We see the establishment of a relationship between the test_animal table and the test_food table with the 'anid' field in the latter table (the foreign key) referencing the 'id' field in the former table.

**Mentor Comments:**
Awesome!

**Overall Comments:**
Thanks  a lot for the code, Mark. I love the stuff :-)

-Pat

**Grade:**
Great
