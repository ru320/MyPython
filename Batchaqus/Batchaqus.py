# Batchaqus.py
# v1.00
# Programm um Abaqus Decks zu starten und zu Tailen
# 24.04.2021 von Ruediger Fichtenau
# History: 
# 24.04.2021 RF Initialversion


################### IMPORTS
import tkinter.filedialog
import tkinter.ttk
import tkinter as tk
from datetime import datetime
import time
import os.path
from pynotifier import Notification
import sys


################### Variablen
DurationTime = 10
nCPUList = []
for i in range(os.cpu_count()):
    nCPUList.append(i+1)



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

#- RunCAE
def RunCAE():
    print('Run CAE')

#- Runabaqus
def Runabaqus():
    print('Run abaqus')

#- Terminate
def Terminate():
    print('Terminate')

#- Suspend
def Suspend():
    print('Suspend')

#- Resume
def Resume():
    print('Resume')



################### main Form
root = tk.Tk()
canvas  = tk.Canvas(root,width = 600,height = 300,bg='black')
canvas.grid(columnspan=5, rowspan=10)

pixelVirtual = tk.PhotoImage(width=1, height=1)


#- Button Beenden
Beenden_btn = tk.Button(root, text='Close', command=lambda:Close(), font='AvenirNextCondensed',bg='black',fg='white',image=pixelVirtual,compound="c",width = 115)
Beenden_btn.grid(column=0,row=0)

#- Button Verzeichnis waehlen
VZ_btn = tk.Button(root, text='Choose Folder', command=lambda:ChooseFLD(), font='AvenirNextCondensed',bg='black',fg='white',image=pixelVirtual,compound="c",width = 115)
VZ_btn.grid(column=1,row=0)

#- Lable CPUs
CPU_Lbl = tk.Label(root,text='CPUs', font='AvenirNextCondensed',bg='black',fg='white',image=pixelVirtual,compound="c",width = 115)
CPU_Lbl.grid(column=0,row=1)

#- Combobox CPUs
nCPUs = tk.IntVar()
CPU_CBX = tk.ttk.Combobox(root,text='CPUs', font='AvenirNextCondensed',width = 16,textvariable = nCPUs,state='readonly')
CPU_CBX['values'] = nCPUList
CPU_CBX.grid(column=1,row=1)
CPU_CBX.set(os.cpu_count())

#- Lable Version
Version_Lbl = tk.Label(root,text='Version', font='AvenirNextCondensed',bg='black',fg='white',image=pixelVirtual,compound="c",width = 115)
Version_Lbl.grid(column=0,row=2)

#- Button CAE
CAE_btn = tk.Button(root, text='CAE', command=lambda:RunCAE(), font='AvenirNextCondensed',bg='lightblue',fg='black',image=pixelVirtual,compound="c",width = 115)
CAE_btn.grid(column=2,row=0)

#- Button Abaqus
CAE_btn = tk.Button(root, text='abaqus', command=lambda:Runabaqus(), font='AvenirNextCondensed',bg='lightblue',fg='black',image=pixelVirtual,compound="c",width = 115,height=72)
CAE_btn.grid(column=2,row=1, rowspan= 2)

#- Terminate CAE
Terminate_btn = tk.Button(root, text='Terminate', command=lambda:Terminate(), font='AvenirNextCondensed',bg='red',fg='black',image=pixelVirtual,compound="c",width = 115)
Terminate_btn.grid(column=3,row=0)

#- supend CAE
Suspend_btn = tk.Button(root, text='Suspend', command=lambda:Suspend(), font='AvenirNextCondensed',bg='orange',fg='black',image=pixelVirtual,compound="c",width = 115)
Suspend_btn.grid(column=3,row=1)

#- Resume CAE
Resume_btn = tk.Button(root, text='Resume', command=lambda:Resume(), font='AvenirNextCondensed',bg='green',fg='black',image=pixelVirtual,compound="c",width = 115)
Resume_btn.grid(column=3,row=2)



#- TextBox Verzeichnis
VZ_TB_Variable = tk.StringVar()
VZ_TB = tk.Entry(root,textvariable=VZ_TB_Variable,font='AvenirNextCondensed',bg='black',fg='white')
VZ_TB.grid(column=0,row=3,columnspan=5,sticky = tk.W+tk.E)

#- TextBox Command
CMD_TB_Variable = tk.StringVar()
CMD_TB = tk.Entry(root,textvariable=CMD_TB_Variable,font='AvenirNextCondensed',bg='black',fg='white')
CMD_TB.grid(column=0,row=4,columnspan=5,sticky = tk.W+tk.E)


root.mainloop()
print(nCPUs.get())

