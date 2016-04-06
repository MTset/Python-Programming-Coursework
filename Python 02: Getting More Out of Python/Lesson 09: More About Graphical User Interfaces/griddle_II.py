from tkinter import *
from tkinter.filedialog import LoadFileDialog, SaveFileDialog, Directory
from tkinter.messagebox import (showinfo, showwarning, showerror, askquestion,
                        askokcancel, askyesno, askyesnocancel, askretrycancel) 
import os

ALL=W+E+N+S
ROWS = 2
COLUMNS = 5
COLORS = ('red', 'blue', 'green', 'black', 'gray')
textcolor = ''

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        for r in range(ROWS):
            self.rowconfigure(r, weight=1)
            frame = LabelFrame(self, bd=2, relief=RIDGE, labelanchor='n',
                text="Frame {0}".format(r+1)
                )
            frame.grid(row=r, column=0, columnspan=2, sticky=ALL)
            frame.bind("<Button-1>", self.frame_click_handler)
                
        file_frame = LabelFrame(self, bd=2, relief=RIDGE, labelanchor='n',
                                text="Frame {0}".format(ROWS+1))
        file_frame.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)

        file_name_frame = LabelFrame(file_frame, bd=0, text="File Name")
        file_name_frame.pack(fill=X)       
        self.file_name = Entry(file_name_frame)
        self.file_name.pack(fill=X)

        file_content_frame = LabelFrame(file_frame, bd=0, text="File Content")
        file_content_frame.pack(fill=BOTH, expand=True)
        scrollbar = Scrollbar(file_content_frame)
        scrollbar.pack(side=RIGHT, fill=Y)        
        self.file_content = Text(file_content_frame, width=0, height=0,
                            wrap=WORD, yscrollcommand=scrollbar.set)
        self.file_content.pack(fill=BOTH, expand=True)
        scrollbar.config(command=self.file_content.yview)

        for c in range(COLUMNS):
            self.columnconfigure(c, weight=1)
            radiobutton = Radiobutton(self, variable=textcolor, fg='white', bg=COLORS[c],
            indicatoron=0, 
            value=COLORS[c], text=COLORS[c].replace('gray', 'open').capitalize(), 
            selectcolor=COLORS[c])
            radiobutton.grid(row=3, column=c, sticky=W+E)
            radiobutton.bind("<Button-1>", self.colorbutton_click_handler)
            
    def frame_click_handler(self, event):
        event.widget["bg"] = "magenta"
        showinfo(
        "Frame Clicked", event.widget["text"] + " clicked at coordinates:\n"
        + "x: " + str(event.x) + "  y: " + str(event.y))
        event.widget["bg"] = root["bg"]
#        print(event.widget.winfo_width(), event.widget["height"])
        explosion = PhotoImage(file="clickreport.gif")
        click_mark = Label(event.widget, image=explosion)
        click_mark.image = explosion
        click_mark.place(relx=((event.x - 2)/event.widget.winfo_width()),
                         rely=((event.y - 16)/event.widget.winfo_height()))
        
    def colorbutton_click_handler(self, event):
        self.file_content["fg"] = event.widget["value"]
        if event.widget["text"] == "Open":
            self.load_file(event.widget)
        elif event.widget["text"] == "Save":
            self.save_file(event.widget)
            
    def load_file(self, open_button):
        file = self.file_name.get()
        if file != "" and os.path.isfile(file):
            file_handle = open(file, "r")
            self.file_content.delete(1.0, END)
            self.file_content.insert(INSERT, file_handle.read())
            file_handle.close()
        else:
            print(showwarning("No File Entered/Found",
            "No File Entered or File Not Found\nPlease Select A File From the Dialog"))
            d = LoadFileDialog(self)
            file_name = d.go(file)
            if file_name is None:
                print(showwarning("No File Selected",
                                  "File Selection Cancelled by User"))
            else:
                self.file_name.insert(0, file_name)
                file_handle = open(file_name, "r")
                self.file_content.delete(1.0, END)
                self.file_content.insert(INSERT, file_handle.read())
                file_handle.close()
        if self.file_content != "":
            open_button["text"] = "Save"
            open_button["fg"] = "yellow"
            
    def save_file(self, open_button):
        file = self.file_name.get()
        if file != "" and os.path.isfile(file):
            file_handle = open(file, "w")
            file_handle.write(self.file_content.get(1.0, END))
            file_handle.close()
        else:
            print(showwarning("No File Entered/Found",
            "No File Entered or File Not Found\nPlease Select A File From the Dialog"))
            d = SaveFileDialog(self)
            file_name = d.go(file)
            if file_name is None:
                print(showwarning("No File Selected",
                                  "File Selection Cancelled by User"))
            else:
                file_handle = open(file_name, "w")
                file_handle.write(self.file_content.get(1.0, END))
                file_handle.close()

        open_button["text"] = "Open"
        open_button["fg"] = "white"
            
root = Tk()
app = Application(master=root)
app.mainloop()