scamb=[1,0,2,3,4,5]
rot1=[5,2,4,3,1,0]
rot2=[2,0,3,1,5,4]
rot3=[4,0,3,5,2,1]
rif=[5,2,1,4,3,0]

def scattoSingolo(r):
    primo=r[0]
    for i in range(len(r)-1):
        r[i]=r[i+1]
    r[len(r)-1]=primo
    return (r)

def giraRotore(scatti,r1,r2,r3):
    r1=scattoSingolo(r1)
    if (scatti % len(r1)==0):
        r2=scattoSingolo(r2)
        if (scatti % (len(r1)^2)==0):
            r3=scattoSingolo(r3)
    return(r1,r2,r3)

parolaInChiaro=input("Inserisci la parola da crittografare: ")
scatti=0
for c in parolaInChiaro:
    #print("Inizio: ",rot1,rot2,rot3)
    nacked=ord(c)-ord('a')
    #print (nacked, "=>", scamb[nacked],
    #					rot1[scamb[nacked]],
    #                    rot2[rot1[scamb[nacked]]],
    #                    rot3[rot2[rot1[scamb[nacked]]]],
    #                    rif[rot3[rot2[rot1[scamb[nacked]]]]])
    andata=rif[rot3[rot2[rot1[scamb[nacked]]]]]

    #print (andata, "<=",
    #					rot3.index(andata),
    #                    rot2.index(rot3.index(andata)),
    #                    rot1.index(rot2.index(rot3.index(andata))),
    #                    scamb.index(rot1.index(rot2.index(rot3.index(andata)))))
    ritorno=scamb.index(rot1.index(rot2.index(rot3.index(andata))))
    coded=ritorno+ord('a')
    print( chr(coded), end="")
    scatti+=1
    rot1,rot2,rot3=giraRotore(scatti,rot1,rot2,rot3)
    #print("Ruoto: ",rot1,rot2,rot3)
