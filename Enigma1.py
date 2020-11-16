#1 Rotore e 1 riflessore
r1= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0]
rif=  [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]


parolaInChiaro=input("Inserisci la parola da crittografare (in MAIUSCOLO): ")
for c in parolaInChiaro:
    nacked=ord(c)-ord('A')
    andata=rif[r1[nacked]]
    ritorno=r1.index(andata)
    coded=ritorno+ord('A')
    print( chr(coded), end="")
print()
