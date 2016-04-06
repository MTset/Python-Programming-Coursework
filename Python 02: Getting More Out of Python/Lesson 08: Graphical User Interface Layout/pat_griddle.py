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


        file_name = Entry(frame_3)
        file_name.pack(fill=X)
        
        file_content = Text(frame_3)
        file_content.pack(fill=BOTH, expand=True)


root = Tk()
app = Application(master=root)
app.mainloop()