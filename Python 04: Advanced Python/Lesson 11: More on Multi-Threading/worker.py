"""
worker.py: a sample worker thread that receives input though one queue and
routes output through another.
"""
from threading import Thread
import time

class WorkerThread(Thread):
    def __init__(self, iq, oq, start_time, *args, **kw):
        """ Initialize thread and save Queue references. """
        Thread.__init__(self, *args, **kw)
        self.iq, self.oq = iq, oq
        self.start_time = start_time
        
    def run(self):
        while True:
            work = self.iq.get()
            if work is None:
                self.oq.put(None)
                end_time = time.clock()
                print("Worker {0} done after {1} milliseconds".format(self.name,
                                     round(end_time - self.start_time, 3)))
                self.iq.task_done()
                break
            i, c = work
            result = (i, self.process(c)) # this is the "work"
            self.oq.put(result)
            self.iq.task_done()
            
    def process(self, s):
        """ This defines how the string is processed to produce a result. """
        return s.upper()