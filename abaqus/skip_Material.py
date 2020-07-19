i = 0
j = 0
mysectkey = session.odbs['C:/temp/Behaelter_VDI2230/Model-1.odb'].sections.keys()
for mysect in mysectkey:
    mysectclas = str(session.odbs['C:/temp/Behaelter_VDI2230/Model-1.odb'].sections[mysect].__class__)
    if "HomogeneousShellSection"  in mysectclas or "HomogeneousSolidSection"  in mysectclas:
        myMat = str(session.odbs['C:/temp/Behaelter_VDI2230/Model-1.odb'].sections[mysect].material)
        myElType = str(session.odbs['C:/temp/Behaelter_VDI2230/Model-1.odb'].materials['STAHL'].elastic.type)
        print(myElType)
        i  =i + 1
    else:
        continue
        i = i + 1
    if myElType != "ISOTROPIC":
        j = j + 1
        continue
    else:
        i  =i + 1
        j = j + 1

print(i)
print(j)