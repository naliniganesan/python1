ss,d1=map(int,input().split())
list=input().split()
s21=[]
for i in list:
   if(int(i)%2!=0):
    s21.append(i)
print(s21[d1-1])
