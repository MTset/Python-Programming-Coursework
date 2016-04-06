"""
This function serializes, stores and returns player's high scores.

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

import os
import shelve
score_error = 'Invalid Score'
player_error = 'Invalid Player'

def high_score(player=None, score=0):
    pathname = "."
    filename = "high_scores.shlf"
    all_high_scores = {}
    high_score_shelf = shelve.open(os.path.join(pathname, filename))
    if type(player) is str and player != str():
        if type(score) is int and score >= -1:
            if  score >= 0:
                if player in high_score_shelf:
                    high_score_shelf[player] = max(high_score_shelf[player],
                                                   score)
                else:
                    high_score_shelf[player] = score
            elif player in high_score_shelf:
                del high_score_shelf[player]
                return player + ' Deleted'
            else:
                return player_error
        else:
            return score_error
        return high_score_shelf[player]
    else:
        for key in high_score_shelf:
            all_high_scores[key] = high_score_shelf[key]
        return all_high_scores
    high_score_shelf.close()

if __name__ == '__main__':
    returned_high_score = high_score("")
    print(returned_high_score)