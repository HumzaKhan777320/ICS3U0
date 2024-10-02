import math as m
x=int(input("Enter a number: "))
y=0
z=0
a=0
print("  N|  SQR|  Cubes|Roots")
print("---+-----+-------+-----")
for i in range (x):
  y=m.pow(i+1,2)
  z=m.pow(i+1,3)
  a=m.sqrt(i+1)
  print("%3d| %4d| %6d| %4.2f"%(i+1,y,z,a))
