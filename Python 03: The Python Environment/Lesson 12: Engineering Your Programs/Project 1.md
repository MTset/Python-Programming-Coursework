**Here are your instructions:**
Create a Python3_Homework12 project and assign it to your Python3_Homework working set. In the Python3_Homework12/src folder, copy property_address.py and test_property_address.py from the last project. Modify property_address.py to accept the following options if called directly, with the five address values used to instantiate an Address class if no parser errors are thrown.

option

default

address?

task

-l/--level INFO yes Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL 
-n/--name Throws a parser error if empty yes Sets the name value of the Address object 
-a/--address Throws a parser error if empty yes Sets the street_address value of the Address object 
-c/--city Throws a parser error if empty yes Sets the city value of the Address object 
-s/--state Throws a parser error if empty yes Sets the state value of the Address object 
-z/--zip_code Throws a parser error if empty yes Sets the zip_code value of the Address object 

If you run your code with the following command-line arguments:

property_address.py -n Tom -a "my street" -c "San Diego" -s "CA" -z 21045

...you should see something like this in property_address.log:
2010-10-11 14:48:59,794 - INFO - __init__ - Creating a new address
Note: When you use the ${string_prompt} or direct input option in the Eclipse run configuration, you can't use single quotes ('). If your input requires quotes, use double quotes ("), so the full string is parsed rather than breaking at white space. If you run your code without command-line arguments, you should see:
Usage: property_address.py [options]
    
property_address.py: error: options -n, -a, -c, -s, -z are required

If you run your code with the following command-line arguments:
property_address.py -l WARNING -n Tom -a "my street" -c "San Diego" -s "CA" -z "EZ 123"
...you should see:
usage: property_address.py [options]

property_address.py: error: option -z requires a valid 5-digit US zip code
...AND you should see something like this in property_address.log:
2010-10-11 17:10:32,702 - ERROR - ZipCodeError - ZIPCODE exception
Note: Your date and time values will vary.

Now, modify your propertyaddress.py program to use the configparser library to load the settings from the following property_address.cfg config file:
[log]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
output = homework12.log

[validators]
zip_code = \d{5}\-\d{4}$
state = [A-Z]{3}$
As you can see, the log formatting, log output, and Address validators are different from what you currently have.

Your project must meet the following conditions:

The tests in test_property_address.py must run correctly. Also, the results of your logfile should appear as below:
2010-10-11 17:34:38,968 - root - ERROR - STATE exception
2010-10-11 17:34:39,098 - root - ERROR - ZIPCODE exception
2010-10-11 17:34:39,112 - root - INFO - Creating a new address
2010-10-11 17:34:39,113 - root - ERROR - NAME exception
2010-10-11 17:34:39,113 - root - INFO - Creating a new address
2010-10-11 17:34:39,113 - root - INFO - Creating a new address 
Note: Your date and time values will vary.

Submit property_address.py, test_property_address.py, and property_address.cfg when they are working to your satisfaction.

**Your Comment:**
none

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Your question about the best IDE to use treads on nearly theological ground. Personally, I use Wing IDE because of its power and simplicity. Others swear by PyCharm with ferocious loyalty. Truth be known, they compare more than they contrast and both are great products. I would encourage you to at least try out Wing - you can download a fully functional version and try it for a month for free; alternatively, you can get the student version and use it forever:

[]()https://wingware.com/

That being said, most professional shops use some sort of hard-core, and multipurpose IDE like Eclipse (Wing and PyCharm are Python-only). That is part of the motivation for including Eclipse in these courses - to give you a feel of working with them.

Great work on this project, by the way.

-Pat

**Grade:**
Great
