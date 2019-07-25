v1,v2=map(int,input().split())
maxima=max(v1,v2)
while(1):
   if(maxima%p1==0 and maxima%p2==0):
         print(maxima)
         break
   maxima+=1
