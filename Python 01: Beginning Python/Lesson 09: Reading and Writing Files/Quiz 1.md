**Question #1:**
How do you make a file available to your program?
What do you do when you are finished working with the file?

**Answer #1:**
1. You open the file using the open() function for reading and/or writing and /or appending. e.g.
f = open('newfile.txt', a')

2. You close the file using the close() function e.g.
f.close

OR

If the file was opened using the with open() statement you exit the with block.

**Comments:**
That's right. The second approach is technically called a "context manager". When the context goes away, everything within it is promptly garbage collected and you don't have a need to do the close () operation. This is particularly useful while debugging when you're app is always crashing.

Here are some choices (most not covered in the Lesson):

ex. f = open("file.txt" "mode")

"mode" needs to be one of these:

Modes	Description
r	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
rb	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
r+	Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
rb+	Opens a file for both reading and writing in binary format. The file pointer will be at the beginning of the file.
w	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
wb	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
w+	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
wb+	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
a	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
ab	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
ab+	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

**Question #2:**
What methods can be used to:

report if a file object is readable?
report if a file object is writable?
return a list of the lines in a file?

**Answer #2:**
1. Using the readable() function. e.g.
f.readable()

2. Using the writable() function. e.g
f.writable()

3. Using the readlines() function. e.g.
open_tasks = open('open_tasks.txt','r').readlines()

**Comments:**

**Overall Comments:**
 Hi Mark,

Terrific work here. Please check out the comments on Q1 for a recitation of additional options for opening a file.

-Pat

**GRADE: Great**
 You have passed this quiz.
