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

py2exe for python3 is here:
https://pypi.python.org/pypi/py2exe/0.9.2.0#downloads

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

####-------UPDATE 12/23/15
####ADDED master branch again, using that instead of getting confused with B1.
####NOTE Finally choosen database type!
    Finally choosen SQLITE as database to use with program. As it seems the easiest to move with the project.
    Requires me to learn the database commands and thus this project should be extended a little longer. But
    should be more capable in terms of expansion.
Finished up basic work with the GUI frames
Started work on the menus GUI. 
Layed groundwork for Backend to interact with sqlite

NOTICE: Can combine a few functions between the two Clock-in and Clock-out classes:
1.validinput
2.validroom
Worth making a parent class for currently 2 functions??

    # NOTE: SQLITE has 5 datatypes:
    #   NULL - returns the value NULL value
    #   INTEGER - The value is a signed integer, stored in 1-8 bytes depending on magnitude
    #   REAL - The value is floating point value, stored as an 8-byte IEEE floating point num
    #   TEXT - The value is a text string, stored using the database encoding (UTF-8, UTF-16BE, UTF-16LE)
    #   BLOB - The value is a blob of data, stored exactly as it was input

####---------UPDATE 12/28/15
So after figuring out how sqlite3 works, I had to open the file
using a cmd terminal. Now onto adding the proper setup rather than
trying to figure out why the sqlite3.exe didn't pick up my file.

SUCCESS: for the most part, apparently I can leave time as a string and parse it later
which seems like the most logical thing to do now. Must change up the what things are formated
and protect against SQLInjection attacks though.

NOTE: Need to create return statements for the createentry function, that way I can check the.
Should also impliment this in other functions not created

####----------UPDATE 12/29/15
Working on StudentLoginClasses, will probably rename.
NEED TO ADD DATES!(12/31/15)

####----------UPDATE 1/3/16 - Happy New year!
Last Day before going back to work, going to start combining the back end with the front end,
Ill leave the Clockout handling for another time. As that requires me to learn how to search through
the Database, which is something I'm not sure how to do yet. 

NOTE: I have found a flaw in how I currently Have my Program setup.
To allow my program to create the database file Under Bin/Sqlite, it requires me to
move out of src. So I have 3 ways to go about this:
1. Move the files to the Main folder
2. Move the place where Ill create the Database
3. Handle it in file, thus creating an abs path in a rather complicated endevour.

Currently going to do the first one, but going to keep the src folder, for graphical purposes

NOTE: It would make things 1 step easier to Remove the RoomAvailability and put everything into 1 page,
thus I can create 1 function that will do what I want without needing to transfer the Student Data and Information.
Which Is what Im going to do now. 

####---------UPDATE 1/4/16
First Day back at school/work
Need to start considering how I am going to handle logouts
1.  
