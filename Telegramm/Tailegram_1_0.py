

################### IMPORTS
from  tkinter import *
from datetime import datetime
import time
import Telegram
import os.path
from pynotifier import Notification


################### Variablen
myFile2Tail = "B:\Temp\Polygon_Rasthaken_Typ_E_3.sta"
print(myFile2Tail)
myRunBool = True
myMessage= str(datetime.now())
myOutputline = ''
SleepTime = 180
DurationTime = 10
Exit = False

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

################### GUI
root = Tk(  )
b = 0
for r in range(2):
   for c in range(2):
      b = b + 1
      Button(root, text = str(b), borderwidth = 1 ).grid(row = r,column = c)


# root.mainloop()

if os.path.isfile('./Notify.png'):
    myNotify("Da ", str(datetime.now()))
else:
    myNotify("nicht da ", str(datetime.now()))