# Bradley Taniguchi
# test database handler with sqlite3 
# Python interaction example
# https://docs.python.org/2/library/sqlite3.html
# Sqlite3 example
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

# NOTE on Primary Keys, IE only 1 version. In full version it will be StudentID
# http://www.techonthenet.com/sqlite/primary_keys.php
# In this test we are just using Student names, which wouldn't function correctly as
#   students may have the same name, and thus ruin the programs ability to rent the room

import sqlite3
import os
from datetime import datetime


def main():
    databasefile = os.path.join(os.path.dirname(__file__), 'bin/Sqlite/TestDatabase.sqlite')  # for ./my_file
    conn = sqlite3.connect(databasefile)  # connect to database
    c = conn.cursor()

    print("Starting Program...")
    c.execute('''CREATE TABLE student_table1 \
              (ID INT PRIMARY KEY NOT NULL,
              NAME CHAR(32) NOT NULL,
              DATE TEXT NOT NULL,
              CLOCKIN TEXT NOT NULL,
              CLOCKOUT TEXT)''')
    c.execute('''INSERT INTO student_table1(ID, NAME, DATE, CLOCKIN, CLOCKOUT)
        VALUES (1, 'Brad', '12/31/15','12:50:32', null)''')  # test insert
    c.execute(''' UPDATE student_table1 SET CLOCKOUT = ? WHERE ID = 1''', ('13:00:35',))
    print("Created Database")
    print("test time print " + str(datetime.now().time().hour))
    conn.commit()
    conn.close()
    # need test read from file!

def clockin(cursor, database, identificationnumber, name):
    """
    :param cursor: Cursor inside of database
    :param database: Database to be changed
    :param identificationnumber: ID of student trying to login
    :param name: Name of student trying to clock in
    :return: null
    """
    clockintime = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)  # does not include seconds
    clockindate = str(datetime.now().date())  # format: 2015-12-31
    mytuple = [identificationnumber, name, clockindate,clockintime]
    c = cursor
    print(">DEBUG: Using insertvalue function")
    try:
        c.execute("INSERT INTO {0} ({1}, {2}, {3}, {4})".format(database, mytuple[0], mytuple[1]), mytuple[2])
    except sqlite3.IntegrityError:
        print("ERROR: Sqlite3 Integrity Error")  # example uses primary key, this doesnt so idk if this will be reached

def clockout(cursor, database, identificationnumber):
    """
    :param cursor: Cursor inside of database
    :param database: Database to be changed
    :param identificationnumber: ID of student trying to login
    :return: null
    """
if __name__ == '__main__':
    main()
