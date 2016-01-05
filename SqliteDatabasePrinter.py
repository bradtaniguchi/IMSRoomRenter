#!/usr/bin/env python3
# Bradley Taniguchi
# 1/4/15
# Quick Dirty Database file checker
import os
import sqlite3

__author__ = 'Bradley Taniguchi'
__version__ = '0.5'


def main():
    databasefile = os.path.join(os.path.dirname(__file__), 'bin/Sqlite/StudentDatabase.sqlite')
    conn = sqlite3.connect(databasefile)  # connect to the database
    c = conn.cursor()
    print("Starting Program... Connect to database at: " + databasefile)
    print("  ID----NAME----DATE----ROOM--TIMEIN-TIMEOUT")
    c.execute("SELECT * FROM student_table1")
    print(c.fetchall())

if __name__ == '__main__':
    main()
