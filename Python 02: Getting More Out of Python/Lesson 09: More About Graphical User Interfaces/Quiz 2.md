**Question 1:**
How do you add a menu bar to a Tkinter root window?

**Your Answer:**
By instantiating the "Menu()" widget with the window as its parent, and configure it as the window's menu item. e.g.
menu = Menu(root)
root.config(menu=menu)

**Mentor Comments:**
none

**Question 2:**
How do you add a file menu to the menu bar?

**Your Answer:**
Import the necessary tkinter.filedialog items.
After instantiating the "Menu" widget as in question 1 use the "add_cascade()" with the menu bar as parent to create the pull-down menu.
Populate the menu with options using the "add_command()" method. e.g.

from tkinter import *
from tkinter.filedialog import LoadFileDialog, SaveFileDialog, Directory

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(height=75, width=75)
        # create a file menu
        menu = Menu(root)
        root.config(menu=menu)
        
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="New Directory", command=self.createdir)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
 
    def createdir(self):
        d = Directory(self)
        print(d.show())
        
    def file_open(self):
        d = LoadFileDialog(self)
        fname = d.go("nosuch.txt", "*py")
        if fname is None:
            print("Cancelled...")
        else:
            print("Open file", fname)
            
    def file_save(self):
        d = SaveFileDialog(self)
        fname = d.go("example", "*.py")
        if fname is None:
            print("Cancelled...")
        else:
            print("Saving file", fname)

root = Tk()
app = Application(master=root)
app.mainloop()

**Mentor Comments:**
filemenu = Menu(menu)

... would be sufficient here.

**Question 3:**
How do you add an "Open" command to the file menu that calls function f when the command is selected by the user?

**Your Answer:**
Using the "add_command() method as in example in question 2. e.g. filemenu.add_command(label="Open", command=self.file_open)

**Mentor Comments:**
none

**Overall Comments:**
Terrific job, Mark. Please see the comments on  Q2 for a small clarification.

-Pat

**Grade:**
Great
