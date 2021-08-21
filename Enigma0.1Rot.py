# Usando un singolo rotore, costante, acquisisce una frase e la codifica

r1= [3, 24, 0, 6, 7, 4, 12, 17, 11, 23, 21, 15, 18, 19, 16, 14, 1, 20, 8, 13, 5, 9, 25, 2, 10, 22]

parolaInChiaro=input("Inserisci la parola da crittografare (in MAIUSCOLO): ")
for c in parolaInChiaro:
    nacked=ord(c)-ord('A')
    coded=r1[nacked]+ord('A')
    print( chr(coded), end="")
print()
