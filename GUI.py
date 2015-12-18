#!/usr/bin/env python3
# Bradley Taniguchi
# 12/18/15
import tkinter as tk
#from tkinter import ttk
#import sqlite3

__author__ = 'Bradley Taniguchi'
__version__ = '0.2.0'


class Application(tk.Tk):
    # inspired from http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    """
    Primary Application manager, holds all frames, and creates and handles static menubar
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)  # container to be used for all frames
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("TEST PROG")
        self.minsize(width=800, height=600)  # Determined constant window size?
        self.maxsize(width=800, height=600)
        self.resizable(width=False, height=False)
        self.create_menubar()  # creates static menubar
        self.frames = {}  # array of frames

        for frame in (PrimaryPage, ClockIn, ClockOut):  # initialize all frame/Classes
            page_name = frame.__name__
            f = frame(container, self)
            self.frames[page_name] = frame
            f.grid(row=0, column=0, sticky="NSEW")

    def show_frame(self, page_name):
        """Show a Frame fro a given page name"""
        f = self.frames[page_name]
        f.tkraise()

    def create_menubar(self):
        """
        creates menubar object, which all menu buttons are attatched to.
        Calls: _create_file_menu, _create_edit_menu, _create_help_menu
        to create their respective menus.
        """
        self.menubar = tk.Menu()
        self.configure(menu=self.menubar)
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


class PrimaryPage(tk.Frame):
    """
    Shows Clock-in and Clock out buttons, and room available,
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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
    ALSO creates comfirm and deny dialog popups upon submitted inputs
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class ClockOut(tk.Frame):
    """
    This displays the Clock-Out screen for a student trying to rent
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


def startmain():
    """
    Starts the neccessary functions abnd classes to use the program
    :return:
    """
    print(">DEBUG: Intro main")
    app = Application()
    app.mainloop()
