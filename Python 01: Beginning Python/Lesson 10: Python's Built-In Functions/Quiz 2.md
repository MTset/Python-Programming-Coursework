**Question #1:**
How do you:

check if all elements in a list, set, or tuple evaluate to true?
return the methods and attributes associated with the value 'Python'?
return all of the global variables?
examine the documentation of an object?

**Answer #1:**
1. Using the all() function. e.g.
&gt;&gt;&gt; lst = [0,1,2,3,4]
&gt;&gt;&gt; all(lst)
False 

Using the dir() function. e.g.
dir('Python')

3. Using the globals() function. e.g.
globals()

4. Using the help() function. e.g.
help(open)

**Comments:**
You can actually extract the global variables in lots of forms - you might examine the differences on the type of object and content produced by the following (interactive play is always encouraged):

&gt;&gt;&gt; globals()
{'__name__': '__main__', '__doc__': None, 'lst': [1, 2, 3], '__builtins__': &lt;module 'builtins' (built-in)&gt;, 'st': {1, 2, 3}, '__package__': None, '__spec__': None, 'r': range(0, 5), '__loader__': &lt;class '_frozen_importlib.BuiltinImporter'&gt;, 'd': {'a': 1, 'b': 2}}
&gt;&gt;&gt; list(globals())
['__name__', '__doc__', 'lst', '__builtins__', 'st', '__package__', '__spec__', 'r', '__loader__', 'd']
&gt;&gt;&gt; list(globals().items())
[('__name__', '__main__'), ('__doc__', None), ('lst', [1, 2, 3]), ('__builtins__', &lt;module 'builtins' (built-in)&gt;), ('st', {1, 2, 3}), ('__package__', None), ('__spec__', None), ('r', range(0, 5)), ('__loader__', &lt;class '_frozen_importlib.BuiltinImporter'&gt;), ('d', {'a': 1, 'b': 2})]
&gt;&gt;&gt; 

Example of using all():

if all([ s.isupper(), s.endswith(".")]):
    print("Your sentence meets the requirements")

... and any():

if any(not s.endswith("."), not s.isupper()):
print("Your input does not meet criteria")

**Overall Comments:**
 Hi Mark,

Great work here. Please review the comments for little bit of additional background.

-Pat

**GRADE: Great**
 You have passed this quiz.
