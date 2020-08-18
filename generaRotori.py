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
random.shuffle(s)
s4=s[:]
random.shuffle(s)
s5=s[:]
print ("s1=",s1,"\ns2=",s2,"\ns3=",s3,"\ns4=",s4,"\ns5=",s5)
