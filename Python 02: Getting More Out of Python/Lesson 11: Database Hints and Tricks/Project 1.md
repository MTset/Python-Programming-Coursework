**Here are your instructions:**
Modify the classFactory.py source code so that the DataRow class returned by the build_row function has another method:

retrieve(self, curs, condition=None)

self is (as usual) the instance whose method is being called, curs is a database cursor on an existing database connection, and condition (if present) is a string of condition(s) which must be true of all received rows.

The retrieve method should be a generator, yielding successive rows of the result set until it is completely exhausted. Each row should be a next object of type DataRow.

**Your Comment:**

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

You have completely nailed it this time :-)  Great job. Here's a little more background:

It makes intuitive sense that a DataRow, customized by build_row to work  with a specific table, would have enough information to implement .retrieve() at the class level, meaning no need for an instance method with self as a  leftmost argument.

The project does not ask for a class level implementation primarily because  all our work with classes so far has been with methods expecting to access instance-level attributes through self.__dict__.

In Python3 we begin to explore "decorator syntax", a syntactic sugar or  shorthand that will enable both class and static methods to be defined quite simply.

@classmethod
def retrieve(cls, curs, condition=None"):

... would in that case have cls automatically set to the class and the body of retrieve would no longer refer to a self, but to cls.table instead.  There would no longer be any need to intialize a DataRow with actual row data, before  calling its retrieve method.  Class-level methods are "selfless".

Static methods are even more aloof or detached from their surrounding class in having no parameters other than those matching explicitly passed  arguments.  No implicit binding of the class or self occurs in static method calls.

These comments preview upcoming concepts so don't worry if the details still seem a bit hazy.

-Pat

**Grade:**
Great
