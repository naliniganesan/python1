ws1,ws2=map(int,input().split())
n1=1
while(n1<=w1 and n1<=w2):
   if(ws1%n==0 and ws2%n==0):
      gc=n
   n1=n1+1
print(gc)
