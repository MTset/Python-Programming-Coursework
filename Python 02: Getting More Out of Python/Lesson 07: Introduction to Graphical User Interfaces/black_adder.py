from tkinter import *

class Application(Frame):
    """ Application main window class. """
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated) """
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        """ Add all the widgets to the main frame. """
        entry_frame = Frame(self)
        self.instructions = Label(entry_frame, 
            text="Enter two numbers and press 'Add' to get their sum.")
        self.input_1_frame = LabelFrame(entry_frame, text="Input 1", labelanchor=S)
        self.input_1 = Entry(self.input_1_frame)
        self.input_2_frame = LabelFrame(entry_frame, text="Input 2", labelanchor=S)
        self.input_2 = Entry(self.input_2_frame)
        self.operation = Label(entry_frame, text=" + ")
        self.instructions.pack(pady=5)
        self.input_1.pack()
        self.input_1_frame.pack(side=LEFT)
        self.operation.pack(side=LEFT)
        self.input_2.pack()
        self.input_2_frame.pack(side=LEFT)
        entry_frame.pack()
        
        result_frame = Frame(self)
        self.result = Label(result_frame, text="Result")
        self.result.pack()
        result_frame.pack(padx=10, pady=10)
        
        command_frame = Frame(self)
        command_frame.pack(side=TOP, padx=10)
        self.QUIT = Button(command_frame, text="Quit", fg="Red", 
            command=self.quit)
        self.QUIT.pack(side=LEFT, padx=5)
        self.ADD = Button(command_frame, text="Add", fg="Blue", 
            command=self.handle_input)
        self.ADD.pack(side=LEFT, padx=5)
        
    def handle_input(self):
        """
        Validate entered value to be floating numbers or able to be converted to
        floating numbers.  If so return their sum, otherwise return an error msg.
        """
        input_values = [self.input_1.get(), self.input_2.get()]
        result = ""
        error_msg = "*** ERROR - {0} {1}***"
        for i, value in enumerate(input_values):
            if value:
                try:
                    input_values[i] = float(value)
                except ValueError:
                    result = error_msg.format('Invalid Input', i + 1)
                    break
            else:
                result = error_msg.format('Missing Input', i + 1)
                break
        if 'ERROR' not in result:
            result = sum(input_values)
        self.result.config(text=result)
        
root = Tk()
root.title("TKinter blackAdder")
root.geometry("350x120")
app = Application(master=root)
app.mainloop()