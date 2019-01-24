"""
Created on May 3, 2018

@author: Thomas Hopkins and Rania Jameel
"""
from tkinter import *


class Credits(Frame):
    """A window for showing project credits."""
    def __init__(self):
        # Setup the window frame (Title, grid, etc)
        Frame.__init__(self)
        self.option_add('*Font', 'arial 12')
        self.pack(expand=YES)
        self.text = """
Created by Thomas Hopkins
           and Rania Jameel

Uses dependencies:
    SymPy (www.sympy.org)
    numpy (www.numpy.org)

Special thanks to:
    Professor McKanry (Rex)












                                                    2018
"""      
        self.creditslabel = Label(self, text=self.text, justify='left')
        self.creditslabel.pack()
