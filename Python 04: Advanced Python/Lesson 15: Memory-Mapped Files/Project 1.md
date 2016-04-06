**Here are your instructions:**
Write a program that creates a ten-megabyte data file in two different ways, and time each method. The first technique should create a memory-mapped file and write the data by setting one chunk at a time using successively higher indexes. The second technique should create an empty binary file and repeatedly use the write() method to write a chunk of data. Show how the timings vary with the size of the chunk.

**Your Comment:**
Hi Kirby,

I've amended the results displayed to be more
informative (I think) with per chunk timings for each size, rather than just totals.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Very nice.

Remember when you have a standard thing that happens every time:

        for _ in range(loops):
            chunk = chunk_size * b"*"  # &lt;----
            f.write(chunk)

you might speed things up by removing it from the loop

        chunk = chunk_size * b"*"
        for _ in range(loops):
            f.write(chunk)

Minor, but memorable.  Good work.

-Kirby

**Grade:**
Great
