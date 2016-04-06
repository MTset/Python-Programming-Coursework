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
from timeit import timeit

FILENAME = "bin_tempfile"
POWER = 24
FILESIZE = 2**POWER # 16MB
# Chunk sizes double each time
CHUNK_SIZES = [2**i for i in range(POWER)]
non_mmap_write_timings = []
mmap_write_timings = []

def mmap_write(chunk_size):
    with open(FILENAME, "w+b") as f:
        mapf = mmap.mmap(f.fileno(), FILESIZE, access=mmap.ACCESS_WRITE, offset=0)
        offset = 0
        loops = int(FILESIZE/chunk_size)
        chunk = chunk_size * b"*"
        for _ in range(loops):
            mapf[offset:offset+chunk_size] = chunk
            offset += chunk_size
    
def non_mmap_write(chunk_size):
    with open(FILENAME, "w+b") as f:
        loops = int(FILESIZE/chunk_size)
        chunk = chunk_size * b"*"
        for _ in range(loops):
            f.write(chunk)

if __name__ == "__main__":
    for chunk_size in CHUNK_SIZES:
        non_mmap_write_timings.append(timeit("non_mmap_write({})".
            format(chunk_size), "from __main__ import non_mmap_write", number =1))
        mmap_write_timings.append(timeit("mmap_write({})".
            format(chunk_size), "from __main__ import mmap_write", number =1))

    os.unlink(FILENAME) # cleanup
    for i, j, k in zip(CHUNK_SIZES, mmap_write_timings, non_mmap_write_timings):
        chunks = FILESIZE/i
        print("Chunk(B): {0:7}{1}wrt/chnk time: {2:10}  mmap wrt/chnk time: {3:10}  ratio [1:{4:6}]"
            .format(i, 2*" ", round(k/chunks, 8), round(j/chunks, 8), round(k/j, 2)))