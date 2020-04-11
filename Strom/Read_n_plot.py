# Read Lines and plot

import matplotlib.pyplot as plt
import numpy as np



myFile = "/home/ru320/Dokumente/python/MyPython/Strom/Strom_def/Strom_Alu_2.inp"
myStromValues = []
myZeitValues  = []


with open(myFile) as f:
    first_line = f.readline()
    for line in f:
        myValues = line.split(",")
        myStrom  = float(myValues[4].split("$")[0].split()[0])
        myZeit = float(myValues[-1].split()[0])
        myStromValues.append(myStrom)
        myZeitValues.append(myZeit) 
        # print(myZeit[0] + "," + myStrom)


x=[]
y=[]
for i in range(0,500):
    # print(str(myZeitValues[i]) + "," + str(myStromValues[i]))
    x.append(myZeitValues[i])
    y.append(myStromValues[i])

plt.xticks(np.arange(min(x), max(x)+1, 100.0))


plt.xticks(np.arange(min(myZeitValues), max(myZeitValues)+1, 100.0))
plt.plot(myZeitValues,myStromValues)
# plt.plot(x,y)

myMaxZeit = 150
myIncr = 1

mySimZeit=[]
mySimStrom = []

for myTime in range(0,myMaxZeit,myIncr):
    mySimZeit.append(myTime)
    m = 0
    for n in myZeitValues:
        if myZeitValues[m] > myTime:
            print("next" + str(myTime))
            mySimStrom.append(myStromValues[m])
            break 
        m = m + 1


print(mySimStrom)

plt.plot(mySimZeit,mySimStrom)

plt.show()

