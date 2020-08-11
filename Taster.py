import time
import keyboard


myBoolP = False
myBoolB = False
myBoolTimer = False
myTime = 0

Count = 0

#keyboard.wait('p')

while True:
    Count +=1
    if Count == 100:
        Count = 0
        print('Reset')
        break


while True:
    Count +=1
    if Count == 1000:
        Count = 0
        #print('Reset')
    if keyboard.is_pressed('p'):
        if myBoolP == True and time.time()*1000.0 - myTime >= 200. and time.time()*1000.0 - myTime < 1000.:
            print('Signal da')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            time.sleep(1)
            print('Timer aus')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            myBoolTimer = False
            myBoolP = False
        elif myBoolP == True and time.time()*1000.0 - myTime >= 1000.:
            print('Signal zu alt')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            time.sleep(1)
            print('Timer aus')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            myBoolTimer = False
            myBoolP = False
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("TimerStart")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            myTime = time.time()*1000.0
            myBoolTimer = True
            myBoolP = True
    if keyboard.is_pressed('b'):
        print("You pressed b")
        break
    if keyboard.is_pressed('t'):
        print("Time")
        print(time.time()*1000.0 - myTime)
    if myBoolP == True and time.time()*1000.0 - myTime >= 1000.:
        print('Timer aus')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        myBoolTimer = False
        myBoolP = False
     




print('Fertig.')