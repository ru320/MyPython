# evmadi.py
# v1.00
# Programm um Abaqus Decks zu starten und zu Tailen
# 02.10.2021 von Ruediger Fichtenau
# History: 
# 02.10.2021 RF Initialversion

################### Check Verison
import platform
myVersion = platform.python_version()

################### IMPORTS tkinter
if myVersion[0] == '3':
    import tkinter.filedialog
    import tkinter.ttk as ttk
    import tkinter as tk

if myVersion[0] == '2':
    import tkFileDialog as filedialog
    import ttk as ttk
    import Tkinter as tk


################### IMPORTS
from os import remove
import time
import os.path
import sys
import base64
from io import BytesIO
# from typing import Text


################### Variablen
Version = '1.0'
data = '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'
if myVersion[0] == '3':
    image_64_decode = base64.b64decode(data) 
    # image_64_decode = base64.decodebytes(data) 

if myVersion[0] == '2':
    image_64_decode = base64.b64decode(data) 

image_result = open('DI_Logo.gif', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
image_result.close()

#- FunktionsVariablen
myFile = ''
View_row = 1
Result_row = 1

#- Gui Variables
BTN_Dict = {}
Result_Title = ['Load','Name', 'Step', 'Frame', 'Result', 'Resulttype', 'View', 'Legend Min' , 'Legend Max' ,'Legend']
Result_Dict  = {}
ViewDict = {}
ViewIndex = 0

#- Dummy Dict
def dummy_Dict():
    global Result_Title
    global Result_Dict
    global Result_row
    Local_Dict = {}
    for myItem in Result_Title:
        Local_Dict[myItem ] = myItem + str(Result_row)
    Local_Dict['ID'] = Result_row
    Result_Dict[str(Result_row)] = Local_Dict
    Result_row += 1

dummy_Dict()
dummy_Dict()

#- Close GUI
def Close():
    root.destroy()

#- Load Result
def Load(Local_row):
    print('Load Result' , Local_row)

#- Ergebnis Speichern
def StoreResult():
    print('Store Result')
    #Umbiegen, StoreView
    global ViewDict
    global ViewIndex
    myVName = session.currentViewportName
    session.viewports['Viewport: 2'].view.setValues(
        nearPlane           =ViewDict[0][0],
        farPlane            =ViewDict[0][1],
        cameraPosition      =ViewDict[0][2],
        cameraUpVector      =ViewDict[0][3],
        cameraTarget        =ViewDict[0][4],
        width               =ViewDict[0][5],
        height              =ViewDict[0][6],)

#- View Speichern
def StoreView():
    global ViewDict
    global ViewIndex
    myVName = session.currentViewportName
    myNearPlane = session.viewports[myVName].view.nearPlane
    myFarPlane  = session.viewports[myVName].view.farPlane
    myCameraPos = session.viewports[myVName].view.cameraPosition
    myCameraUPV = session.viewports[myVName].view.cameraUpVector
    myCameraTar = session.viewports[myVName].view.cameraTarget
    width       = session.viewports[myVName].view.width
    height      = session.viewports[myVName].view.height
    myView = [myNearPlane,myFarPlane,myCameraPos,myCameraUPV,myCameraTar,width,height]
    ViewDict[ViewIndex] = myView
    ViewIndex += 1
    print('Store View')
    print(myView)

#- Choose File GUI
def ChooseFILE():
    global myFile
    print('Choose File')
    if myVersion[0] == '3':
        myFile = tk.filedialog.askopenfilename(title = "Select XML file for EVMADI",filetypes = (("XML Files","*.xml"),))
    if myVersion[0] == '2':
        myFile = filedialog.askopenfilename(title = "Select XML file for EVMADI",filetypes = (("XML Files","*.xml"),))
    LoadSettings()

#- Load Settings
def LoadSettings():
    global Result_row
    global Result_Dict
    Result_row = 1
    print('Load ' + myFile)
    for myDict in Result_Dict:
        AddRow(Result_Dict[myDict])

#- Save Settings
def Save():
    global myFile
    if myVersion[0] == '3':
        mySaveFile = tk.filedialog.asksaveasfile(title = "Save XML file for EVMADI",mode='w', defaultextension=".xml")
    if myVersion[0] == '2':
        mySaveFile = filedialog.asksaveasfile(title = "Save XML file for EVMADI",mode='w', defaultextension=".xml")
    if mySaveFile is None: # asksaveasfile return `None` if dialog closed with "cancel".
        print('Abbruch')
        return
    myFile = mySaveFile.name
    print('Save ' + str(myFile))
     

#- Remove Row
def RemoveRow(FrameName,Local_row,Local_col):
    print(FrameName, Local_row, Local_col)
    BTNName = 'BTN_' + FrameName + '_' + str(Local_col) + '_' + str(Local_row)
    btn = BTN_Dict[BTNName]
    btn.destroy()

#- Add View Row
def AddRow(Local_Dict):#Name, Step, Frame, Rsult, Resulttype, View, Legend_Min , Legend_Max ,Legend):
    global Result_row
    global Result_Dict
    myCol = 0
    #- Load
    BTN_Load = tk.Button(Results_Frame, text='Load', command=lambda:Load(Local_Dict['ID']), font='Verdana',image=pixelVirtual,compound="c",height=8)
    BTN_Load.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Name
    Name = Local_Dict['Name']
    TXT_Name = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_Name.insert(tk.END,Name)
    TXT_Name.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Step
    Step = Local_Dict['Step']
    TXT_Step = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_Step.insert(tk.END,Step)
    TXT_Step.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Frame
    Frame = Local_Dict['Frame']
    TXT_Frame = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_Frame.insert(tk.END,Frame)
    TXT_Frame.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Result
    Result = Local_Dict['Result']
    TXT_Result = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_Result.insert(tk.END,Result)
    TXT_Result.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Resulttype
    Resulttype = Local_Dict['Resulttype']
    CMB_Resulttype = ttk.Combobox(Results_Frame,width=10,height=20,values=["Contour","Symbols"],font='Verdana')
    CMB_Resulttype.grid(column=myCol,row=Result_row)
    if Resulttype == "Symbols":
        CMB_Resulttype.current(1)
    else:
        CMB_Resulttype.current(0)
    myCol +=1
    #- Vieworientation
    View = Local_Dict['View']
    TXT_View = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_View.insert(tk.END,View)
    TXT_View.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Legende Min
    Legende_Min = Local_Dict['Legend Min']
    TXT_Legende_Min = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_Legende_Min.insert(tk.END,Legende_Min)
    TXT_Legende_Min.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Legende Max
    Legende_Max = Local_Dict['Legend Max']
    TXT_Legende_Max = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_Legende_Max.insert(tk.END,Legende_Max)
    TXT_Legende_Max.grid(column=myCol,row=Result_row)
    myCol +=1
    #- Legende
    Legende = Local_Dict['Legend']
    TXT_Legende = tk.Text(Results_Frame,width=10,height=1,font='Verdana')
    TXT_Legende.insert(tk.END,Legende)
    TXT_Legende.grid(column=myCol,row=Result_row)
    myCol +=1
    print('Result row' + str(Result_row))
    Result_row += 1

#- Add BTN
def AddBTN(Frame,FrameName,Local_row,Local_col):
    print(FrameName, Local_row, Local_col)
    Name = 'BTN_' + FrameName + '_' + str(Local_col) + '_' + str(Local_row)
    btn =  tk.Button(Frame, text='Close', command=lambda:RemoveRow(FrameName, Local_row, Local_col), font='Verdana',bg='black',fg='white',image=pixelVirtual,compound="c",width = 115)
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
Logo = tk.PhotoImage(file= 'DI_Logo.gif')
# Logo = tk.PhotoImage(file= 'B:\\temp\\DI_Logo.gif')
Logo_Label = tk.Label(Logo_Frame,image=Logo,bg='white')
Logo_Label.grid(column=1,row=0)

#- Results Headder Grid
Results_Headder_Frame = tk.Frame(root, bg='#f89c0e', width=450, height=50, pady=3)
Results_Headder_Frame.grid(column=0,row=1) 
Results_Label = tk.Label(Results_Headder_Frame, text= 'Saved Results',font='Verdana') 
Results_Label.grid(column=0,row=0) 

#- Results Grid
Results_Frame = tk.Frame(root, width=450, height=50, pady=3)
Results_Frame.grid(column=0,row=2)
for i,myTitle in enumerate(Result_Title):
    Results_Titel_Label = tk.Label(Results_Frame, text= myTitle,font='Verdana') 
    Results_Titel_Label.grid(column=i,row=0) 


#- View Headder Grid
View_Headder_Frame = tk.Frame(root, bg='#f89c0e', width=450, height=50, pady=3)
View_Headder_Frame.grid(column=0,row=3)
View_Label = tk.Label(View_Headder_Frame, text= 'Saved Views',font='Verdana') 
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
#- Add BTN
btn =  tk.Button(Buttons_Frame, text='Store Result', command=lambda:StoreResult(), font='Verdana',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- Add BTN
btn =  tk.Button(Buttons_Frame, text='Store View', command=lambda:StoreView(), font='Verdana',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- Load BTN
btn =  tk.Button(Buttons_Frame, text='Load', command=lambda:ChooseFILE(), font='Verdana',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- ReLoad BTN
btn =  tk.Button(Buttons_Frame, text='Reload', command=lambda:LoadSettings(), font='Verdana',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- Save BTN
btn =  tk.Button(Buttons_Frame, text='Save', command=lambda:Save(), font='Verdana',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1
#- Close BTN
btn =  tk.Button(Buttons_Frame, text='Close', command=lambda:Close(), font='Verdana',fg='black',image=pixelVirtual,compound="c",width = 115)
btn.grid(column=myCol,row=0)
myCol += 1

##- Label Grid
Label_Frame = tk.Frame(root, bg='#f89c0e', width=450, height=50, pady=3)
Label_Frame.grid(column=0,row=6)
Logo_Label = tk.Label(Label_Frame,bg='#f89c0e', text= 'Enhanced View Manager for Abaqus by DI',font='Verdana') 
Logo_Label.grid(column=1,row=0) 



root.mainloop()

