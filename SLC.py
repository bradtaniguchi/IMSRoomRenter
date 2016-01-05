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
    def __init__(self, studentid=0, name="John Doe", room=0):
        self.name = name  # if not given an input, use default IE John Doe
        self.studentid = studentid
        self.room = room  # default room 0, before choosen room


class StudentCollection:
    """
    Student handler and creation aspect.
    """
    def __init__(self, listofstudents=None):  # DO NOT USE: list = [], GOTME!
        if listofstudents is None:
            listofstudents = []  # list of student classes
    # WORK HERE WITH SEARCH ALGORITHM IF NEEDED!


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

    def clockin(self, studentidnumber, studentname, roomnumber):  # clock into a room
        """
        Creates a Student Entry into the database.
        Date format is : 2015-12-31
        :param studentidnumber: ID number of student, PRIMARY KEY for searches
        :param studentname: Name of Student logging in.
        :param roomnumber: Room checking into
        """
        conn = sqlite3.connect(self.databasefile)  # create connection to database
        c = conn.cursor()
        clockintime = str(datetime.now().time().hour) + ':' + str(datetime.now().time().minute)  # doesn't include secs
        clockindate = str(datetime.now().date())  # format: 2015-12-31
        clockouttime = "NULL"
        mytuple = [studentidnumber, studentname, clockindate, roomnumber, clockintime, clockouttime]
        print(">DEBUG: Using INSERT INTO")
        try:
            #c.execute("INSERT INTO {0} ({1}, {2}, {3}, {4}, {5})".format(
            #        "student_table1", mytuple[0], mytuple[1], mytuple[2], mytuple[3], mytuple[4]))
            c.execute("INSERT INTO student_table1 values (?, ?, ?, ?, ?, ?)", mytuple)
            print("SUCCESS: Added Student login:" + studentname + " at " + clockintime)  # make this return statement!
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