k=input()
for s in range(0,len(k)):
    
    if (k[s].isalpha() and k[s].isnumeric()):
        print("No")
else:
        print("Yes")
