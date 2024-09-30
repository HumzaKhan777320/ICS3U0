x=int(input("Enter a whole number >0"))
z=1
z1=1
y=2
y1=2
for i in range(x):
  print(i+1,end=" ")
  print(z, end=" ")
  z+=y
  y+=1
  print(z1)
  z1*=y1
  y1+=1
