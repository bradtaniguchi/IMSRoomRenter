#!/usr/bin/env python3
# Bradley Taniguchi
# 12/21/15

from datetime import datetime
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
        returnstring = "ID" + str(self.studentid) + " Name: " + str(self.name) + " ClockinDate " \
                       + str(self.clockindate) + " Room: " + str(self.room) + " ClockinTime: " + str(self.clockintime)\
                       + " ClockoutTime: " + str(self.clockouttime)
        return returnstring

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
            print(">DEBUG: Contents of convertraw:" + str(self.listofstudents))  # NEEDS TESTING!

    def printcontents(self):
        """
        Prints the contents of listofstudents
        :return: String of object classes and their contents
        """
        mystring = ""
        for Student in self.listofstudents:
            mystring += (Student.printvalues())
        return mystring  # TEST THIS!


class DataBaseInterface:
    """
    Primary Database interface handler
    """
    def __init__(self, filename='bin/Sqlite/StudentDatabase.sqlite'):  # currently redundant
        self.filedirectory = filename
        self.databasefile = os.path.join(os.path.dirname(__file__), str(filename))
        #self.conn = sqlite3.connect(self.databasefile) # forgot about conn.commit, conn.close
        #self.c = self.conn.cursor()
        if os.path.isfile(self.databasefile):
            print(">DEBUG: File Exists!")
        else:
            print(">DEBUG: File Doesn't Exist, creating it now..")
            print(str(self.databasefile))
            print(str(filename))
            self._createstudentdatabase(self.databasefile)  # create the file

    def _createstudentdatabase(self, database):
        """
        Creates The Student Database if there isn't one already
        :return: true if creating database was a succuess
        """
        conn = sqlite3.connect(database)  # create connection to database
        c = conn.cursor()
        print(">DEBUG: Creating Student Database at: " + self.filedirectory)
        c.execute('''CREATE TABLE student_table1
                 (ID INT PRIMARY KEY NOT NULL,
                  NAME CHAR(32) NOT NULL,
                  DATE TEXT NOT NULL,
                  ROOM INT NOT NULL,
                  CLOCKIN TEXT NOT NULL,
                  CLOCKOUT TEXT)''')
        conn.commit()
        conn.close()
        print(">DEBUG: Database Created Successfully!")

    def clockin(self, studentobject):  # clock into a room
        """
        Creates a Student Entry into the database.
        From Student Object
        :param studentobject: Primary Object in which to create clockin entry
        """
        #studentobject = Student(studentobject)  # cast studentobject as Student
        conn = sqlite3.connect(self.databasefile)  # create connection to database
        c = conn.cursor()
        mytuple = [studentobject.studentid, studentobject.name, studentobject.clockindate, studentobject.room,
                   studentobject.clockintime, studentobject.clockouttime]
        print(">DEBUG: Using INSERT INTO")
        try:
            c.execute("INSERT INTO student_table1 values (?, ?, ?, ?, ?, ?)", mytuple)
            print("SUCCESS: Added Student login:" + studentobject.name + " at " + studentobject.clockintime)  # make this return statement!
        except sqlite3.IntegrityError:
            print("ERROR: Sqlite3 Integrity Error")  # make this return statement!
        #except sqlite3.OperationalError:
        #    print("ERROR: Sqlite3 OperationalError, with inputs: " + str(mytuple))
        conn.commit()
        conn.close()

    def gathercollection(self, year, month, day):
        """
        NOTE: Learn how to parse through database by time.
        Reads Database and returns StudentCollection list for the current day.
        :return: returns a StudentCollection list for the current day
        """
        print(">DEBUG: GatherCollection called....")

    @staticmethod
    def clockout(studentidnumber, studentname):  # clock out of a room
        """
        Search through studentidnumbers in database and add to last column clockout time.
        :param studentidnumber: Primary Key for Searches
        :param studentname:  Seconary key for Searches, If unmatched raise exception
        :return:
        """
        print(">DEBUG: Clockout function attempted...")