# Statischer_FKM_Nachweis.py
# v1.00
# erzugt die notwendigen Ausgabegroessen fuer den statsichen FKM- Nachweis
# 16.07.2020 von Ruediger Fichtenau und Andras Vertesaljai
# History: 
# 16.07.2020 RF|AV Initialversion




print("     _ _        _                        _                       ")
print("  __| (_) ___  (_)_ __   __ _  ___ _ __ (_) ___ _   _ _ __ ___   ")
print(" / _` | |/ _ \ | | '_ \ / _` |/ _ \ '_ \| |/ _ \ | | | '__/ _ \  ")
print("| (_| | |  __/ | | | | | (_| |  __/ | | | |  __/ |_| | | |  __/_ ")
print(" \__,_|_|\___| |_|_| |_|\__, |\___|_| |_|_|\___|\__,_|_|  \___(_)")
print("                        |___/                                    ")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Imports
import odbAccess
from abaqusConstants import *
import abaqusMath
import sys
import shutil
from shutil import copyfile
from abaqus import session


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ODB Zugriff
myVName = session.currentViewportName
dispOdb = session.viewports[myVName].displayedObject.name
myODB = session.odbs[dispOdb]
myOdbName = os.path.splitext(os.path.basename(dispOdb))[0]
scratchOdb = session.ScratchOdb(odb=myODB)


#Geom
myAssembly = myODB.rootAssembly
myInstances = myAssembly.instances.keys()

#Step
mySteps = myODB.steps.keys()
myCurrentStepIndex = session.viewports[myVName].odbDisplay.fieldFrame[0]
myCurrentFrameIndex = session.viewports[myVName].odbDisplay.fieldFrame[1]
myCurrentStep = myODB.steps.keys()[myCurrentStepIndex]


myFrames = myODB.steps[myCurrentStep].frames
myTotalTime = myODB.steps[myCurrentStep].totalTime
myTimePeriode = myODB.steps[myCurrentStep].timePeriod


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Werkstoffe Holen
myMaterials = myODB.materials.keys()

#Field Auswahl
myField = []
myMaterialDict = {}
for myMaterial in sorted(myMaterials):
    myField.append([ 'Werkstoffklasse fuer: ' + myMaterial , 'S'])

print('Werkstoffklassen:')
print ('S   = Stahl')
print ('GS')
print ('GJS')
print ('GJM')
print ('GJL')
print ('ALK = Aluminium Knet')
print ('ALG = Aluminium Guss')

myMatList = getInputs(
    fields=myField,
    label='Bitte Werkstoffklasse eingeben? (S | GS | GJS | GJM | GJL | ALK | ALG)',
    dialogTitle='Werkstoffklasse')
#Umsortieren
for i, myKey in enumerate(sorted(myMaterials)):
                myMaterialDict[myKey] = myMatList[i]

#Dicts
myFSigmaZDict = {}
myFSigmaDDict = {}
myFtauDict = {}
myqDict = {}

myFSigmaZDict['S'] = 1.0
myFSigmaZDict['GS'] = 1.0
myFSigmaZDict['GJS'] = 1.0
myFSigmaZDict['GJM'] = 1.0
myFSigmaZDict['GJL'] = 1.0
myFSigmaZDict['ALK'] = 1.0
myFSigmaZDict['ALG'] = 1.0

myFSigmaDDict['S'] = 1.0
myFSigmaDDict['GS'] = 1.0
myFSigmaDDict['GJS'] = 1.3
myFSigmaDDict['GJM'] = 1.5
myFSigmaDDict['GJL'] = 2.5
myFSigmaDDict['ALK'] = 1.0
myFSigmaDDict['ALG'] = 1.5

myFtauDict['S'] = 0.577
myFtauDict['GS'] = 0.577
myFtauDict['GJS'] = 0.65
myFtauDict['GJM'] = 0.75
myFtauDict['GJL'] = 1.0
myFtauDict['ALK'] = 0.577
myFtauDict['ALG'] = 0.75

myqDict['S'] = 0.
myqDict['GS'] = 0.0  # Achtung nicht eindeutigt
myqDict['GJS'] = 0.264
myqDict['GJM'] = 0.544
myqDict['GJL'] = 1.0
myqDict['ALK'] = 0.
myqDict['ALG'] = 0.544



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Step Schreiben
myStepName = 'FKM + ' + myCurrentStep
try:
    sessionStep = scratchOdb.Step(name=myStepName , description='FKM Step mit Notwendigen Ausgaben', domain=TIME, timePeriod=1.0)
except:
    print('Step existiert bereits')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Schleife ueber Step Frame
for myFrame in myFrames:
    myTime = myFrame.frameValue
    myFrameID = myFrame.frameId
    myCurrentTime = myTime + myTotalTime
    print('StepTime: = ' + str(myTime) +' | TotalTime: = ' + str(myCurrentTime) + ' | ID:= ' + str(myFrameID))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Frame Schreiben
    try:
        sessionFrame = sessionStep.Frame(frameId=myFrameID, frameValue=myTime, description='FKM ' + str(myCurrentTime))
    except:
        print('Frame existiert bereits')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #myNewField
    print('Feld erstellen')
    try:
        E_Field_ZD = sessionFrame.FieldOutput(name='ZD Werte',description='Rü ist ein Gott', type=SCALAR)
    except:
        print('Field existiert bereits')
    try:
        EFieldZ = sessionFrame.FieldOutput(name='Zähler',description='Rü ist ein Gott', type=SCALAR)
    except:
        print('Field existiert bereits')
    try:
        EFieldN = sessionFrame.FieldOutput(name='Nenner',description='Rü ist ein Gott', type=SCALAR)
    except:
        print('Field existiert bereits')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Ergebnisse holen
    myS1 = session.odbs[dispOdb].steps[myCurrentStep].frames[myFrameID].fieldOutputs['S'].getScalarField(invariant=MAX_PRINCIPAL)
    myS2 = session.odbs[dispOdb].steps[myCurrentStep].frames[myFrameID].fieldOutputs['S'].getScalarField(invariant=MID_PRINCIPAL)
    myS3 = session.odbs[dispOdb].steps[myCurrentStep].frames[myFrameID].fieldOutputs['S'].getScalarField(invariant=MIN_PRINCIPAL)
    #Ergebnis Mathematik
    #Minus1 = (abs(myS1) + 1 ) / (abs(myS1) + 1 )
    #ZugDruck = max(Minus1 , (myS1 + myS2 + myS3) / abs(1e-20 + (myS1 + myS2 + myS3)))
    #Ergebnis Schrieben
    #sessionField = sessionFrame.FieldOutput(name='Zug - Druck', description='Zug - Druck',field=ZugDruck)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Ergebnismathematik fuer einzelne Bauteile
    #Werkstoff bestimmen
    for myInstance in myInstances:
        print(myInstance)
        mySections = myODB.rootAssembly.instances[myInstance].sectionAssignments
        myODBInstance = myODB.rootAssembly.instances[myInstance]
        for mySection in mySections:
            mySubSetSection = mySection.sectionName
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Check ob Section einen Normalen Werkstoff als Grundlage hat
            ### Kein Massepunkt
            ### Keine Traegheit
            ### Kein Rigid?
            ### Kein Gummi
            # Hier muss ein Skip rein
            mySubSetMat = myODB.sections[mySubSetSection].material
            print(mySubSetMat)
            mySubSet = mySection.region
            mySubS1= myS1.getSubset(region=mySubSet)
            mySubS2= myS2.getSubset(region=mySubSet)
            mySubS3= myS3.getSubset(region=mySubSet)
            myElements = mySubSet.elements
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Liste der Werte
            myElementList = []
            myZDValues = []
            myNennerList = []
            myZaehlerList = []
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Mathematik
            print('Schleife')
            for i,v in enumerate(mySubS1.values):
                if v.elementLabel not in myElementList:
                    myElementList.append(v.elementLabel)
                myZaehler = mySubS1.values[i].data + mySubS2.values[i].data + mySubS3.values[i].data
                myNenner = abs(mySubS1.values[i].data + mySubS2.values[i].data + mySubS3.values[i].data)
                if myNenner == 0.0:
                    myZD = 1.0
                else:
                    myZD = max(-1.0 , myZaehler / myNenner)
                myZDValues.append((myZD,))
                #myNennerList.append((myNenner,))
                #myZaehlerList.append((myZaehler,))
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Ergebnis schreiben
            print('Ergebnis schreiben')
            myElementListTuple = tuple(myElementList)
            myZDValuesTuple = tuple(myZDValues)
            myNennerTuple = tuple(myNennerList)
            myZahelerTuple = tuple(myZaehlerList)
            E_Field_ZD.addData(position=INTEGRATION_POINT, instance=myODBInstance,labels=myElementListTuple, data=myZDValuesTuple)
            #EFieldZ.addData(position=INTEGRATION_POINT, instance=myODBInstance,labels=myElementListTuple, data=myZahelerTuple)
            #EFieldN.addData(position=INTEGRATION_POINT, instance=myODBInstance,labels=myElementListTuple, data=myNennerTuple)


