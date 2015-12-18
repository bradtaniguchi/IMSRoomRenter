#!/usr/bin/env python3
# Bradley Taniguchi
# 11/30/15
__author__ = 'Bradley Taniguchi'
__version__ = '0.1.7'

import tkinter as tk
from tkinter import ttk
import sqlite3


class PrimaryFrame(tk.Frame):
    """
    Shows Clock-in and Clock out buttons, and room available,
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.textboxtext = tk.StringVar()  # Create string variable
        self.bheight=2
        self.bwidth=2
        self.bpadx=2
        self.bpady=2
        self.parent = parent
        self.TextBox = tk.Entry(self, width=30, textvariable=self.textboxtext)
        self.TextBox.grid(column=0, columnspan=6, row=0, sticky=tk.N, padx=self.bpadx, pady=self.bpady)
        self.pack()


class ClockIn(tk.Frame):
    """
    This displays the Clock-In screen for a student trying to rent a room.
    Directly Interacts with the database and calls back the PrimaryFrame once completed
    -ALSO creates comfirm and deny dialog popups upon submitted inputs
    """
    def __init__(self, parent, controller):
        self.controller = controller


class ClockOut(tk.Frame):
    """
    This displays the Clock-Out screen for a student trying to rent
    """
    def __init__(self, parent, controller):
        self.controller = controller


class WindowHandler(tk.Frame):
    """
    Creates the topbar menu, and holds the PrimaryFrame and changes the internal frame
    according to variable displayframe, normall initiated to PrimaryFrame
    """
    def __init__(self, parent, displayframe):
        tk.Frame.__init__(self, parent)
        self._create_menubar(parent)  # does the heavy lifting
        PrimaryFrame(parent).pack(side="top", fill="both", expand=True)
        self.frames = {}

    def _create_menubar(self, parent):
        """
        creates menubar object, which all menu buttons are attatched to.
        Calls: _create_file_menu, _create_edit_menu, _create_help_menu
        to create their respective menus.
        """
        self.menubar = tk.Menu()
        parent.configure(menu=self.menubar)
        self._create_file_menu()
        self._create_edit_menu()
        self._create_help_menu()

    def _create_file_menu(self):
        """creates filemenu, and cascade. """
        filemenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Quit", command=self.dumb)  #DUMB referenced!

    def _create_edit_menu(self):
        """creates editmenu, and cascade. """
        editmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=editmenu)

    def _create_help_menu(self):
        """creates helpmenu, and cascade. """
        helpmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self.dumb)  #DUMB referenced!

    @staticmethod
    def dumb():
        print(">DEBUG: DumbFunction used")


def startmain():
    """
    Starts the neccessary functions and classes to use program
    """
    print(">DEBUG: Into main")
    root = tk.Tk()
    root.title("TEST PROG")  # change title
    root.minsize(width=800, height=600)  # Determined constant window size?
    root.maxsize(width=800, height=600)
    root.resizable(width=False, height=False)
    WindowHandler(root)
    root.mainloop()




