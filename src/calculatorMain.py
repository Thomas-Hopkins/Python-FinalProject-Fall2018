"""
Created on Apr 19, 2018

@author: Thomas Hopkins and Rania Jameel

+This module runs calculatorNotes.py, calculatorRegular.py, and graphingCalculator.py in a single GUI interface. 
    It also runs a credits window alongside these to show credits for the program.

+This requires dependencies sympy and numpy. Sympy on its own requires the mpmath dependency. These are used in
    the graphing module for some calculations and parsing.
    SymPy (www.sympy.org)
    mpmath (www.mpmath.org)
    numpy (www.numpy.org)

+ The notes section of this program reads and writes text files to the accompanying ./data directory. The graphing
    module makes use of dictionaries to store some values. Many for loops are used. Comments are provided to see 
    what may be happening at certain intervals in the code.
"""
import argparse
from tkinter import *
from tkinter import ttk
import calculatorNotes, calculatorRegular, calculatorCredits

main = Tk()
main.title("Calculator")
main.geometry('250x450')
main.iconbitmap(bitmap='../Data/icon.ico')
main.resizable(width=False, height=False)
nb = ttk.Notebook(main)
nb.pack(expand=YES, fill=BOTH)

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nograph", help="Runs the calculator without graphing functionality.", action='store_true')
args = parser.parse_args()

if args.nograph:
    nb.add(calculatorRegular.Calculator(), text='Regular')
    nb.add(calculatorNotes.Notes(), text='Notes')
    nb.add(calculatorCredits.Credits(), text='Credits')
else:
    import graphingCalculator
    nb.add(calculatorRegular.Calculator(), text='Regular')
    nb.add(graphingCalculator.GraphingCalc(), text='Graphing')
    nb.add(calculatorNotes.Notes(), text='Notes')
    nb.add(calculatorCredits.Credits(), text='Credits')

main.mainloop()
