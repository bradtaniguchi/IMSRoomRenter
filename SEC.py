#!/usr/bin/env python3
# Bradley Taniguchi
# 12/18/15

import tkinter as tk
from tkinter import scrolledtext  # for large textbox


class Popups(tk.Toplevel):
    def __init__(self, displaytitle="NOTITLE", displaytext="NOMSG", displaybuttontext="Done"):
        tk.Toplevel.__init__(self)  # any controller?
        self.title(displaytitle)
        msg = tk.Message(self, text=displaytext)
        msg.pack()

        button = tk.Button(self, text=displaybuttontext, command=self.exitwindow)
        button.pack()

    def exitwindow(self):
        self.destroy()  # destory popupwindow


class DebugBox(tk.Toplevel):
    """
    Displays a large uneditable text area to display current contents of database
    """
    def __init__(self, displaytitle="DebugBox", displaytext="NOMSG", displaybuttontext="done"):
        tk.Toplevel.__init__(self)
        self.title(displaytitle)
        self.textfield = scrolledtext.ScrolledText(master=self,
                                                   wrap=tk.WORD,
                                                   width=50,
                                                   height=20)
        self.inserttext(displaytext)
        self.textfield.configure(state='disabled')
        self.textfield.pack()

    def inserttext(self, text):
        print("tired insert")
        self.textfield.insert(tk.INSERT, text)
    def exitwindow(self):
        self.destroy()


class ComfirmationDialog(tk.Toplevel):
    def __init__(self, displaytitle="ComfirmationDialog", displaytext="NOMSG"):
        """
        Creates a TopLevel window, with yes no dialogs
        :param displaytitle: Text to be displayed on titlebar
        :param displaytext: Text to be displayed in the middle of the frame
        :return: True/False for Yes, No button comfirmation. No if frame deletion
        """
        #CLEARLY UNFINISHED!


class InfoBar:
    def __init__(self, parent, comfunc, comfuncparam, width=23, relcolumn=0, relrow=0):
        """
        Used to Dynamically create any number of rows to display information
        :param parent: Parent class, Frame
        :param comfunc: Command Function, command to use from parent.
        :param comfuncparam: Command Function parameter, only accepts 1
        :param width: width of tk.entry
        :param relcolumn: relative column for tk.Entry
        :param relrow: relative row
        :param relrow: relative row, to help position them during initiation loop
        """
        self.parent = parent
        self.width = width
        self.relcolumn = relcolumn
        self.relrow = relrow
        self.stringvar = tk.StringVar()
        self.infoentry = tk.Entry(parent, width=self.width, textvariable=self.stringvar)
        self.infoentry.grid(column=self.relcolumn, row=self.relrow)
        self.infobutton = tk.Button(parent, height=1, width=2, command=lambda: comfunc(comfuncparam))
        self.infobutton.grid(column=(int(self.relcolumn)+1), row=self.relrow)


class RoomButton:
    def __init__(self, parent, comfunc, comfuncparam, text="?", relcolumn=0, relrow=0):
        """
        Used to dynamically create any number of classroom buttons.
        :param parent: Parent class, Frame
        :param comfunc: Command Function, command to use from parent
        :param comfuncparam: Command Function Parameter, only accepts 1(room)
        :param text: Text for Button (room number)
        :param relcolumn: Relative Column
        :param relrow: Relative Row
        """
        self.parent = parent
        self.text = text
        self.relcolumn = relcolumn
        self.relrow = relrow
        self.button = tk.Button(parent, height=1, width=1, text=self.text,
                                command=lambda: comfunc(comfuncparam))
        self.button.grid(column=self.relcolumn, row=self.relrow)
