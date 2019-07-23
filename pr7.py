nalu=list(input())
for i in range(0,len(nalu),2):
   nalu[i],nalu[i+1]=nalu[i+1],nalu[i]
sur=''.join(nalu)
print(sur)
