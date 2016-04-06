"""
mathquiz.py: tests your speed at adding the squares of two random numbers between 1 and 10 
"""
import random
import time

def validate_input(answer):
    if answer.isdigit() and int(answer) != 0:
        return True
    return

def validate_answer(answer, a, b):
    sum_of_squares = a**2 + b**2
    if int(answer) == sum_of_squares:
        return "right"
    else:
        return "wrong"
    
def get_randint():
    return random.randint(1, 10)

def mathquiz():
    answer_count = []
    answer_right = 0
    total_time = 0
    while len(answer_count) < 5:
        a = get_randint()
        b = get_randint()
        answer_start = time.time()
        answer = input("What is the sum of the squares of {0} and {1}? ".format(a, b))
        answer_stop = time.time()
        # don't include invalid input in results, just move on
        if validate_input(answer):
            answer_time = answer_stop - answer_start
            total_time += answer_time
            answer_count.append((answer_time, validate_answer(answer, a, b)))
            print("{0} is {1}!".format(answer, answer_count[len(answer_count) - 1][1]))
        else:
            print("The answer must be a valid natural number")
    # output results        
    print()
    for i, answer in enumerate(answer_count):
        print("Question #{0} took {1} seconds to complete and was {2}".format(i+1, round(answer[0],1), answer[1]))
        if answer[1] ==  "right":
            answer_right += 1
        
    print("\nYou took {0} seconds to finish the quiz.".format(round(total_time, 1)))
    print("Your average time was {0} seconds per question.".format(round(total_time/5, 1)))
    print("You answers were {0}% correct.".format((answer_right*100)/5))
    
if __name__ == "__main__":
    mathquiz()
    
    