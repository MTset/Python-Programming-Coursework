**Here are your instructions:**
Write a subclass sstr of the standard str type that implements the "&lt;&lt;" and "&gt;&gt;" methods as a cyclic shifting of the characters in the string. It should pass the following tests, which you should embody as unit tests in a separate test module:
&gt;&gt;&gt; s1 = sstr("abcde")
&gt;&gt;&gt; s1 &lt;&lt; 0
'abcde'
&gt;&gt;&gt; s1 &gt;&gt; 0
'abcde'
&gt;&gt;&gt; s1 &lt;&lt; 2
'cdeab'
&gt;&gt;&gt; s1 &gt;&gt; 2
'deabc'
&gt;&gt;&gt; s1 &gt;&gt; 5
'abcde'
&gt;&gt;&gt; (s1 &gt;&gt; 5) &lt;&lt; 5 == 'abcde'
True

**Your Comment:**

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

You've done a terrific job on this. Particularly insightful to realize that you can simply return the sstr object, resulting in the most parsimonious possible solution.

-Pat

**Grade:**
Great
