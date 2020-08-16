NUMEROSCAMBI=5
#scamb=[1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
scamb=[]
rot1= [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]
rot2= [7, 25, 20, 0, 12, 22, 8, 23, 5, 14, 11, 9, 16, 18, 2, 1, 3, 6, 10, 19, 21, 15, 13, 4, 24, 17]
rot3= [17, 10, 1, 14, 8, 18, 19, 24, 6, 4, 25, 11, 20, 2, 9, 23, 16, 0, 12, 3, 5, 13, 7, 15, 22, 21]
rotori=[rot1,rot2,rot3]
#rif=[5,2,1,4,3,0]
rif=[2,3,0,1,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,21,20,23,22,25,24]

def scattoSingolo(r):
    # Fa anvanzare il rotore di una posizione
    primo=r[0]
    for i in range(len(r)-1):
        r[i]=r[i+1]
    r[len(r)-1]=primo
    return (r)

def impostaRotore(r,c):
    # Gira il rotore sino alla lettera scelta
    while (chr(r[0]+ord("a"))!=c):
        r=scattoSingolo(r)
    return (r)


def giraRotore(scatti,r1,r2,r3):
    # Aziona il meccanismo di scatto partendo dal primo rotore ed eventualmente coinvolgendo gli altri
    r1=scattoSingolo(r1)
    if (scatti % len(r1)==0):
        r2=scattoSingolo(r2)
        if (scatti % (len(r1)^2)==0):
            r3=scattoSingolo(r3)
    return(r1,r2,r3)

def setupRotori(rotori):
	# Setup rotori Enigma: scelta della sequenza dei rotori e delle lettere iniziali per ciascuno
	r=int(input("Inserisci il rotore uno :"))
	r1=rotori[r-1]
	r=int(input("Inserisci il rotore due :"))
	r2=rotori[r-1]
	r=int(input("Inserisci il rotore tre :"))
	r3=rotori[r-1]

	setR1=input("Inserisci la posizione rotore1: ")
	setR2=input("Inserisci la posizione rotore2: ")
	setR3=input("Inserisci la posizione rotore3: ")
	r1=impostaRotore(r1,setR1)
	r2=impostaRotore(r2,setR2)
	r3=impostaRotore(r3,setR3)
	return (r1,r2,r3)

def setupScambi(scamb):
    #inizializzo il vettore degli scambi
    for i in range(26):
        scamb.append(i)

    for i in range(NUMEROSCAMBI):
        spina=input("Inserisci lo scambio (es: er per scambiare la e con la r): ")
        temp=scamb[ord(spina[0])-ord("a")]
        scamb[ord(spina[0])-ord("a")]=scamb[ord(spina[1])-ord("a")]
        scamb[ord(spina[1])-ord("a")]=temp

    return(scamb)


r1,r2,r3=setupRotori(rotori)
scamb=setupScambi(scamb)

parolaInChiaro=input("Inserisci la parola da crittografare: ")
scatti=0
for c in parolaInChiaro:
    if c != " ":
    	nacked=ord(c)-ord('a')
    	andata=rif[r3[r2[r1[scamb[nacked]]]]]
    	ritorno=scamb.index(r1.index(r2.index(r3.index(andata))))
    	coded=ritorno+ord('a')
    	print( chr(coded), end="")
    else:
        print ( " ", end="")
    scatti+=1
    r1,r2,r3=giraRotore(scatti,r1,r2,r3)
print()
