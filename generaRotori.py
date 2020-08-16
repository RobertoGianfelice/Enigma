import random


s=[]
for i in range(26):
    s.append(i)
random.shuffle(s)
s1=s[:]
random.shuffle(s)
s2=s[:]
random.shuffle(s)
s3=s[:]
print ("s1=",s1,"\ns2=",s2,"\ns3=",s3)
