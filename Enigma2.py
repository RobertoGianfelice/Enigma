#1 Rotore e 1 riflessore
r1= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0]
rif=  [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]

def scattoSingolo(r):
    # Fa anvanzare il rotore di una posizione
    primo=r[0]
    for i in range(len(r)-1):
        r[i]=r[i+1]
    r[len(r)-1]=primo
    return (r)


def giraRotore(scatti,passoR1,passoR2,r1,r2,r3):
    # Aziona il meccanismo di scatto partendo dal primo rotore ed eventualmente coinvolgendo gli altri
    # utilizzando il periodo del primo e secondo rotore impostati dall'utente
    r1=scattoSingolo(r1)
    if (scatti % passoR1==0):
        r2=scattoSingolo(r2)
        if (scatti % (passoR1*passoR2)==0):
            r3=scattoSingolo(r3)
    return(r1,r2,r3)


parolaInChiaro=input("Inserisci la parola da crittografare (in MAIUSCOLO): ")
for c in parolaInChiaro:
    nacked=ord(c)-ord('A')
    andata=rif[r1[nacked]]
    ritorno=r1.index(andata)
    coded=ritorno+ord('A')
    print( chr(coded), end="")
print()
