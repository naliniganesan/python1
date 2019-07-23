d1=int(input())
s12=[]
for g12 in range(0,d1):
 pan2=input()
 s12.append(pan2)
ven12=[]
for d1 in zip(*s12):
 if(d1.count(h12[0])==len(g12)):
  ven12.append(g12[0])
 else:
  break
print(''.join(ven12))
