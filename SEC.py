#!/usr/bin/env python3
# Bradley Taniguchi
# 12/18/15
#SEC = Secondary Classes, to argument the primary GUI components

import tkinter as tk
from tkinter import scrolledtext  # for large textbox

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

class DebugBox(tk.Toplevel):
    """
    Displays a large uneditable text area to display current contents of database
    """
    def __init__(self, displaytitle="DebugBox", displaytext="NOMSG", displaybuttontext="done"):
        tk.Toplevel.__init__(self)
        self.title(displaytitle)
        self.textfield = scrolledtext.ScrolledText(master=self,
                                                   wrap=tk.WORD,
                                                   width=50,
                                                   height=20)
        self.inserttext(displaytext)
        self.textfield.configure(state='disabled')
        self.textfield.pack()

    def inserttext(self, text):
        self.textfield.insert(tk.INSERT, text)

class ComfirmationDialog(tk.Toplevel):
    def __init__(self, displaytitle="ComfirmationDialog", displaytext="NOMSG"):
        """
        Creates a TopLevel window, with yes no dialogs
        :param displaytitle: Text to be displayed on titlebar
        :param displaytext: Text to be displayed in the middle of the frame
        :return: True/False for Yes, No button comfirmation. No if frame deletion
        """
        #CLEARLY UNFINISHED!