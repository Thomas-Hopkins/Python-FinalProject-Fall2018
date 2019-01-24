"""
Created on May 3, 2018

@author: Thomas Hopkins and Rania Jameel
"""
from tkinter import *
from tkinter import messagebox
import sys
import numpy
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
import turtle

class GraphingCalc(Frame):
    """Class that graphs up to 3 equations at a time."""
    def __init__(self):
        # Setup the window frame (Title, grid, etc)
        Frame.__init__(self)
        self.option_add('*Font', 'arial 10 bold')
        self.pack(expand=YES, fill=BOTH)
        # make three stringvar variables for storing equations
        equation1, equation2, equation3 = StringVar(), StringVar(), StringVar()
        # Store the equation variables in a dictionary for easy recall, and a dict for equation colors.
        self.entrydict = {'1': equation1, '2': equation2, '3': equation3}
        self.colordict = {'1': 'red', '2': 'blue', '3': 'purple'}
        
        # used for solving later on.
        self.transformations = (standard_transformations + (implicit_multiplication_application,))
        
        # Make a frame for equation fields
        self.equationframe = Frame(self)
        self.equationframe.pack(side=TOP, expand=YES, fill=BOTH)
        
        # Create the entry fields for the equations
        for num, equation in self.entrydict.items():
            self.equationLabel(self.equationframe, TOP, num)
            self.equationBox(self.equationframe, equation)
            
        # Create a button that will graph the equations
        self.graphButton = Button(self.equationframe, text='Graph it!', command=self.draw)
        self.graphButton.pack(side=BOTTOM,expand=YES, fill=BOTH)
        
        # Create a frame for the graph
        self.graphframe = Frame(self)
        self.graphframe.pack(side=BOTTOM, expand=YES, fill=BOTH)
        
        # Create a canvas object parented to the graph frame for graphing
        self.graph = Canvas(self.graphframe, width=250, height=200)
        self.graph.pack(side=TOP, expand=YES, fill=BOTH)

    def equationBox(self, parent, equation):
        # Creates a box for entering an equation
        child = Entry(parent, justify='left', textvariable=equation, relief=FLAT, bd=-1)
        child.pack(side=TOP, expand=YES, fill=BOTH)
        return child

    def equationLabel(self, parent, side, text):
        # Creates label for an equation box.
        child = Label(parent, text="Equation " + str(text), justify='center', fg=self.colordict[text], relief=GROOVE, bd=5)
        child.pack(side=side,expand=YES, fill=BOTH)
        return child
     
    def draw(self, xcoord=10, ycoord=10):
        """This function will draw the graph."""
        self.graph.delete('all')  # Clear the graph
        t = turtle.RawTurtle(self.graph)  # Create a turtle object parented to the canvas object
        screen = t.getscreen()
        screen.setworldcoordinates(-xcoord, -ycoord, xcoord, ycoord)  # Setup coordinates
        t.hideturtle()
        # Draws the graph axis
        t.speed(500)
        t.up()
        t.goto(0, -ycoord)
        t.down()
        t.goto(0, ycoord)
        t.up()
        t.goto(-xcoord, 0)
        t.down()
        t.goto(xcoord, 0)
        t.up()
        # graph the equations
        for graph, equation in self.entrydict.items():
            if equation.get() != '':  # if there is a entered equation
                equation = equation.get().replace('^', '**')  # replace ^'s to **'s
                equation = str(parse_expr(equation, transformations=self.transformations))  # Parses input to work more like expected in calculations
                                                                                            # Notably 2x -> 2*x and proper multiplication with parens
                equation = equation.replace('x', 'num')  # replace x's with num for use in variable
                t.color(self.colordict[graph])  # get the color for the graph
                try:
                    for num in numpy.linspace(-xcoord, xcoord, xcoord*30):
                        t.goto(num, eval(equation))  # evaluate the equation to find y
                        t.down()
                except:
                    # could not calculate the equation
                    messagebox.showerror("CALCULATION ERROR", "Could not calculate. Make sure to make proper use of parenthesis.\n\
Make sure to include * when multiplying. IE) 2*(x+2) not 2(x+2)")
                t.up()


if __name__ == '__main__':
    GraphingCalc().mainloop()
