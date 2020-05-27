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



# Window def
window = tkinter.Tk()
window.title("HIEC 2 JPEG")
window.geometry('430x200')


# Funktionen
def clickedPath():
    root = tkinter.Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(parent=root, initialdir="/home", title="Verzeichnis auswählen")
    tbPfad.delete( 1.0,END)
    tbPfad.insert( END,dirname)
    Anzahl(dirname)

def Conversion():
    messagebox.showinfo('Message title', 'Message content')

def Anzahl(mypdir):
    print(mypdir)
    if os.path.isdir(mypdir):
        Counter = 0
        Files = os.listdir(mypdir)
        for File in Files:
            [Dummy, Ext] = os.path.splitext(File)
            if Ext == ".heic":
                Counter += 1
            elif Ext == ".HEIC":
                Counter += 1
        lblANZ.configure(text= str(Counter) + " Bilder")

def quit():
       window.destroy()


# Button Verzeichnis
btnPfad = tkinter.Button(window,text='Verzeichnis auswählen', command=clickedPath)
btnPfad.grid(column=0,row=0)



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
btnQuit.grid(column=1,row=6)


# Wiederholung
window.mainloop()