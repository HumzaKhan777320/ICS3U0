a=open("words40.dat",'r')
b=[]
for i in range(40):
    b.append(a.readline().strip())
for i in range(len(b)):
    for j in range(i):
        if(b[i]<b[j]):
            b[i],b[j]=b[j],b[i]
for i in range(1,5):
    for k in range(1,11):
        print(b[i*k-1], end = "  ")
    print("\n")
a.close()
print(f"{len(b)} words.")
