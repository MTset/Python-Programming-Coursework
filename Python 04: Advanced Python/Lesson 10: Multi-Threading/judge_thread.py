"""
judge_thread.py: determine whether changing the current directory using
os.chdir in one thread changes the current directory for:

    * a thread that already existed before the call to os.chdir. - Thread-1
    * a thread that is created after the call to os.chdir. - Thread-3
"""
import threading
import os
import time
change = "BEFORE"

class ThreadBare(threading.Thread):
    def run(self):
        global change
        if self.name == "Thread-2":
            os.chdir("..")
            change = "AFTER"
            print('{0} performed os.chdir("..")'.format(self.name))
            
        for _ in range(2):
            print("I am {0} in process {1} in directory {2} {3} dir change".format
                  (self.name, os.getpid(), os.getcwd(), change))
            time.sleep(3)
        
for i in range(3):
    ThreadBare().start()