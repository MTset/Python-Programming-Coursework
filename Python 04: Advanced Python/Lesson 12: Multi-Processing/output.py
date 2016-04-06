"""
output.py: The output proces for the miniature framework.
"""
identity = lambda x: x

import multiprocessing
import sys
import time

class OutProcess(multiprocessing.Process):
    def __init__(self, N, q, start_time, sorting=False, *args, **kw):
        """ Initialize thread and save queue references. """
        multiprocessing.Process.__init__(self, *args, **kw)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
        self.start_time = start_time
        
    def run(self):
        """ Extract items from output queue and print until all done. """
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # This is the real output packet
                self.output.append(p)
        print(len(self.output))
        end_time = time.clock()
        print("Output process terminating after {0} milliseconds".format(
                                                round(end_time - self.start_time, 3)))
        sys.stdout.flush()