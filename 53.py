nsd=int(input())
vsu=0
i=0
while(nsd>0):
    i=nsd%10
    vsu=vsu+i
    nsd=nsd//10
print(vsu)
