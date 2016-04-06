**Question #1:**
Can a positional argument provide a value for a keyword parameter?

**Answer #1:**
Yes, e.g

def param_test1(John,Paul,Mark, **where):
    
    print('before: ', where)
    where[John] = John
    where[Paul] = Paul
    where[Mark] = Mark
    print('after: ', where)
        
param_test1('Anderson', 'McCarty', 'Tsikanovski', Anderson='New York',McCarty='London',Tsikanovski='Paris')

produces:

before: {'Tsikanovski': 'Paris', 'Anderson': 'New York', 'McCarty': 'London'}
after: {'Tsikanovski': 'Tsikanovski', 'Anderson': 'Anderson', 'McCarty': 'McCarty'}

**Comments:**

**Question #2:**
Can a keyword argument provide a value for a positional parameter?

**Answer #2:**
Yes. e.g.

def param_test1(John,Paul,Mark, **where):
    
    print('before: ', John, Paul, Mark)
    John = where[John]
    Paul = where[Paul]
    Mark = where[Mark]
    print('after: ', John, Paul, Mark)
        
param_test1('Anderson', 'McCarty', 'Tsikanovski', Anderson='New York',McCarty='London',Tsikanovski='Paris')

produces:

before: Anderson McCarty Tsikanovski
after: New York London Paris 

**Comments:**

**Question #3:**
What happens when you call a function with too many positional arguments, and the function definition doesn't have a sequence-parameter?

**Answer #3:**
You get a Type error: e.g.

def param_test1(John,Paul,Mark, **where):
    
    print('before: ', where)
    where[John] = John
    where[Paul] = Paul
    where[Mark] = Mark
    print('after: ', where)
        
param_test1('Anderson', 'McCarty', 'Tsikanovski', 'George', Anderson='New York',McCarty='London',Tsikanovski='Paris')

results in:

Traceback (most recent call last):
File "./marktest.py", line 12, in &lt;module&gt;
param_test1('Anderson', 'McCarty', 'Tsikanovski', 'George', Anderson='New York',McCarty='London',Tsikanovski='Paris')
TypeError: param_test1() takes 3 positional arguments but 4 were given 

**Comments:**

**Overall Comments:**
 Wonderful!

-Kelly

**GRADE: Great**
 You have passed this quiz.
