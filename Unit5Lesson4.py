a=open("words40.dat",'r')
b=[]
for i in range(40):
    b.append(a.readline().replace('\n', ''))
print(b)
