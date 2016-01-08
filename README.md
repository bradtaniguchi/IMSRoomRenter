# IMSExcelGUI
### Bradley Taniguchi
### 1/7/16
### IMS Excel GUI Log-in app
### Created for the CSUDH Instructional Media Services study room timesheet.
This program is writen in Python3 and handles an Sqlite3 database to keep track of logins, and logouts.

####LOGIN PROCEDURE:
    Requires a student to input name ID and choose which room they would like to checkinto. 
    Creates an entry into the Sqlite database with the following atribs:
    - ID 
    - Name
    - Date
    - Room Number
    - TimeIn
    - TimeOut (Left as None when clocking in)
####LOGOUT PROCEDURE
    Requires a student to comfirm their entry data, and logout thru clicking button.
    Edits the corresponding database entry under TimeOut

Project Hosted at: https://github.com/bradtaniguchi/IMSExcelGUI
Download Program here: https://github.com/bradtaniguchi/IMSExcelGUI/archive/master.zip
updated: 1/7/16
