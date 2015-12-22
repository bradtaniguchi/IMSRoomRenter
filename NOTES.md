# IMSExcelGUI
### Bradley Taniguchi
### 11/17/18
### IMS Excel GUI Log-in app
##### Created for the CSUDH Instructional Media Services study room timesheet.
This program is writen in python and handles an excel spreadsheet for room logins.
The following Attributes are Mandatory during login
1. Name
2. ID
3. Room (0 is unknown)
The Following are Automatically filled out during login:
1. Date
2. Time
The Following are Automatically filled out during logout:
1. Date
2. Time

LOGIN PROCEDURE:
  Requires a student to input name, where all following data values will be linked to in an object, the ID and room.
  Program checks to see if student currently logged in or logged out.
  IF not Logged in:
    ask for ID, and Room number(optional)
  IF Logged in:
    ask to log out of Room (shows room number of NOT 0)
    
  OPTIONAL FEATURES:
    AutoCompletion for Student names, allowing quicker logins, relogins
    Admin login, allowing for editing, viewing of current logged in students
###===============NOTES===============
http://stackoverflow.com/questions/8514471/proper-installation-script-for-a-small-python-program-not-module-under-linux

####------UPDATE 12/16/15
Starting on project Friday
going to use sqlite3
EX: conn = sqlite3.connect('example.db')
sqlite3 needs to be installed to test. Or at least have a test database file
to play around with.

https://www.sqlite.org/download.html

- x64 bit version .dll 
#####AND
- sqlite3 console.

documentation to follow once database is setup(.dll, .def file) and set to path:
https://www.sqlite.org/cli.html

####-------UPDATE 12/18/15
Started re-organized code into GUI.py, going to remove main.py soon.
added basic GUI functionality, no actual functionality
still need to work ClockIn and ClockOut

####-------UPDATE 12/21/15
Created most of the menus
added buttons and visual aspects of finished pages
need to create backend