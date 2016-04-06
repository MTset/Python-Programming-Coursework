"""                                  
worker.py: a sample worker process that receives input
       through one queue and routes output through another.         
"""    
                 
from multiprocessing import Process
import sys
import time
    
class WorkerProcess(Process):
    def __init__(self, iq, oq, start_time, *args, **kw):
        """Initialize process and save Queue references."""
        Process.__init__(self, *args, **kw)        
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
        sys.stdout.flush()                          
    def process(self, s):
        """This defines how the string is processed to produce a result."""      
        return s.upper()