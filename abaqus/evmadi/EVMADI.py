# evmadi.py
# v1.00
# Programm um Abaqus Decks zu starten und zu Tailen
# 02.10.2021 von Ruediger Fichtenau
# History: 
# 02.10.2021 RF Initialversion


################### IMPORTS
from os import remove
import tkinter.filedialog
import tkinter.ttk
import tkinter as tk
import time
import os.path
import sys
import base64
from io import BytesIO


################### Variablen
Version = '1.0'
data = b'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'
image_64_decode = base64.decodebytes(data) 
image_result = open('DI_Logo.png', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)

#- FunktionsVariablen
myFile = ''
View_row = 1

#- Gui Variables
BTN_Dict = {}


#- Close GUI
def Close():
    root.destroy()

#- Choose File GUI
def ChooseFILE():
    global myFile
    print('Choose File')
    myFile = tk.filedialog.askopenfilename(title = "Select XML file for EVMADI",filetypes = (("XML Files","*.xml"),))
    LoadSettings()

#- Load Settings
def LoadSettings():
    global View_row
    View_row = 0
    print('Load ' + myFile)
    for i in range(20):
        AddRow()

#- Save Settings
def Save():
    print('Save ' + myFile)

#- Remove Row
def RemoveRow(FrameName,Local_row,Local_col):
    print(FrameName, Local_row, Local_col)
    BTNName = 'BTN_' + FrameName + '_' + str(Local_col) + '_' + str(Local_row)
    btn = BTN_Dict[BTNName]
    btn.destroy()

#- Add View Row
def AddRow():
    global View_row
    print(View_row)
    View_row += 1

#- Add BTN
def AddBTN(Frame,FrameName,Local_row,Local_col):
    print(FrameName, Local_row, Local_col)
    Name = 'BTN_' + FrameName + '_' + str(Local_col) + '_' + str(Local_row)
    btn =  tk.Button(Frame, text='Close', command=lambda:RemoveRow(FrameName, Local_row, Local_col), font='AvenirNextCondensed',bg='black',fg='white',image=pixelVirtual,compound="c",width = 115)
    btn.grid(column=Local_col,row=Local_row)
    BTN_Dict[Name] = btn


################### main Form
root = tk.Tk()
root.title('EVMADI ' + Version)
root.configure(background='white')
rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
# canvas  = tk.Canvas(root,width = 600,height = 300,bg='white')
# canvas  = tk.Canvas(root,bg='white')
# canvas.grid(columnspan=1, rowspan=3)

pixelVirtual = tk.PhotoImage(width=1, height=1)

#- Logo
Logo_Frame = tk.Frame(root, bg='white', width=450, height=50, pady=3)
Logo_Frame.grid(column=0,row=0)
Logo = tk.PhotoImage(file="DI_Logo.png")  
Logo_Label = tk.Label(Logo_Frame,image=Logo,bg='white')
Logo_Label.grid(column=1,row=0)

#- Results Headder Grid
Results_Headder_Frame = tk.Frame(root, bg='#f89c0e', width=450, height=50, pady=3)
Results_Headder_Frame.grid(column=0,row=1)
Results_Label = tk.Label(Results_Headder_Frame, text= 'Saved Results') 
Results_Label.grid(column=0,row=0) 

#- Results Grid
Results_Frame = tk.Frame(root, bg='grey', width=450, height=50, pady=3)
Results_Frame.grid(column=0,row=2)
for i, j in zip(range(5), range(10)):
    btn =  tk.Button(Results_Frame, text='Close', command=lambda:Close(), font='AvenirNextCondensed',bg='black',fg='white',image=pixelVirtual,compound="c")
    btn.grid(column=i,row=j)

#- View Headder Grid
View_Headder_Frame = tk.Frame(root, bg='#f89c0e', width=450, height=50, pady=3)
View_Headder_Frame.grid(column=0,row=3)
View_Label = tk.Label(View_Headder_Frame, text= 'Saved Views') 
View_Label.grid(column=0,row=0) 

#- View Grid
View_Frame = tk.Frame(root, bg='white', width=rootWidth, height=rootHeight, pady=3)
View_Frame.grid(column=0,row=4)
for i in range(5):
    for j in range(2):
        AddBTN(View_Frame, 'VIEWFrame', i, j)

##- Buttons Grid
Buttons_Frame = tk.Frame(root, bg='grey', width=450, height=50, pady=3)
Buttons_Frame.grid(column=0,row=5)
myCol = 0
#- Load BTN
btn =  tk.Button(Buttons_Frame, text='Load', command=lambda:ChooseFILE(), font='AvenirNextCondensed',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- ReLoad BTN
btn =  tk.Button(Buttons_Frame, text='Reload', command=lambda:LoadSettings(), font='AvenirNextCondensed',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- Save BTN
btn =  tk.Button(Buttons_Frame, text='Save', command=lambda:Save(), font='AvenirNextCondensed',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- Close BTN
btn =  tk.Button(Buttons_Frame, text='Close', command=lambda:Close(), font='AvenirNextCondensed',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1

##- Label Grid
Label_Frame = tk.Frame(root, bg='#f89c0e', width=450, height=50, pady=3)
Label_Frame.grid(column=0,row=6)
Logo_Label = tk.Label(Label_Frame,bg='#f89c0e', text= 'Enhanced View Manager for Abaqus by DI') 
Logo_Label.grid(column=1,row=0) 



root.mainloop()