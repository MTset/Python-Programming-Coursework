**Here are your instructions:**
Create a Python3_Homework07 project and assign it to your Python3_Homework working set. In the Python3_Homework07/src folder, create a program named furnishings.py that includes a Furnishing class. During instantiation, this class should ask for a "room" argument. Then, create the following classes that inherit from the Furnishing class: Sofa, Bookshelf, Bed, and Table.

Use the built-in list type to record the furniture in your own home that matches the classes above. So for example, you might have:
&gt;&gt;&gt; from furnishings import * 
&gt;&gt;&gt; home = [] 
&gt;&gt;&gt; home.append(Bed('Bedroom'))
&gt;&gt;&gt; home.append(Sofa('Living Room'))

Now, write a map_the_home() function to convert that to a built-in dict type where the rooms are the individual keys and the associated value is the list of furniture for that room. If we ran that code against what we display in our command line, we might see:
&gt;&gt;&gt; map_the_home(home)
{'Bedroom': [&lt;furnishings.Bed object at 0x39f3b0&gt;], 'Living Room': [&lt;furnishings.Sofa object at 0x39f3b0&gt;]}

Also write a counter() function that prints the types of furniture and how many there are of each type. The results, based on our example:
&gt;&gt;&gt; counter(home)
Beds: 1
Bookshelves: 0
Sofas: 1
Tables: 0

Your project should meet the following conditions:
You should include a test_furnishings.py program that tests the map_the_home() function.

Submit furnishings.py and test_furnishings.py when they are working to your satisfaction.

**Your Comment:**
Hi Pat,

Please run furnishings.py directly to see formated output.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

You put together some of the most amazing tests in the business. Not only does your main app work as advertised, but these tests prove that is unequivocally the case.

Totally awesome!

-Pat

**Grade:**
Great
