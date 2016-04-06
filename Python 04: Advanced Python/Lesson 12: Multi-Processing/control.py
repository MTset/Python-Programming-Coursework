"""                                  
control.py: Creates queues, starts output and worker processes,
        and pushes inputs into the input queue.
"""                                 
from multiprocessing import Queue, JoinableQueue    
from output import OutProcess
from worker import WorkerProcess
import random
import time

start_time = time.clock()

if __name__ == '__main__':
    WORKERS = 10                    
    
    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))                  
    
    ot = OutProcess(WORKERS, outq, start_time, sorting=True)              
    ot.start()                              
    
    for i in range(WORKERS):                
        w = WorkerProcess(inq, outq, start_time)            
        w.start()                            
    instring = "".join([chr(random.sample(range(97,123), 1)[0]) for _ in range(1000)])
    # feed the process pool with work units    
    for work in enumerate(instring):        
        inq.put(work)                        
    # terminate the process pool              
    for i in range(WORKERS):                
        inq.put(None)                        
    inq.join()                             
    end_time = time.clock()
    print("Control process terminating after {0} milliseconds".format(
                                                round(end_time - start_time, 3)))