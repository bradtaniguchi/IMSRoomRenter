# Bradley Taniguchi
# Swap Test, to check logic and structure.
# Could be simplified, but this way its VERY easy to understand whats going on
# Easier to impliment back into main program

def test(studentinroom1exists, studentinroom2exists):
    Flag = False  # flag that rooms have been changed
    if (not studentinroom1exists) or (not studentinroom2exists):  # both are in rooms
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("NO Students in Either Room!")
        Flag = True
    if (studentinroom1exists) and (not studentinroom2exists):  # Student In Room1, but no one in Room2
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("Moving Student1 into Room2")
        Flag = True
    if (not studentinroom1exists) and (studentinroom2exists):  # No one in Room1, but Student in Room2
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("Moving Student2 into Room1")
        Flag = True
    if not Flag:  # really the "else"
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("Swapping Both Rooms")

print("================\n\n")
test(True, True)
print("================\n\n")
test(True, False)
print("================\n\n")
test(False, True)
print("================\n\n")
test(True, False)
