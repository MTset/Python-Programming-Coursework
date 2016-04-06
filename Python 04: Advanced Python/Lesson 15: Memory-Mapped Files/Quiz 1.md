**Question 1:**
Does accessing a memory-mapped file using indexing affect the position used by the readline() method?

**Your Answer:**
Indexed access to the content of a memory mapped file leaves the file pointer unchanged for the readline() method.

**Mentor Comments:**
none

**Question 2:**
What should the first argument to the mmap.mmap() function be?

**Your Answer:**
The first argument to mmap.mmap is a file number (an internal number used to identify the file to the operating system), which is obtained by calling the file's fileno() method.

**Mentor Comments:**
none

**Question 3:**
How does mmap.mmap() achieve high-speed inter-process communication?

**Your Answer:**
By allowing the OS to optimize paging operations while using a shared memory block which is mapped to each processes address space.

**Mentor Comments:**
right, the memory mapped file is a window between processes

**Overall Comments:**
Excellent.

-Kirby

**Grade:**
Great
