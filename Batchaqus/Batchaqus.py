# Batchaqus.py
# v1.00
# Programm um Abaqus Decks zu starten und zu Tailen
# 24.04.2021 von Ruediger Fichtenau
# History: 
# 24.04.2021 RF Initialversion


################### IMPORTS
import tkinter.filedialog
import tkinter as tk
from datetime import datetime
import time
import os.path
from pynotifier import Notification


################### Variablen
DurationTime = 10



################### Defs
#- Notification
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

#- Close GUI
def Close():
    root.destroy()

#- Choose Folder GUI
def ChooseFLD():
    print('Choose Folder')
    WorkingDir = tk.filedialog.askdirectory()
    VZ_TB_Variable.set(WorkingDir)

################### main Form
root = tk.Tk()
canvas  = tk.Canvas(root,width = 700,height = 300,bg='black')
canvas.grid(columnspan=5, rowspan=10)


#- Button Beenden
Beenden_btn = tk.Button(root, text='Close', command=lambda:Close(), font='AvenirNextCondensed',bg='black',fg='white')
Beenden_btn.grid(column=0,row=0)

#- Button Verzeichnis waehlen
VZ_btn = tk.Button(root, text='Choose Folder', command=lambda:ChooseFLD(), font='AvenirNextCondensed',bg='black',fg='white')
VZ_btn.grid(column=1,row=0)

#- TextBox Verzeichnis
VZ_TB_Variable = tk.StringVar()
VZ_TB = tk.Entry(root,textvariable=VZ_TB_Variable,font='AvenirNextCondensed',bg='black',fg='white')
VZ_TB.grid(column=0,row=1,columnspan=5,sticky = tk.W+tk.E)

#- TextBox Command
CMD_TB_Variable = tk.StringVar()
CMD_TB = tk.Entry(root,textvariable=CMD_TB_Variable,font='AvenirNextCondensed',bg='black',fg='white')
CMD_TB.grid(column=0,row=2,columnspan=5,sticky = tk.W+tk.E)


root.mainloop()

