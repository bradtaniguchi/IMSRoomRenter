# IMSExcelGUI
#### Bradley Taniguchi
#### 1/21/16
#### IMS Excel GUI Log-in app
#### Created for the CSUDH Instructional Media Services study room timesheet.
This program is writen in Python3 and handles an Sqlite3 database to keep track of logins, and logouts.

###LOGIN PROCEDURE:
    Requires a student to input name ID and choose which room they would like to checkinto. 
    Creates an entry into the Sqlite database with the following atribs:
    - ID 
    - Name
    - Date
    - Room Number
    - TimeIn
    - TimeOut (Left as None when clocking in)
###LOGOUT PROCEDURE
    Requires a student to comfirm their entry data, and logout thru clicking button.
    Edits the corresponding database entry under TimeOut

Project Hosted on github [here][1]
Download Program [here][2]

###License
    Copyright (C) 2016  Bradley Taniguchi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
###Contributions
This programing, being a personal project means any contributions should be focused on bug fixing 
or optimization. Any other contributions can be handled on a sitatuation to situation basis. 

###Maintainers
The project is currently in final project form, but still being maintained if bugs are found.
Maintained by [Bradley Taniguchi][3]

updated: 1/21/16

[1]: https://github.com/bradtaniguchi/IMSExcelGUI
[2]: https://github.com/bradtaniguchi/IMSExcelGUI/archive/master.zip
[3]: https://github.com/bradtaniguchi