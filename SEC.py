#!/usr/bin/env python3
# Bradley Taniguchi
# 12/18/15

import tkinter as tk
from tkinter import scrolledtext  # for large textbox
import GUI


class Popups(tk.Toplevel):
    def __init__(self, displaytitle="NOTITLE", displaytext="NOMSG", displaybuttontext="Done"):
        tk.Toplevel.__init__(self)  # any controller?
        self.title(displaytitle)
        msg = tk.Message(self, text=displaytext)
        msg.pack()

        button = tk.Button(self, text=displaybuttontext, command=self.exitwindow)
        button.pack()

    def exitwindow(self):
        self.quit()
        self.destroy()  # destory popupwindow


class DebugBox(tk.Toplevel):
    """
    Displays a large uneditable text area to display current printouts
    """
    def __init__(self, parentobject, displaytitle="DebugBox", displaybuttontext="done"):
        tk.Toplevel.__init__(self)
        self.title(displaytitle)
        self.textfield = scrolledtext.ScrolledText(master=self,
                                                   wrap=tk.WORD,
                                                   width=50,
                                                   height=20)
        self.controller = parentobject  # object creating this object
        self.displaytext = ""
        self.textfield.grid(column=0, columnspan=2, row=0)
        self.loadbutton = tk.Button(self, height=1, width=10, text="Reload", command=lambda: self.updatestring())
        self.loadbutton.grid(column=0, row=1)
        self.exitbutton = tk.Button(self, height=1, width=10, text="Exit", command=lambda: self.exitwindow())
        self.exitbutton.grid(column=1, row=1)
        self.updatestring()

    def updatestring(self):
        self.textfield.configure(state='normal')
        self.displaytext = self.controller.mydebugstring  # LEAP OF FAITH!
        self.textfield.insert(tk.END, "==============================")
        self.textfield.insert(tk.END, str(self.displaytext))
        self.textfield.configure(state='disabled')

    def exitwindow(self):
        self.quit()
        self.destroy()


class AboutMenu(tk.Toplevel):
    """
    Displays from the Help menu, details the project, and resources for this program.

    """
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("IMSRoomRenter About")
        self.mainstring = ("IMSRoomRenter Version " + GUI.__version__ + "\n\n" +
                           "Created by " + GUI.__author__ + "\n\n" +
                           "For the Instructional Media Service Department\n" +
                           "At California State University Dominguez Hills\n\n" +
                           "Using Python3, Tkinter and Sqlite3\n\n" +
                           "Project Was started on 1/18/15, \n"
                           "and version 1.0.0 was declared complete on 1/7/16\n\n"
                           "Project is hosted at: \n"
                           "https://github.com/bradtaniguchi/IMSRoomRenter\n")
        self.primarylabel = tk.Label(self, text=self.mainstring, padx=5, pady=1, relief=tk.SUNKEN)
        self.primarylabel.pack()
        self.button = tk.Button(self, text="Done", command=self.exit)
        self.button.pack()

    def exit(self):
        self.quit()
        self.destroy()


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

