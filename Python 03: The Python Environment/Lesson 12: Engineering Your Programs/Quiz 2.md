**Question 1:**
What is the name of Python's configuration file library?

**Your Answer:**
configparser

**Mentor Comments:**
none

**Question 2:**
What are some advantages that the INI format has over XML or JSON?

**Your Answer:**
simplicity
speed
human and machine readability
wide acceptance across most platforms

**Mentor Comments:**
It's not either / or:  all there formats serve their own purposes.

What's important is not "which is the best for all purposes" but "which best suits my needs for this particular situation?"

As R0ml, prominent thinker in open source community, was saying at OSCON:  if you have the source code why do you need configuration files, just change the source.

In a way he's right in that one of the source code files may serve to collect common settings and defaults in some area, just as a .cfg file might do.

Using a settings.py for one's application is another popular option.

**Question 3:**
How do you comment out a line of an INI file?

**Your Answer:**
By using # at the beginning of the line.

**Mentor Comments:**
For configuration files only, you can use the semicolon character, as well.

**Question 4:**
What extension should you use for your setting files? What extensions should you not use?

**Your Answer:**
GOOD: .ini, .cfg, cnf, conf, config
BAD: any file extension used for executables, e.g, .py, exe, .bat, .run

**Mentor Comments:**
Great answer.

**Overall Comments:**
This is awesome, Mark..

-Pat

**Grade:**
Great
