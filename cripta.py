scamb=[1,0,2,3,4,5]
rot1=[5,2,4,3,1,0]
rot2=[2,0,3,1,5,4]
rot3=[4,0,3,5,2,1]
rif=[5,2,1,4,3,0]

def giraRotore(scatti,r1,r2,r3):
    primo=r1[0]
    for i in range(len(r1)-1):
        r1[i]=r1[i+1]
    r1[len(r1)-1]=primo
    if (scatti mod len(r1)==0):
        primo=r2[0]
        for i in range(len(r2)-1):
            r2[i]=r2[i+1]
        r2[len(r2)-1]=primo
        if (scatti mod len(r1)^2==0):
            primo=r3[0]
            for i in range(len(r3)-1):
                r3[i]=r3[i+1]
            r3[len(r3)-1]=primo


    return(r1,r2,r3)

parolaInChiaro=input("Inserisci la parola da crittografare: ")
scatti=0
for c in parolaInChiaro:
    print("Inizio: ",rot1,rot2,rot3)
    nacked=ord(c)-ord('a')
    print (nacked, "=>", scamb[nacked],
    					rot1[scamb[nacked]],
                        rot2[rot1[scamb[nacked]]],
                        rot3[rot2[rot1[scamb[nacked]]]],
                        rif[rot3[rot2[rot1[scamb[nacked]]]]])
    andata=rif[rot3[rot2[rot1[scamb[nacked]]]]]
    print (andata, "<=",
    					rot3.index(andata),
                        rot2.index(rot3.index(andata)),
                        rot1.index(rot2.index(rot3.index(andata))),
                        scamb.index(rot1.index(rot2.index(rot3.index(andata)))))
    ritorno=scamb.index(rot1.index(rot2.index(rot3.index(andata))))
    coded=ritorno+ord('a')
    print(coded, "=>", chr(coded))
    rot1,rot2,rot3=list(giraRotore(scatti,rot1,rot2,rot3))
    scatti+=1
    print("Ruoto: ",rot1,rot2,rot3)
