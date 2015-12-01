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
===============NOTES===============
http://stackoverflow.com/questions/8514471/proper-installation-script-for-a-small-python-program-not-module-under-linux

