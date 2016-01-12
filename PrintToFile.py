#!/usr/bin/env python3
# Bradley Taniguchi
# 1/12/16
import tkinter as tk
from SLC import DataBaseInterface
import sqlite3
import os
from datetime import datetime


class PrintToFile(tk.Toplevel):
    """
    Displays a toplevel window that
    """
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("IMSRoomRenter PrintToFile")
        self.primarylabel = tk.Label(self, text="Printing to file...", relief=tk.SUNKEN)
        self.primarylabel.pack()
        self.button = tk.Button(self, text="Done", command=self.exit)
        self.button.pack()

    def createdatabasefile(self, relwritedir, databasepath, tablename):
        """
        Opens file, calls readdatabase, and prints out the contents to the file.
        :param relwritedir: Relative location to write text file to.
        :param databasepath: Relative location to database
        :param tablename: Name of table to read within the database
        # note: os.path.isfile('filepath')
        """
        writefile = os.path.join(os.path.dirname(__file__), relwritedir)  # ADD NAME OF FILE AT END!
        log_file = open(writefile, "w")
        log_file.write("Database PrintOut at: " + str(datetime.now().date()))
        log_file.write(self.readdatabase(databasepath, tablename))

    @staticmethod
    def readdatabase(relfilepath, tablename):
        """
        Reads the Whole Database located at relfilepath, which is relative location to this file.
        :param relfilepath: relative filepath from file to databasefile
        :param tablename: name of file to read.
        :return: String of all tuples within database.
        """
        databasefile = os.path.join(os.path.dirname(__file__), relfilepath)  # check refile
        print("PATH: " + databasefile)
        primarytextstring = ""
        conn = sqlite3.connect(databasefile)
        c = conn.cursor()
        c.execute("SELECT * FROM " + str(tablename))
        myrawlist = c.fetchall()
        for mytuple in myrawlist:
            print(mytuple)
            primarytextstring += (str(mytuple) + "\n")
        print("Number of Students in Database: " + str(len(myrawlist)))
        return primarytextstring

    def exit(self):
        self.quit()
        self.destroy()
