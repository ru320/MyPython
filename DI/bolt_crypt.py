import string
import random
import os
import itertools

# Verschlüsselt den String myText und speichert das Ergebnis unter filename.
def encrypt(myText, filename):
    asciisource     = string.ascii_uppercase
    dezisource      = "123456789"
    specialsource   = "0.,@:;_-? "
    source = asciisource + dezisource + specialsource
    mysourcelen = len(source)

    offset = random.choice(dezisource)
    shift = random.choice(dezisource)
    textposition = 0
    EndBool = False

    myText = myText.upper()

    # Prüfe, ob myText nur Buchstaben entält, die verschlüsselt werden können.
    for c in myText:
        if c not in source:
            raise Exception("Can't encrypt Character '{}'.".format(c))

    # Payload 
    #-------------------------------------------------
    laenge = len(myText)
    zeilen_laenge = 64

    # Erzeuge Pfad und loesche Inhalt
    #-------------------------------------------------
    dir_name = os.path.dirname(filename)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Create File 
    #-------------------------------------------------
    with open(filename, 'w') as the_file:
        for i in range(256):
            randstr = ""
            Zeilenpos = textposition * int(shift)**2
            while True:
                if Zeilenpos >= zeilen_laenge:
                    Zeilenpos = Zeilenpos - zeilen_laenge
                    # print(Zeilenpos)
                else:
                    break
            for j in range(zeilen_laenge):
                # Zusatz
                if i == 2 and j == 2:
                    # Offset
                    randstr += random.choice(offset)
                elif i == 5 and j == min(int(offset) * int(offset), zeilen_laenge - 1):
                    # Shift
                    randstr += random.choice(shift)
                elif i >= 10 and j == Zeilenpos:
                    if textposition < laenge:
                        myChar = myText[textposition].upper()
                        myCharPos = source.find(myChar)
                        myNewPos = int(myCharPos) + int(offset) + int(textposition) * int(shift)
                        while True:
                            if myNewPos >= mysourcelen:
                                myNewPos = myNewPos - mysourcelen
                            else:
                                break
                        myNewChar = source[myNewPos]
                        # print(myChar + ' | ' + str(myCharPos) + ' | ' + str(myNewPos) + ' | ' + str(myNewChar))
                        textposition += 1
                        randstr += myNewChar
                    elif textposition >= laenge and EndBool == False:
                        randstr += '|'
                        textposition += 1
                        EndBool = True
                    elif textposition >= laenge and EndBool == True:
                        textposition += 1
                        randstr += random.choice(source)
                else:
                    randstr += random.choice(source)
                    # randstr += "-"
            the_file.write(randstr + '\n')


def decrypt(myCryptText):
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

    myCryptText = myCryptText.replace("\r\n", "\n")
    lines = myCryptText.split("\n")

    offset = myCryptText[offsetpos]
    shiftpos = zeilenlaenge * 5 + 5 + min(int(offset) * int(offset), zeilenlaenge - 1)
    shift = myCryptText[shiftpos]
   

    myText = ""
    textposition = 0
    for i,myline in zip(itertools.count(), lines):
        Zeilenpos = textposition * int(shift)**2
        while True:
            if Zeilenpos >= zeilenlaenge:
                Zeilenpos = Zeilenpos - zeilenlaenge
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

    return myDecryptedText

# Zum Testen
if __name__ == '__main__':
    encrypt("asiouqweoiwuerkds4weoiuxck,wrexcoiuewr.dfsdllum,wer,", "E:/test.lic")

    with open("test.lic", 'r') as file:
        print(decrypt(file.read()))
