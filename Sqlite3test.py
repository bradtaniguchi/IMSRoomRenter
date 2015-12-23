# Bradley Taniguchi
# test database handler with sqlite3 
# Python interaction example
# https://docs.python.org/2/library/sqlite3.html
# Sqlite3 example
# http://www.thegeekstuff.com/2012/09/sqlite-command-examples/

import sqlite3

conn = sqlite3.connect('example.database')  # connect to database
c = conn.cursor()


# create table, NOT NECCESSARY in primary program
c.execute('''CREATE TABLE Students (name text, )''')