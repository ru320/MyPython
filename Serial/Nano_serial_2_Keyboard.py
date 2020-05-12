import serial
from pynput.keyboard import Key, Controller
keyboard = Controller() 

ser = serial.Serial('/dev/ttyUSB0',9600)
i = 0

while True:
    # Serial lesen
    line = ser.readline().decode('utf-8').rstrip()
    if "Pfeil Hoch" == str(line):
        print(line + str(i))
        keyboard.press('B')
        keyboard.release('B')
        i+=1


