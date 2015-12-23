#!/usr/bin/env python3
# Bradley Taniguchi
# 12/21/15

import datetime  # to get time and date


class Student:
    """
    Handles student object creation. Holds data attributes for students logging in and out
    Also handles time function when creating new student.
    FUTURE UPDATE: allow for completion - return
    :input:
        name - Name of the student, primary sorting component (mandatory)
        studentid - Student ID of student login in, (mandatory)
    """
    def __init__(self, name="John Doe", studentid=0):
        self.name = name  # if not given an input, use default IE John Doe
        self.studentid = studentid
        self.date
        # create tuple to hold date, time(hour, minute)

    def createentry(self, room=0, ):
        """
        Change time entry for student
        :return:
        """
        mycurrenttime = datetime.datetime.now().time()
        print(">DEBUG: mycurrenttime variable: \n>   hour: " + str(mycurrenttime._hour) +
              "\n>   min" + str(mycurrenttime))

# add StudentCollection hanlders below