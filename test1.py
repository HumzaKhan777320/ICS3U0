import math as m
x=int(input())
d=[]
for i in range (3,x+1):
    z=i**2+((i//2*(i+1))**2)
    y=(i//2*(i+1)+1)**2
    if(z==y):
        print(i)
        print(m.sqrt(z-(i**2)))
        print(int(m.sqrt(y)))
        print("_______________________")
