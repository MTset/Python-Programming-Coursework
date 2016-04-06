"""
A program that creates a sixteen-megabyte data file in two different ways, and
times each method.

The first technique creates a memory-mapped file and writes the data by setting
one chunk at a time using successively higher indexes.

The second technique creates an empty binary file and repeatedly uses the write()
method to write a chunk of data.

Finally it shows how the timings vary with the size of the chunk.

NB: file size chosen as a power of 2 (in this case to produce a file over 
ten-megabyte) to allow for a simple chunk size progression (avoiding fractions
and rounding) from 1 byte to half the desired file size.  Conveniently, the sum
of all the chunks in this progression equal the file size - 1. 
"""
import os
import mmap
from time import clock

FILENAME = "bin_tempfile"
POWER = 24
FILESIZE = 2**POWER # 16MB
# Chunk sizes double each time
CHUNK_SIZES = [2**i for i in range(POWER)]
non_mmap_write_timings = []
mmap_write_timings = []

def mmap_write():
    with open(FILENAME, "w+b") as f:
        mapf = mmap.mmap(f.fileno(), FILESIZE, access=mmap.ACCESS_WRITE, offset=0)
        offset = 0
        for chunk_size in CHUNK_SIZES:
            chunk = chunk_size * b"*"
            # time only the write of the chunk in CPU seconds
            time_start = clock()
            mapf[offset:offset+chunk_size] = chunk
            mapf.flush() # significantly improves performance
            time_stop = clock()
            offset += chunk_size
            mmap_write_timings.append(time_stop - time_start)
    
def non_mmap_write():
    with open(FILENAME, "w+b") as f:
        for chunk_size in CHUNK_SIZES:
            chunk = chunk_size * b"*"
            # time only the write of the chunk in CPU seconds
            time_start = clock()
            f.write(chunk)
            time_stop = clock()
            non_mmap_write_timings.append(time_stop - time_start)

if __name__ == "__main__":
    mmap_write()
    print("    mmap file of {0} bytes created".format(os.path.getsize("bin_tempfile")))
    non_mmap_write()
    print("Non-mmap file of {0} bytes created".format(os.path.getsize("bin_tempfile")))
    print()
    os.unlink(FILENAME) # cleanup
    for i, j, k in zip(CHUNK_SIZES, mmap_write_timings, non_mmap_write_timings):
        print("Chunk Size: {0:10}{1}write():mmap write ratio [1:{2:10}]".format(
                                                        i, 4*" ", round(k/j, 4)))