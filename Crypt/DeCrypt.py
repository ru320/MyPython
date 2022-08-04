import random
import string
import os

asciisource     = string.ascii_uppercase
dezisource      = "123456789"
specialsource   = "0.,@:;_-? "
source = asciisource + dezisource + specialsource
mysourcelen = len(source)


zeilenlaenge = 64
Absatze = 2
OffsetIniPos = 2
offsetpos = zeilenlaenge * Absatze + Absatze + OffsetIniPos

TextBeginnZeile = 10
textposition = 0

myFile = 'DI_Bolts.lic'
myFile = 'somefile.txt'


with open(myFile, 'r') as the_file:
    myCyptText = the_file.read()
    offset = myCyptText[offsetpos]
    shiftpos = zeilenlaenge * 5 + 5 + int(offset) * int(offset)
    shift = myCyptText[shiftpos]

print(offset)
print(shift)



myText = ""
textposition = 0
with open(myFile, 'r') as the_file:
    for i,myline in enumerate(the_file):
        Zeilenpos = textposition * int(shift)**2
        while True:
            if Zeilenpos >= zeilenlaenge:
                Zeilenpos = Zeilenpos - zeilenlaenge
            else:
                break
        if i == TextBeginnZeile:
            print(myline)
        if i >= TextBeginnZeile:
            myChar = myline[Zeilenpos]
            textposition +=1
            print(myChar,Zeilenpos)
            if myChar == "|":
                break
            myText += str(myChar)
            
print(myText)
myDecryptedText = ""
for i,myChar in enumerate(myText):
    myCharPos = source.find(myChar)
    myNewPos = int(myCharPos) - int(offset) - int(i) * int(shift)
    while True:
        if myNewPos < 0:
            myNewPos = myNewPos + mysourcelen
        else:
            break
    myNewChar = source[myNewPos]
    myDecryptedText += myNewChar

print(myDecryptedText)



