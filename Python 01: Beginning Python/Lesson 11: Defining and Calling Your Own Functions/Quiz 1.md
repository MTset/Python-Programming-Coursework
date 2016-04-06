**Question #1:**
Write a function that returns the string "This is now lowercase:" plus the lowercase representation of its string argument, as a single string.

**Answer #1:**
def tolower(str):
    """ lower-cases a string """
    a = "This is now lowercase: " + str.lower()
    return a
    
while True:
    a = input('enter a string to be lower-cased: ')
    print(tolower(a))

**Comments:**
This works. More simply one might go:

def lower(text):
     return "This is now lowercase:" + text.lower()

**Question #2:**
Do parameters become arguments or do arguments become parameters?

**Answer #2:**
Arguments passed to a function become parameters.

**Comments:**

**Question #3:**
Can a function access variables defined outside of its body? If so, where?

**Answer #3:**
Yes, a function can access variables defined outside of it's body, as long as they are defined before the function is called.

A function can alter variables defined outside it's body, as long as they are declared as global variables within it's body.

**Comments:**
Right. Note that it doesn't matter how they entered the global namespace (could be with use of the 'global' keyword or where it's declared). This is an important point. If you declare a variable above the function at the "module level" it automatically becomes part of the global namespace. You might run this bit of code:

print('If declared at the "module level" a variable is part of the global namespace')
print('before:')
print(dir())
x =10
print('after:')
print(dir())
print()

def foo():
    print("I can print x. It's:", x)
    y = x
    print("I can use it in an expression. y is:", y)
    print("But I can't *change* it unless it's bound")

def bar():
    x+=1

foo()	
bar()

... To produce this output:

If declared at the "module level" a variable is part of the global namespace
before:
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
after:
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'x']

I can print x. It's: 10
I can use it in an expression. y is: 10
But I can't *change* it unless it's bound

Traceback (most recent call last):
... 
UnboundLocalError: local variable 'x' referenced before assignment 

**Overall Comments:**
 Hi Mark,

This is terrific. Please have a look at the comments on Q3 for some clarifications. It's absolutely critical to get the notion of variable scoping down early. If you don't you will almost certainly go insane later ;-)

-Pat

**GRADE: Great**
 You have passed this quiz.
