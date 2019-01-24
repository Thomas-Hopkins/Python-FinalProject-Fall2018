"""
Created on May 3, 2018

@author: Thomas Hopkins and Rania Jameel
"""
from tkinter import *
from tkinter import messagebox
from math import sqrt


class Calculator(Frame):
    """A regular calculator"""
    def __init__(self):
        rowlist = (["C", "+/-", "<-"], ["STO", "RCL", "x"+u"\u00B2", u"\u221A"+"x"],
                   ["7", "8", "9", "/"], ["4", "5", "6", "*"], ["1", "2", "3", "-"], ["0", ".", "+"], ["="])
        
        # Setup the window frame (Title, grid, etc)
        Frame.__init__(self)
        self.option_add('*Font', 'arial 14 bold')
        self.pack(expand=YES, fill=BOTH)
        self.memory = StringVar()
        self.display = StringVar()
        
        Entry(self, relief=RIDGE, textvariable=self.display, justify='right', bd=30, bg='#dce3e5')\
            .pack(side=TOP, expand=YES, fill=BOTH)
                
        for btns in rowlist:  # Go through each button row
            frame= self.row(self, TOP)  # make a frame for the row
            for char in btns:  # Go through each button in the row and make a button and get it's command
                self.button(frame, LEFT, char, self.getcommand(char, self.display, self.memory))
        
    def row(self, parent, side):
        """Creates a frame child object parented to another object (Usually another frame) with pack method."""
        child = Frame(parent, borderwidth=4, bd=4, bg='#dce3e5')
        child.pack(side=side, expand=YES, fill=BOTH)
        return child
    
    def button(self, parent, side, text, command):
        """Creates a button child object parented to another object (Normally a frame) with pack method """
        child = Button(parent, text=text, command=command)
        child.pack(side=side,expand=YES, fill=BOTH)
        return child
    
    def getcommand(self, command, value, mem):
        """This function holds extra button commands."""
        if command == "C": # Clear command
            func = lambda: value.set('')
        elif command == "+/-":  # toggle plus/minus command
            func = lambda: value.set(value.get().lstrip('-')) if float(value.get()) < 0 else value.set('-' + value.get())
        elif command == "<-":  # Backspace command
            func = lambda: value.set(value.get()[:-1])
        elif command == "STO":  # store memory
            func = lambda: mem.set(value.get())
        elif command == "RCL":  # Recall memory
            func = lambda: value.set(value.get() + mem.get())
        elif command == "x"+u"\u00B2":  # Square
            func = lambda: value.set(float(value.get())**2)
        elif command == u"\u221A"+"x":  # Square root
            func = lambda: value.set(sqrt(float(value.get())))
        elif command in ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "+"]:  # "Normal" buttons
            func = lambda: value.set(value.get() + command) 
        elif command == "=":  # Equals
            func = lambda: self.calculate()
        return func
    
    def calculate(self):
        """This function calculates whatever display object it is sent. An error box is shown if it fails."""
        try:
            self.display.set(eval(self.display.get()))
        except:
            messagebox.showerror('ERROR', "Could not calculate: %s" % self.display.get())


if __name__ == "__main__":
    Calculator().mainloop()
