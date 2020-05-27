#!/usr/bin/env python3
# Convert HEIC2JPEG
# R.Fichtenau
# 27.05.2020
# ///////////////////////////////////////


# Imports
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import subprocess
from subprocess import *

# Variablen
myDir = ""
myBilder = []

# Window def
window = tkinter.Tk()
window.title("HIEC 2 JPEG")
window.geometry('430x200')


# Funktionen
def clickedPath():
    global myDir
    root = tkinter.Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(parent=root, initialdir="/home", title="Verzeichnis auswählen")
    myDir = dirname
    tbPfad.delete( 1.0,END)
    tbPfad.insert( END,dirname)
    Anzahl(dirname)


def Conversion():
    global myDir
    Anzahl(myDir)
    global myBilder
    cmd = "cd " + myDir + "; for file in *.heic; do heif-convert $file ${file/%.heic/.jpg}; done"
    for myBild in myBilder:
        myNewBild = myBild[0:-4] + "jpg"
        cmd = "cd " + myDir + " && heif-convert '" + myBild + "' '" + myNewBild + "'"
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT,
            close_fds=False)
        #messagebox.showinfo('Message title', cmd)

def Anzahl(mypdir):
    global myBilder
    print(mypdir)
    if os.path.isdir(mypdir):
        Counter = 0
        Files = os.listdir(mypdir)
        for File in Files:
            [Dummy, Ext] = os.path.splitext(File)
            if Ext == ".heic":
                Counter += 1
                myBilder.append(File)
            elif Ext == ".HEIC":
                Counter += 1
                myBilder.append(File)
        lblANZ.configure(text= str(Counter) + " Bilder")

def quit():
       window.destroy()


# Button Verzeichnis
btnPfad = tkinter.Button(window,text='Verzeichnis auswählen', command=clickedPath)
btnPfad.grid( columnspan=2,row=0)



# Pfadangabe
lbl = tkinter.Label(window, text="Verzeichnis:")
lbl.grid(column=0, row=1)
tbPfad = tkinter.Text(window, height=2, width=30)
tbPfad.insert( END,"")
tbPfad.grid(column=1, row=1)

# Anzahl Bilder
lblANZ = tkinter.Label(window, text="0")
lblANZ.grid(column=0, row=3)

# Button Convert
btnConvert= tkinter.Button(window,text='Konvertieren', command=Conversion)
btnConvert.grid(column=1,row=3)

# Button Quit
lbldummy1 = tkinter.Label(window, text="")
lbldummy1.grid(column=0, row=4)
lbldummy2 = tkinter.Label(window, text="")
lbldummy2.grid(column=0, row=5)
btnQuit = tkinter.Button(window,text='Beenden', command=quit)
btnQuit.grid( columnspan=2,row=6)
lbldummy2 = tkinter.Label(window, text="In Herbrechtingen ist es immer am schönsten!!!")
lbldummy2.grid( columnspan=2, row=7)


# Wiederholung
window.mainloop()