#!/usr/bin/env python3
# Bradley Taniguchi
# 1/4/15
# Quick Dirty Database file checker
from datetime import datetime
import os
import sqlite3

__author__ = 'Bradley Taniguchi'
__version__ = '0.5'


def main():
    print("Daily or Master?")
    print("Dailys[1]")
    print("Master[2]")
    bin = input(">: ")
    if bin > 1:
        masterentries()
    elif bin <= 1:
        dailyentries()
    print("End Program....")


def dailyentries():  # prints out only entries for current date
    print("<<<<<DAILY-ENTIRES>>>>>")


def masterentries():  # prints out ALL entires
    print("<<<<<MASTER-ENTRIES>>>>>")
    databasefile = os.path.join(os.path.dirname(__file__), 'bin/Sqlite/StudentDatabase.sqlite')
    conn = sqlite3.connect(databasefile)  # connect to the database
    c = conn.cursor()
    print("Starting Program... Connect to database at: " + databasefile)
    print("  ID----NAME----DATE----ROOM--TIMEIN-TIMEOUT")
    c.execute("SELECT * FROM student_table1")
    print(c.fetchall())

if __name__ == '__main__':
    main()
