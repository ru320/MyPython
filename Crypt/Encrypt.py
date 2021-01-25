
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
position = 0

myText = 'Ich bin ein Gott'
laenge = len(myText)


with open('somefile.txt', 'w') as the_file:
    for i in range(256):
        randstr = ""
        for j in range(256):
            # Zusatz
            if i == 2 and j == 2:
                # Offset
                randstr += random.choice(offset)
            elif i == 5 and j == int(offset) * int(offset):
                # Shift
                randstr += random.choice(shift)
            elif i >= 10 and i == j:
                if position < laenge:
                    myChar = myText[position].upper()
                    myCharPos = source.find(myChar)
                    myNewPos = int(myCharPos) + int(offset) + int(position) * int(shift)
                    while True:
                        if myNewPos >= mysourcelen:
                            myNewPos = myNewPos - mysourcelen
                        else:
                            break
                    myNewChar = source[myNewPos]
                    print(myChar + ' | ' + str(myCharPos) + ' | ' + str(myNewPos) + ' | ' + str(myNewChar))
                    position += 1
                    randstr += myNewChar
            else:
                # randstr += random.choice(source)
                randstr += "-"
        the_file.write(randstr + '\n')



