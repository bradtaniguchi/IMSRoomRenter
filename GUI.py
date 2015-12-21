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
        self.minsize(width=200, height=150)  # Determined constant window size?
        self.maxsize(width=200, height=150)
        self.resizable(width=False, height=False)
        self.create_menubar()  # creates static menubar
        self.frames = {}  # array of frames

        for F in (PrimaryPage, ClockIn, RoomAvailability,ClockOut):  # initialize all frame/Classes
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        self.show_frame("PrimaryPage")

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
        filemenu.add_command(label="foo", command=self.dumb)  #DUMB referenced!
        filemenu.add_command(label="Quit", command=self.quitprogram)  #DUMB referenced!

    def _create_edit_menu(self):
        """creates editmenu, and cascade. """
        editmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Change2Prim", command=lambda: self.show_frame("PrimaryPage"))  # ADDED FOR DEBUGGING!
        editmenu.add_command(label="Change2ClockIn", command=lambda: self.show_frame("ClockIn"))
        editmenu.add_command(label="Change2ClockOut", command=lambda: self.show_frame("ClockOut"))
        editmenu.add_command(label="Change2RA", command=lambda: self.show_frame("ClockIn"))


    def _create_help_menu(self):
        """creates helpmenu, and cascade. """
        helpmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self.dumb)  #DUMB referenced!

    def quitprogram(self):
        print(">DEBUG: Quiting program via filemenu")
        self.quit()

    @staticmethod
    def dumb():
        print(">DEBUG: DumbFunction used")


class PrimaryPage(tk.Frame):
    """
    Shows Clock-in and Clock out buttons, and room available,
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.roomsavailablestring = tk.StringVar()  # IMPORTANT!
        self.controller = controller
        self.textboxtext = tk.StringVar()  # Create string variable
        self.bheight=2
        self.bwidth=2
        self.bpadx=2
        self.bpady=2
        self.parent = parent
        self.clockinbutton = tk.Button(self, height=1, width=10, text="Clock-In",
                                       command=lambda:self.changeframe("ClockIn"))
        self.clockinbutton.grid(column=0, row=0, padx=self.bpadx, pady=self.bpady)  # EDIT TO CENTER!
        self.clockoutbutton = tk.Button(self, height=1, width=10, text="Clock-Out",
                                        command=lambda:self.changeframe("ClockOut"))
        self.clockoutbutton.grid(column=0, row=1, padx=self.bpadx, pady=self.bpady)
        self.ralabel = tk.Label(self, text="Rooms Available:")
        self.ralabel.grid(column=0, row=2, padx=self.bpadx, pady=self.bpady)
        self.ratextbox = tk.Entry(self, width=2, textvariable=self.roomsavailablestring)
        self.ratextbox.grid(column=1, row=2, padx=self.bpadx, pady=self.bpady)
        self.ratextbox.configure(state='readonly')
        self.pack()
        self.startup_room_check()  # run startup check

    def startup_room_check(self):
        """
        When the program starts, it checks how many rooms are available from reading the
        object created from read file. TO BE CREATED LATER
        """
        self.change_room_capacity(5)  # default start value temp!

    def change_room_capacity(self, newcapacity):
        """
        Changes room capacity.
        """
        self.roomsavailablestring.set(newcapacity)
        print(">DEBUG: PrintFunction")

    def changeframe(self, framestring):
        """
        Showes different frame, prints change to log.
        """
        print(">DEBUG: Changed frame to " + framestring)
        self.controller.show_frame(framestring)

    @staticmethod
    def dumb():
        print(">DEBUG: DumbFunction for PrimaryPage used")


class ClockIn(tk.Frame):
    """
    This displays the Clock-In screen for a student trying to rent a room.
    Directly Interacts with the database and calls back the PrimaryFrame once completed
    ALSO creates comfirm and deny dialog popups upon submitted inputs
    NOTE: No padx, or pady??
    6 or 12 spots for the buttons AND label?
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.testwork = tk.Label(self, text="ClockInPage")
        self.testwork.grid(column=0, row=0)
        self.namevariable = tk.StringVar()  # Create string variable
        self.idvariable = tk.StringVar()  # numeric string variable
        self.clockinlabel = tk.Label(self, text="Clock-In")
        self.clockinlabel.grid(column=0, columnspan=2, row=0, sticky=tk.NSEW)
        self.namelabel = tk.Label(self, text="Name:")
        self.namelabel.grid(column=0, row=1)
        self.nametextbox = tk.Entry(self, width=15, textvariable=self.namevariable)
        self.nametextbox.grid(column=1, row=1)
        self.studentidlabel = tk.Label(self, text="Student ID:")
        self.studentidlabel.grid(column=0, row=2)
        self.studentidtextbox = tk.Entry(self, width=15, textvariable=self.idvariable)
        self.studentidtextbox.grid(column=1, row=2)
        self.roomsavlabel = tk.Label(self, text="Room 1-5")


    def checkroom(self, roomnumber ):
        if roomnumber > 5 or roomnumber <= 0 :
            return False  # keep things simple, bad class number then NOT available Duh!
        else:
            print(">DEBUG: TRYING TO CHECK IF ROOM AVAILABLE!")
            return True  # test value, this program has NO IDEA if rooms are actually available

class RoomAvailability(tk.Frame):
    """
    Displays the 5 rooms based on availability v was herefdfgsa
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.roomslabel = tk.Label(self, text="Rooms Available")
        self.roomslabel.grid(column=0, row=0)


class ClockOut(tk.Frame):
    """
    This displays the Clock-Out screen for a student trying to rent
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.testwork = tk.Label(self, text="ClockOutPage")
        self.testwork.grid(column=0, row=0)


def startmain():
    """
    Starts the neccessary functions abnd classes to use the program
    :return:
    """
    print(">DEBUG: Intro main")
    app = Application()
    app.mainloop()
