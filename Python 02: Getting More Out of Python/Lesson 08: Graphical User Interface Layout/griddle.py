from tkinter import *
import random

ALL = N+S+E+W
RANGE = 2
R = range(255)
G = range(255)
B = range(255)

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        for r in range(RANGE):
            self.random_bg()
            self.rowconfigure(r, weight=1)
            frame = Label(self, bd=1, relief=RIDGE, fg="white",
                text="Color #{0:02X}{1:02X}{2:02X}".format(self.r, self.g, self.b),
                bg="#{0:02X}{1:02X}{2:02X}".format(self.r, self.g, self.b)
                ).grid(row=r, column=0, columnspan=2, sticky=ALL)
                
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=3, column=c,
            sticky=W+E)
        self.random_bg()
        frame = Label(self, bd=1, relief=RIDGE, fg="white",
                text="Color #{0:02X}{1:02X}{2:02X}".format(self.r, self.g, self.b),
                bg="#{0:02X}{1:02X}{2:02X}".format(self.r, self.g, self.b)
            ).grid(row=0, column=2,
            rowspan=2, columnspan=3, sticky=ALL)
            
    def random_bg(self):
        self.r = random.choice(R)
        self.g = random.choice(G)
        self.b = random.choice(B)        
        
root = Tk()
app = Application(master=root)
app.mainloop()