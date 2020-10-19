#1 Rotore e 1 riflessore
rot1= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0]
rif=  [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]

r1=rot1

parolaInChiaro=input("Inserisci la parola da crittografare: ")
for c in parolaInChiaro:
    if c != " ":
    	nacked=ord(c)-ord('a')
    	andata=rif[r1[nacked]]
    	ritorno=r1.index(andata)
    	coded=ritorno+ord('a')
    	print( chr(coded), end="")
    else:
        print ( " ", end="")
print()
