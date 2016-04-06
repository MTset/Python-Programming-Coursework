**Here are your instructions:**
Write a GUI-based program to build a window layout as shown below. When the frame is resized, the buttons should stay the same height and expand sideways. Frame 1 and Frame 2 should always be the same height and width as each other, and Frame 3 should be half as wide again as they are (i.e. 150% wider, as shown below).  Labeling each Frame is optional / good exercise.
+---------------------+--------------------------------+
|                     |                                |
|                     |                                |
|                     |                                |
|      Frame 1        |                                |
|                     |                                |
|                     |                                |
|                     |                                |
+---------------------+               Frame 3          |
|                     |                                |
|                     |                                |
|                     |                                |
|     Frame 2         |                                |
|                     |                                |
|                     |                                |
+----------+----------+----------+----------+----------+
| Button 1 | Button 2 | Button 3 | Button 4 | Button 5 |
+----------+----------+----------+----------+----------+

**Your Comment:**
Hi Pat,

Thanks for your comments.  In my previous project the error message produced is correct, just
obviously not well worded.  I was trying to indicate which of the inputs, which correspond to the
index, is in error as opposed to reporting the incorrect value itself.  Clearly it was not obvious to
you, so is unlikely to be obvious to others.  I'll have another look at it and fix it up.

Cheers,

Mark

**Items Handed In**
Open Project Handed In

**Overall Comments:**
Hi Mark,

Sure, you're welcome to fix it and turn it in again. I just gave it a "no pass" to lower the shields and allow you to do so. That really necessary from my perspective, but go for it!

You have done a terrific job on this assignment. Your GUI has great "curb appeal" and maintains it geometry under all conditions. All this, and blindingly colorful (keeping me awake) :-)

In case you're interested, here's how you might center a label using pack ():

label2 = Label(frame2, text="Frame 2").pack(fill=BOTH, expand=True)

And here is some advice for Project 3:

-It's actually fine to use a pack and grid manager together as long as they aren't put in control of the same widgets.  So packing a Label into a Frame that was stretched to a grid is straightforward. 

-Grids take more work in that each row and column should be configured.   You actually got self.rowconfigure(0, weight=1) twice, but because  default weight is 0,  our button row 2 stays thin and trim, as it should.

-I recommend with experimenting with a pack manager for placement of widgets in Frame3. Those widgets would be Entry and Text widgets respectively. The first should stay thin and trim across the bottom or top while the Text object should balloon to fill the rest of the frame, no real estate wasted.

For your inspection and viewing pleasure, here's an alternative solution to this objective:

from tkinter import *

ALL=W+E+N+S
class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(2,weight=1)
          
        frame_1= Frame(self, width=100,height=200, border=10, relief=RIDGE,  bg="red")
        frame_1.grid(row=0, column=0, rowspan=2,columnspan=2,sticky=ALL)
                
        frame_2= Frame(self, height=200, border=10, relief=RIDGE,  bg="blue")        
        frame_2.grid(row=2, column=0, rowspan=2,columnspan=2,sticky=ALL)
                
        frame_3= Frame(self,border=10, relief=RIDGE, bg="green")        
        frame_3.grid(row=0, column=2, rowspan=4,columnspan=3,sticky=ALL)
        
        for r in range(5):
            self.columnconfigure(r,weight=1) 
            Button(self, text="Button {0}".format(r+1)).grid(row=4, column=r, sticky=E+W)
        
        label_1 = Label(frame_1, text="FRAME 1", bg="red", fg="white" )
        label_1.pack(fill="both", expand=True)
        
        label_2 = Label(frame_2, text="FRAME 2", bg="blue",fg="white" )
        label_2.pack(fill="both", expand=True)

        label_3 = Label(frame_3, text="FRAME 3", bg="green",fg="white" )
        label_3.pack(fill="both", expand=True)

root = Tk()
app = Application(master=root)

-Pat

**Grade:**
Great
