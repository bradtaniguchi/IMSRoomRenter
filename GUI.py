#!/usr/bin/env python3
# Bradley Taniguchi
# 12/18/15
import tkinter as tk
from datetime import datetime
from SLC import DataBaseInterface
from SLC import Student, StudentCollection  # to create and handle StudentObjects
from SEC import Popups  # to create popups
from SEC import DebugBox  # to create debugbox
from SEC import InfoBar  # to display
__author__ = 'Bradley Taniguchi'
__version__ = '0.3.7'


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
        self.minsize(width=300, height=300)  # Determined constant window size?
        self.maxsize(width=300, height=300)
        self.resizable(width=False, height=False)
        self.create_menubar()  # creates static menubar
        self.frames = {}  # array of frames
        self.databaseposition = 'bin/Sqlite/StudentDatabase.sqlite'  # default database position
        self._create_databaseinterface(self.databaseposition)

        for F in (PrimaryPage, ClockIn, ClockOut):  # initialize all frame/Classes
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        self.show_frame("PrimaryPage")

    def _create_databaseinterface(self, databasepos):
        """
        Creates the DatabaseInterface at the designated file position, set by default at
        "bin/Sqlite/StudentDatabase.sqlite". Check Debugger to see if database was created or not.
        """
        self.mydatabase = DataBaseInterface(self.databaseposition)  # NOTE the default is the same everywhere

    def show_frame(self, page_name):
        """Show a Frame for a given page name"""
        f = self.frames[page_name]
        f.tkraise()

    def create_menubar(self):
        """
        creates menubar object, which all menu buttons are attatched to.
        Calls: _create_file_menu, _create_edit_menu, _create_help_menu
        to create their respective menus.
        """
        self.menubar = tk.Menu()  # is this OK????
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
        editmenu.add_command(label="Change2RA", command=lambda: self.show_frame("RoomAvailability"))
        editmenu.add_command(label="CreateTestPopup", command=lambda: self.showpopup)  # TEST!
        editmenu.add_command(label="ShowDebugBox", command=lambda: self.showdebugbox("TEST!"))
        editmenu.add_command(label="TestDaily", command=lambda: self.testdaily())

    def testdaily(self):
        currentdate = str(datetime.now().date())
        mydatabaseinterface = DataBaseInterface()
        mystudentcollection = mydatabaseinterface.gathercollection()
        mydatabaseinterface.dailycollection(mystudentcollection, currentdate)
        self.showdebugbox(str(mydatabaseinterface))

    def _create_help_menu(self):
        """creates helpmenu, and cascade. """
        helpmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self.dumb)  #DUMB referenced!

    def quitprogram(self):
        print(">DEBUG: Quiting program via filemenu")
        self.quit()

    def showdebugbox(self, textboxtext):
        """
        Displays Current Contents of Database, using DatabaseInterface
        :param textboxtext: String to Display in Box
        """
        mydebugbox = DebugBox("DebugBox", textboxtext)
        mydebugbox.mainloop()

    @staticmethod
    def dumb():
        print(">DEBUG: DumbFunction used")

    @staticmethod
    def showpopup(self):
        mypopup = Popups()
        mypopup.mainloop()


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
                                       command=lambda: self.changeframe("ClockIn"))
        self.clockinbutton.grid(column=0, row=0, padx=self.bpadx, pady=self.bpady)  # EDIT TO CENTER!
        self.clockoutbutton = tk.Button(self, height=1, width=10, text="Clock-Out",
                                        command=lambda: self.changeframe("ClockOut"))
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
        Secondary SpecFunction, to be used in the future to allow for more than 5 rooms
        to be used.
        """
        self.roomsavailablestring.set(newcapacity)
        #print(">DEBUG: PrintFunction")

    def changeframe(self, framestring):
        """
        Showes different frame, prints change to log.
        :param stramestring: Frame to Change to
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
        self.roomvaraible = 0  # default integer variable
        self.clockinlabel = tk.Label(self, text="Clock-In")
        self.clockinlabel.grid(column=0, columnspan=6, row=0, sticky=tk.NSEW)
        self.namelabel = tk.Label(self, text="Name:")
        self.namelabel.grid(column=0, row=1)
        self.nametextbox = tk.Entry(self, width=32, textvariable=self.namevariable)
        self.nametextbox.grid(column=1, columnspan=5, row=1)
        self.studentidlabel = tk.Label(self, text="Student ID:")
        self.studentidlabel.grid(column=0, row=2)
        self.studentidtextbox = tk.Entry(self, width=32, textvariable=self.idvariable)
        self.studentidtextbox.grid(column=1, columnspan=5, row=2)
        self.roomslabel = tk.Label(self, text="Rooms Available")
        self.roomlabel = tk.Label(self, text="Room:")
        self.roomlabel.grid(column=0, row=3)
        self._createroombuttons()
        self.roomchosentext = tk.StringVar()
        self.roomchosentext.set("0")
        self.roomchosenentry = tk.Entry(self, width=2, textvariable=self.roomchosentext)
        self.roomchosenentry.grid(column=0, row=4)
        self.clockinbutton = tk.Button(self, height=1, width=5, text="submit",
                                       command=lambda: self.clockin(self.namevariable.get(),
                                                                    self.idvariable.get(), self.roomvaraible))
        self.clockinbutton.grid(column=0, columnspan=6, row=4)

    def _createroombuttons(self):
        self.room1button = tk.Button(self, height=1, width=1, text="1",
                                     command=lambda: self.roomnumber(1))
        self.room1button.grid(column=1, row=3)

        self.room2button = tk.Button(self, height=1, width=1, text="2",
                                     command=lambda: self.roomnumber(2))
        self.room2button.grid(column=2, row=3)

        self.room3button = tk.Button(self, height=1, width=1, text="3",
                                     command=lambda: self.roomnumber(3))
        self.room3button.grid(column=3, row=3)

        self.room4button = tk.Button(self, height=1, width=1, text="4",
                                     command=lambda: self.roomnumber(4))
        self.room4button.grid(column=4, row=3)

        self.room5button = tk.Button(self, height=1, width=1, text="5",
                                     command=lambda: self.roomnumber(5))
        self.room5button.grid(column=5, row=3)

    def roomnumber(self, num):
        self.roomvaraible = num
        self.roomchosentext.set(str(num))

    def clearinputs(self):
        """
        Clears inputs of following(4):
        """
        self.namevariable.set("")
        self.idvariable.set("")
        self.roomchosentext.set("0")
        self.roomvaraible = 0

    @staticmethod
    def validinput(name, studentid):
        if len(name) > 32 or len(name) < 1:  # input length ONLY accepted up to 32 characters
            return False, "Invalid Name"  # name not accepted
        if len(studentid) > 32 or len(studentid) < 1:  # input length ONLY accepted up to 32 characters
            return False, "Invalid ID"  # id not accepted
        return True, "Valid Input"  # name and id are accppted

    def changeframe(self, framestring):
        """
        Showes different frame, prints change to log.
        :param stramestring: Frame to Change to
        """
        print(">DEBUG: Changed frame to " + framestring)
        self.controller.show_frame(framestring)

    @staticmethod
    def checkroom(roomnumber):
        if roomnumber > 5 or roomnumber <= 0:
            return False  # keep things simple, bad class number then NOT available Duh!
        else:
            print(">DEBUG: TRYING TO CHECK IF ROOM AVAILABLE!")
            return True  # test value, this program has NO IDEA if rooms are actually available

    def clockin(self, name, studentid, room):
        """
        Clocks a student into a room, calls checkroom, to check the room, and checks inputs
        for student id and name. All inputs must come back valid to proceed.
        Gathers time and date
        :param name: Name of Student to Clock in
        :param studentid: Id of student that needs to clock in
        :return:
        """
        print(">DEBUG: Starting Clockin function with:\n" + "    " + str(name) + "\n    " + str(studentid))
        booleanreturn, stringreturn = self.validinput(name, studentid)
        if self.checkroom(room) and booleanreturn is True:  # Room and inputs OK
            clockindate = str(datetime.now().date())  # format: 2015-12-31
            clockintime = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)
            mystudentlogin = Student(studentid, name, clockindate, room, clockintime)  # no clockin as None
            mydatabaseinterface = DataBaseInterface()  # default file location
            mydatabaseinterface.clockin(mystudentlogin)
            self.clearinputs()
            self.changeframe("PrimaryPage")
        else:
            print(">DEBUG: ERROR! Bad Input: " + stringreturn)
            #go onto fix things here:


class ClockOut(tk.Frame):
    """
    This displays the Clock-Out screen for a student trying to rent
    UNDERGOING OVERHAUL 1/6/16
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.clockoutmainlabel = tk.Label(self, text="Clockout")
        #self.clockoutmainlabel.grid(column=0, columnspan=2, row=0)
        self.Descriptorinfo = tk.Label(self, text="StudentInfo")
        self.Descriptorinfo.grid(column=0, row=1)
        self.Descriptorclockout = tk.Label(self, text="Clockout")
        self.Descriptorclockout.grid(column=1, row=1)
        self.clockoutinforows = []  # list of clockoutbuttons
        self.createinforows(5, 2)  # initiation
        self.updatestudents()

    def createinforows(self, rows, startrow):
        """
        Dynamically make 0-5 rows to display information
        :param rows: rows to make
        :param startrow: starting column to set .grid
        """
        for i in range(rows):
            myinfobar = InfoBar(self, self.clockout, i, 23, 0, int(startrow + i))  # create myinfobar
            self.clockoutinforows.append(myinfobar)

    def updatestudents(self):
        """
        WARNING Heavy Database Usage! Needs optimization!!!
        Updates the Current Students clockedin, calls:
            .gathercollection() - to get all students EVER USES DATABASE
            .dailycollection() - returns StudentCollection for just today, USES DATETIME
            .whosclockedin - returns JUST whos clocked in!
        """
        print(">DEBUG: UpdatingStudents...")
        todaysdate = str(datetime.now().date())
        mydatabaseinterface = DataBaseInterface()  # to interact with database
        mystudentcollection = mydatabaseinterface.gathercollection()  # gets all entries, actually reads database
        mystudentcollection = mydatabaseinterface.dailycollection(mystudentcollection, todaysdate)  # only todays
        mystudentcollection = mydatabaseinterface.whosclockedin(mystudentcollection)  # ONLY clocked in
        # now that I have a collection of students ONLY logged in, display data from them.
        print(">>DEBUG: Students Inside of Rooms" + str(len(mystudentcollection.listofstudents)))
        for i in mystudentcollection.listofstudents:  # for student in mystudentcollection
            print(self.clockoutinforows[i].stringvar.set(mystudentcollection.listofstudents[i].name))

    def clockout(self, buttonnumber):
        """
        Reads the Contents of the choosen info, IE Button1 = info1
        :param buttonnumber: 1-5 number
        :return:
        """
        print(">>DEBUG:  " + str(buttonnumber))

    @staticmethod
    def checkroomvalid(room):  # remove with database check!
        """
        Checks to see if input of room is valid, IE 1-5
        """
        if room > 5 or room < 1:
            return False
        else:
            return True

    def changeframe(self, framestring):
        print(">DEBUG: Changed frame to " + framestring)
        self.controller.show_frame(framestring)


def startmain():
    """
    Starts the neccessary functions abnd classes to use the program
    :return:
    """
    print(">DEBUG: Intro main")
    app = Application()
    app.mainloop()
