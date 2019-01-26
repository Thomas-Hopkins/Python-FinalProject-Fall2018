"""
Created on May 3, 2018

@author: Thomas Hopkins and Rania Jameel
"""
from tkinter import *
from tkinter import messagebox
import os

path = "../Notes/"


class Notes(Frame):
    """This class adds functionality for saving, opening, and writing notes."""
    def __init__(self):
        # Setup the window frame (Title, grid, etc)
        Frame.__init__(self)
        self.option_add('*Font', 'arial 10 bold')
        self.pack(expand=YES)
        # set the filename
        self.filename = StringVar()
        self.filename.set('filename.txt')
        
        # Setup a frame at the top of the Notes frame for buttons
        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=TOP, expand=YES, fill=BOTH)
        # Save button
        self.saveBtn = Button(self.buttonFrame, text="Save", command= self.saveNote)
        self.saveBtn.pack(side=LEFT)
        # Open button
        self.openBtn = Button(self.buttonFrame, text="Open", command= self.openNote)
        self.openBtn.pack(side=LEFT)
        # new button
        self.newBtn = Button(self.buttonFrame, text="New", command= self.newNote)
        self.newBtn.pack(side=LEFT)
        # File name label
        self.filelabel = Entry(self.buttonFrame, relief=RIDGE, bd=2, textvariable=self.filename, justify='right')
        self.filelabel.pack(side=LEFT, expand=YES, fill=BOTH)
        
        # Frame for text
        self.textPane = Frame(self)
        self.textPane.pack(expand=YES,fill=BOTH)
        
        # Scrolling bar on Y vertical
        self.yscroll = Scrollbar(self.textPane, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, expand=YES, fill=BOTH)
        
        # Text area for typing into a file
        self.textArea = Text(self.textPane,  relief=GROOVE, bd=5, yscrollcommand=self.yscroll.set, font='arial')
        self.textArea.pack(expand=YES, fill=BOTH)
        self.yscroll["command"] = self.textArea.yview  # parent the scrolling to the text area

    def saveNote(self):
        """This function saves the note."""
        if not os.path.exists(path):  # if folder does not exist make it
            os.makedirs(path)
        if self.filename.get() != "":  # If the filename is not empty
            if not os.path.exists(path + self.filename.get()):  # if the file doesn't exist
                self.file = open(path + self.filename.get(), 'w')  # open a file/create it
                self.file.write(self.textArea.get("1.0", END))  # write and close it
                self.file.close()
            else:  # if the file does exist ask if the user wishes to overwrite it.
                question = messagebox.askquestion('Warning', 'Are you sure you want to overwrite %s?' %
                                                  self.filename.get(), icon='warning')
                if question == 'yes':  # If answer is yes overwrite it
                    self.file = open(path + self.filename.get(), 'w')
                    self.file.write(self.textArea.get("1.0", END))
                    self.file.close()
        else:
            messagebox.showerror('ERROR', "Must enter a filename!")
            
    def openNote(self):
        if self.textArea != '':  # if the text box isn't empty ask user if they have saved their current work.
            question = messagebox.askquestion('Warning', 'Have you saved your note?\nPressing yes will delete this '
                                                         'current note.', icon='warning')
            if question == 'yes': # if they want to continue
                try:  # open the file and read it
                    self.file = open(path + self.filename.get(), 'r')
                    self.textArea.delete("1.0", END)
                    self.textArea.insert("1.0", self.file.read())
                    self.file.close()
                except:  # if it fails file doesn't exist.
                    messagebox.showerror('ERROR', "File does not exist!")
    
    def newNote(self):
        usercont=True
        if self.textArea != '':  # if text is not empty ask user if they wish to continue
            question = messagebox.askquestion('Warning', 'Have you saved your note?\nPressing yes will delete this '
                                                         'current note.', icon='warning')
            if question == 'yes':
                usercont = True
            else:
                usercont = False
        if usercont:  # if the user wishes to continue, or text box is empty
            self.filename.set('')  # remove filename
            self.textArea.delete('1.0', END)  # delete all text


if __name__ == '__main__':
    Notes().mainloop()
