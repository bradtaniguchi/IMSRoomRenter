#!/usr/bin/env python3
# Bradley Taniguchi
# 1/4/15
# Quick Dirty Database file checker
from datetime import datetime
import os
import sqlite3
import SLC  # to create studentcollection/ students

__author__ = 'Bradley Taniguchi'
__version__ = '0.5'


def main():
    print("Daily or Master?")
    print("Dailys[1]")
    print("Master[2]")
    bin = input("> ")
    if int(bin) > 1:
        masterentries()
    elif bin <= 1:
        dailyentries()
    print("<<<<<<End Program>>>>>>>")


def dailyentries():  # prints out only entries for current date
    """
    Reads WHOLE database, prints out only those with column[2] that accord with date.
    NOTE: Date format is: 2015-12-31
    IMPORTANT test area for later parsing.
    """
    print("<<<<<DAILY-ENTIRES>>>>>")


def masterentries():  # prints out ALL entires
    """
    TestField to create studentObjects
    NOTE: Format from Database:
    (12356, 'brad', '2016-01-05', 5, '12:49', 'NULL')
    """
    print("<<<<<MASTER-ENTRIES>>>>>")
    databasefile = os.path.join(os.path.dirname(__file__), 'bin/Sqlite/StudentDatabase.sqlite')
    conn = sqlite3.connect(databasefile)  # connect to the database
    c = conn.cursor()
    print("Starting Program... Connect to database at: " + databasefile)
    print("  ID----NAME----DATE----ROOM--TIMEIN---TIMEOUT")
    c.execute("SELECT * FROM student_table1")
    myrawlist = c.fetchall()
    for tuple in myrawlist:
        print(tuple)  # creates new line for each
        mystudent = SLC.Student(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])
        print(">DEBUG: mystudent created with data: " )

if __name__ == '__main__':
    main()
