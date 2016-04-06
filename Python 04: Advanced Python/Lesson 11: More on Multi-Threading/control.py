"""
control.py: Creates queues, starts output and worker threads,
and pushes inputs into the input queue
"""

from queue import Queue
from output import OutThread
from worker import WorkerThread
import random
import time

start_time = time.clock()

WORKERS = 10

inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS *1.5))

ot = OutThread(WORKERS, outq, start_time)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq, start_time)
    w.start()

# Input string is lower-case so the worker threads still 'do' something.  
instring = "".join([chr(random.sample(range(97,123), 1)[0]) for _ in range(1000)])
for work in enumerate(instring):
    inq.put(work)
    
for i in range(WORKERS):
    inq.put(None)
    
inq.join()
end_time = time.clock()
print("Control thread terminating after {0} milliseconds".format(
                                                round(end_time - start_time, 3)))