scamb=[0,2,1,3]
rot1=[3,2,0,1]
rot2=[2,1,0,3]
rot3=[1,2,0,3]
rif=[3,2,1,0]

def giraRotore(rot):
    primo=rot[0]
    for i in range[len(rot)]:
        rot[i]=rot[i+1]
    rot[len(rot)-1]=primo
    return(rot)

parolaInChiaro=input("Inserisci la parola da crittografare: ")

for c in parolaInChiaro:
    nacked=ord(c)-ord('a')
    print (nacked, "=>", scamb[nacked],
    					rot1[scamb[nacked]],
                        rot2[rot1[scamb[nacked]]],
                        rot3[rot2[rot1[scamb[nacked]]]],
                        rif[rot3[rot2[rot1[scamb[nacked]]]]])
    andata=rif[rot3[rot2[rot1[scamb[nacked]]]]]
    print (andata,
    					rot3.index(andata),
                        rot2.index(rot3.index(andata)),
                        rot1.index(rot2.index(rot3.index(andata))),
                        scamb.index(rot1.index(rot2.index(rot3.index(andata)))))
    ritorno=scamb.index(rot1.index(rot2.index(rot3.index(andata))))
    coded=ritorno+ord('a')
    print(coded, "=>", chr(coded))

print(giraRotore(rot1))
