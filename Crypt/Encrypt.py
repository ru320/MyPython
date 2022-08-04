import random
import string
import os

asciisource     = string.ascii_uppercase
dezisource      = "123456789"
specialsource   = "0.,@:;_-? "
source = asciisource + dezisource + specialsource
mysourcelen = len(source)


#domain = os.environ['userdomain']
#print(domain)

offset = random.choice(dezisource)
shift = random.choice(dezisource)
textposition = 0
EndBool = False



myText = 'test 64'
laenge = len(myText)
zeilen_laenge = 64

with open('somefile.txt', 'w') as the_file:
    for i in range(256):
        randstr = ""
        Zeilenpos = textposition * int(shift)**2
        while True:
            if Zeilenpos > zeilen_laenge:
                Zeilenpos = Zeilenpos - zeilen_laenge
                # print(Zeilenpos)
            else:
                break
        for j in range(zeilen_laenge):
            # Zusatz
            if i == 2 and j == 2:
                # Offset
                randstr += random.choice(offset)
            elif i == 5 and j == int(offset) * int(offset):
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
                    EndBool = True
            else:
                # randstr += random.choice(source)
                randstr += "-"
        the_file.write(randstr + '\n')
