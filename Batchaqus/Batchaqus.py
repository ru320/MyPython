# Batchaqus.py
# v1.00
# Programm um Abaqus Decks zu starten und zu Tailen
# 24.04.2021 von Ruediger Fichtenau
# History: 
# 24.04.2021 RF Initialversion


################### IMPORTS
import tkinter as tk
from datetime import datetime
import time
import os.path
from pynotifier import Notification


################### Variablen


################### Defs
def myNotify(myTitle,myMessage):
    if sys.platform == 'linux':
        Notification(
            title=myTitle,
            description=myMessage,
            # icon_path='Notify.ico', # On Windows .ico is required, on Linux - .png
            duration=DurationTime,                              # Duration in seconds
            urgency='normal',
        ).send()
    else:
        Notification(
            title=myTitle,
            description=myMessage,
            icon_path='Notify.ico', # On Windows .ico is required, on Linux - .png
            duration=DurationTime,                              # Duration in seconds
            urgency='normal',
        ).send()


################### main Form
root = tk.Tk()
canvas  = tk.Canvas(root,width = 600,height = 300)
canvas.grid(columnspan = 4)

root.mainloop()
