#!/usr/bin/env python3
# Bradley Taniguchi
# 12/21/15

import os
import sqlite3


class Student:
    """
    Handles student objects populates StudentCollection
    """
    def __init__(self, studentid, name, clockindate=None, room=None, clockintime=None, clockouttime=None):
        self.studentid = studentid
        self.name = name  # if not given an input, use default IE John Doe
        self.clockindate = clockindate  # date of student clockin
        self.room = room  # room of person clocking in
        self.clockintime = clockintime  # time of clockin
        self.clockouttime = clockouttime  # time of clockout, can be None/Null

    def printvalues(self):
        """
        Returns values for testing
        :return: String, to be displayed
        """
        returnstring = "ID " + str(self.studentid) + " N: " + str(self.name) + " CDate " \
                       + str(self.clockindate) + " R: " + str(self.room) + " Cin: " + str(self.clockintime)\
                       + " Cout: " + str(self.clockouttime)
        return returnstring

    def rawtuple(self):
        """
        Returns a raw tuple for more Effecient displays than printvalues
        :return: Tuple: [ID, Name, ClockinDate, Room, ClockinTime, ClockOutTime]
        """
        returntuple = [self.studentid, self.name, self.clockindate, self.room, self.clockintime, self.clockouttime]
        return returntuple


class StudentCollection:
    """
    Student handler and creation aspect.
    """
    def __init__(self, listofstudents=None):  # DO NOT USE: list = [], GOTME!
        if listofstudents is None:
            self.listofstudents = []  # list of student classes

    def convertraw(self, rawlist):
        """
        Given RawList from fetchall(), create a list of StudentObjects
        :param rawlist: Raw list of Tuples, each tuple corresponds to 1 student.
        """
        for mytuple in rawlist:
            mystudent = Student(mytuple[0], mytuple[1], mytuple[2], mytuple[3], mytuple[4], mytuple[5])
            self.listofstudents.append(mystudent)

    def printcontents(self):
        """
        Prints the contents of listofstudents
        :return: String of object classes and their contents
        """
        mystring = ""
        for student in self.listofstudents:
            mystring += (student.printvalues())
        return mystring  # TEST THIS!


class DataBaseInterface:
    """
    Primary Database interface handler
    """
    def __init__(self, filename='bin/Sqlite/StudentDatabase.sqlite'):  # currently redundant
        self.filedirectory = filename
        self.databasefile = os.path.join(os.path.dirname(__file__), str(filename))

    def checkifdatabaseexists(self, databasefile):
        """
        Checks if database exists
        :param databasefile: Location of database file
        """
        path = os.path.join(os.path.dirname(__file__), str(databasefile))
        if os.path.isfile(path):
            print("D>DEBUG: File Exists!")
        else:
            print("D>DEBUG: File Doesn't Exist, creating it now..")
            print(str(self.databasefile))
            print(str(self.filedirectory))
            self._createstudentdatabase(path)  # create the file

    def _createstudentdatabase(self, database):
        """
        Creates The Student Database if there isn't one already
        :return: true if creating database was a succuess
        """
        conn = sqlite3.connect(database)  # create connection to database
        c = conn.cursor()
        print("D>DEBUG: Creating Student Database at: " + self.filedirectory)
        c.execute('''CREATE TABLE student_table1
                 (ID INT NOT NULL,
                  NAME CHAR(32) NOT NULL,
                  DATE TEXT NOT NULL,
                  ROOM INT NOT NULL,
                  CLOCKIN TEXT NOT NULL,
                  CLOCKOUT TEXT)''')
        conn.commit()
        conn.close()
        print("D>DEBUG: Database Created Successfully!")

    def swaprooms(self, room1, room2, currentdate):
        """
        Swaps who-ever was in room1 with room2,
        :param room1: Swaps with room2
        :param room2: Swaps with room1
        :param currentdate: The date on which these two students exist, generally current
        """
        if (room1 > 5 or room1 < 0) or (room2 > 5 or room2 < 0):  # room out of range
            print("D>DEBUG: RoomOutOfRange: R1: " + str(room1) + " R2: " + str(room2))
            return  # ERROR
        else:
            print("D>DEBUG: Swaping room " + str(room1) + " and " + str(room2))
            mystudentcollection = self.whosclockedin(self.dailycollection(self.gathercollection(),
                                                                          currentdate))  # get whos clocked in
            mystudent1tuple = Student(-0, "NAME-ERR", "DATE-ERR", "ROOM-ERR", "CLOCKIN-ERR", "CLOCKOUT-ERR")
            studentinroom1exists = False  # cheap way to tell if we found students
            studentinroom2exists = False
            for student in mystudentcollection.listofstudents:  # find students with dates
                if student.room == room1:
                    mystudent1tuple = student
                    studentinroom1exists = True  # We have room 1
                    continue  # go thru loop again
                elif student.room == room2:
                    mystudent2tuple = student  # We have room 2
                    studentinroom2exists = True
                    continue
                    # Now to check to handle the instances where rooms are filled
            if studentinroom1exists and studentinroom2exists:  # Both have people in rooms
                print("POOP")

            elif studentinroom1exists and not studentinroom2exists:  # Student in Room1, but no one in Room2
                '''
                mytuple = mystudent1tuple.room  # reference before assignment???
                mytuple = [mystudent1tuple.room, mystudent1tuple.studentid, mystudent1tuple.name,
                            mystudent1tuple.clockindate, studentobject.room, mystudent1tuple.clockouttime,
                            studentobject.clockintime]
                mytuple.room = room2  # change room
                conn = sqlite3.connect(self.databasefile)  # create connection to database
                c = conn.cursor()
                try:
                    c.execute("UPDATE student_table1 SET ROOM = ? WHERE ID  = ? AND NAME = ? \
                              AND DATE = ? AND ROOM = ? AND CLOCKOUT = ? AND CLOCKIN = ?", mytuple)
                except sqlite3.IntegrityError:
                    print("D>ERROR: Sqlite3 Integrity Error")
                '''

            elif not studentinroom1exists and studentinroom2exists:  # No one in Room1, but Student in Room2
                print("PPOOP")

            else:  # No Students in Either Room! Error!
                print("D>DEBUG: Error")
                return  # to not show successful swap

        print("D>DEBUG: Swaping Students in Room: " + room1 + " and " + room2)
        return

    def clockin(self, studentobject):  # clock into a room
        """
        Creates a Student Entry into the database.
        From Student Object
        :param studentobject: Primary Object in which to create clockin entry
        """
        conn = sqlite3.connect(self.databasefile)  # create connection to database
        c = conn.cursor()
        mytuple = [studentobject.studentid, studentobject.name, studentobject.clockindate, studentobject.room,
                   studentobject.clockintime, studentobject.clockouttime]
        print("D>DEBUG: Clocking Student in...")
        try:
            c.execute("INSERT INTO student_table1 values (?, ?, ?, ?, ?, ?)", mytuple)
        except sqlite3.IntegrityError:
            print("D>ERROR: Sqlite3 Integrity Error")  # make this return statement!
        conn.commit()
        conn.close()

    def gathercollection(self):
        """
        This Function Reads the Whole database, and creates a StudentCollection out of Them.
        :return: Collection of ALL Students
        """
        conn = sqlite3.connect(self.databasefile)  # create connection to database
        c = conn.cursor()
        c.execute("SELECT * FROM student_table1")
        myrawlist = c.fetchall()  # fetch from execute
        conn.commit()
        conn.close()
        mystudentcollection = StudentCollection()
        mystudentcollection.convertraw(myrawlist)  # converts myrawlist to collection to .listofstudents
        return mystudentcollection

    @staticmethod
    def dailycollection(studentcollection, currentdate):
        """
        Given Student Collection, parse through the data of all students of THE DAY inside of .listofstudents
        :param studentcollection: Collection of Student Objects, will be reading Date for comparison
        :param currentdate: Format is: 2015-12-31
        :return: Collection of students ONLY for the current day
        """
        mystudentcollection = StudentCollection()  # to return the smaller collection
        for student in studentcollection.listofstudents:  # for each student in Studentcollection
            if student.clockindate == currentdate:
                mystudentcollection.listofstudents.append(student)
        return mystudentcollection

    @staticmethod
    def whosclockedin(dailystudentcollection):
        """
        Given the students clocked in currently today, returns those that are clocked in, or have None as clockouttime
        :param dailystudentcollection: Collection of students only for today.
        :return: CurrentLogins, very small collection of 0-5 logins
        """
        mystudentcollection = StudentCollection()
        for student in dailystudentcollection.listofstudents:
            if student.clockouttime is None:
                mystudentcollection.listofstudents.append(student)
        return mystudentcollection  # return of studentcollection of ONLY those logged in

    def clockout(self, studentobject):  # clock out of a room
        """
        Search through studentidnumbers in database and add to last column clockout time.
        Will skip over Database entries that are already clocked out, with same information
        :param studentobject Primary Object to create clockin entry
        """
        print("D>DEBUG: Clockout function attempted...")
        conn = sqlite3.connect(self.databasefile)
        c = conn.cursor()
        mytuple = [studentobject.clockouttime, studentobject.studentid, studentobject.name,
                   studentobject.clockindate, studentobject.room, studentobject.clockintime]
        try:
            print("D>DEBUG: tuple:" + str(mytuple))
            c.execute("UPDATE student_table1 SET CLOCKOUT = ? WHERE ID  = ? AND NAME = ? \
                      AND DATE = ? AND ROOM = ? AND CLOCKIN = ?", mytuple)
        except sqlite3.IntegrityError:
            print("D>ERROR: Sqlite3 Integrity Error")
        conn.commit()
        conn.close()

