#Pannello scambiatori
scamb=[1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
rif=  [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]


parolaInChiaro=input("Inserisci la parola da crittografare: ")
for c in parolaInChiaro:
    if c != " ":
        nacked=ord(c)-ord('a')
        print("nacked=",nacked)
        andata=scamb[nacked]
        coded=andata+ord('a')
        print("andata",chr(coded))
        andata=rif[andata]

        ritorno=scamb.index(scamb[andata])

        coded=ritorno+ord('a')
        print("ritorno---->",chr(coded))
    else:
        print ( " ", end="")
print()
