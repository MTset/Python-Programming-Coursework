**Objective:**
This project builds on the previous one.

Copy your final.py file to a file named final2.py, then modify final2.py to print a histogram of the word lengths. A histogram is a chart with columns whose heights correspond to the data they represent.

Below is an example of possible output from running the updated program with the declaration.txt file:

 
 Length    Count
       1       16
       2      267
       3      267
       4      169
       5      140
       6      112
       7       99
       8       68
       9       61
      10       56
      11       35
      12       13
      13        9
      14        7
      15        2

  400 -|                                             
       |                                             
       |                                             
       |                                             
       |                                             
  300 -|                                             
       |                                             
       |   ******                                    
       |   ******                                    
       |   ******                                    
  200 -|   ******                                    
       |   ******                                    
       |   *********                                 
       |   ************                              
       |   ************                              
  100 -|   ***************                           
       |   ******************                        
       |   ************************                  
       |   ***************************               
       |   ******************************            
    0 -+-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
       | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
Hints for Program Design: You don't need to be quite as sophisticated as the standard solution in your scaling and labeling, but you should consider how to handle inputs where the counts are smaller (e.g. in the 5-50 range). The real trick is working out what should be printed in each column for every row—it would be much easier to print the histogram sideways (meaning that's not an acceptable alternative). Because our vertical (y-axis) scale is in increments of 20, we don't see representations of word lengths of fewer occurrences than 20 (the 12- through 15-character words).

**Here are the files you handed in:**
python1Homework/clear_screen.py

**Overall Comments:**
 Congratulations on completing Python 1!! Good luck in Python 2 and have fun!!

-Kelly

**GRADE: Great**
 You have passed this objective.
