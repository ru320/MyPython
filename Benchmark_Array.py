import time
import random
import sys
sys.getdefaultencoding()


# Variablen
Dict_1 = {}
Dict_2 = {}
Dict_3 = {}
Dict_4 = {}
Dict_5 = {}
Dict_6 = {}
Dict_7 = {}
Dict_8 = {}
Dict_9 = {}
Dict_10 = {}
TotalTime = 0
TimeDict = {}


# Schleifen
def Schelife(N):
    start_time = time.time()
    short_time = time.time()
    Anteil = 1
    for n in range(N):
        if N/100 * 5 * Anteil <= n:
            Anteil +=1
            print(str(100. / N * n) + "%")
            TimeDict[str(100. / N * n)] = time.time() - short_time
            short_time = time.time()
        x = random.uniform(10.5, 100.5)
        Dict_1[n] = x
        Dict_2[n] = x
        Dict_3[n] = x
        Dict_4[n] = x
        Dict_5[n] = x
        Dict_6[n] = x
        Dict_7[n] = x
        Dict_8[n] = x
        Dict_9[n] = x
        Dict_10[n] = x
    DeltaTime = time.time() - start_time
    return DeltaTime


Elemente = int(200)
for i in range(10):
    TotalTime += Schelife(Elemente)
print("--- %s seconds ---" % (TotalTime / 3.0))

for mytime in TimeDict:
    print(str(mytime) + " | " + str(TimeDict[mytime]))