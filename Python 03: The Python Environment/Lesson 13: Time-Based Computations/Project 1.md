**Here are your instructions:**
Create a Python3_Homework13 project and assign it to your Python3_Homework working set. In the Python3_Homework13/src folder, create a program named mathquiz.py. In this program, you will create a math quiz. This quiz will ask the user five addition questions adding random integers between 1 and 10 inclusive. Each answer will be timed so you can generate the following time results:
* Time for each question
* Total time for all questions
* Average time per question

This program needs to generate random numbers using Python's random library.

Your project should meet the following conditions:

You must include a working test_mathquiz.py unittest file that tests at least one function. Each time the test runs, it must present random integers.

Your code must generate output that looks like this:
What is the sum of 6 and 6? 12
12 is right!
What is the sum of 5 and 4? 9
9 is right!
What is the sum of 4 and 2? 6
6 is right!
What is the sum of 1 and 1? 2
2 is right!
What is the sum of 9 and 2? 111
111 is wrong!
Question #1 took about 1 seconds to complete and was right.
Question #2 took about 1 seconds to complete and was right.
Question #3 took about 1 seconds to complete and was right.
Question #4 took about 2 seconds to complete and was right.
Question #5 took about 2 seconds to complete and was wrong.
You took 9 seconds to finish the quiz
Your average time was 1.8 seconds per question

Submit mathquiz.py and test_mathquiz.py when your programs are working to your satisfaction.

**Your Comment:**
Hi Pat,

Since there was nothing in the original brief about it being OO, I took an egalitarian approach to
this problem, i.e. classless code.  I have however made the testing more (hopefully acceptably)
comprehensive.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

There was no need to use any particular style here. The main thing that we are trying to teach is the importance of writing code in such a way that it can be tested - this even if the application is complicated by a user interface, a GUI, etc. The trick is to break things up enough so that the key parts of the codes are both modularized and exposed to the test suite. You've done an awesome job of implementing a completely reasonable solution.

This project suggests an architecture where the user / GUI is left to human testers while underlying business logic is tested with unittest.  Separation into Model / View / Controller is called MVC design, where Model is roughly the business logic and computational core, View is the user interface, and controller is the go-between glue that holds these two together.  Uitests may focus on M and to some extent C, whereas the user experience is emulated by human testers or "robot" software that simulates users.

Congratulations on completing this objective and, as a result, graduating from Python 3. It has  been a real pleasure to work with you again. I wish you all the best luck in Python 4, where we shall meet again.

Here's one strategy that takes the "robot" approach by essentially  hijacking the system standard input stream. (This goes well above the objective's  requirements). Following that (tough to find in the sea of code - look for this delimiter ==================) is an example using mock:

#math_quiz.py

Python 3 - Homework 13
Create a math quiz. This quiz will ask the user five addition questions adding 
random integers between 1 and 10 inclusive. Each answer will be timed so you can 
generate the following time results:
    -Time for each question 
    -Total time for all questions 
    -Average time per question
This program needs to generate random numbers using Python's random library. 
"""

from datetime import datetime
from random import Random
import logging

logging.basicConfig(filename='math-quizdebug.log',  level=logging.DEBUG)

class MathQuiz:
    """
    MathQuiz Class - Creates an entire MathQuiz using MathQuestion Objects
    Usage: First Create a MathQuiz object and then call the method apply_quiz()
           to execute the quiz. If apply_quiz was executed in a normal way, the 
           flag answered is changed to True state.
    Example:
      my_quiz = MathQuiz()
      my_quiz.apply_quiz()
    
    """
    def __init__(self):
        logging.debug("Starting MathQuiz at: {0}".format(datetime.now()))
        self.questions = [MathQuestion("Question #1"), MathQuestion("Question #2"),
                          MathQuestion("Question #3"), MathQuestion("Question #4"),
                          MathQuestion("Question #5")]
        self.answered = False
        
    def apply_quiz(self):
        """
        Execute the Math Quiz.
        """
        for question in self.questions:
            question.ask_question()
        #
        self.answered = True
        #                
        for q in self.questions:
            print("{0} took about {1} seconds to complete and was {2}.".format(
                q.qname,
                #round(q.duration.total_seconds()), q))
                round(q.total_seconds()), q))
        #
        message1 = "You took {0:.2f} seconds to finish the quiz.".format(self.quiz_total_time())
        logging.debug(message1)
        print(message1)
        #
        message2 = "Your average time was {0:.2f} seconds per question.".format(self.question_average())
        logging.debug(message2)
        print(message2)
        
    def question_average(self):
        """
        Calculate average per Question
        """
        return self.quiz_total_time() / len(self.questions)

    def quiz_total_time(self):
        """
        Calculate Quiz Total Time in Seconds
        """
        #I Think timedelta.total_seconds() is for Python 3.2 &gt;= version 
        #dt = [t.duration.total_seconds() for t in q.questions]        
        dt = [t.total_seconds() for t in q.questions]
        return sum(dt)
        

class MathQuestion:
    """
    Class MathQuestions used to create questions adding
    random integers between 1 and 10 inclusive 
    Usage: To create you MathQuestion object, you need to provide
           a name to each question you create. To execute questions
           you need to call ask_question() method. Once ask_question
           is executed in a normal way, the result flag is changed
           to True if the questions was answered correctly, the flag
           answered is changed to True because the question was executed.           
    Example: 
        q1 = MathQuestion("Question #1")
        q1.ask_question()
    """
    def __init__(self, qname):
        r = Random()
        self.a = r.randint(1,10)
        self.b = r.randint(1,10)
        self.result = False
        self.answered = False
        self.qname = qname

    def ask_question(self):
        """
        Executes a Math question
        """
        past_now = datetime.now()
        logging.debug("Executing MathQuestion {0} with {1}, {2} ".format(self.qname, self.a, self.b))
        #
        n = input("What is the sum of {0} and {1}? ".format(self.a, self.b))
        #        
        future_now = datetime.now()
        #
        self.addresult = self.a + self.b
        self.result = (int(n) == self.addresult)
        if(self.result):            
            print("{0} is right!".format(n))
        else:            
            print("{0} is wrong!".format(n))
        #
        self.answered = True
        self.duration = future_now - past_now        
        
        logging.debug("duration: %s ,add_result: %d, result: %s, input: %s" % (
                        self.duration, self.addresult, self.result, n))
        return self.duration, self.result
    
    
    def total_seconds(self):
        """
        Calculate total seconds from Time duration.
        """
        timedelta = self.duration
        return (timedelta.microseconds + (timedelta.seconds + timedelta.days * 24 * 3600) * 10**6) / 10**6

    def __str__(self):
        """
        The String represents the MathQuestion State
        """      
        if self.answered:
            if self.result:
                return "Right"
            else:
                return "Wrong"
        else:
            return "Not answered"

    def __repr__(self):
        return "MathQuestion(title={0}, a={1}, b={2}, result={3}, answered={4})".format(\
                self.qname, self.a, self.b, self.result, self.answered)

if __name__ == '__main__':
    try:
        q = MathQuiz()
        q.apply_quiz()
    except ValueError as err:
        logging.debug(err)

===
#test_math_quiz.py

"""
Created on 31/05/2014

MathQuiz Test Module
"""

import sys
import unittest
from math_quiz import MathQuestion
from math_quiz import MathQuiz

class TestMathQuiz(unittest.TestCase):
    
    def testMathQuiz(self):
        """
        Test MathQuiz - read inputs from mquiz-input.txt
        in order to test MathQuiz inputs.
        """
        math_quiz = MathQuiz()
        #Prepare Input
        backstdin = sys.stdin
        filein = open('mquiz-input.txt', 'r')
        sys.stdin = filein
        
        # Verify Invalid Input
        self.assertRaises(ValueError, math_quiz.apply_quiz) #Wrong Input
        self.assertRaises(ValueError, math_quiz.apply_quiz) #Blank Input
        
        #After Wrong Input answered state still in false.
        self.assertFalse(math_quiz.answered)
        
        #Release Resources and Restore Input
        filein.close()
        sys.stdin = backstdin
        
    def testMathQuestion(self):
        """
        Test MathQuestion - Read inputs from mquestion-input.txt
        in order to test MathQuestion inputs
        """
        q1 = MathQuestion("Question #1")
        q1.a = 10
        q1.b = 20
        #Prepare Input
        backstdin = sys.stdin
        filein = open('mquestion-input.txt', 'r')
        sys.stdin = filein

        #Test Sum Operation with the right answer
        q1.ask_question()
        self.assertEqual(30, q1.addresult)
        self.assertTrue(q1.answered)
        
        #Test Sum Operation with the wrong answer
        q1.ask_question()
        self.assertFalse(q1.result)
            
        #Verify Invalid Input
        self.assertRaises(ValueError, q1.ask_question) #Wrong Input
        self.assertRaises(ValueError, q1.ask_question) #Blank Input
        
        #Release Resources and Restore Input
        filein.close()
        sys.stdin = backstdin
        

if __name__ == '__main__':
    unittest.main()

 ==================) 

Here is an alternative solution using the Python mock library. It is beyond the scope of this class, but well worth a look. You can read all about it here:

https://docs.python.org/3/library/unittest.mock-examples.html

##mathquiz.py

of the bottom
import random
import datetime

def get_time_calcs(times):
    total_time = 0
    for t in times:
        total_time += t[0]
    avg_time = total_time / len(times)
    return total_time, avg_time

def get_numbers():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def get_user_input(num1, num2):
    return int(input("What is the sum of {} and {}: \n".format(num1, num2)))

def quiz():

    times = []
    for _ in range(5):
        num1, num2 = get_numbers()
        before = datetime.datetime.now()
        answer = get_user_input(num1, num2)
        answer_was = "right" if num1 + num2 == answer else "wrong"
        print("{} is {}".format(answer, answer_was))
        after = datetime.datetime.now()
        diff = after - before
        times.append((diff.seconds, answer_was))
    
    total_time, avg_time = get_time_calcs(times)
    return times, total_time, avg_time
 

def do_quiz():
    times, total_time, avg_time = quiz()
    for i, (t, a) in enumerate(times):
        print("Question #{} took about {} seconds to complete and was {}".format(i + 1, t, a))
    print (times)
    
    print("You took {} seconds to finish the quiz".format(total_time))
    print("Your average time was {} seconds per quiz".format(avg_time))
    
if __name__ == "__main__":
    do_quiz()

########### test_mathquiz.py ##############

import unittest
import time
#import mathquiz.get_numbers
from mathquiz import get_time_calcs, quiz
from unittest.mock import patch

def mocked_get_user_input(a, b):
    time.sleep(1)
    return 8

class Test(unittest.TestCase):

    def test_get_time_calcs(self):
        times = [(1.12, 'wrong'), (5.1, 'wrong'), (2.4, 'right'), (1.0, 'right'), (6.9, "right")]
        expected_total = 16.52
        expected_avg = 3.304
        result = get_time_calcs(times)
        self.assertEqual(result[0], expected_total)
        self.assertEqual(result[1], expected_avg)
    

    @patch("mathquiz.get_user_input")
    @patch('mathquiz.get_numbers')
    def test_quiz_right_answers(self, get_numbers, get_user_input):
        get_numbers.return_value = (3, 5)
        get_user_input.side_effect = mocked_get_user_input
        times, total_time, avg_time = quiz()
        self.assertEqual(times, [(1, 'right'), (1, 'right'), (1, 'right'), (1, 'right'), (1, 'right')])
        self.assertEqual(total_time, 5)
        self.assertEqual(avg_time, 1)
        

    @patch("mathquiz.get_user_input")
    @patch('mathquiz.get_numbers')
    def test_quiz_wrong_answers(self, get_numbers, get_user_input):
        get_numbers.return_value = (4, 5)
        get_user_input.side_effect = mocked_get_user_input
        times, total_time, avg_time = quiz()
        self.assertEqual(times, [(1, 'wrong'), (1, 'wrong'), (1, 'wrong'), (1, 'wrong'), (1, 'wrong')])
        self.assertEqual(total_time, 5)
        self.assertEqual(avg_time, 1)
        
if __name__ == "__main__":
    unittest.main()

-Pat

**Grade:**
Great
