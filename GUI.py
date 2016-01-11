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
from SEC import RoomButton  # dynamically create RoomButtons
from SEC import AboutMenu  # to display about

__author__ = 'Bradley Taniguchi'
__version__ = '1.0.5'
# version 1.0.5 completed 1/11/16


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
        self.title("IMSRoomRenter v.1")
        self.minsize(width=300, height=150)  # Determined constant window size?
        self.maxsize(width=300, height=150)
        self.resizable(width=False, height=False)
        self.menubar = tk.Menu()  # is this OK????
        self.create_menubar()  # creates static menubar
        self.frames = {}  # array of frames
        self.databaseposition = 'bin/Sqlite/StudentDatabase.sqlite'  # default database position
        self._create_databaseinterface()
        self.loggedinstudents = []  # to see who is logged in. Gathered from Clockout
        self.roomsavail = 5
        self.mydebugstring = ""
        for F in (PrimaryPage, ClockIn, ClockOut):  # initialize all frame/Classes
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        self.show_frame("PrimaryPage")
        # self.primupdatescreens()

    def primupdatescreens(self):
        self.sysprint(">>DEBUG: PrimUpdating screens...")
        self.frames["ClockOut"].updatestudents()  # updates Students
        self.loggedinstudents = self.frames["ClockOut"].mystudentcollection.listofstudents
        self.frames["ClockIn"].updatescreens()  # update WHICH rooms are available
        self.frames["ClockOut"].updatescreens()  # CHANGE ALL OF THESE TO ACCEPT THE ARRAY! easier to read!
        self.frames["PrimaryPage"].updatescreens()  # update how many rooms available!

    def _create_databaseinterface(self):
        """
        Creates the DatabaseInterface at the designated file position, set by default at
        "bin/Sqlite/StudentDatabase.sqlite". Check Debugger to see if database was created or not.
        """
        self.mydatabase = DataBaseInterface(self.databaseposition)  # NOTE the default is the same everywhere
        self.mydatabase.checkifdatabaseexists(self.databaseposition)  # checks to see if databasefile exists

    def show_frame(self, page_name):
        """
        Show a Frame for a given page name
        :param page_name: page to change to
        """
        self.primupdatescreens()  # EDIT THIS
        f = self.frames[page_name]
        f.tkraise()

    def create_menubar(self):
        """
        creates menubar object, which all menu buttons are attatched to.
        Calls: _create_file_menu, _create_edit_menu, _create_help_menu
        to create their respective menus.
        """
        self.configure(menu=self.menubar)
        self._create_file_menu()
        self._create_edit_menu()
        self._create_help_menu()

    def _create_file_menu(self):
        """creates filemenu, and cascade. """
        filemenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="PrintDataBase", command=self.dumb)  # DUMB referenced!
        filemenu.add_command(label="Quit", command=self.quitprogram)  # DUMB referenced!

    def _create_edit_menu(self):
        """creates editmenu, and cascade. """
        editmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Go to MainPage", command=lambda: self.show_frame("PrimaryPage"))
        editmenu.add_command(label="CreateTestPopup", command=lambda: self.showpopup("title", "text"))  # TEST!
        editmenu.add_command(label="ShowDebugBox", command=lambda: self.showdebugbox())
        # editmenu.add_command(label="TestDaily", command=lambda: self.testdaily())

    def testdaily(self):
        currentdate = str(datetime.now().date())
        mydatabaseinterface = DataBaseInterface()
        mystudentcollection = mydatabaseinterface.gathercollection()
        mystudentcollection = mydatabaseinterface.dailycollection(mystudentcollection, currentdate)
        self.sysprint(str(mystudentcollection.listofstudents[0]))
        self.showdebugbox()

    def _create_help_menu(self):
        """creates helpmenu, and cascade. """
        helpmenu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=lambda: self.showaboutmenu())  # TEST!

    @staticmethod
    def showaboutmenu():
        """
        Displays the About Menu
        """
        myaboutmenu = AboutMenu()
        myaboutmenu.mainloop()

    def quitprogram(self):
        self.sysprint(">:Quiting program via filemenu")
        self.quit()
        self.destroy()

    def sysprint(self, appendtext):
        """
        Updates the string of debugbox, adds newline and timestamp
        :param appendtext: text to append to debugbox
        """
        thetime = (str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute) + ":" +
                   str(datetime.now().time().second))
        self.mydebugstring += (">["+str(thetime)+"]" + appendtext + "\n")

    def showdebugbox(self):
        """
        Displays Current Contents of Database, using DatabaseInterface
        """
        mydebugbox = DebugBox("DebugBox", self.mydebugstring)
        mydebugbox.mainloop()  # needs work

    def dumb(self):
        self.updatedebugbox(">DEBUG: DumbFunctionUsed!")
        print(">DEBUG: DumbFunction used")

    def showpopup(self, title, text):
        mypopup = Popups(title, text)
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
        self.bheight = 2
        self.bwidth = 2
        self.bpadx = 2
        self.bpady = 2
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


    def updatescreens(self):
        """
        Updates Rooms Available for display
        """
        self.controller.sysprint("Updating Screens in PrimaryPage")
        stringtoprint = str(5-len(self.controller.loggedinstudents))  # undynamic
        self.roomsavailablestring.set(stringtoprint)

    def changeframe(self, framestring):
        """
        Showes different frame, prints change to log.
        :param framestring: Frame to Change to
        """
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
        self.roombuttonslist = []
        self._createroombuttons(5, 1, 3)
        self.roomchosentext = tk.StringVar()
        self.roomchosentext.set("0")
        self.roomchosenentry = tk.Entry(self, width=2, textvariable=self.roomchosentext)
        self.roomchosenentry.grid(column=0, row=4)
        self.clockinbutton = tk.Button(self, height=1, width=5, text="submit",
                                       command=lambda: self.clockin(self.namevariable.get(),
                                                                    self.idvariable.get(), self.roomvaraible))
        self.clockinbutton.grid(column=0, columnspan=6, row=4)
        self.listofopenrooms = []

    def _createroombuttons(self, buttons, startcolumn, startrow):  # change to dynamic amount at another time!
        for i in range(buttons):
            myroombutton = RoomButton(self, self.roomnumber, (i+1), str(i+1), startcolumn+i, startrow)
            self.roombuttonslist.append(myroombutton)

    def updatescreens(self):
        """
        Reads the Application class and checks the list of clocked in students seeing which rooms are available
        """
        mylistofrooms = []
        for student in self.controller.loggedinstudents:
            mylistofrooms.append(int(student.room))
        self.listofopenrooms = mylistofrooms  # changes rooms available.
        for roombuttonobject in self.roombuttonslist:  # for each number in list, set all enabled!
            roombuttonobject.button.configure(state=tk.ACTIVE)
        for i in self.listofopenrooms:  # for each number in list
            self.roombuttonslist[i-1].button.configure(state=tk.DISABLED)  # disables rooms filed

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
        :param framestring: Frame to Change to
        """
        self.controller.show_frame(framestring)

    def clockin(self, name, studentid, room):
        """
        Clocks a student into a room, calls checkroom, to check the room, and checks inputs
        for student id and name. All inputs must come back valid to proceed.
        Gathers time and date
        :param name: Name of Student to Clock in
        :param studentid: Id of student that needs to clock in
        :param room: Room of Student to clockin
        :return:
        """
        #print(">DEBUG: Starting Clockin function with:\n" + "    " + str(name) + "\n    " + str(studentid))
        booleanreturn, stringreturn = self.validinput(name, studentid)
        if booleanreturn is True:  # Room and inputs OK
            if room == 0:
                self.controller.sysprint("ERROR! Room 0!")
                mypopup = Popups("ERROR!", "Bad Input Choose  room!")
                mypopup.mainloop()
            else:
                clockindate = str(datetime.now().date())  # format: 2015-12-31
                clockintime = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)
                mystudentlogin = Student(studentid, name, clockindate, room, clockintime)  # no clockin as None
                mydatabaseinterface = DataBaseInterface()  # default file location
                mydatabaseinterface.clockin(mystudentlogin)
                self.clearinputs()
                self.changeframe("PrimaryPage")
        else:
            self.controller.sysprint(">ERROR! Bad Input: " + stringreturn)
            mypopup = Popups("Error!", "Bad Input " + stringreturn)
            mypopup.mainloop()


class ClockOut(tk.Frame):
    """
    This displays the Clock-Out screen for a student trying to rent
    UNDERGOING OVERHAUL 1/6/16
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Descriptorinfo = tk.Label(self, text="StudentInfo")
        self.Descriptorinfo.grid(column=0, row=1)
        self.Descriptorclockout = tk.Label(self, text="Clockout")
        self.Descriptorclockout.grid(column=1, row=1)
        self.clockoutinforows = []  # list of clockoutbuttons
        self.mydatabaseinterface = DataBaseInterface()  # updated on updatestudents
        self.mystudentcollection = StudentCollection()  # updated on updatestudents
        self.createinforows(5, 2)  # initiation

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
        CREATES self.
        Updates the Current Students clockedin, calls:
            .gathercollection() - to get all students EVER USES DATABASE
            .dailycollection() - returns StudentCollection for just today, USES DATETIME
            .whosclockedin - returns JUST whos clocked in!
        """
        self.controller.sysprint(">DEBUG: UpdatingStudents...")
        todaysdate = str(datetime.now().date())
        self.mystudentcollection = self.mydatabaseinterface.gathercollection()  # gets all entries
        self.mystudentcollection = self.mydatabaseinterface.dailycollection(self.mystudentcollection, todaysdate)
        self.mystudentcollection = self.mydatabaseinterface.whosclockedin(self.mystudentcollection)  # ONLY clocked in
        # now that I have a collection of students ONLY logged in, display data from them.
        i = 0  # for loop
        for student in self.mystudentcollection.listofstudents:  # for student in mystudentcollection
            self.clockoutinforows[i].stringvar.set(student.name + "-" + str(student.studentid))
            i += 1

    def updatescreens(self):
        """
        Updates the Screens on Clockout, with blanks, also updates students
        """
        for bar in range(len(self.clockoutinforows)):
            self.clockoutinforows[bar].stringvar.set("-------------------------")
        self.updatestudents()

    def clockout(self, buttonnumber):
        """
        Reads the Contents of the choosen info, IE Button1 = info1
        Change the Student Clockout time from None to time right now
        :param buttonnumber: 1-5 number
        :return:
        """
        self.clockoutinforows[buttonnumber].stringvar.set("-------------------------")  # clears out
        clockouttime = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)
        try:
            self.mystudentcollection.listofstudents[buttonnumber].clockouttime = clockouttime
            self.controller.sysprint(">DEBUG: ClockoutMethod trying.." +
                                     str(self.mystudentcollection.listofstudents[buttonnumber].name) +
                                     " at " + clockouttime)
            self.mydatabaseinterface.clockout(self.mystudentcollection.listofstudents[buttonnumber])
            logoutstring = ("Logout of " + str(self.mystudentcollection.listofstudents[buttonnumber].name) + " At " +
                            clockouttime)
            self.changeframe("PrimaryPage")
            mypopup = Popups("Logout Successful", logoutstring, "Ok")
            mypopup.mainloop()

        except:  # meh to broad?
            self.controller.sysprint(">ERROR!: Bad Clockout")
            pass

    def changeframe(self, framestring):
        self.controller.show_frame(framestring)


def startmain():
    """
    Starts the neccessary functions abnd classes to use the program
    :return:
    """
    print(">DEBUG: Intro main")
    app = Application()
    app.mainloop()
