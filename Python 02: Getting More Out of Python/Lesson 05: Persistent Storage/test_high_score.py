"""
Test module for the function high_score.

Input to high_score:
    Player Name (str) [, Player's current score (int <= 0)]
Output from high_score:
    If a valid player name is input and the player does not exist on the DB they
    will be added. If a valid current score is also input it will become the
    high score and is returned.  If no current score is input, the current score
    will be 0.  It will become the high score and it will be returned. If an
    invalid current score is input an error message is returned.
    
    If a valid player name is input and the player exists on the DB and no
    current score is provided the previous stored high score will be returned.
    If a valid current high score is provided the higher of the previous high
    score and the current score will become the new high score and will be
    returned
    
    If a valid player name is input and the player exists on the DB and a
    current score of -1 is provided, the player is deleted from the DB.  A
    confirmation message is returned.  If the player does not exist on the DB an
    error message is returned.

    If no valid player name is input or the input is None, a dict all players
    with their respective high scores is returned.
"""

import unittest
import os
import tempfile
import shutil
import high_score

class TestHighScore(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp("testdir")
        self.curdir = os.getcwd()
        os.chdir(self.tempdir)
        
    def test_high_score(self):
        test_name_score_expected = [
        # Ensure new player with no score returns High-Score of 0
        ("test 1", "Alice", int(), 0),
        # Ensure new player with invalid score returns error message
        ("test 2", "White Rabbit", -5, "Invalid Score"),
        # Ensure new player with a score returns High-Score of score
        ("test 3", "Mad Hatter", 5, 5),
        # Ensure existing player with no score returns previous High-Score
        ("test 4", "Mad Hatter", int(), 5),
        # Ensure existing player with invalid score returns error message
        ("test 5", "Mad Hatter", "10/6", "Invalid Score"),
        # Ensure existing player with lower score returns previous High-Score
        ("test 6", "Mad Hatter", 2, 5),
        # Ensure existing player with higher score returns new High-Score
        ("test 7", "Alice", 10, 10),
        # Ensure no input or no valid player name, no matter the score, returns
        # dict of all High-Scores keyed by player.
        ("test 8", str(), int(), {"Alice": 10, "Mad Hatter": 5}),
        ("test 9", 10, 20, {"Alice": 10, "Mad Hatter": 5}),
        ("test 10", 10, "Alice", {"Alice": 10, "Mad Hatter": 5}),
        # Ensure existing player can be deleted with a score of -1
        # Also cleans up the DB, thus resetting the tests
        ("test 11", "Alice", -1, "Alice Deleted"),
        ("test 12", "Mad Hatter", -1, "Mad Hatter Deleted"),
        # Ensure only a valid existing player can be deleted with a score of -1
        # Double checks results of test above.
        ("test 13", "Alice", -1, "Invalid Player"),
        ("test 14", str(), int(), {})
        ]
        
        for test, name, score, expected in test_name_score_expected:
            observed = high_score.high_score(name, score)
            self.assertEqual(expected, observed, "Expected: " + str(expected) +
                                                 " - Observed: " + str(observed)
                                                 + " in " + test)

    def tearDown(self):
        os.chdir(self.curdir)
        shutil.rmtree(self.tempdir)
        
if __name__ == '__main__':
    unittest.main()