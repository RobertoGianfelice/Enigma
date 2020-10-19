#Pannello scambiatori
scamb=[1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

parolaInChiaro=input("Inserisci la parola da crittografare: ")
for c in parolaInChiaro:
    if c != " ":
        nacked=ord(c)-ord('a')
        andata=scamb[nacked]
        coded=andata+ord('a')
        print("andata",chr(coded))

        ritorno=scamb[andata]
        coded=ritorno+ord('a')
        print("ritorno",chr(coded))
    else:
        print ( " ", end="")
print()
