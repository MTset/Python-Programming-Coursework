**Here are your instructions:**
Write a function (not a class) that takes two arguments, a string player name and an integer score, and keeps a "high score" table in a Python shelve. If the integer argument is higher than the given player's current high score (or if the player has no recorded high score), log the value as this player's new high score. The function should return the player's current high score. Remember, a function is not the same thing as a class and it's a function that's needed.

Again, write a separate test module that verifies the operation of the function.

**Your Comment:**

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

As to this project, you've done a really good job coming up with comprehensive tests and a clever way to delete players.

This being said, your tests look more difficult than necessary to write and easy to make mistakes with.  If you cast them in this form:

def test_somthing(self):
    name, score, exp = ("Bree", 50, 50)
    observed = high_score(name, score)
    self.assertEqual(observed, exp, 
                     "I'm looking for: " + str(exp) + 
                     " but got:  " + str(observed))

... you're automatically populating the test and the error message with the data.  Not so important for one test but what about the second?

In this format, it's easy to recycle code:

def test_somthing_else(self):
    name, score, exp = ("Bree", 40, 50)
    #recycled code
    self.assertEqual(observed, exp, 
                     "I'm looking for: " + str(exp) + 
                     " but got:  " + str(observed)) 

.... and it's not too tough to extend it to run any number of tests with very little typing/debugging:

def test_a_bunch(self):
    name_score_exp = [('Bree', 50, 50),  #new score
                      ('Bree', 60, 60),  #higher score
                      ('Bree', -10, 60), #lower score
                      ('Fred', 0, 0)    #new score for new player
                      ]
    
    for name, score, exp in name_score_exp:
        self.assertEqual(observed, exp, 
                         "I'm looking for: " + str(exp) + 
                         " but got:  " + str(observed)) 

Also, whenever you are writing the file it is best practice to create a temporary directory. You want to ensure that your app and its tests are not in any way dependent upon the filesystem and you also want to ensure that you do not leave a bunch of carnage behind in your wake.

Overall, however, this is a very awesome project.

-Pat

**Grade:**
Great
