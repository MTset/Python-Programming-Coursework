**Question 1:**
What is a good way to manage data and its custom behaviors across multiple programs?

**Your Answer:**
A good way to manage data and its custom behaviors while keeping it portable is by converting it into to a structured object e.g. a bunch class.
Mentor Comments:
Right. And more generally objects to store data and behaviors.

**Question 2:**
What is a bunch class?

**Your Answer:**
A bunch class is a structured object that saves data as attributes together with custom behaviors acting on the data as methods.  The attributes are stored dynamically using the __dict__ attribute's update() method. e.g.

class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

**Mentor Comments:**
none

**Question 3:**
Should you include a test for code inside the main program, and why or why not?

**Your Answer:**
Usually it is better to put the test code into a separate test module, allowing for greater clarity and simpliciy of the core module and the test modules.  This also helps if the core module is refactored and stops the needless import of the unittest module every time the core module is run.
Mentor Comments:
A module might have a small self-diagnostic / dependency checker that's distinct from the full back office testing suite that's used to develop the module.  I.e. there's a kind of testing that's useful to the end user who is not trying to develop the module, just see if it reports being happy with its new home and able to do its work.

**Overall Comments:**

**Grade:**
Great
