"""
find_regex.py: find the start and end positions of a search string in a file
using a regex
Input: textfile file name, search string
Output: returns a tuple of start, end values
"""

import re

def locate_search_string(textfile = None, search_string = None):
    try:
        textfile = open(textfile, 'r')
        text = textfile.read()
        textfile.close()
    except:
        return "Missing or unreadable file"

    if search_string and search_string != "":
        search = re.search(search_string, text)
        if search:
            return (search.span())
    return

if __name__ == "__main__":
    string_location = locate_search_string("text_to_search.txt",
                                           "Regular Expressions")
    print(string_location)