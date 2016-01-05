#!/usr/bin/env python3
# Bradley Taniguchi
# 12/18/15
#SEC = Secondary Classes, to argument the primary GUI components

import tkinter as tk
class Popups(tk.Toplevel):
    def __init__(self, displaytitle="NOTITLE", displaytext="NOMSG", displaybuttontext="Done"):
        tk.Toplevel.__init__(self)  # any controller?
        self.title(displaytitle)
        msg = tk.Message(self, text=displaytext)
        msg.pack()

        button = tk.Button(self, text=displaybuttontext, command=self.exitwindow)
        button.pack()

    def exitwindow(self):
        self.destroy()  # destory popupwindow

class ComfirmationDialog(tk.Toplevel):
    def __init__(self, displaytitle="ComfirmationDialog", displaytext="NOMSG"):
        """
        Creates a TopLevel window, with yes no dialogs
        :param displaytitle: Text to be displayed on titlebar
        :param displaytext: Text to be displayed in the middle of the frame
        :return: True/False for Yes, No button comfirmation. No if frame deletion
        """
