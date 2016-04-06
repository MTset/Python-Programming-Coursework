**Question 1:**
What are the three commonly held fundamental concepts of object-oriented programming?

**Your Answer:**
Encapsulation
Inheritance
Polymorphism

**Mentor Comments:**
none

**Question 2:**
What is inheritance?

**Your Answer:**
The ability of a subclass (child) to inherit all the attributes, i.e. data and methods of the super (parent) class, allowing for their reuse and for the creation of a hierarchical relationship structure of classes.

**Mentor Comments:**
Yes, subclasses enjoy a heritage, a treasure chest of capabilities thanks to ancestor classes.  Inheritance is the ability of subclasses to just assume ancestral wealth.

**Question 3:**
Encapsulation is the idea that the only way to access or change the data inside an object is by calling its methods; what is Python's take on it?

**Your Answer:**
In Python, by default all attributes and methods of a class are public, meaning they are all accesible an can be changed directly.  Attribute and method names which start with a double underscore are considered private, though they too can be accessed directly, if required.

**Mentor Comments:**
Right.  You probably need to have tasted Java or C++ to sense the other end of the spectrum where  controlling access to the guts of objects is a primary focus of the compiler.  Keywords like private and public and friend start to pop up next to every new method and variable.  Python stays crisp in part by only invoking such syntax if really required, with a default of not needing.

Smalltalk is another one with no concept of directly setting internal states. It's all done through method calls only.

**Question 4:**
What is the method resolution order for class Puppy(Dog, Young, Untrained)? 

**Your Answer:**
The lookup order for an attribute or method in this case is impossible to determine with certainty, but assuming going from most specialized to least specialized class and biasing left-to-right it would be:
Puppy -&gt; Dog -&gt; Young -&gt; Untrained -&gt; Object.

**Mentor Comments:**
none

**Overall Comments:**
This is awesome, Mark.

-Pat

**Grade:**
Great
