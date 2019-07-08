n1,r1=map(int,input().split())
s1=list(map(int,input().split()[:n]))
count1=0
for i in range(0,n1):
    if(s1[i]==r1):
        count1=count1+1
print(count1)
