from datetime import datetime
import time
import Telegram
import os.path
from pynotifier import Notification

myFile2Tail = "B:\Temp\Polygon_Rasthaken_Typ_E_3.sta"
print(myFile2Tail)
myRunBool = True
myMessage= str(datetime.now())
myOutputline = ''
SleepTime = 180
DurationTime = 10
Exit = False

def myNotify(myTitle,myMessage):
    Notification(
        title=myTitle,
        description=myMessage,
        icon_path="abq_Batcher.png.ico", # On Windows .ico is required, on Linux - .png
        duration=DurationTime,                              # Duration in seconds
        urgency='normal'
    ).send()


Telegram.SendMultTelegram("Start " + myFile2Tail)
Telegram.SendMultTelegram(datetime.now())
myNotify("Start " + myFile2Tail, str(datetime.now()))
time.sleep(DurationTime)

while myRunBool:
    if os.path.isfile(myFile2Tail):
        with open(myFile2Tail, encoding='utf8') as f:
            for line in f:
                myOutputline = line.strip()
                if "THE ANALYSIS HAS COMPLETED SUCCESSFULLY" in myOutputline:
                    myRunBool = False
                    Telegram.SendMultTelegram(myFile2Tail + " ist fertig")
                    Telegram.SendMultTelegram(datetime.now())
                    myNotify(myFile2Tail + " ist fertig", str(datetime.now()))
                    Exit  =True
                if "THE ANALYSIS HAS NOT BEEN COMPLETED" in myOutputline or "***ERROR: Process terminated by" in myOutputline:
                    myRunBool = False
                    Telegram.SendMultTelegram(myFile2Tail + " hat abgebrochen")
                    Telegram.SendMultTelegram(datetime.now())
                    myNotify(myFile2Tail + " hat abgebrochen", str(datetime.now()))
                    Exit  =True
            if myOutputline != myMessage:
                myMessage = myOutputline
                Telegram.SendMultTelegram(myOutputline)
                myNotify(myFile2Tail , myOutputline)
            if Exit:
                break
            time.sleep(SleepTime)
    else:
            time.sleep(SleepTime)

Telegram.SendMultTelegram("Programm Beendet " + myFile2Tail)
myNotify("Programm beendet " + myFile2Tail, str(datetime.now()))
