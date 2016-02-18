# Bradley Taniguchi
# Swap Test, to check logic and structure.
# Could be simplified, but this way its VERY easy to understand whats going on
# Easier to impliment back into main program


def test(studentinroom1exists, studentinroom2exists):
    if studentinroom1exists and studentinroom2exists:  # Both have people in rooms
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("Swap Students in both Rooms!")
        return
    elif studentinroom1exists and (not studentinroom2exists):  # Student In Room1, but no one in Room2
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("Moving Student1 into Room2")
        return
    elif (not studentinroom1exists) and studentinroom2exists:  # No one in Room1, but Student in Room2
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("Moving Student2 into Room1")
        return
    else:  # Gets here if NO ONE IN ROOMS
        print(">>>" + str(studentinroom1exists) + ">>>" + str(studentinroom2exists))
        print("ERROR! NO ONE IN ROOMS!")
        return

print("================\n\n")
test(True, True)
print("================\n\n")
test(True, False)
print("================\n\n")
test(False, True)
print("================\n\n")
test(True, False)
