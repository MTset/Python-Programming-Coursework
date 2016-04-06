**Question 1:**
Can a class inherit its parent's properties?

**Your Answer:**
Yes.  e.g. defining teacher as in the lesson.
Adding: class StudentTeacher(Teacher):
            pass

After creating t: an instance of Teacher and t2: an instance of StudentTeacher, dir() produces identical results:
dir(t)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age', '_classes', '_first_name', '_grade', '_last_name', 'age', 'classes', 'first_name', 'grade', 'grades', 'last_name']
dir(t2)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age', '_classes', '_first_name', '_grade', '_last_name', 'age', 'classes', 'first_name', 'grade', 'grades', 'last_name']

**Mentor Comments:**
"""
Little Experiment with properties inheritance
"""

class Polygon:
    """
    Polygon Class with sides properties
    """
    def __init__(self):
        self._sides = 3
        
    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, value):
        if value &lt; 3:
            raise AttributeError("Cannot Create Polygon with less 3 Sides")
        self._sides = value

class Triangle(Polygon):
    """
    Triangle Class: Inherit's side propertie
    """
    
    def __init__(self):
        super().__init__()        

if __name__ == '__main__':
    p = Polygon()
    t = Triangle()
    #t.sides = 1 --&gt; this will raise an AttributeError
    #                implemented in parent's class

**Question 2:**
Name a disadvantage to using properties.

**Your Answer:**
A small amount of coding extra work up front.
Possible processing overhead if more lightweight methods, e.g. special methods would have done.

**Mentor Comments:**
none

**Question 3:**
What exception should you raise when some code tries to set a read-only property?

**Your Answer:**
AttributeError

**Mentor Comments:**
none

**Overall Comments:**
This is perfect, Mark.

-Pat

**Grade:**
Great
