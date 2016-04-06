**Question 1:**
Which techniques can be used to receive input from the command line?

**Your Answer:**
Processing the sys.argv list directly, where the [0] element is the name of the script being run followed by [1]... as the script's options.
Using optparse.OptionParser to process the sys.argv list at a higher level.

**Mentor Comments:**
none

**Question 2:**
If parser = OptionParser(), how do you add more options?

**Your Answer:**
parser.add_option(name1 ..., nameN [, **parms])

**Mentor Comments:**
none

**Question 3:**
How do you call for help using optparse?

**Your Answer:**
By using the -h or --help option.

**Mentor Comments:**
none

**Question 4:**
Does the program run normally when you call for help as in the last answer?

**Your Answer:**
By using the -h or --help option only the help text is displayed, no other code is run.

**Mentor Comments:**
none

**Question 5:**
How do you create a parser error?

**Your Answer:**
By calling parser.error("error text")

**Mentor Comments:**
none

**Overall Comments:**
Stellar performance here, Mark.

-Pat

**Grade:**
Great
