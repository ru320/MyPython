import random
import string
import os

asciisource     = string.ascii_uppercase
dezisource      = "123456789"
specialsource   = "0.,@:;_-? "
source = asciisource + dezisource + specialsource
mysourcelen = len(source)


zeilenlaenge = 256
Absatze = 2
OffsetIniPos = 2
offsetpos = zeilenlaenge * Absatze + Absatze + OffsetIniPos

TextBeginnZeile = 10
textposition = 0


with open('somefile.txt', 'r') as the_file:
    myCyptText = the_file.read()
    offset = myCyptText[offsetpos]
    shiftpos = zeilenlaenge * 5 + 5 + int(offset) * int(offset)
    shift = myCyptText[shiftpos]



myText = ""
textposition = 0
with open('somefile.txt', 'r') as the_file:
    for i,myline in enumerate(the_file):
        Zeilenpos = textposition * int(shift)**2
        while True:
            if Zeilenpos > 255:
                Zeilenpos = Zeilenpos - 256
            else:
                break
        if i >= TextBeginnZeile:
            myChar = myline[Zeilenpos]
            textposition +=1
            if myChar == "|":
                break
            myText += str(myChar)
            

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



