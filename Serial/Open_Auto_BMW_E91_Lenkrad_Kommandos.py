# Open Auto BMW E91 Lenkrad Kommandos
# R.Fichtenau
# 12.05.2020
# ///////////////////////////////////////
# 4 Lenkradtasten werden gelesen.
# Pfeil Hoch    ==> Next track      ==> N
# Pfeil Runter  ==> Previous track  ==> V
# Sprechen      ==> Voice command   ==> M
# Telefon       ==> Phone           ==> P
# ///////////////////////////////////////
# Adressen und Werte des CAN- Befehls sind in der If Abfrage
# ///////////////////////////////////////

# - Imports
import serial
from pynput.keyboard import Key, Controller
import time

# - Variablen
keyboard = Controller() 
VerbindungsBool = False


# - Endlosschleife
while True:
    # - Setup Serial
    try:
        # - Setze Verbindung
        ser = serial.Serial('/dev/ttyUSB0',9600) # Achtung: Adresse muss am Pi passen
        VerbindungsBool = True
    except :
        # - Schlafe 3 Sekunden wenn keine verbindung
        VerbindungsBool = False
    # - Check ob Serial
    if VerbindungsBool:
        print("Verbindung da")
        # Serial lesen
        line = ser.readline().decode('utf-8').rstrip()
        # Fallunterscheidungen
        # Pfeil Hoch    ==> Next track      ==> N
        if "Pfeil Hoch" == str(line):
            keyboard.press('N')
            keyboard.release('N')
        # Pfeil Runter  ==> Previous track  ==> V
        if "Pfeil Runter" == str(line):
            keyboard.press('V')
            keyboard.release('V')
        # Sprechen      ==> Voice command   ==> M
        if "Sprechen" == str(line):
            keyboard.press('M')
            keyboard.release('M')
        # Telefon       ==> Phone           ==> P
        if "Telefon" == str(line):
            keyboard.press('P')
            keyboard.release('P')
    else:
        print("Sleep, keine Verbindung")
        time.sleep(3)
